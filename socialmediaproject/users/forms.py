from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    # widget : Mask all the characters which will be typed in that form
    password = forms.CharField(widget=forms.PasswordInput)