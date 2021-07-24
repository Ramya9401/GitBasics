from django.shortcuts import render,redirect
from django.http import HttpResponse
from firstapp.models import Register
# Create your views here.

def home(request):
	return HttpResponse("hi good evening to all.......")

def htmltag(request):
	return HttpResponse("<h2>Hi welcome to APSSDC programs</h2>")

def usernameprint(request,uname):
	return HttpResponse("<h2>Hi welcome <span style='color:blue'>{}</span></h2>".format(uname))

def usernameandage(request,un,ag):
	return HttpResponse("<h3 style='text-align:center;background-color:pink;padding:23px'> Hi user <span style='color:yellow'>{}</span> and your age is <span style='color:blue'>{}</span></h3>".format(un,ag))

def empdetails(request,eid,ename,eage):
	return HttpResponse("<script>alert('Hi welcome {}')</script><h3> Hi welcome <span style='color:yellow'>{}</span> and your age is <span style='color:blue'>{}</span> and your id is {}</h3>".format(ename,ename,eage,eid))

def htm(request):
	return render(request,'html/sample.html')

def ytname(request,name):
	return render(request,'html/ytname.html',{'n':name})

def empname(request,id,ename):
	k={'i':id,'n':ename}
	return render(request,'html/ehtml.html',k)

def studentdetails(request):
	return render(request,'html/stud.html')

def internaljs(request):
	return render(request,'html/internaljs.html')

def myform(request):
	if request.method=="POST":
		#print(request.POST)    # to get all the details at once
		name=request.POST['name']
		rollno=request.POST['rollno']
		mailid=request.POST['mailid']
		#print(name,rollno,mailid)     # to get details one by one
		data={'username':name,'rno':rollno,'email':mailid}
		return render(request,'html/display.html',data)

	return render(request,'html/myform.html')

def task1(request):
	if request.method=="POST":
		first=request.POST['fname']
		last=request.POST['lname']
		email=request.POST['emailid']
		number=request.POST['number']
		gender=request.POST['gender']
		address=request.POST['address']
		language=request.POST.getlist('checkbox')
		clanguage=request.POST['Language']
		data={'fname':first,'lname':last,'emailid':email,'number':number,'gender':gender,'address':address,'language':language,'clanguage':clanguage}
		return render(request,'html/disptask1.html',data)
	return render(request,'html/task1.html')

def task2(request):
	if request.method=="POST":
		uname=request.POST['username']
		pword=request.POST['password']
		data={'username':"ramya090401@gmail.com",'password':"Ammaramya@1"}
		if uname in data.values():
			if pword in data.values():
				return HttpResponse("user is valid")
		else:
			return HttpResponse("user is not valid")
	return render(request,'html/task2.html')

def bootstrapfun(request):
	return render(request,'html/btstrp.html')

def btstrpform(request):
	return render(request,'html/btstrpform.html')

def btregi(request):
	return render(request,'html/btregi.html')

def orgreg(request):
	reg=Register(name="vidhya",email="vidhya@gmail.com")
	reg.save()
	return HttpResponse("details are entered")

def reg1(request):
	if request.method=="POST":
		name=request.POST['name']
		email=request.POST['email']
		reg=Register(name=name,email=email)
		reg.save()
		return HttpResponse("details are entered")
	return render(request,'html/orgreg.html')

def retrive(request):
	reg=Register.objects.all()
	data={'data':reg}
	return render(request,'html/retrive.html',data)

def sview(request,y):
	w=Register.objects.get(id=y)
	return render(request,'html/sview.html',{'y':w})
	#return HttpResponse("your name is : {} and your emailid is: {}".format(w.name,w.email))

def supdate(request,u):
	t=Register.objects.get(id=u)
	if request.method=="POST":
		name=request.POST['name']
		email=request.POST['email']
		t.name=name
		t.email=email
		t.save()
		return redirect('/retrive')
	return render(request,'html/supdate.html',{'u':t})

def sdelete(request,d):
	b=Register.objects.get(id=d)
	if request.method=="POST":
		b.delete()
		return redirect('/retrive')
	return render(request,'html/sdelete.html',{'z':b})













