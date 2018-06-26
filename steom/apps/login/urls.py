from django.urls import path
from . import views

urlpatterns = [
	path('', views.login_auth, name='login_auth'),
	path('logout', views.logout_auth, name='logout_auth'),
]