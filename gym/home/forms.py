from django.forms import ModelForm
from django import forms
from home.models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['fist_name',
                  'last_name',
                  'adress',
                  'email',
                  'phone',
                  ]
