from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article
from user_profile.models import User_profile, User_action

# значит нам надо создать
# параметр request означает запрос типа. Запрос же знаешь да?
# ну когда мы переходим на какой то адрес в браузере мы отправляем какой то запрос
# либо get, либо post. Ну короче просто запрос пока можешь не париться
# дальше мы вернем пока какой то html при переходе по этому адресу
# нам над сначала импортировать функцию которая будет отбражать http страницу
# сейчас мы возвращаем инлайново хттп. Теперь нам надо все таки с файла
# возвращать ну обычный html файл. Да. Для этого нам надо создать папки и файлсам
# теперь у нас есть файлик, можно возвратить его
# теперь нам надо подключить бутсрап и сделать менюшку

def home_view(request):
	articles = Article.objects.all()
	return render(request, 'articles/home.html', {"articles": articles}) 

def articles_view(request,num):
	if request.user.is_authenticated:
		user_profile = User_profile.objects.get(user = request.user)
		user_action = User_action.objects.get(user = request.user)
		article = Article.objects.get(id = num)
		return render(request ,'articles/some_article.html',{"article":article,
			"user_articles":user_profile.articles.all(),
			"useractions":user_action.actions.all(),
			"user":request.user})
	else:
	 	article = Article.objects.get(id = num)
	 	return render(request ,'articles/some_article.html',{"article":article})
def save(request,num):
	user_profile = User_profile.objects.get(user = request.user)
	user_profile.articles.add(Article.objects.get(id = num))
	return redirect(f'/articles/{num}/')

def delete(request,num):
	user_profile = User_profile.objects.get(user = request.user)
	user_profile.articles.remove(Article.objects.get(id = num))
	return redirect(f'/articles/{num}/')

def like(request,num):
	article = Article.objects.get(id = num)
	print(article.likes)
	article.likes += 1
	print(article.likes)
	article.save()
	user_action = User_action.objects.get(user = request.user)
	user_action.actions.add(Article.objects.get(id = num))
	return redirect(f'/articles/{num}/')

def dislike(request,num):
	article = Article.objects.get(id = num)
	dislikes = article.dislikes
	article.dislikes +=  1
	article.save()
	user_action = User_action.objects.get(user = request.user)
	user_action.actions.add(Article.objects.get(id = num))
	return redirect(f'/articles/{num}/')