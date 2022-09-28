from email import message
from django.shortcuts import render,redirect
from django.contrib import messages

# Create your views here.
def register(request):
     if request.method=='POST':
        messages.error(request,'Testing error messages')
        return redirect('register')
      #REGISTER USER
     else:
       return render(request,'accounts/register.html')


def login(request):
    if request.method=='POST':
    #   LOGIN USER  
     return render(request,'accounts/login.html')



def logout(request):
    return redirect(request,'index')

def dashboard(request):
    return redirect(request,'accounts/dashboard.html')