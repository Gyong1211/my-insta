from django.contrib.auth import get_user_model, login as django_login, logout as django_logout, authenticate
from django.shortcuts import render, redirect

from .forms import LoginForm, SignupForm

User = get_user_model()


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            django_login(request, user)
            return redirect('post:post_list')
    else:
        if request.user.is_authenticated:
            return redirect('post:post_list')

    return render(request, 'member/login.html')


def logout(request):
    django_logout(request)
    return redirect('post:post_list')



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.create_user()
            django_login(request, user)
            return redirect('post:post_list')
    else:
        pass
    return render(request, 'member/signup.html')
