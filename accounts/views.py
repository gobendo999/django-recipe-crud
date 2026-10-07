from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def register_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
            return redirect('register')

        User.objects.create_user(username=username, password=password)
        messages.success(request, 'Account created. Please login.')
        return redirect('login')

    return render(request, 'register.html')


def login_page(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password'],
        )
        if user:
            login(request, user)
            return redirect('recaipe_list')
        messages.error(request, 'Invalid username or password')
        return redirect('login')

    return render(request, 'login.html')


def logout_page(request):
    logout(request)
    return redirect('login')