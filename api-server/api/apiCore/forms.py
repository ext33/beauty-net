from django import forms
from django.http import Http404
from django.shortcuts import get_object_or_404

from api.models import ServiceSignup


class ServiceSignupForm(forms.ModelForm):
    class Meta:
        model = ServiceSignup
        fields = ['FIO', 'service', 'email', 'time', 'master', 'branch_office']

    def __init__(self, *args, **kwargs):
        super(ServiceSignupForm, self).__init__(*args, **kwargs)
        for key in self.fields:
            self.fields[key].required = True

    def update(self, pk):
        instance = get_object_or_404(ServiceSignup.objects.all(), pk=pk)
        if self.is_valid():
            instance.FIO = self.cleaned_data['FIO']
            instance.service = self.cleaned_data['service']
            instance.time = self.cleaned_data['time']
            instance.master = self.cleaned_data['master']
            instance.branch_office = self.cleaned_data['branch_office']
            instance.save(update_fields=['FIO', 'service', 'time', 'master', 'branch_office'])
            return instance
        else:
            raise Http404
