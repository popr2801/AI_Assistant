from django import forms
from .models import User,Files

class fileForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ['uploaded_file']

class questionForm(forms.Form):
    question = forms.CharField()

class loginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': ' Email','class': 'email-input'}),
        label=''
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': ' Password','class': 'password-input'}),
        label=''
    )

class registerForm(forms.ModelForm):
    first_name = forms.CharField(
        widget = forms.TextInput(attrs={'placeholder': 'First Name'}),
        label = ''
    )
    last_name = forms.CharField(
        widget = forms.TextInput(attrs={'placeholder': 'Last Name'}),
        label = ''
    )
    email = forms.EmailField(
        widget = forms.EmailInput(attrs={'placeholder': ' Email','class': 'email-input'}),
        label = ''
    )
    password = forms.CharField(
        widget = forms.PasswordInput(attrs={'placeholder': ' Password','class': 'password-input'}),
        label = ''
    )
    class Meta:
        model = User
        fields = ["first_name","last_name","email"]