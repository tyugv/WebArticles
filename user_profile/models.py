from django.db import models
from django.contrib.auth.models import User
from articles.models import Article
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save

# мы тут импортируем Юзер чтобы связать с нашим кастомным классом, поскольку
# мы дополяем их модель. Эт понятно?


class User_profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	articles = models.ManyToManyField(Article)
	number = models.CharField(max_length=12, null=True)
	
	def __str__(self):

		return self.user.username


@receiver(post_save, sender=User)
def my_handler(sender, instance, created, **kwargs):
    if created:
        pers = User_profile()
        pers.user = instance
        pers.save()
'''
так как мы щас создали модель нашу чтобы сохранить в бд нам надо создать миграцию, то бишь
не, норм
крч когда мы создаем что то для хранения в бд в файлика models мы должны прописать миграции, чтобы
джанго понял, что мы чет поменяли или добавили для хранения в базе данных
поэтому мы сначала прописываем python3 manage.py makemigrations
чтобы он сначала создал миграции, а потом пишем python3 manage.py migrate, чтобы произвести непосредственно миграцию саму
то есть сначала он делает некий план этим makemigrations, а потом уже командой migrate саму миграцию выполняет
в админке мы должны увидеть эти таблицы
пока у нас таблица с юзерами, который по дефолту джанго хендлит. Да, они должны будут добавиться да
но для начала надо миграции сделать
он не добавил, потому что нам надо это тоже указать в файле admin.py
'''
