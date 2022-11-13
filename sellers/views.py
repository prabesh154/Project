from django.shortcuts import render,redirect
from django.contrib import messages
from sellers.models import Seller


# Create your views here.



def seller(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        location = request.POST['location']
        message = request.POST['message']
      
        seller = Seller(name=name,email=email,phone=phone,location=location,message=message)
        seller.save()

        messages.success(request,'Your query has been submitted. Our team will get back to you in a while')
        return redirect ('/seller/')

    



     

    
     