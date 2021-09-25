from django import forms
from .models import *

class shopform(forms.ModelForm):
    class Meta:
        model=shop
        fields='__all__'
