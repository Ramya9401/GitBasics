from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
	age=models.IntegerField(default=20)
	mobilenumber=models.CharField(max_length=10,null=True)
	uimg=models.ImageField(upload_to='profilepics/',default='res.jpg')
	t=[(1,'guest'),(2,'manager'),(3,'user')]
	role=models.IntegerField(choices=t,default=1)

class Rolereq(models.Model):
	f=[(2,'manager'),(3,'user')]
	rltype=models.IntegerField(choices=f)
	pfe=models.ImageField(upload_to='Rolereqpics/',default='res.jpg')
	is_checked=models.BooleanField(default=False)
	uname=models.CharField(max_length=50)
	ud=models.OneToOneField(User,on_delete=models.CASCADE)


class Restaurants(models.Model):
	rname=models.CharField(max_length=30)
	nitems=models.IntegerField()
	timings=models.CharField(max_length=50)
	address=models.CharField(max_length=50)
	rsimg=models.ImageField(upload_to='Restaurantimages/',default='res.jpg')
	uid=models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return self.rname



class Items(models.Model):
	y=[('df','select item type'),('NV','non-veg'),('vg','veg'),]
	p=[('sl','select availability'),('AV',"available"),('NA','not-available')]
	iname=models.CharField(max_length=100)
	icategory=models.CharField(choices=y,default="df",max_length=12)
	price=models.DecimalField(decimal_places=3,max_digits=10)
	img=models.ImageField(upload_to='Itemsimages/',default="panner.jpg")
	iavail=models.CharField(choices=p,default='sl',max_length=20)
	rsid=models.ForeignKey(Restaurants,on_delete=models.CASCADE)