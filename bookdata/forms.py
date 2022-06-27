from django import forms
from.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


class LogBookRegister(UserCreationForm):
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    firstname = forms.CharField(max_length=20)
    lastname =  forms.CharField(max_length=20)
    password = forms.PasswordInput()
    class Meta:
        model = User
        fields = ('username','email','firstname','lastname','password1','password2')


# logbook fields
class LogBookForm(forms.ModelForm):   
    class Meta:
        model = LogBookData
        fields = '__all__'
    


class UserForm(forms.ModelForm):
    pass


class ProfileForm(forms.ModelForm):
    class Meta:
        model =  Profile
        fields = '__all__'
     



