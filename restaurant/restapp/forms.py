#from django.forms import ModelForm
from restapp.models import Restaurants,Items,User,Rolereq
from django import forms
#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm

class ReForm(forms.ModelForm):
	class Meta:
		model=Restaurants
		fields=['rname','nitems','timings','rsimg','address']
		widgets={
		"rname":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"enter restaurant name",}),
		"nitems":forms.NumberInput(attrs={"class":"form-control my-2","placeholder":"enter number of items avaliabe in restaurant",}),
		"timings":forms.TimeInput(attrs={"class":"form-control my-2","placeholder":"enter timings","type":"time",}),
		"address":forms.Textarea(attrs={"class":"form-control my-2","placeholder":"enter address","rows":4,}),
		}

class ItemsForm(forms.ModelForm):
	class Meta:
		model=Items
		fields=['rsid','iname','icategory','price','iavail','img']
		widgets={
		"rsid":forms.Select(attrs={"class":"form-control my-2","placeholder":"select restaurant",}),
		"iname":forms.TextInput(attrs={'class':"form-control my-2","placeholder":"enter items list"}),
		"icategory":forms.Select(attrs={'class':"form-control my-2","placeholder":"enter item category"}),
		"price":forms.NumberInput(attrs={'class':"form-control my-2","placeholder":"enter price"}),
		"iavail":forms.Select(attrs={'class':"form-control my-2","placeholder":"enter items avaliability"}),
		}

class UsgForm(UserCreationForm):
	password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control mx-2","placeholder":"enter password"}))
	password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control mx-2","placeholder":"enter confirm password"}))
	class Meta:
		model=User
		fields=["username"]
		widgets={
		"username":forms.TextInput(attrs={"class":"form-control mx-2","placeholder":"enter username",}),
		}

class Rltype(forms.ModelForm):
	class Meta:
		model=Rolereq
		fields=["uname","rltype","pfe"]
		widgets={
		"rltype":forms.Select(attrs={"class":"form-control my-2",}),
		
		}

class Rlupd(forms.ModelForm):
	class Meta:
		model=User
		fields=["username","role"]
		widgets={
		"username":forms.TextInput(attrs={"class":"form-control my-2","readonly":True}),
		"role":forms.Select(attrs={"class":"form-control my-2"})
		}

class Pfup(forms.ModelForm):
	class Meta:
		model=User
		fields=["username","first_name","last_name","email","age","mobilenumber","uimg"]
		widgets={
		"username":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"update username"}),
		"first_name":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"update firstname"}),
		"last_name":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"update lastname"}),
		"email":forms.EmailInput(attrs={"class":"form-control my-2","placeholder":"update email"}),
		"age":forms.NumberInput(attrs={"class":"form-control my-2","placeholder":"update number"}),
		"mobilenumber":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"update mobilenumber"}),
		}
class Chpwd(PasswordChangeForm):
	old_password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control mx-2","placeholder":"enter old password"}))
	new_password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control mx-2","placeholder":"enter  new password"}))
	new_password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control mx-2","placeholder":" confirm password"}))
	class Meta:
		model=User
		fields=["old_password","new_password1","new_password2"]
		