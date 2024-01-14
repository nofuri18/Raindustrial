# accounts/forms.py
from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import UserCreationForm
from django import forms
# from django.contrib.auth.forms import AuthenticationForm

# class UserAdminCreationForm(UserCreationForm):
#     class Meta:
#         model = get_user_model()
#         fields = ['Email', 'full_name']

class LoginForm(forms.Form):
    email = forms.CharField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


