from django.urls import path
from apps.games import views

urlpatterns = [
	path('', views.index, name='index'),
	path('list/', views.listGame, name='list_games'),
	path('add/',views.addGame, name='add_games'),
	path('remove/<int:game_id>/',views.removeGame, name='remove_games'),
	path('edit/<int:game_id>/',views.editGame, name='edit_games'),
]