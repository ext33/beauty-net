from abc import ABC, abstractmethod
from typing import Type

from django import forms
from django.core.handlers.wsgi import WSGIRequest
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseNotAllowed, JsonResponse, HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from django.db import models

from djresty import rest


class ExceptionRestyResponse(Exception):
    def __init__(self, response):
        self.r = response


class RestyExtraParams(dict):
    """
    Wrapper on dict, for able function add
    extra param to api view functions
    """
    pass


class RestyPlugin(ABC):

    @abstractmethod
    def exec(self, request: WSGIRequest, *args, **kwargs) -> 'RestyExtraParams|None':
        pass


class MethodAllow(RestyPlugin):

    def __init__(self, methods=None):
        self.methods = methods

    def exec(self, request: WSGIRequest, *args, **kwargs):
        if not self.methods:
            return
        if request.method not in self.methods:
            raise ExceptionRestyResponse(HttpResponseNotAllowed(self.methods))


class FormValidator(RestyPlugin):
    def __init__(self, form, method='POST', raise_on_invalid=True, raise_status_code=400, *args, **kwargs):
        self.form = form
        self.method = method
        self.raise_on_invalid = raise_on_invalid
        self.raise_status_code = raise_status_code
        self.args = args
        self.kwargs = kwargs

    def exec(self, request: WSGIRequest, *args, **kwargs) -> 'RestyExtraParams|None':
        data = request.POST if self.method == 'POST' else request.GET
        form: forms.Form = self.form(data=data, files=request.FILES, *self.args, **self.kwargs)
        if not form.is_valid():
            if self.raise_on_invalid:
                raise ExceptionRestyResponse(JsonResponse(
                    status=self.raise_status_code,
                    data=form.errors)
                )
        return RestyExtraParams({
            'form': form
        })


class ListPaginator(RestyPlugin):
    def __init__(self, max_count=100):
        self.max_count = max_count
        self.min_count = 0

    def exec(self, request: WSGIRequest, *args, **kwargs) -> 'RestyExtraParams|None':
        def paginator(object_list):
            try:
                page_number = request.GET['page']
            except MultiValueDictKeyError:
                page_number = 1

            try:
                page = int(page_number)
                if page < 1:
                    page = 1
            except (TypeError, ValueError):
                page = 1

            try:
                limit = int(self.max_count)
                if limit < self.min_count:
                    limit = self.min_count
                if limit > self.max_count:
                    limit = self.max_count
            except (ValueError, TypeError):
                limit = self.max_count

            data_paginator = Paginator(object_list, limit)
            try:
                objects = data_paginator.page(page)
            except PageNotAnInteger:
                objects = data_paginator.page(1)
            except EmptyPage:
                objects = data_paginator.page(data_paginator.num_pages)

            data = {
                'previous_page': objects.has_previous() and objects.previous_page_number() or None,
                'next_page': objects.has_next() and objects.next_page_number() or None,
                'data': objects.object_list
            }
            return data

        return RestyExtraParams({
            'paginator': paginator
        })


class RetrieveModelByPkPlugin(RestyPlugin):
    def __init__(self, model: Type[models.Model], raise_on_not_found=True, raise_status_code=404,
                 create_if_not_exist=False, key_name='pk', defaults=None, pass_arg_name='obj'):
        self.pass_arg_name = pass_arg_name
        self.defaults = defaults
        self.key_name = key_name
        self.raise_status_code = raise_status_code
        self.raise_on_not_found = raise_on_not_found
        self.create_if_not_exist = create_if_not_exist
        self.model = model

    def exec(self, request: WSGIRequest, *args, **kwargs) -> 'RestyExtraParams|None':
        if self.key_name not in kwargs:
            raise ValueError("You have not specify pk url")
        model_args = {self.key_name: kwargs[self.key_name]}
        if self.create_if_not_exist:
            obj = self.model.objects.get_or_create(
                defaults=self.defaults,
                **model_args
            )
        else:
            try:
                obj = self.model.objects.get(
                    **model_args
                )
            except self.model.DoesNotExist:
                obj = None
                if self.raise_on_not_found:
                    raise ExceptionRestyResponse(
                        HttpResponse(status=self.raise_status_code)
                    )

        return RestyExtraParams({
            self.pass_arg_name: obj
        })
