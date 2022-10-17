from django import forms

class ContectFrom(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.EmailField()
    content = forms.CharField()