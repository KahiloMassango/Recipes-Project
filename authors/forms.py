from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name', 
            'last_name',
            'username',
            'email',
            'password',
        ]   
        labels = {
            'username':'Username',
            'first_name':'First name',
            'last_name': 'Last name',
            'email':'E-mail',
            'password':'Password',
        }
        help_texts = {
            'email':'O E-mail tem que ser válido'
        }
        error_messages = {
            'username': {
                'required':'Este campo não pode estar vazio.',
            }
        }
        widgets = {
            'first_name': forms.TextInput(attrs={
            'placeholder':'First Name'
            }),
            'last_name': forms.TextInput(attrs={
            'placeholder':'Last Name'
            }),
            'username': forms.TextInput(attrs={
            'placeholder':'Username'
            }),
            'password': forms.PasswordInput(attrs={
            'placeholder':'Type your password here'
            }),
        }