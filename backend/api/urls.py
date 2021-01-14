from django.urls import path, include
from django.contrib import admin
from .views import *

urlpatterns = [
    path('', index_view, name='index'),
    path('api/', include(('api.apiCore.router', 'api'), namespace='api')),
    path('admin/', admin.site.urls),
]
