from django.core.handlers.wsgi import WSGIRequest
from django.urls import path
from djresty import rest, plugins
from netWeb.api.v1.forms import ServiceSignupForm
from netWeb.models import *


class ServicesApi(rest.RestyView):
    @rest.resty(
        url='services_list',
        name='get-services-list',
        plugins=[
            plugins.MethodAllow(['GET']),
            plugins.ListPaginator(),
        ],
        csrf_exempt=True,
    )
    def get_list(self, request: WSGIRequest, paginator):
        services = []
        for service in Services.objects.all():
            data = {
                       'id': service.id,
                       'name': service.name,
                       'duration': service.duration,
                       'price': service.price,
                       'master': service.master.FIO
                   },
            services.append(data)
        services = paginator(services)
        return rest.RestyResponse({
            'services': services
        }, safe=False)

    @rest.resty(
        url='service_by_pk/<int:pk>',
        name='get-service-pk',
        plugins=[
            plugins.MethodAllow(['GET']),
        ],
        csrf_exempt=True,
    )
    def get_by_pk(self, request: WSGIRequest, pk: int):
        try:
            service = Services.objects.get(pk=pk)
        except Services.DoesNotExist:
            return rest.RestyResponse(
                {'error': "Doesn't exist"},
                status=404
            )
        return rest.RestyResponse({
            'id': service.id,
            'name': service.name,
            'duration': service.duration,
            'price': service.price,
            'master': service.master.FIO
        })


class PersonalApi(rest.RestyView):
    @rest.resty(
        url='personal_list',
        name='get-personal-list',
        plugins=[
            plugins.MethodAllow(['GET']),
            plugins.ListPaginator(),
        ],
        csrf_exempt=True,
    )
    def get_list(self, request: WSGIRequest, paginator):
        personal = []
        for personal in Personal.objects.all():
            data = {
                       'id': personal.id,
                       'FIO': personal.FIO,
                       'branch_office': personal.branch_office.address
                   },
            personal.append(data)
        personal = paginator(personal)
        return rest.RestyResponse({
            'personals': personal
        }, safe=False)

    @rest.resty(
        url='personal_by_pk/<int:pk>',
        name='get-personal-pk',
        plugins=[
            plugins.MethodAllow(['GET']),
        ],
        csrf_exempt=True,
    )
    def get_by_pk(self, request: WSGIRequest, pk: int):
        try:
            personal = Personal.objects.get(pk=pk)
        except Personal.DoesNotExist:
            return rest.RestyResponse(
                {'error': "Doesn't exist"},
                status=404
            )
        return rest.RestyResponse({
            'id': personal.id,
            'FIO': personal.FIO,
            'branch_office': personal.branch_office
        })


class OfficesApi(rest.RestyView):
    @rest.resty(
        url='office_list',
        name='get-office-list',
        plugins=[
            plugins.MethodAllow(['GET']),
            plugins.ListPaginator(),
        ],
        csrf_exempt=True,
    )
    def get_list(self, request: WSGIRequest, paginator):
        offices = []
        for office in BranchOffice.objects.all():
            data = {
                       'id': office.id,
                       'office_name': office.office_name,
                       'address': office.address,
                       'telephone': office.telephone
                   },
            offices.append(data)
        offices = paginator(offices)
        return rest.RestyResponse({
            'offices': offices
        }, safe=False)

    @rest.resty(
        url='office_by_pk/<int:pk>',
        name='get-office-pk',
        plugins=[
            plugins.MethodAllow(['GET']),
        ],
        csrf_exempt=True,
    )
    def get_by_pk(self, request: WSGIRequest, pk: int):
        try:
            office = BranchOffice.objects.get(pk=pk)
        except Personal.DoesNotExist:
            return rest.RestyResponse(
                {'error': "Doesn't exist"},
                status=404
            )
        return rest.RestyResponse({
            'id': office.id,
            'office_name': office.office_name,
            'address': office.address,
            'telephone': office.telephone
        })


class ServiceSignupApi(rest.RestyView):
    @rest.resty(
        url='set_signup',
        name='set-signup',
        plugins=[
            plugins.MethodAllow(['POST']),
            plugins.FormValidator(ServiceSignupForm)
        ],
        csrf_exempt=True
    )
    def set(self, request: WSGIRequest, form: ServiceSignupForm):
        if form.is_valid():
            note = form.save()
            return rest.RestyResponse({
                'id':  note.id,
                'FIO': note.FIO,
                'service': note.service.name,
                'time': note.time,
                'master': note.master.FIO,
                'branch_office': note.branch_office.address
            })
        else:
            return rest.RestyResponse({
                'error': 'Invalid data'
            })

    @rest.resty(
        url='update_signup/<pk>',
        name='update-signup',
        plugins=[
            plugins.MethodAllow(['POST']),
            plugins.FormValidator(ServiceSignupForm)
        ],
        csrf_exempt=True
    )
    def update(self, request: WSGIRequest, pk, form: ServiceSignupForm):
        try:
            new_note = ServiceSignup.objects.get(id=pk)
        except ServiceSignup.DoesNotExist:
            return rest.RestyResponse(
                {'error': "Doesn't exist"},
                status=404
            )
        if form.is_valid():
            new_note = form.update(new_note)
            return rest.RestyResponse({
                'id': new_note.id,
                'FIO': new_note.FIO,
                'service': new_note.service.name,
                'time': new_note.time,
                'master': new_note.master.FIO,
                'branch_office': new_note.branch_office.address
            })
        else:
            return rest.RestyResponse({
                'error': 'Invalid data'
            })

    @rest.resty(
        url='signup_by_pk/<pk>',
        name='get-signup-by-pk',
        plugins=[
            plugins.MethodAllow(['GET']),
        ],
        csrf_exempt=True
    )
    def get_by_pk(self, request: WSGIRequest, pk):
        try:
            note = ServiceSignup.objects.get(id=pk)
        except ServiceSignup.DoesNotExist:
            return rest.RestyResponse(
                {'error': "Doesn't exist"},
                status=404
            )
        return rest.RestyResponse({
            'id':  note.id,
            'FIO': note.FIO,
            'service': note.service.name,
            'time': note.time,
            'master': note.master.FIO,
            'branch_office': note.branch_office.address
        })


urlpatterns = [
    path('services/', ServicesApi(name='services').urls),
    path('personal/', PersonalApi(name='personal').urls),
    path('offices/', OfficesApi(name='offices').urls),
    path('signup/', ServiceSignupApi(name='signup').urls),
]
