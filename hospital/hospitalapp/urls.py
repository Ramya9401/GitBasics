from django.urls import path
from hospitalapp import views
from django.contrib.auth import views as v

urlpatterns = [
	path('',views.home,name='hm'),
	path('about/',views.about,name="ab"),
	path('main/',views.main,name="mp"),
	path('dlist/',views.dlist,name="dl"),
	path('dupdate/<int:u>/',views.dlupdate,name="dup"),
	path('dldelete/<int:d>/',views.dldelete,name="ddl"),
	path('dview/<int:v>/',views.dlview,name="dv"),
	path('plist/',views.plist,name="pl"),
	path('pupdate/<int:u>/',views.pupdate,name="pup"),
	path('pdelete/<int:d>/',views.pdelete,name="pdl"),
	path('reg/',views.registration,name="reg"),
	path('login/',v.LoginView.as_view(template_name='code/login.html'),name="lg"),
	path('logout/',v.LogoutView.as_view(template_name='code/logout.html'),name="lgo"),
	path('roletype/',views.rolereq,name='rlrq'),
	path('gvpr/',views.gvpr,name="gvpr"),
	path('gvupdate/<int:u>/',views.gvupdate,name="gvup"),
	path('gvdelete/<int:d>/',views.gvdelete,name="gvdl"),
	path('profile/',views.profile,name="pf"),
	path('profupdate/',views.pfupdate,name="pfup"),
	path('chpwd/',views.changepwd,name="chpwd"),
	path('pdetails/<int:v>/',views.pdetails,name="pd"),
	path('pview/',views.pview,name="pv"),
	path('medic/',views.medic,name="md"),
	path('mupdate/',views.mupdate,name="mdup"),
	path('pmview/',views.pmview,name="pmv"),
]