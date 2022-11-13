from django.urls import path
#path is attached to the method in a view
from . import views

urlpatterns = [
    path('',views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search',views.search, name='search'),
    
    
    
]

