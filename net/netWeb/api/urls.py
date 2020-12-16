from django.urls import include
from django.urls import path

urlpatterns = [
    path('v2/', include(('netWeb.api.v2.router', 'netWeb'), namespace='v2')),
]
