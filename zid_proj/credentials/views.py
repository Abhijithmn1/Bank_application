from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')

    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "USERNAME ALREDY TAKEN")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save();
                print('user created')
                return render(request, 'login.html')
        else:
            messages.info(request, "Password not match")
            return redirect('register')
        return redirect('/')
    return render(request, "registration.html")


def logout(request):
    auth.logout(request)
    return redirect('/')
