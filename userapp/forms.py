from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30,label='',
               widget=forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"User Name .."
               }) 
               )
    first_name = forms.CharField(max_length=30,label='',
               widget=forms.TextInput(attrs={
                   "class":"form-control",
                   "placeholder":"Enter your full name.."
               }) 
               )
    email = forms.EmailField(required=False,label='',
            widget=forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"Enter your email..(optional)"
            })
            )
    password1 = forms.CharField(max_length=30,label='',
               widget=forms.PasswordInput(attrs={
                   "class":"form-control",
                   "placeholder":"Password"
               }) 
               )
    password2 = forms.CharField(max_length=30,label='',
               widget=forms.PasswordInput(attrs={
                   "class":"form-control",
                   "placeholder":"confirmation Password"
               }) 
               )

    terms_and_conditions = forms.CharField(max_length=30,label='By signing up you agree to our terms and conditions.',
               widget=forms.CheckboxInput(attrs={
                   "class":"form-check-input tc_checkbox",          
               }) 
               )

    class Meta:
        model=User
        fields =['username', 'first_name', 'email','password1','password2']


class UpdateRegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields =[ 'username', 'first_name', 'last_name', 'email']

class UpdateProfileForm(forms.ModelForm):
    date_of_birthday = forms.DateField(required=False,
        widget=forms.TextInput( attrs={
        "type":"date",
    })
    )
    class Meta:
        model = Profile
        fields = ['image','date_of_birthday','phone','permanent_address','present_address']


from django.contrib.auth.forms import AuthenticationForm, UsernameField

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(label = "Phone",widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your phone number',}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password',
        }
))