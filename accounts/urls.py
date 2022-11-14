from django.urls import path
#path is attached to the method in a view
from . import views

urlpatterns = [
    path('login',views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout',views.logout, name='logout'),
    path('dashboard',views.dashboard, name='dashboard'),
    path('sellcontact',views.sellcontact,name='sellcontact')
    
]
