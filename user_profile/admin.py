from django.contrib import admin
from articles.models import Article
from user_profile.models import User_profile

# здесь мы просто говорим, чтобы джанго зарегал наши модели в этой админке
# сейчас мы должны будем их увидеть в амдинке

admin.site.register(Article)
admin.site.register(User_profile)
