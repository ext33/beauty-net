from django.urls import include
from django.urls import path

urlpatterns = [
    path('v1/', include(('netWeb.api.v1.views', 'netWeb'), namespace='v1')),
]
