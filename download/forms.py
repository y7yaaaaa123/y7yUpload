from dataclasses import field
from django import forms
from .models import *
class Uplode(forms.ModelForm):
    class Meta:
        model =FilesAdmin
        fields='__all__'