from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class RegisterForm(UserCreationForm):
    # email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1']


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfilePicForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
