from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        max_length=100,
        required=True,
        help_text='Digite um Email válido.',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite um Email Válido',

            })
    )


    first_name = forms.CharField(
        max_length=40,
        required=True,
        help_text='Digite seu Primeiro Nome.',
        widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Seu Primeiro Nome',            
            })
    )

    last_name = forms.CharField(
        max_length=150,
        required=True,
        help_text='Digite o restante do nome.',
        widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Complete o Nome',            
            })
    )

    username = forms.CharField(
        max_length=50,
        required=True,
        help_text='Escolha seu nome de Usuário.',
        widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Este Nome de Usuário será usado para o Login',            
            })
    )

    password1 = forms.CharField(
        required=True,
        help_text='Digite uma senha.',
        widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite uma Senha',            
            })
    )

    password2 = forms.CharField(
        required=True,
        help_text='Repita sua senha.',
        widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Repita a Senha',            
            })
    )

    checkterms = forms.BooleanField(
        required= True,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )


    class Meta:
        model = User
        fields = [
            'email', 'first_name', 'last_name', 'username', 
            'password1', 'password2', 'checkterms', 
        ]


class UserAuthenticationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')

    def clean(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            if not authenticate(username=username, password=password):
                raise forms.ValidationError('Erro - Verifique os dados') 