from django.contrib.auth import get_user_model, login as django_login, logout as django_logout, authenticate
from django.shortcuts import render, redirect

User = get_user_model()


def login(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            django_login(request, user)
            return redirect('post:post_list')
        else:
            return render(request, 'member/login.html')

    else:
        return render(request, 'member/login.html')


def logout(request):
    django_logout(request)
    return redirect('post:post_list')


def signup(request):
    pass
