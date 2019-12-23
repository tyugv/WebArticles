from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import User_profile
from .forms import UserRegisterForm
import requests

'''
помнишь про views? короче каждой адресной строке сопоставляется функция вьюс, которая там перенаправляет на html файл
но перед перенаправлением можно выполнять бекенд логику какую то и передавать данные в html файл
'''

def home_view(request):
    return render(request, 'user_profile/profile.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            number = form.cleaned_data['phoneNumber']
            prof = User_profile()
            prof.user = user
            prof.number = number
            # вот здесь надо отправить на апи запрос 
            prof.save()
            data = {
                'phoneNumber': number,
                'message': 'Ваш телефон использовался для регистрации на сайте localhost:8000'
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


