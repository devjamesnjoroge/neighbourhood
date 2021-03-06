from django import forms
from .models import *
from django.contrib.auth.models import User as auth_User

class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        fields = ['name', 'location', 'occupants', 'hood_image']
        exclude = ['admin']

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['business_name', 'business_email', 'business_snap_pic']
        exclude = ['user', 'neighbourhood']
