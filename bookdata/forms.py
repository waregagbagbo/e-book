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
    

# create a user form to enable profile be changed by the user
class UserUpdateForm(forms.ModelForm):
    class Meta:
       model= User
       fields = ('username','first_name', 'last_name', 'email')
    

#This is now the full  user profile form
class ProfileForm(forms.ModelForm):    
    class Meta:
        model =  Profile
        fields = ('kndi_number','speciality','gender')




     



