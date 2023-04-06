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

    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your username'}),
        label='Username',
        help_text=(
            'Username must have letters, numbers or one of those @.+-_.'
            'The length should be between 4 and 150 characters.'
        ),
        error_messages={
            'required': 'This field must not be empty',
            'min_length': 'Username must have at least 4 characters',
            'max_length': 'Username must have less than 150 characters',
        },
        min_length=4, max_length=150,
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Ex.: John'}),
        error_messages={'required': 'Write your first name'},
        label='First name'
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Ex.: Doe'}),
        error_messages={'required': 'Write your last name'},
        label='Last name'
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Your e-mail'}),
        error_messages={'required': 'E-mail is required'},
        label='E-mail',
        help_text='The e-mail must be valid',
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
        help_text=(
            'Password must have at least one uppercase letter'
            'one lowercase letter and one number.'
            'Length should be at least 8 charecters.'
        ),
        error_messages={
            'required': 'Password must not be empty',
            'error': (
                'Password does not meet the requirements'
                'Password and Password2 must be equal'
                'at least 8 characters.'
            )
        },

        validators=[strong_password]
        )
    password2 = forms.CharField(
        label='Password2',
        widget=forms.PasswordInput(attrs={'placeholder': 'Repeat your password'}),  # noqa
        error_messages={'required': 'Please, repeat your password'}
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
