from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User, auth

# Create your views here.
def index(request):
    return render(request,'index.html')
    
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # if User.objects.filter(username=username).exists():
        #     messages.info(request,'Username taken')
        #     # return redirect('index.html')
        # elif User.objects.filter(email=email).exists():
        #     messages.info(request,'Email taken')
        #     # return redirect('index.html')
        # else:
        user = User.objects.create_user(username=username, password=password,email=email)
        user.save()
        print('user created')
        return redirect('login')
    else:
        return render(request, 'index.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home.html')
        else:
            return redirect('index.html')

    else:
        return render(request,'index.html')

def homepage(request):
    return render(request, 'home.html')
