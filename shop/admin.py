from django.contrib import admin
from . models import *
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag', 'price', 'status', 'is_featured', 'has_discount', 'percentage_off', 'price_before_discount', 'discount_days_left')
    list_editable = ('status',)
admin.site.register(Product, ProductAdmin)  


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','image_tag')
admin.site.register(Category, CategoryAdmin) 

# Order
class CartOrderAdmin(admin.ModelAdmin):
	list_editable=('paid_status','order_status')
	list_display=('user','total_amt','paid_status','order_dt','order_status')
admin.site.register(CartOrder,CartOrderAdmin)

class CartOrderItemsAdmin(admin.ModelAdmin):
	list_display=('invoice_no','item','image_tag','qty','price','total')
admin.site.register(CartOrderItems,CartOrderItemsAdmin)
