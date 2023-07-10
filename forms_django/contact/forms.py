from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre', max_length=100)
    surname = forms.CharField(label='Apellido', max_length=100)
    country = forms.CharField(label='País', max_length=100)
    university = forms.CharField(label='Universidad', max_length=100)
    career = forms.CharField(label='Carrera', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
