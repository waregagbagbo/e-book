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
        #phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$',error_message = ("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))
        exclude = ['user']      
 

#This is now the full  user profile form
class ProfileForm(forms.ModelForm):
    rst_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField() 

    class Meta:
        model =  Profile
        fields = '__all__'
        exclude = ['user']


def form_validation_error(form):
    msg = ""
    for field in form:
        for error in field.errors:
            msg += "%s: %s \\n" % (field.label if hasattr(field, 'label') else 'Error', error)
    return msg




     



