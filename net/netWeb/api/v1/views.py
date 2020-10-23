from django.core.handlers.wsgi import WSGIRequest
from django.urls import path
from djresty import rest, plugins
from netWeb.models import Services


class ServicesApi(rest.RestyView):
    @rest.resty(
        url='get_services',
        name='get-services',
        plugins=[
            plugins.MethodAllow(['GET']),
            plugins.ListPaginator(),
        ],
        csrf_exempt=True,
    )
    def get_services(self, request: WSGIRequest, paginator):
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


urlpatterns = [
    path('services/', ServicesApi(name='services').urls),
]