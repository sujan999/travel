from django import forms

from .models import Contact
from .models import Hero


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['fullname', 'email', 'address', 'phone_number', 'message']


class HeroForm(forms.ModelForm):
    class Meta:
        model = Hero
        fields = ['image', 'caption', 'sub_headings']
