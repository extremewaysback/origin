from django.contrib import admin
from .models import Order, OrderItem

#Use modelinline for the orderitem model to include it as an inline in the orderadmin class
class OrderItemInline(admin.TabularInline):
    model=OrderItem
    raw_id_fields=['product']
    
class OrderAdmin(admin.ModelAdmin):
    list_display=['id','first_name','last_name','email','address','postal_code','city','paid','created','updated']
    list_filter=['paid','created','updated']
    inlines=[OrderItemInline]
    
admin.site.register(Order,OrderAdmin)
    
