from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def index(request):
    return render(request,'index.html')
def Authentification_User(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info("le nom d'utilisateur ou mot de passe est incorect veillez entrer les coordonnees valides")
    else:
        context={'form':AuthenticationForm()}
    return render(request,'index.html',context)
def Deconnection_user(request):
    logout(request)
    return redirect('index')
