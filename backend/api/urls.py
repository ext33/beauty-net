from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from .views import *

urlpatterns = [
    path('', index_view, name='index'),
    path('api/', include(('api.apiCore.router', 'api'), namespace='api')),
    path('admin/', admin.site.urls),
] \
 # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
