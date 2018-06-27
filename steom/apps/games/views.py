from .models import Game
from .forms import GameForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

@login_required
def index(request):
	return render(request, 'base.html')

@login_required
def addGame(request):
	template_name = 'add_game.html'
	if request.method == 'POST':
		form = GameForm(request.POST or None, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('index')
	else: # get
		form = GameForm()
	return render(request, template_name, {'form': form})

@login_required
def removeGame(request, game_id):
	game = Game.objects.get(id=game_id)
	if game.delete():
		return redirect('list_games')
	else: # si no existe
		# return render(request, template_name)
		return redirect('index')

@login_required
def listGame(request):
	template_name = 'list_games.html'
	context = {}
	game = Game.objects.all()
	context["games"] = game
	return render(request, template_name, context)

@login_required
def editGame(request, game_id):
	template_name = 'add_game.html'
	game = get_object_or_404(Game, id = game_id)
	if request.method == 'POST':
		form = GameForm(request.POST or None, request.FILES, instance=game)
		if form.is_valid():
			form.save()
			return redirect('index')
	else: # get
		form = GameForm(instance=game)
	return render(request, template_name, {'form': form})

def compareGames(request, game1_id, game2_id):
	template_name = 'compare_games.html'
	context = {}
	game1 = get_object_or_404(Game, pk = game1_id)
	game2 = get_object_or_404(Game, pk = game2_id)
	context['game1'] = game1
	context['game2'] = game2
	return render(request, template_name, context)
