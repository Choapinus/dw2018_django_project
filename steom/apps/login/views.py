from .forms import UserForm
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, logout, login

# Create your views here.

def login_auth(request):
	
	template = 'login.html'

	logout(request)

	if request.POST:
		username = request.POST["user"]
		pwd = request.POST["pwd"]

		user = authenticate(username=username, password=pwd)

		if user is not None:
			login(request, user)
			return HttpResponseRedirect(reverse('index'))
			# return render(request, 'base.html')
		else:
			messages.warning(request, 'Usuario o contraseña invalidos')
	
	return render(request, 'login.html')

def logout_auth(request):
	logout(request)
	return redirect('login_auth')

def register_user(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			username, email = form.cleaned_data['username'], form.cleaned_data['email']
			password = form.cleaned_data['password']
			new_user = User.objects.create_user(username, email, password)
			new_user.is_active = True
			new_user.save()
			return render(request, 'login.html')
	else:
		form = UserForm()

	return render(request, 'create_user.html', {'form': form})