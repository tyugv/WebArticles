from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import User_profile, User_action
from .forms import UserRegisterForm
import requests

'''
помнишь про views? короче каждой адресной строке сопоставляется функция вьюс, которая там перенаправляет на html файл
но перед перенаправлением можно выполнять бекенд логику какую то и передавать данные в html файл
'''

def home_view(request):
    user_profile = User_profile.objects.get(user = request.user)
    return render(request, 'user_profile/profile.html',{"user_profile":user_profile,
                                                        "Articles":user_profile.articles.all()})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            number = form.cleaned_data['phoneNumber']
            prof = User_profile()
            prof.user = user
            prof.number = number
            #prof.save()
            prof2 = User_action()
            prof2.user = user
            #prof2.save()
            # вот здесь надо отправить на апи запрос 
            
            data = {
                'phoneNumber': number,
                'message': 'Ваш телефон использовался для регистрации на сайте https://morning-retreat-65606.herokuapp.com/'
            }
            resp = requests.post('https://q9sbuwsqh6.execute-api.us-east-1.amazonaws.com/myNewStage/orderinfo', json=data, headers={'Content-type': 'application/json'})
            print('-----------------------')
            print(resp)
            print('-----------------------')
            messages.success(request, f'Your account has been created! Now you can login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user_profile/register.html', {'form': form})


