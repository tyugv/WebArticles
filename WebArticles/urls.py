from django.contrib import admin
from django.urls import path, include
from user_profile import views as user_profile_views
from django.contrib.auth import views as auth_views
'''
 короче тут второй строчкой мы говорим, что если у нас в адресной строке
 будет 127.0.0.1/articles, то он пойдет в этот файл
'''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('profile/', include('user_profile.urls')),
    path('register/', user_profile_views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='user_profile/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user_profile/logout.html'), name='logout'),
    path('accounts/', include('allauth.urls')),
]
