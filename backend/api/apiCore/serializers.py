from rest_framework import serializers
from api.models import *


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
        fields = ['id', 'FIO', 'service', 'email', 'master', 'time', 'branch_office']


class ServiceSignupSerializerDisplay(serializers.ModelSerializer):
    service = serializers.CharField(
        source='service.name',
        read_only=True
    )
    master = serializers.CharField(
        source='master.FIO',
        read_only=True
    )
    time = serializers.CharField(
        source='time.__str__',
        read_only=True
    )
    branch_office = serializers.CharField(
        source='branch_office.address',
        read_only=True
    )

    class Meta:
        model = ServiceSignup
        fields = ['id', 'FIO', 'service', 'master', 'time', 'branch_office']


class SignupTimeSerializer(serializers.ModelSerializer):
    time = serializers.CharField(
        source='__str__'
    )

    class Meta:
        model = SignupTime
        fields = ['id', 'master', 'time']