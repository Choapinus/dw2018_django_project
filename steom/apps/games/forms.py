from django import forms
from .models import Game, Developer

class GameForm(forms.ModelForm):
	class Meta:
		model = Game
		fields = '__all__'
		exclude = ['id']

class DeveloperForm(forms.ModelForm):
	class Meta:
		model = Developer
		fields = '__all__'
		exclude = ['id']