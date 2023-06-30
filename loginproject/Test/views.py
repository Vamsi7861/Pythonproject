from django.shortcuts import render,redirect
from django.contrib import messages
from .models import User
from django.contrib.auth  import authenticate,login,logout
# Create your views here.
def home(request):
    return render(request,'index.html')
def register(request):
    if request.method=='POST':
      name=request.POST['name']
      email=request.POST['email']
      phone=request.POST['phone']
      username=request.POST['username']
      password=request.POST['password']
     
      if  User.objects.filter(email=email).exists(): 
         messages.info(request,'user already present')
         return redirect('/register')
      else:
          us=User(name=name,email=email,phone=phone,password=password,username=username)
          us.save()
          return redirect('/login')
         
    else:
     return render(request,'register.html')
def login(request):
    if request.method=='POST':
       name=request.POST['username']
       npassword=request.POST['password']
       
      
       user = authenticate(username = name,password = npassword)

       if user is not None:
            login(request, user)
            messages.info(request,'login success')
            return redirect("/")
       else:
          messages.info(request,'invalid input')
          return redirect('/login')
    else:
       return render(request,'login.html')