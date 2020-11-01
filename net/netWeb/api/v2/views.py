from rest_framework.response import Response
from rest_framework import viewsets

from netWeb.api.v2.forms import *
from netWeb.api.v2.serializers import *
from netWeb.models import Services, Personal


class ServicesViewSet(viewsets.ViewSet):
    queryset = Services.objects.all()

    def list(self, request):
        serializer = ServicesSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def by_pk(self, request, pk=None):
        service = get_object_or_404(self.queryset, pk=pk)
        serializer = ServicesSerializer(service)
        return Response(serializer.data)


class PersonalViewSet(viewsets.ViewSet):
    queryset = Personal.objects.all()

    def list(self, request):
        serializer = PersonalSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def by_pk(self, request, pk=None):
        service = get_object_or_404(self.queryset, pk=pk)
        serializer = PersonalSerializer(service)
        return Response(serializer.data)


class BranchOfficesViewSet(viewsets.ViewSet):
    queryset = BranchOffice.objects.all()

    def list(self, request):
        serializer = BranchOfficesSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def by_pk(self, request, pk=None):
        service = get_object_or_404(self.queryset, pk=pk)
        serializer = BranchOfficesSerializer(service)
        return Response(serializer.data)


class ServiceSignupViewSet(viewsets.ViewSet):
    queryset = ServiceSignup.objects.all()

    @staticmethod
    def create(request):
        form = ServiceSignupForm(request.POST)
        signup = form.save()
        serializer = ServiceSignupSerializer(signup)
        return Response(serializer.data)

    @staticmethod
    def update(request, pk=None):
        form = ServiceSignupForm(request.POST)
        new_signup = form.update(pk)
        serializer = ServiceSignupSerializer(new_signup)
        return Response(serializer.data)

    def by_pk(self, request, pk=None):
        signup = get_object_or_404(self.queryset, pk=pk)
        serializer = ServiceSignupSerializer(signup)
        return Response(serializer.data)
