from django import forms

class fileForm(forms.Form):
    file = forms.FileField(required=False)
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
