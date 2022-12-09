
from django.db import models
from datetime import datetime
from realtors.models import Realtor


class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    place = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    Face = models.CharField(max_length=50,blank=True)
    road_access = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    price = models.CharField(max_length=30)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    parking = models.CharField(max_length=50)
    sqft = models.CharField(max_length=50,blank=True)
    area_covered = models.CharField(max_length=50,blank=True)
    floors = models.CharField(max_length=50)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published =models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.title