from django.urls import path
from restapp import views
from django.contrib.auth import views as v

urlpatterns = [
	path('',views.home,name='hm'),
	path('about/',views.about,name='ab'),
	path('contact/',views.contact,name='ct'),
	path('restnames/',views.restnames,name="rl"),
	path('rupdate/<int:m>/',views.rupdate,name="ru"),
	path('rstview/<int:n>/',views.rstview,name="rstv"),
	path('items/',views.items,name='il'),
	path('iupdate/<int:u>/',views.iupdate,name="iu"),
	path('idelete/<int:d>/',views.idelete,name="id"),
	path('itview/<int:v>/',views.itview,name="iv"),
	path('reg/',views.registration,name="reg"),
	path('login/',v.LoginView.as_view(template_name='app/login.html'),name="lg"),
	path('logout/',v.LogoutView.as_view(template_name='app/logout.html'),name="lgo"),
	path('roletype/',views.rolereq,name='rlrq'),
	path('gvpr/',views.gvpr,name='gvpr'),
	path('gvupdate/<int:u>/',views.gvupdate,name="gvup"),
	path('profile/',views.profile,name="pf"),
	path('pfup/',views.pfupdate,name="pfup"),
	path('fdb/',views.feedback,name="fd"),
	path('chpwd/',views.changepwd,name="chpwd"),
]