from django import forms
from hospitalapp.models import Doctors,Patients,User,Rolereq,Medic
#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm


class Dform(forms.ModelForm):
	class Meta:
		model=Doctors
		fields=['dname','dage','special','exp','tfrom','tto','dimg']
		widgets={
		"dname":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"enter doctor name"}),
		"dage":forms.NumberInput(attrs={"class":"form-control my-2","placeholder":"enter age"}),
		"special":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"enter specialization"}),
		"exp":forms.NumberInput(attrs={"class":"form-control my-2","placeholder":"enter experience"}),
		"tfrom":forms.TimeInput(attrs={"class":"form-control my-2","placeholder":"enter from timings","type":"time"}),
		"tto":forms.TimeInput(attrs={"class":"form-control my-2","placeholder":"enter to timmings","type":"time"}),

		}

class Pform(forms.ModelForm):
	class Meta:
		model=Patients
		fields=['did','pname','page','diag','visits']
		widgets={
		"did":forms.Select(attrs={"class":"form-control my-2","placeholder":"Doctors list"}),
		"pname":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"enter patient name"}),
		"page":forms.NumberInput(attrs={"class":"form-control my-2","placeholder":"enter patient age"}),
		"diag":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"enter patient diagonization"}),
		"visits":forms.NumberInput(attrs={"class":"form-control my-2","placeholder":"enter patient visits"}),
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

class Mform(forms.ModelForm):
	Some_choices=[(1,'Morning'),(2,'Afternoon'),(3,'Night')]
	time=forms.MultipleChoiceField(choices=Some_choices,widget=forms.CheckboxSelectMultiple())
	class Meta:
		model=Medic
		fields=['med','time']
		widgets={
		"med":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"enter medicine"}),
		}
		