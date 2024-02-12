from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField()
    # widget : Mask all the characters which will be typed in that form
    password = forms.CharField(widget=forms.PasswordInput)
    
# This form is goinf to use inbuilt 'User' model provided by django
class UserRegistrationForm(forms.ModelForm):
    
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = {'username','email','first_name'}
    
    # Checking if password == password2
    def check_password(self):
        if self.cleaned_data['password'] != self.cleaned_data['password2']:
            raise forms.ValidationError('Passwords do not match!')
        return self.cleaned_data['password2']