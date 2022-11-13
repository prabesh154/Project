from django.db import models
from datetime import datetime


# Create your models here.
class Seller(models.Model):
    name = models.CharField(max_length =25)
    phone = models.IntegerField(null=False )
    email = models.EmailField(max_length = 30)
    location = models.CharField(max_length =25 ,default=1)
    message = models.TextField(blank=True ,max_length=150)
    contact_date = models.DateTimeField(default = datetime.now,blank=True)
    def __str__(self):
        return self.name
        