from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
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
        if password_1==password_2:
         myuser = User.objects.create_user(username,email,password_1)
         myuser.fname = first_name
         myuser.lname = last_name
         myuser.save() 
         messages.success(request, "Account created")
         return render(request,"signin.html")
        if User.objects.filter(username = username).first():
         messages.error(request, "This username is already taken")
        else:
            messages.error(request, "password is not equal")
            

    return render(request,'signup.html')
def signin(request):
   
   if request.method == 'POST':
        username = request.POST.get('username')
        password_1 = request.POST.get('password1')
        user = authenticate(username = username,password=password_1)
        if user != None:
            login(request,user)
            
            return render(request,"homepage.html")
        else:
            messages.error(request,"bad cerdentials")

   return render(request,'signin.html')    

def signout(request):
    
    logout(request)
    return redirect('home')