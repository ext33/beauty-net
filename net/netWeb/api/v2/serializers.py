from rest_framework import serializers
from netWeb.models import *


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ['id', 'name', 'duration', 'price', 'master']


class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal
        fields = ['id', 'FIO', 'telephone', 'address', 'employment_date', 'branch_office']


class BranchOfficesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchOffice
        fields = ['id', 'office_name', 'address', 'telephone']


class ServiceSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceSignup
        fields = ['id', 'FIO', 'service', 'time', 'master', 'branch_office']
