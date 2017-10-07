from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre', max_length=100)
    file = forms.ImageField(label='Imagen')
    message = forms.CharField(label='Mensaje', max_length=100)
