from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2',)
    username = forms.CharField(
        required=True,
        label='ID',
        widget= forms.TextInput(
          attrs = {
            'class' : 'form-control',
            'placeholder' : '영문 소문자 또는 영문 대문자, 숫자 조합 6~12 자리',
            'style' : 'color:rgb(102, 77, 3);'
                      'border-color:rgb(230, 217, 179);',
          }
        )
    )
    email = forms.EmailField(
        required=True,
        label='Email',
        widget= forms.EmailInput(
          attrs = {
            'class' : 'form-control',
            'placeholder' : 'Email 입력',
            'style' : 'color:rgb(102, 77, 3);'
                      'border-color:rgb(230, 217, 179);',
          }
        )
    )
    password1 = forms.CharField(
        required=True,
        label='Password1',
        widget= forms.PasswordInput(
          attrs = {
            'class' : 'form-control',
            'placeholder' : '영문, 숫자, 특수문자(~!@#$%^&*) 조합 8~15 자리',
            'style' : 'color:rgb(102, 77, 3);'
            'border-color:rgb(230, 217, 179);',
          }
        )
    )
    password2 = forms.CharField(
        required=True,
        label='Password2',
        widget= forms.PasswordInput(
          attrs = {
            'class' : 'form-control',
            'placeholder' : '영문, 숫자, 특수문자(~!@#$%^&*) 조합 8~15 자리',
            'style' : 'color:rgb(102, 77, 3);'
            'border-color:rgb(230, 217, 179);',
          }
        )
    )



class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = get_user_model()
        fields = ('username', 'email', 'image',)
    username = forms.CharField(
        required=True,
        label='ID',
        widget= forms.TextInput(
          attrs = {
            'class' : 'form-control',
            'placeholder' : 'ID 입력',
            'style' : 'color:rgb(102, 77, 3);'
                      'border-color:rgb(230, 217, 179);',
          }
        )
    )
    email = forms.EmailField(
        required=True,
        label='Email',
        widget= forms.EmailInput(
          attrs = {
            'class' : 'form-control',
            'placeholder' : 'Email 입력',
            'style' : 'color:rgb(102, 77, 3);'
                      'border-color:rgb(230, 217, 179);',
          }
        )
    )
    image = forms.ImageField(
        required=False,
        label='Profile_image',
        widget= forms.ClearableFileInput(
          attrs = {
            'class' : 'form-control',
          }
        )
    )

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        max_length=30,
        required=True,
        label='ID',
        widget= forms.TextInput(
          attrs = {
            'class' : 'form-control',
            'placeholder' : 'ID 입력',
            'style' : 'color:rgb(102, 77, 3);'
                      'border-color:rgb(230, 217, 179);',
          }
        )
    )
    password = forms.CharField(
        label='Password',
        widget= forms.PasswordInput(
          attrs = {
            'class' : 'form-control',
            'placeholder' : 'Password 입력',
            'style' : 'color:rgb(102, 77, 3);'
                      'border-color:rgb(230, 217, 179);',
          }
        )
    )