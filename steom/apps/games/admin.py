from django.contrib import admin
from apps.games.models import *

# Register your models here.

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
	list_display = ['name_game', 'category',]
	search_fields = ('name_game',)

@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
	list_display = ['name_developer',]
	search_fields = ('location',)	
