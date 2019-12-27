from django.conf.urls import url
from . import views
from django.urls import path



urlpatterns = [
	path('', views.home_view, name="articles-home"),
	path('<num>/',views.articles_view, name = "some article"),
	path('<num>/save/',views.save, name = "save"),
	path('<num>/delete/',views.delete, name = "delete"),
	path('<num>/like/',views.like, name = "like"),
	path('<num>/dislike/',views.dislike, name = "dislike")
]