from django.contrib.auth.models import User
from django import forms

class UserForm(forms.Form):
	username = forms.CharField(
		label = 'Nombre de usuario', 
		max_length = 100,
		error_messages = {
				'invalid': "Este campo solo puede contener letras, numeros y @/./+/-/_ caracters."
		}
	)
	email = forms.EmailField()
	password = forms.CharField(label="Ingresa tu contraseña", widget=forms.PasswordInput)
	password_confirmation = forms.CharField(label="Reingresa tu contraseña", widget=forms.PasswordInput)

	def clean_username(self):            
		existing = User.objects.filter(username__iexact=self.cleaned_data['username'])
		if existing.exists():
			raise forms.ValidationError("El nombre de usuario que ha ingresado ya se encuentra en uso.")
		else:
			return self.cleaned_data['username']

	def clean_email(self):
		#if you want unique email address. else delete this function
		if User.objects.filter(email__iexact=self.cleaned_data['email']):
			raise forms.ValidationError("El email que ha ingresado ya se encuentra en uso.")
		return self.cleaned_data['email']

	def clean(self):
		if 'password' in self.cleaned_data and 'password_confirmation' in self.cleaned_data:
			if self.cleaned_data['password'] != self.cleaned_data['password_confirmation']:
				raise forms.ValidationError("Las contraseñas no coinciden.")
		return self.cleaned_data