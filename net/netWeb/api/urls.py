from django.urls import include
from django.urls import path

urlpatterns = [
    path('v1/', include(('netWeb.api.v1.views', 'netWeb'), namespace='v1')),
    path('v2/', include(('netWeb.api.v2.router', 'netWeb'), namespace='v2')),
]
