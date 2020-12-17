from django.core.exceptions import ValidationError
from django.shortcuts import get_list_or_404
from rest_framework.response import Response
from rest_framework import viewsets

from netWeb.api.v2.forms import *
from netWeb.api.v2.serializers import *
from netWeb.models import Services, Personal


class ServicesViewSet(viewsets.ViewSet):
    queryset = Services.objects.all()

    def list(self, request):
        serializer = ServicesSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def by_pk(self, request, pk=None):
        try:
            service = get_object_or_404(self.queryset, pk=pk)
            serializer = ServicesSerializer(service)
        except(ValueError):
            return Response(status=404)
        return Response(serializer.data)


class PersonalViewSet(viewsets.ViewSet):
    queryset = Personal.objects.all()

    def list(self, request):
        serializer = PersonalSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def by_pk(self, request, pk=None):
        try:
            service = get_object_or_404(self.queryset, pk=pk)
            serializer = PersonalSerializer(service)
        except(ValidationError):
            return Response(status=404)
        return Response(serializer.data)


class BranchOfficesViewSet(viewsets.ViewSet):
    queryset = BranchOffice.objects.all()

    def list(self, request):
        serializer = BranchOfficesSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def by_pk(self, request, pk=None):
        try:
            service = get_object_or_404(self.queryset, pk=pk)
            serializer = BranchOfficesSerializer(service)
        except(ValidationError):
            return Response(status=404)
        return Response(serializer.data)


class ServiceSignupViewSet(viewsets.ViewSet):
    queryset = ServiceSignup.objects.all()

    @staticmethod
    def create(request):
        form = ServiceSignupForm(request.POST)
        if form.is_valid():
            signup = form.save()
            serializer = ServiceSignupSerializer(signup)
            return Response(serializer.data)
        else:
            return Response({'result': 'error', 'error': 'invalid form data'})

    @staticmethod
    def update(request, pk=None):
        form = ServiceSignupForm(request.POST)
        new_signup = form.update(pk)
        serializer = ServiceSignupSerializer(new_signup)
        return Response(serializer.data)

    def cancel(self, request, pk=None):
        try:
            signup = get_object_or_404(self.queryset, pk=pk)
            signup.delete()
        except(ValidationError):
            return Response(status=404)
        return Response({'result': 'success'})

    def by_pk(self, request, pk=None):
        try:
            signup = get_object_or_404(self.queryset, pk=pk)
            serializer = ServiceSignupSerializerDisplay(signup, context={'request': request})
        except(ValidationError):
            return Response(status=404)
        return Response(serializer.data)


class SignupTimeViewSet(viewsets.ViewSet):
    queryset = SignupTime.objects.all()

    def by_master(self, request, pk=None):
        try:
            signup_time = get_list_or_404(self.queryset, master=pk)
            serializer = SignupTimeSerializer(signup_time, many=True)
        except(ValidationError):
            return Response(status=404)
        return Response(serializer.data)
