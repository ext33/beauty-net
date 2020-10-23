from django import forms
from netWeb.models import ServiceSignup


class ServiceSignupForm(forms.ModelForm):
    class Meta:
        model = ServiceSignup
        fields = ['FIO', 'service', 'time', 'master', 'branch_office']

    def __init__(self, *args, **kwargs):
        super(ServiceSignupForm, self).__init__(*args, **kwargs)
        for key in self.fields:
            self.fields[key].required = True
