from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re


def strong_password(password):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')
    if not regex.match(password):
        raise ValidationError(
            'Password does not meet the requirements'
        )


class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
        help_text=(
            'Password must have at least one uppercase letter'
            'one lowercase letter and one number.'
            'Length should be at least 8 charecters.'
        ),
        error_messages={
            'required': 'Password must not be empty'
        },

        validators=[strong_password]
        )
    password2 = forms.CharField(
        label='Confirm password',
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'})
        )

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
            'username': 'Username',
            'first_name': 'First name',
            'last_name': 'Last name',
            'email': 'E-mail',
        }
        help_texts = {
            'email': 'E-mail must be valid.'
        }
        error_messages = {
            'username': {
                'required': 'Username must not be empty.',
            }
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Ex.: John'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Ex.: Doe'}),
            'username': forms.TextInput(attrs={'placeholder': 'Your username'}),  # noqa
            'email': forms.EmailInput(attrs={'placeholder': 'Your e-mail'})
        }

    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            password_confirmation_error = ValidationError('Password and Password2 must be equal', code='invalid')  # noqa   
            raise ValidationError({
                'password': password_confirmation_error,
                'password2': password_confirmation_error,
            })
