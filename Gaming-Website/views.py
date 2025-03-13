from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from service.models import  Contact
from django.core.exceptions import ObjectDoesNotExist

@login_required
def Home(request):
    return render(request,'home.html', {})

def Register(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phno = request.POST.get('phno')

        new_user = User.objects.create_user(name, email, password)
        new_user.phno = phno

        new_user.save()
        return redirect('login')
    return render(request,'Register.html', {})

def Login(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('Error, user does not exist')
    return render(request,'login.html', {})

def logoutuser(request):
    logout(request)
    return redirect('login')

def GovtEvents(request):
    return render(request,'events.html', {})

def FunQuiz(request):
    return render(request,'funquiz.html', {})

def Quiz(request):
    return render(request,'quiz.html', {})

def Quiz2(request):
    return render(request,'quiz2.html', {})

def Quiz3(request):
    return render(request,'quiz3.html', {})

def Contactus(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        messages = request.POST['message']
        ins = Contact(username=username,message=messages, email=email)
        ins.save()
        print("ok")
    return render(request,'contactus.html', {})

