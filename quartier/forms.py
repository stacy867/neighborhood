from .models import BusinessClass,Profile
from django import forms

class NewBizForm(forms.ModelForm):
    class Meta:
        model = BusinessClass
        exclude = ['user']

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']        