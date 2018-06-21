from django.urls import path
from apps.games import views

urlpatterns = [
	path('', views.index, name='index')
]