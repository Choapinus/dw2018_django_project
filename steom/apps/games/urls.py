from django.urls import path
from apps.games import views

urlpatterns = [
	path('', views.index, name='index'),
	path('list/', views.listGame, name='list_games'),
	path('add/',views.addGame, name='add_game'),
	path('remove/<int:game_id>/',views.removeGame, name='remove_games'),
	path('edit/<int:game_id>/',views.editGame, name='edit_games'),
	path('compare/<int:game1_id>/<int:game2_id>/',views.compareGames, name='compare_games'),
	path('buy/',views.buyGames, name='buy_games'),
]