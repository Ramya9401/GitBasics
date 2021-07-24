from django.shortcuts import render,redirect
from django.http import HttpResponse
from restapp.forms import ReForm,ItemsForm,UsgForm,Rltype,Rlupd,Pfup,Chpwd
from restapp.models import Restaurants,Items,Rolereq,User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from restaurant import settings

# Create your views here.

def home(request):
	w=Restaurants.objects.filter(uid_id=request.user.id)
	t=Restaurants.objects.all()
	return render(request,'app/home.html',{'c':w,'y':t})

def about(request):
	return render(request,'app/about.html')

def contact(request):
	return render(request,'app/contact.html')

@login_required
def restnames(request):
	y=Restaurants.objects.filter(uid_id=request.user.id)
	if request.method=="POST":
		t=ReForm(request.POST,request.FILES)
		if t.is_valid():
			c=t.save(commit=False)
			c.uid_id=request.user.id
			c.save()
			messages.success(request,"Restaurant added successfully")
			return redirect('/restnames')
	t=ReForm()
	return render(request,'app/restnames.html',{'q':t,'a':y})

@login_required
def rupdate(request,m):
	k=Restaurants.objects.get(id=m)
	if request.method=="POST":
		e=ReForm(request.POST,request.FILES,instance=k)
		if e.is_valid():
			e.save()
			messages.warning(request,"{} Restaurant updated succesfully".format(k.rname))
			return redirect('/restnames')
	e=ReForm(instance=k)
	return render(request,'app/rupdate.html',{'x':e})

def rdelete(request,r):
	l=Restaurants.objects.get(id=r)
	if request.method=="POST":
		messages.info(request,"{} Restaurant deleted successfully".format(l.rname))
		l.delete()
		return redirect('/restnames')
	return render(request,'app/rdelete.html',{'z':l})
@login_required
def rstview(request,n):
	a=Restaurants.objects.get(id=n)
	return render(request,'app/rstview.html',{'z':a})

@login_required
def items(request):
	st=list(Restaurants.objects.filter(uid_id=request.user.id))
	mm=Items.objects.all()
	d,i={},0
	for mp in mm:
		for h in st:
			if mp.rsid_id == h.id:
				d[i] = mp.iname,mp.icategory,mp.price,mp.img,mp.iavail,mp.id,h.rname
				i=i+1
	if request.method=="POST":
		k=ItemsForm(request.POST,request.FILES)
		if k.is_valid():
			n=k.save(commit=False)
			messages.success(request,'{} item is added successfully'.format(n.iname))
			n.save()
			return redirect('/items')
	k=ItemsForm()
	return render(request,'app/items.html',{'r':k,'er':st,'s':d.values()})

@login_required
def iupdate(request,u):
	k=Items.objects.get(id=u)
	if request.method=="POST":
		l=ItemsForm(request.POST,request.FILES,instance=k)
		if l.is_valid():
			l.save()
			messages.info(request,"{} items are updated".format(k.iname))
			return redirect('/items')
	l=ItemsForm(instance=k)
	return render(request,'app/iupdate.html',{'m':l})

	
def idelete(request,d):
	t=Items.objects.get(id=d)
	if request.method=="POST":
		messages.warning(request,"{} item is deleted".format(t.iname))
		t.delete()
		return redirect('/items')
	return render(request,'app/idelete.html',{'z':t})

def itview(request,v):
	a=Items.objects.get(id=v)
	return render(request,'app/itview.html',{'z':a})

def registration(request):
	if request.method=="POST":
		d=UsgForm(request.POST)
		if d.is_valid():
			d.save()
			return redirect('/login')
	d=UsgForm()
	return render(request,'app/reg.html',{'t':d})

@login_required
def rolereq(request):
	p=Rolereq.objects.filter(ud_id=request.user.id).count()
	if request.method=="POST":
		k=Rltype(request.POST,request.FILES)
		if k.is_valid():
			y=k.save(commit=False)
			y.ud_id=request.user.id
			y.uname=request.user.username
			y.save()
			return redirect('/')
	k=Rltype()
	return render(request,'app/rolereq.html',{'d':k,'c':p})

@login_required
def gvpr(request):
	u=User.objects.all()
	r=Rolereq.objects.all()
	d={}
	for n in u:
		for m in r:
			if n.is_superuser == 1 or n.id!=m.ud_id:
				continue
			else:
				d[m.id]=m.uname,m.rltype,n.role,n.id
	return render(request,'app/gvpr.html',{'h':d.values()})

@login_required
def gvupdate(request,u):
	y=Rolereq.objects.get(ud_id=u)
	d=User.objects.get(id=u)
	if request.method=="POST":
		n=Rlupd(request.POST,instance=d)
		if n.is_valid():
			n.save()
			y.is_checked=1
			y.save()
			return redirect('/gvpr')
	n=Rlupd(instance=d)
	return render(request,'app/gvupdate.html',{'c':n})

@login_required
def profile(request):
	return render(request,'app/profile.html')

@login_required
def pfupdate(request):
	y=User.objects.get(id=request.user.id)
	if request.method=="POST":
		pfl=Pfup(request.POST,request.FILES,instance=y)
		if pfl.is_valid():
			pfl.save()
			return redirect('/profile')
	pfl=Pfup(instance=y)
	return render(request,'app/pfupdate.html',{'z':pfl})

@login_required
def feedback(request):
	if request.method=="POST":
		sd=request.POST['snmail'].split(',')
		sm=request.POST['sub']
		mg=request.POST['msg']
		rt=settings.EMAIL_HOST_USER
		dt=send_mail(sm,mg,rt,sd)
		if dt == 1:
			return redirect('/')
	return render(request,'app/feedback.html')

@login_required
def changepwd(request):
	if request.method=="POST":
		k=Chpwd(user=request.user,data=request.POST)
		if k.is_valid():
			k.save()
		return redirect('/')
	k=Chpwd(user=request)
	return render(request,'app/chpwd.html',{'t':k})


