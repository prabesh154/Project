from email import message
from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from buyers.models import Buyer
from listings.models import Listing
from accounts.models import Sellcontactss

# Create your views here.



def register(request):
    #REGISTER USER
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if len(username)<4:
         messages.error(request,'Username should contain more than 4 letters. ')
         return redirect('register')
        

        if len(password and password2)<5:
          messages.error(request,'Password should be of more than 4 digits ')
          return redirect('register')
      #Check for validation
        if password==password2:
        #check duplicate username
          if User.objects.filter(username=username).exists():
            messages.error(request,'That username is taken already')
            return redirect('register')
        
          else:
            if User.objects.filter(email=email).exists():
             messages.error(request,'This email is already in use')
             return redirect('register')
           
            
            else:
              user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
              user.save()
              messages.success(request,'You are now registered and you can log in')
              
              return redirect('login')


        else:
         messages.error(request,'Passwords do not match')  
         return redirect('register')

    else:
     return render(request,'accounts/register.html')






def login(request):
    if request.method=='POST':
      username = request.POST['username']
      password = request.POST['password']

      user = auth.authenticate(username=username,password=password)
      
      if user is not None:
        auth.login(request,user)
        messages.success(request,'You are logged in')
        return redirect('dashboard')
        
        


      else:
       messages.error(request,'Invalid credentials')
       return redirect('login')
    else:
      return render(request,'accounts/login.html')




def logout(request):
    if request.method=='POST':
        auth.logout(request)
        messages.success(request,'You are logged out')
        return redirect('index')

def dashboard(request):
  user_contacts = Buyer.objects.order_by('-contact_date').filter(user_id=request.user.id)
  context = {
    'buyers':user_contacts

  }
  
  return render (request,'accounts/dashboard.html',context)

def sellcontact(request):
    if request.method =="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        location=request.POST['location']
        message=request.POST['message']

        sellcontact=Sellcontactss(
            name=name,
            email=email,
            phone=phone,
            location =location,
            message=message
        )
        sellcontact.save()

         

        
       
        
        messages.success(request,'Thanks for contacting Us')
        return render(request,'pages/sellcontact.html')

    else:

     return render(request,'pages/sellcontact.html')


 


     