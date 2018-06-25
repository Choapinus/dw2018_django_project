from django.shortcuts import render
from django.http import HttpResponse
from .models import Game
#from .form import *

# Create your views here.

def index(request):
	return HttpResponse('<p>holi</p>')


def addGame(request):
	template_name = ''
	if request.method == 'POST': # O get
		form = GameForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('index')


def removeGame(request, game_id):
	game = Game.objects.get(id=game_id)
	if game.delete():
		return redirect('index')

def listGame(request):
	template_name = ''
	context = {}
	game = Game.objects.all()
	context["games"] = game
	return render(request, template_name, context)

def editGame(request, game_id):
	template_name = ''
	game = get_object_or_404(Game, id = game_id)
	if request.method == 'POST':
		form = GameForm(request.POST or None, request.FILES, instance=game)
		if form.is_valid():
			form.save()
			return redirect('index')
		else:
			form = GameForm(instance=game)
		return (request, template_name, {'form' : form})




