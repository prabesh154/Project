from django.urls import path

from. import views

urlpatterns = [
    path('contactbuy',views.contactbuy,name='contactbuy')
]