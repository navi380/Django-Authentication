from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User , auth
from django.contrib import messages


def signup(request):
    if request.method == 'POST':
        username=request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repeat=request.POST['confirm_password']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        if password==repeat:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username already exist')
                return redirect('/signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already register')
                return redirect('/signup')
            else:
                user=User.objects.create_user(username=username,password=password, email=email ,first_name=firstname, last_name = lastname)
                user.save()
                return redirect('/signin')
        else:
            messages.error(request, 'paassword not match')
            return redirect('/signup')


    else:
        return  render(request,'signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user= auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('/signin')

    else:
        return  render(request,'signin.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def index(request):
    return render(request , 'index.html')
