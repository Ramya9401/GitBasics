from django.shortcuts import render,redirect
from django.http import HttpResponse
from hospitalapp.models import Doctors,Patients,User,Rolereq,Medic
from hospitalapp.forms import Dform,Pform,UsgForm,Rltype,Rlupd,Pfup,Chpwd,Mform
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# Create your views here.

def home(request):
	t=Doctors.objects.filter(uid_id=request.user.id)
	g=Patients.objects.all()
	return render(request,'code/home.html',{'y':t,'l':g})

def about(request):
	return render(request,'code/about.html')

@login_required
def main(request):
	t=Doctors.objects.all()
	return render(request,'code/main.html',{'y':t})

@login_required
def dlist(request):
	y=Doctors.objects.filter(uid_id=request.user.id)
	if request.method=="POST":
		t=Dform(request.POST,request.FILES)
		if t.is_valid():
			c=t.save(commit=False)
			c.uid_id=request.user.id
			c.save()
			messages.success(request,"doctor is added succesfully")
			return redirect('/dlist')
	t=Dform()
	return render(request,'code/dlist.html',{'q':t,'a':y})

@login_required
def dlupdate(request,u):
	k=Doctors.objects.get(id=u)
	if request.method=="POST":
		e=Dform(request.POST,request.FILES,instance=k)
		if e.is_valid():
			e.save()
			messages.success(request,"{} details updated successfully".format(k.dname))
			return redirect('/dlist')
	e=Dform(instance=k)
	return render(request,'code/dlupdate.html',{'t':e})

@login_required
def dldelete(request,d):
	l=Doctors.objects.get(id=d)
	if request.method=="POST":
		messages.warning(request,"{} deleted successfully".format(l.dname))
		l.delete()
		return redirect('/dlist')
	return render(request,'code/dldelete.html')

@login_required
def dlview(request,v):
	v=Doctors.objects.get(id=v)
	return render(request,'code/dlview.html',{'z':v})

@login_required
def plist(request):
	st=list(Doctors.objects.filter(uid_id=request.user.id))
	y=Patients.objects.all()
	d,i={},0
	for l in y:
		for h in st:
			if l.did_id == h.id:
				d[i]=l.pname,l.diag,l.visits,l.id,h.dname
				i=i+1
	if request.method=="POST":
		t=Pform(request.POST,request.FILES)
		if t.is_valid():
			t.save()
			messages.success(request,"patient is added succesfully")
			return redirect('/plist')
	t=Pform()
	return render(request,'code/plist.html',{'y':t,'a':d.values(),'er':st})

@login_required
def pupdate(request,u):
	k=Patients.objects.get(id=u)
	if request.method=="POST":
		e=Pform(request.POST,request.FILES,instance=k)
		if e.is_valid():
			e.save()
			messages.success(request,"{} details updated successfully".format(k.pname))
			return redirect('/plist')
	e=Pform(instance=k)
	return render(request,'code/pupdate.html',{'t':e})

@login_required
def pdelete(request,d):
	t=Patients.objects.get(id=d)
	if request.method=="POST":
		messages.warning(request,"{} deleted successfully".format(t.pname))
		t.delete()
		return redirect('/plist')
	return render(request,'code/pdelete.html')


def registration(request):
	if request.method=="POST":
		d=UsgForm(request.POST)
		if d.is_valid():
			d.save()
			return redirect('/login')
	d=UsgForm()
	return render(request,'code/reg.html',{'t':d})

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
	return render(request,'code/rolereq.html',{'d':k,'c':p})


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
	return render(request,'code/gvpr.html',{'h':d.values()})

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
	return render(request,'code/gvupdate.html',{'c':n})

@login_required
def gvdelete(request,d):
	n = Rolereq.objects.get(id=d-1)
	t = User.objects.get(id=n.ud_id)
	if request.method == "POST":
		n.delete()
		t.role = 1
		t.save()
		return redirect('/gvpr')
	return render(request,'code/gvdlte.html',{'d':n})

@login_required
def profile(request):
	return render(request,"code/profile.html")

@login_required
def pfupdate(request):
	t=User.objects.get(id=request.user.id)
	if request.method=="POST":
		l=Pfup(request.POST,request.FILES,instance=t)
		if l.is_valid():
			l.save()
			messages.success(request,"profile updated successfully")
			return redirect('/profile')
	l=Pfup(instance=t)
	return render(request,"code/pfupdate.html",{'z':l})

@login_required
def changepwd(request):
	if request.method=="POST":
		t=Chpwd(user=request.user,data=request.POST)
		if t.is_valid():
			t.save()
			return redirect('/')
	t=Chpwd(user=request)
	return render(request,'code/chpwd.html',{'y':t})

@login_required
def pdetails(request,v):
	t=Patients.objects.filter(did_id=v)
	return render(request,'code/pdetails.html',{'a':t})

@login_required
def pview(request):
	t=Patients.objects.all()
	return render(request,'code/pview.html',{'a':t})

@login_required
def medic(request):
	m=Medic.objects.all()
	return render(request,'code/medic.html',{'l':m})

@login_required
def mupdate(request):
	if request.method=="POST":
		m=Mform(request.POST or None)
		if 'save' in request.POST:
			post=m.save()
		return redirect('/mupdate')
	else:
		m=Mform()
	return render(request,'code/mupdate.html',{'l':m})

@login_required
def pmview(request):
	m=Medic.objects.all()
	return render(request,'code/pmview.html',{'l':m})