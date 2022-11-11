from django.contrib import admin
from .models import Buyer
# Register your models here.
class BuyerAdmin(admin.ModelAdmin):
   list_display = ('id','name','listing','email','contact_date','realtor')
   list_display_links = ('id','name')
   search_fields = ('name','email','listing')
   list_filter = ('realtor','name')
   list_per_page = 25
   
admin.site.register(Buyer,BuyerAdmin)
