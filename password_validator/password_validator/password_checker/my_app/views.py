from django.shortcuts import render,redirect
from .models import UserRegister
# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        UserRegister.objects.create(name=name,email=email,password=password)

        return render(request,'register.html',{'msg':'User registered successfully'})
    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = UserRegister.objects.get(email=email,password=password)
            request.session['user'] = user.email
            return redirect('dashboard')
        except :
            return render(request,'login.html',{'msg':'Invalid email or password'})
    return render(request,'login.html')

import re
def dashboard(request):
    result = ''
    if request.method == 'POST':
        password = request.POST.get("password")
        if len(password) < 8:
            result = "Password must be atleast 8 characters ."
        elif not re.search("[A-Z]", password):
            result = "Password must contain at least one uppercase letter."
        elif not re.search("[a-z]", password):
            result = "Password must contain at least one lowercase letter."
        elif not re.search("[!@#$%^&*]", password):
            result = "Password must contain at least one special character."
        elif not re.search("[0-9]", password):
            result = "Password must contain at least one digit."
        else:
            result = "Password is too Strong....!!!"
    return render(request,'dashboard.html',{'result':result})

def logout(request):
    request.session.flush()
    return redirect('index')
