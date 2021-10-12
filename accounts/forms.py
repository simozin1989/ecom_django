from django import forms
from django.forms import fields
from . import models
from django.contrib.auth.models import User



class UserForm(forms.ModelForm):

    class Meta:
        models = User
        fields  = ['username','firstname','last_name','email']




class ProfileForm(forms.ModelForm):
    class Meta:
        models = models.Profile
        fields  = ['image','country','address']



