from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegForm(UserCreationForm):
	email= forms.EmailField()
	class Meta():
		model=User
		fields=['username','email','password1','password2']


class LoginForm(forms.Form):
	username=forms.CharField(max_length=200)
	password=forms.CharField(max_length=200, widget=forms.PasswordInput)

class CreationForm(forms.ModelForm):
	class Meta():
		model=Post
		fields=['title','content']