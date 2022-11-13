from django.urls import path
#path is attached to the method in a view
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('about',views.about, name='about'),
    path('seller',views.seller, name='seller'),
    path ('delete_buyerlist/<int:listing_id>',views.delete_buyerlist,name='delete_buyerlist')
]

