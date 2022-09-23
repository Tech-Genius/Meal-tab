from re import M
from django.contrib import admin
from . models import *

# Register your models here.


# admin.site.register(Popular)

class PromoAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag')
admin.site.register(Promo, PromoAdmin)    

  

class BreakfastAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'image_tag')
admin.site.register(Breakfast, BreakfastAdmin)

class LunchAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'image_tag')
admin.site.register(Lunch, LunchAdmin)

class DinnerAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'image_tag')
admin.site.register(Dinner, DinnerAdmin)

class ChefAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'image_tag')
admin.site.register(Chef, ChefAdmin)    

