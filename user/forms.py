from django import forms
from.models import *

class Userprofileform(forms.ModelForm):
    class Meta:
        model = Userprofile
        fields='__all__'
