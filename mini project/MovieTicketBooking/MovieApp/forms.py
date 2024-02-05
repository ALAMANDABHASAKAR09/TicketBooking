from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User,Movie

class UserForm(UserCreationForm):
	password1=forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2",
		"placeholder":"Password",
		}))
	password2=forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control my-2",
		"placeholder":"Password Again",
		}))
	class Meta:
		model = User
		fields= ["username","uid"]
		widgets={
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Username",
			}),
		"uid":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Unique Id",
			}),
		}
class MovieForm(forms.ModelForm):
	class Meta:
		model=Movie
		fields=["movie","moviename","language","showtime","price"]
		widgets={
		"movie":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Movie Title",
			}),
		"moviename":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"U/A or A",
			}),
		"language":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Language",
			}),
		"showtime":forms.Select(attrs={
			"class":"form-control my-2",
			"placeholder":"Show Timings",
			}),
		"price":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Price",
			}),
		}