from django.shortcuts import render,redirect
from django.contrib import messages
from buyers.models import Buyer
from django.core.mail import send_mail
from django.contrib.auth.models import User
# Create your views here.
def contact(request):
 if not  request.user.is_authenticated:
     messages.error(request,' Login in to Proceed')
     return redirect('/accounts/login')
 
# Create your views here.
 else:
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        realtor = request.POST['realtor']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

     #Check if user has made inquiry already:
        if request.user.is_authenticated:
            user_id = request.user.id
            has_connected = Buyer.objects.all().filter(listing_id=listing_id,user_id=user_id)
            if has_connected:
                messages.error(request,'You have already made an inquiry for this listing')
                return redirect ('/listings/'+listing_id)

        contact = Buyer(listing=listing,listing_id=listing_id,name=name,email=email,
        phone=phone,message=message,user_id=user_id,realtor=realtor)
        contact.save()

        #send maul
        send_mail (
            'Property Listing Inquiry',
            'There has been an inquiry for '+listing+'.Sign into the admin panel for more info',
            'rijalprabesh154@gmail.com',
            [realtor_email,'rijalprabesh145@gmail.com'],
            fail_silently=False

        )

        messages.success(request,'Your request has been submitted. A realtor will get back to you in a while')
        return redirect ('/listings/'+listing_id)
 
 
   

        
      
    