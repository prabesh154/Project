from ast import keyword
from django.shortcuts import get_object_or_404,render,redirect
from .models import Listing
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from .choices import price_choices,district_choices,bedroom_choices



def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context={
        'listings':paged_listings
        
    }
    return render(request, 'listings/listings.html',context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    

    context ={
        'listing': listing
    }

    return render(request, 'listings/listing.html',context)

 

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
    #keywords
    if 'keywords' in request.GET:
      keywords = request.GET['keywords']
      if keywords:
        queryset_list= queryset_list.filter(description__icontains=keywords)
    
    #place
    if 'place' in request.GET:
      place = request.GET['place']
      if place:
        queryset_list= queryset_list.filter(place__iexact=place)

    
     #district
    if 'district' in request.GET:
      district = request.GET['district']
      if district:
        queryset_list= queryset_list.filter(district__iexact=district)

      #bedrooms
    if 'bedrooms' in request.GET:
      bedrooms = request.GET['bedrooms']
      if bedrooms:
        queryset_list= queryset_list.filter(bedrooms__iexact=bedrooms)

        #price
    if 'price' in request.GET:
      price = request.GET['price']
      if price:
        queryset_list= queryset_list.filter(price__lte=price)

    context = {
        'district_choices': district_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'listings': queryset_list,
        'values': request.GET   #TO PRESERVE INPUTS

      }
    return  render(request, 'listings/search.html',context)

    
