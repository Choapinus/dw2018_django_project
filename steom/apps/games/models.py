from django.db import models

class Game(models.Model):
	name_game = models.CharField(max_length= 100)
	category = models.CharField(max_length=100)
	gender = models.CharField(max_length=100)
	developer = models.ForeignKey('developer', on_delete = models.CASCADE)
	photo = models.ImageField(upload_to='photos')
	price = models.PositiveIntegerField()
	description = models.TextField(max_length=1000)
	release_date = models.DateField()
	system_requirements = models.TextField(max_length=1000)

	def __str__ (self):
		return self.name_game

class developer(models.Model):
	name_developer = models.CharField(max_length=100)
	foundation = models.DateField()
	location = models.CharField(max_length=100)

	def __str__ (self):
		return self.name_developer





		