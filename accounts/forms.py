from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2',)


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = get_user_model()
        fields = ('username', 'email',)

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        max_length=30,
        required=True,
        label='ID',
        widget= forms.TextInput(
          attrs = {
            'class' : 'form-control',
            'placeholder' : 'ID 입력'
          }
        )
    )
    password = forms.CharField(
        label='pssword',
        widget= forms.PasswordInput(
          attrs = {
            'class' : 'form-control',
            'placeholder' : 'password 입력'
          }
        )
    )