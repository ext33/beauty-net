from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(BranchOffice)
class Office(admin.ModelAdmin):
    list_display = ('office_name', 'address', 'telephone')


@admin.register(Inventory)
class Inventory(admin.ModelAdmin):
    list_display = ('name', 'serial_number', 'price', 'quantity', 'delivery_date', 'branch_office')
    list_filter = ('delivery_date', 'branch_office')


@admin.register(Personal)
class Personal(admin.ModelAdmin):
    list_display = ('FIO', 'telephone', 'address', 'branch_office')
    list_filter = ('employment_date', 'branch_office')


@admin.register(Services)
class Services(admin.ModelAdmin):
    list_display = ('name', 'duration', 'price', 'master')
    list_filter = ('master',)


@admin.register(ServiceSignup)
class SignUp(admin.ModelAdmin):
    list_display = ('FIO', 'service', 'email', 'master', 'time', 'branch_office')
    list_filter = ('service', 'master', 'time', 'branch_office', 'signup_time')


@admin.register(SignupTime)
class SignupTime(admin.ModelAdmin):
    list_display = ('master', 'a_time', 'a_date')
    list_filter = ('master', 'a_date')
