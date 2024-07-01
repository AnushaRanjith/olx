from django import forms
from django.contrib.auth.models import User
from olxapp.models import OlxModel

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password"]

class UserLoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","password"]


class EditForm(forms.ModelForm):
    class Meta:
        model=OlxModel
        exclude=['user',]

        
