from django.urls import path
from .views import *


urlpatterns = [
    path('services-list/', ServicesViewSet.as_view({'get': 'list'}), name='services-list'),
    path('services-by-pk/<int:pk>', ServicesViewSet.as_view({'get': 'by_pk'}), name='services-by-pk'),
    path('personal-list/', PersonalViewSet.as_view({'get': 'list'}), name='personal-list'),
    path('personal-by-pk/<int:pk>', PersonalViewSet.as_view({'get': 'by_pk'}), name='personal-by-pk'),

]
