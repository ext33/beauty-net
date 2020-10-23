from django.core.handlers.wsgi import WSGIRequest
from django.urls import path
from djresty import rest, plugins
from netWeb.models import *


class ServicesApi(rest.RestyView):
    @rest.resty(
        url='get_list',
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


class PersonalApi(rest.RestyView):
    @rest.resty(
        url='get_list',
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


class OfficesApi(rest.RestyView):
    @rest.resty(
        url='get_list',
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
                       'office_name': office.FIO,
                       'address': office.address,
                       'telephone': office.telephone
                   },
            offices.append(data)
        offices = paginator(offices)
        return rest.RestyResponse({
            'offices': offices
        }, safe=False)


urlpatterns = [
    path('services/', ServicesApi(name='services').urls),
]