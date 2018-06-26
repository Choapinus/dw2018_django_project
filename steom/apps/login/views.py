from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, logout, login

# Create your views here.

def login_auth(request):
	
	template = 'login.html'

	if request.POST:
		username = request.POST["user"]
		pwd = request.POST["pwd"]

		user = authenticate(username=username, password=pwd)

		if user is not None:
			login(request, user)
			# return HttpResponseRedirect(reverse('games_list'))
			return HttpResponse("welcome " + username)
		else:
			messages.warning(request, 'Usuario o contraseña invalidos')
	
	return render(request, 'login.html')

def logout_auth(request):
	logout(request)
	return redirect('login_auth')