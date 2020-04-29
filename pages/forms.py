from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Uploadproperty


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        help_texts = {
            'username': None,
            'email': None,
            'password': None,

        }


class Upload_property(forms.ModelForm):
    class Meta:
        model = Uploadproperty
        fields = ['property_cat', 'property_type', 'project_name', 'description',
                  'price', 'image', 'image1', 'image2', 'image3', 'image4', 'contact_PersonName', 'contact_Number', 'contact_email']
