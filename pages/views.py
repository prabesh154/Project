
from django.shortcuts import render,redirect,get_object_or_404
from listings.choices import price_choices,district_choices,bedroom_choices
from listings.models import Listing
from realtors.models import Realtor
from buyers.models import Buyer


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'district_choices': district_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices
    }
    return render(request,'pages/index.html', context)

def about(request):
    #for getting realtors
    realtors = Realtor.objects.order_by('-hire_date')
    # for mvp
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors':realtors,
        'mvp_realtors':mvp_realtors
    }
    return render(request,'pages/about.html',context)


def seller(request):
    return render(request,'pages/seller.html')

def delete_buyerlist(request, listing_id):
       listing = get_object_or_404(Buyer, pk=listing_id)
       listing.delete()
       return redirect ('accounts/dashboard')   

