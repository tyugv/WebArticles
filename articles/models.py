from django.db import models

# нам надо еще создать объект статьи, чтобы статьи хранить
# там надо связать 

class Article(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField(max_length=1000)
	imgLink = models.CharField(max_length=200)

	def __str__(self):
		return self.title