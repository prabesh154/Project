from email import message
from email.policy import default
from pyexpat import model
from django.db import models
from datetime import datetime
from realtors.models import Realtor
# Create your models here.


class Buyer(models.Model):
    listing = models.CharField(max_length =200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length = 200)
    email = models.CharField(max_length = 100)
    realtor = models.CharField(max_length=200 ,default=1)
    phone = models.CharField(max_length = 100)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default = datetime.now,blank=True)
    user_id = models.IntegerField(blank=True)
    def __str__(self):
        return self.name
        
