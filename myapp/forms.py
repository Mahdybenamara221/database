from django import forms
from myapp.models import Asset

class form(forms.ModelForm):
    class Meta:
        model=Asset
        fields="__all__"

