from django.db import models
from django.utils.html import mark_safe
from general.models import Promo
from account.models import User
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



# Order
status_choice=(
        ('process','In Process'),
        ('shipped','Shipped'),
        ('delivered','Delivered'),
    )
class CartOrder(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    total_amt=models.FloatField()
    paid_status=models.BooleanField(default=False)
    order_dt=models.DateTimeField(auto_now_add=True)
    order_status=models.CharField(choices=status_choice,default='process',max_length=150)

    class Meta:
        verbose_name_plural='Orders'



class CartOrderItems(models.Model):
    order=models.ForeignKey(CartOrder,on_delete=models.CASCADE)
    invoice_no=models.CharField(max_length=150)
    item=models.CharField(max_length=150)
    image=models.CharField(max_length=200)
    qty=models.IntegerField()
    price=models.FloatField()
    total=models.FloatField()

    class Meta:
        verbose_name_plural='Order Items'

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.image))