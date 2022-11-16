from django import forms
from django.contrib.auth.models import User


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'date_joined')
        widgets = {
            'username': forms.TextInput(attrs={'disabled': True}),
            'email': forms.TextInput(attrs={'disabled': True}),
            'first_name': forms.TextInput(attrs={'disabled': True}),
            'last_name': forms.TextInput(attrs={'disabled': True}),
            'date_joined': forms.TextInput(attrs={'disabled': True}),
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
