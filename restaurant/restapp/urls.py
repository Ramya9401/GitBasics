from django.urls import path
from restapp import views

urlpatterns = [
	path('',views.home,name='hm'),
	path('about/',views.about,name='ab'),
	path('contact/',views.contact,name='ct'),
	path('login/',views.login,name='ln'),

]