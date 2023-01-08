from django import forms
from . models import shop

class ProdForm(forms.ModelForm):
    class Meta:
        model=shop
        fields=['name','desc','img','price']
