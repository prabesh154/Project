from django.shortcuts import render,redirect
from django.contrib import messages
from buyers.models import Sellercontact

# Create your views here.
def sellercontact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        location = request.POST['phone']
        message = request.POST['message']

    sellercontact = Sellercontact(name=name,email=email,phone=phone,location=location,message=message)
    sellercontact.save()

    messages.success('Your request has been submitted. A realtor will get back to you in a while')
    return redirect ('/sellercontact/')