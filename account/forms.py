from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation

class Loginform(forms.Form):
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"class":"form-control"}))

class Regform(UserCreationForm):
    password1 = forms.CharField(
            label="Password",
            required=False,
            strip=False,
            widget=forms.PasswordInput(attrs={"autocomplete": "new-password","class":"form-control"}),
            help_text=password_validation.password_validators_help_text_html(),
        )
    password2 = forms.CharField(
            label="Password confirmation",
            required=False,
            widget=forms.PasswordInput(attrs={"autocomplete": "new-password","class":"form-control"},),
            strip=False,
            help_text=("Enter the same password as before, for verification."),
        )
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control","placeholder":"enter Firstname"}),
            "last_name":forms.TextInput(attrs={"class":"form-control","placeholder":"enter lastname"}),
            "email":forms.TextInput(attrs={"class":"form-control","placeholder":"enter email"}),
            "username":forms.TextInput(attrs={"class":"form-control","placeholder":"enter username"}),
         
        }
          
        