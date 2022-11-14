from django.contrib import admin
from .models import Sellcontactss
# Register your models here.


# Register your models here.
class SellcontactssAdmin(admin.ModelAdmin):
   list_display = ('id','name','email')
   list_display_links = ('id','name')
   list_per_page = 25
   
admin.site.register(Sellcontactss,SellcontactssAdmin)
