from django.urls import path
#path is attached to the method in a view
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('about',views.about, name='about')
]

