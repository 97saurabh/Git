from django import forms
from . import models

class FormName(forms.Form):
    name=forms.IntegerField()
class ContactForm1(forms.ModelForm):
    class Meta:
        fields=('subject','sender')
        model= models.ContactModel1

class ContactForm2(forms.ModelForm):
    class Meta:
        fields=('message',)
        model= models.ContactModel2
