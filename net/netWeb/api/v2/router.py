from django.urls import path
from .views import *


urlpatterns = [
    path('services-list/', ServicesViewSet.as_view({'get': 'list'}), name='services-list'),
    path('services-by-pk/<int:pk>', ServicesViewSet.as_view({'get': 'by_pk'}), name='services-by-pk'),
    path('personal-list/', PersonalViewSet.as_view({'get': 'list'}), name='personal-list'),
    path('personal-by-pk/<int:pk>', PersonalViewSet.as_view({'get': 'by_pk'}), name='personal-by-pk'),
    path('offices-list/', BranchOfficesViewSet.as_view({'get': 'list'}), name='offices-list'),
    path('offices-by-pk/<int:pk>', BranchOfficesViewSet.as_view({'get': 'by_pk'}), name='offices-by-pk'),
    path('create-signup/', ServiceSignupViewSet.as_view({'post': 'create'}), name='create-signup'),
    path('update-signup/<pk>', ServiceSignupViewSet.as_view({'post': 'update'}), name='update-signup'),
    path('signup-by-pk/<pk>', ServiceSignupViewSet.as_view({'get': 'by_pk'}), name='signup-by-pk'),
    path('signup-time/<pk>', SignupTimeViewSet.as_view({'get': 'by_master'}), name='signup-time'),
    path('signup-cancel/<pk>', ServiceSignupViewSet.as_view({'get': 'cancel'}), name='signup-cancel'),
]
