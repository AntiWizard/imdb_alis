from django import forms

from users.models import CustomUser


class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "password"}), label="password")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "password confirm"}),
                                label="password confirm")

    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2')
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': "email@gmail.com"}),
        }


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "password"}))

    class Meta:
        model = CustomUser
        fields = ('email', 'password')
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': "email@gmail.com"}),
        }
