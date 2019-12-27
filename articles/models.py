from django.db import models
from django.contrib.auth.models import User

# нам надо еще создать объект статьи, чтобы статьи хранить
# там надо связать 

class Article(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField(max_length=1000)
	imgLink = models.CharField(max_length=200)
	likes = models.PositiveIntegerField(default = 0)
	dislikes = models.PositiveIntegerField(default =0)
	#likes_str = str(likes)
	#dislikes_str = str(dislikes)
	def __str__(self):
		return self.title
	def likes_str(self):
		return str(self.likes)
	def dislikes_str(self):
		return str(self.dislikes)




	