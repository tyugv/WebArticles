from django.conf.urls import url
from . import views
from django.urls import path


# сюда пойдет и посмотрит куда дальше ему двигаться,
# здесь пусто в кавычках понятно же почему да? да
# первый параметр это пусть адресный, второй параметр это функция в которую
# перейдется по этой адресной строке, там мы типа будем рисовать хтмл и всю
# логику писать, третий параметр это просто удобное название для обращения потом

# он выдает ошибку потому что у нас еще нет такой функции в файле views.py

urlpatterns = [
	path('', views.home_view, name="articles-home"),
	path('<num>/',views.articles_view, name = "some article"),
	path('<num>/save/',views.save, name = "save"),
	path('<num>/delete/',views.delete, name = "delete")
]