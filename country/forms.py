from django import forms

class CountryForm(forms.Form):
    name = forms.CharField(max_length=40, label='Name')
    continent = forms.CharField(max_length=20, label='Continente')
    