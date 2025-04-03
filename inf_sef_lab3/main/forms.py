from django import forms
from .models import Product


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)


class MyForm(forms.Form):
    myvalue = forms.CharField(label='MyValue')
