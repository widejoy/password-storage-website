from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
def home(request):
    return render(request,'main.html')
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password_1 = request.POST.get('password1')
        password_2 = request.POST.get('password2')
        myuser = User.objects.create_user(username,email,password_1)
        myuser.fname = first_name
        myuser.lname = last_name
        myuser.save() 
        messages.success(request, "Account created")
        return redirect('signin')

    return render(request,'signup.html')
def signin(request): 
    return render(request,'signin.html')
def signout(request):
    pass