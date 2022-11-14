from django.db import models

# Create your models here.
class Sellcontactss(models.Model):
    
    name = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 100)
    location = models.CharField(max_length = 50,blank=True)
    phone = models.PositiveIntegerField()
    message = models.TextField(blank=True)
    
    
    def __str__(self):
        return self.name