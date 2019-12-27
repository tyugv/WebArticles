from django.db import models
from django.contrib.auth.models import User
from articles.models import Article
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save



class User_profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	articles = models.ManyToManyField(Article, blank=True)
	number = models.CharField(max_length=12, null=True, blank=True)
	def __str__(self):

		return self.user.username

class User_action(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	actions = models.ManyToManyField(Article, blank=True)
	def __str__(self):

		return self.user.username



@receiver(post_save, sender=User)
def my_handler(sender, instance, created, **kwargs):
    if created:
        pers = User_action()
        pers.user = instance
        pers.save()
        pers = User_profile()
        pers.user = instance
        pers.save()