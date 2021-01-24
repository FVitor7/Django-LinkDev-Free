from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


def verify_lenght_password(password):
    if len(password) < 8:
        raise forms.ValidationError("O password é muito pequeno!")


def verify_lenght_username(username):
    if len(username) < 5:
        raise forms.ValidationError("O nome de usuário é muito curto!")


def verify_username_exists(username):
    if User.objects.filter(username=username).exists() == True:
        raise forms.ValidationError("Username não disponivel!")


def verify_email_exists(email):
    if User.objects.filter(email=email).exists() == True:
        raise forms.ValidationError("E-mail não disponivel!")


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label='',
        max_length=254,
        validators=[verify_email_exists, ],
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        )
    )

    username = forms.CharField(
        label='',
        max_length=30,
        min_length=5,
        required=True,
        validators=[verify_lenght_username, verify_username_exists, ],
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control",
            }
        )
    )

    password1 = forms.CharField(
        label='',
        max_length=30,
        min_length=8,
        required=True,
        validators=[verify_lenght_password, ],
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control",
                "onkeyup": "check()",
                "id": "password1",
                'data-toggle': 'password',
                'autocomplete': 'off',
                'required data-eye': 'True'
            }
        )
    )

    password2 = forms.CharField(
        label='',
        max_length=30,
        min_length=8,
        required=True,
        validators=[verify_lenght_password, ],
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirm Password",
                "class": "form-control",
                "onkeyup": "check()",
                "id": "password2",
                'data-toggle': 'password',
                'autocomplete': 'off',
                'required data-eye': 'True'
            }
        )
    )

    class Meta:
        model = User

        fields = ('username', 'email', 'password1', 'password2',)

        def verify_two_passwords(self):
            cleaned_data = super(SignUpForm, self).clean()
            password = cleaned_data.get("password1")
            confirm_password = cleaned_data.get("password2")

            if password != confirm_password:
                raise forms.ValidationError(
                    "Você digitou duas senhas diferentes! Tente novamente."
                )
