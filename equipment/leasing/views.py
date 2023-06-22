from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import UserRegistration

# Create your views here.
# @login_required(function='HomePage')
def HomePage(request):
    return render(request, 'Home.html')

def SignupPage(request):
    if request.method == 'POST':
        name = request.POST.get('input-name')
        username = request.POST.get('input-username')
        email = request.POST.get('input-email')
        phone = request.POST.get('input-phone')
        address = request.POST.get('input-address')
        password = request.POST.get('input-password')
        terms = request.POST.get('terms') == 'Yes'

        registration = UserRegistration(Name=name, UserName=username, Email=email, Phone=phone, Address=address,
                                        Password=password, TermAndConditions=terms)
        registration.save()

        # if User.objects.filter(username=username).exists():
        #     return HttpResponse('Username already exists.')
        #
        # registration = User.objects.create_user(username,email, password )
        # registration.save()

        return redirect('login')

    return render(request, 'UserRegistrations.html')


def AdminLoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('input-username')
        password = request.POST.get('input-password')

        try:
            if username == 'admin' and password == 'password':
                return redirect('/adminpanel')
            else:
                return HttpResponse('Inavlid Admin')

        except UserRegistration.DoesNotExist:
            return HttpResponse('Invalid Admin')

    return render(request, 'Adminlogin.html')

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('input-username')
        password = request.POST.get('input-password')

        try:
            user = UserRegistration.objects.get(UserName=username, Password=password)
            if user is not None:
                UserRegistration(request, user)
                return redirect('/home')

        except UserRegistration.DoesNotExist:
            return HttpResponse('Invalid User')


        # user = authenticate(request, username= username, password= password)

        # if user is not None:
        #     login(request, user)
        #     return redirect('home')
        # else:
        #     return HttpResponse('username or password wrong.')

    return render(request, 'UserLogin.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def AdminPanel(request):
    return HttpResponse('Welcome to admin panel')