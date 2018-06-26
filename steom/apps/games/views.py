from .models import Game
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import GameForm

# Create your views here.

@login_required
def index(request):
	return render(request, 'base.html')

@login_required
def addGame(request):
	template_name = ''
	if request.method == 'POST':
		form = GameForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('index')
	else: # get
		form = GameForm()
		return render(request, template_name, {'form': form})

@login_required
def removeGame(request, game_id):
	template_name = ''
	game = Game.objects.get(id=game_id)
	if game.delete():
		return redirect('index')
	else: # si no existe
		return render(request, template_name)

@login_required
def listGame(request):
	template_name = 'list_games.html'
	context = {}
	game = Game.objects.all()
	context["games"] = game
	return render(request, template_name, context)

@login_required
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
	else: # get
		form = GameForm()
		return render(request, template_name, {'form': form})