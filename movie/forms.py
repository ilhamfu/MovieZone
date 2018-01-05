from django import forms

class LoginForm(forms.Form):
	Username = forms.CharField(max_length=100)
	Password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
	Username = forms.CharField(max_length=100)
	Password = forms.CharField(widget=forms.PasswordInput)
	First = forms.CharField(max_length=100)
	Last = forms.CharField(max_length=100)
