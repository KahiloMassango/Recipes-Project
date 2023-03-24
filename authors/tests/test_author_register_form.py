from django.test import TestCase
from authors.forms import RegisterForm
from parameterized import parameterized


class AuthorRegisterFormUnitTest(TestCase):
    @parameterized.expand([
        ('first_name', 'Ex.: John'),
        ('last_name', 'Ex.: Doe'),
        ('username', 'Your username'),
        ('email', 'Your e-mail'),
        ('password', 'Password'),
        ('password2', 'Confirm password')
    ])
    def test_fields_placeholder(self, field, placeholder):
        form = RegisterForm()
        current_placeholder = form[field].field.widget.attrs['placeholder']
        self.assertEqual(placeholder, current_placeholder)

    @parameterized.expand([
        ('username', ('Obrigatório. 150 caracteres ou menos. Letras, números e @/./+/-/_ apenas.')),
        ('email', 'E-mail must be valid.'),
        ('password', (
            'Password must have at least one uppercase letter'
            'one lowercase letter and one number.'
            'Length should be at least 8 charecters.'
        )),
    ])
    def test_fields_help_text(self, field, help_text):
        form = RegisterForm()
        field_help_text = form[field].field.help_text
        self.assertEqual(help_text, field_help_text)
