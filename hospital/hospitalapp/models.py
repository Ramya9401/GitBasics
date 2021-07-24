from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
	age=models.IntegerField(default=20)
	mobilenumber=models.CharField(max_length=10,null=True)
	uimg=models.ImageField(upload_to='profilepics/',default='hosp.jpg')
	t=[(1,'Guest'),(2,' HR Manager'),(3,'Patient'),(4,'Doctor')]
	role=models.IntegerField(choices=t,default=1)

class Rolereq(models.Model):
	f=[(2,'HR Manager'),(3,'Patient'),(4,'Doctor')]
	rltype=models.IntegerField(choices=f)
	pfe=models.ImageField(upload_to='Rolereqpics/',default='hosp.jpg')
	is_checked=models.BooleanField(default=False)
	uname=models.CharField(max_length=50)
	ud=models.OneToOneField(User,on_delete=models.CASCADE)


class Doctors(models.Model):
	dname=models.CharField(max_length=20)
	dage=models.IntegerField()
	special=models.CharField(max_length=15)
	exp=models.IntegerField()
	tfrom=models.CharField(max_length=20)
	tto=models.CharField(max_length=20)
	dimg=models.ImageField(upload_to='Hospitalimages/',default='hosp.jpg')
	uid=models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return self.dname


class Patients(models.Model):
	pname=models.CharField(max_length=20)
	page=models.IntegerField()
	diag=models.CharField(max_length=30)
	visits=models.IntegerField()
	pimg=models.ImageField(upload_to='patientimages/',default='hosp.jpg')
	did=models.ForeignKey(Doctors,on_delete=models.CASCADE)
  
	def __str__(self):
		return self.pname

class Medic(models.Model):
	name=models.CharField(max_length=20)
	med=models.CharField(max_length=20)
	t=[(1,'morning'),(2,'Afternoon'),(3,'Night')]
	time=models.IntegerField(choices=t)
	