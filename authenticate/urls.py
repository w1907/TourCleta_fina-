from django.urls import path
from django.conf.urls import url
from authenticate import views

urlpatterns = [
	path('signin/', views.signin, name="authenticate.signin"),
	path('signout/', views.signout, name="authenticate.signout"),
	path('register/', views.register, name="authenticate.register"),
	url(r'^profile/$', views.perfil, name='my_profile')
]