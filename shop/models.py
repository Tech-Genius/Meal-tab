from django.db import models
from django.utils.html import mark_safe
from general.models import Promo

# Create your models here.






class Category(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to= "category")
    slug = models.SlugField(default='slug')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'


          

    def image_tag(self)    :
        return mark_safe('<img src = "%s" width="50" height = "50" />' % (self.image.url))    



class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    image = models.ImageField(upload_to= "products")
    price = models.PositiveIntegerField()  
    status = models.BooleanField(default=True) 
    category = models.ManyToManyField(Category, related_name='category')
    is_featured = models.BooleanField(default=False)
    has_discount = models.BooleanField(default=False)
    discount_days_left = models.PositiveIntegerField(default=0)
    percentage_off = models.PositiveIntegerField(default=0)
    price_before_discount = models.PositiveIntegerField(default=0)



    def __str__(self):
        return self.title

    class Meta:
       ordering = ['title']    

    def image_tag(self)    :
        return mark_safe('<img src = "%s" width="50" height = "50" />' % (self.image.url))
