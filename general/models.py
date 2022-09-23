
from django.db import models
from django.utils.html import mark_safe

# Create your models here.

# class Color(models.Model):
#     title = models.CharField(max_length=255)
#     color_code = models.CharField(max_length=255)

#     def color_bg(self):
#         return mark_safe('<div style = " width="50"; height = "50"; background-color:%s"> </div>' % (self.color_code))   

#     def __str__(self):
#         return self.title





class Promo(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    days_left = models.CharField(max_length=225)
    image = models.ImageField(upload_to= "promo_images")
    percentage_off = models.CharField(max_length=200)
    price = models.CharField(max_length=205)


    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height = "50" />' % (self.image.url))   


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']  


# class Popular(models.Model):
#     title = models.CharField(max_length=255)
#     slug = models.SlugField()
#     image = models.ImageField(upload_to= "promo_images")
#     price = models.CharField(max_length=205)







#     def __str__(self):
#         return self.title



#     class Meta:
#         ordering = ['title']    





class Breakfast(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    image = models.ImageField(upload_to= "products")
    price = models.PositiveIntegerField()  

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src = "%s" width="50" height = "50" />' % (self.image.url))   


class Lunch(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    image = models.ImageField(upload_to= "products")
    price = models.PositiveIntegerField()  



    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src = "%s" width="50" height = "50" />' % (self.image.url))     



class Dinner(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    image = models.ImageField(upload_to= "products")
    price = models.PositiveIntegerField()  

  
    def __str__(self):
        return self.title

    def image_tag(self)    :
        return mark_safe('<img src = "%s" width="50" height = "50" />' % (self.image.url)) 



class Chef(models.Model):
    name = models.CharField(max_length=225)
    position = models.CharField(max_length=225)
    image = models.ImageField(upload_to="chef-images") 
    instagram = models.CharField(max_length=225)  
    twitter = models.CharField(max_length=225)
    facebook = models.CharField(max_length=225) 


    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe('<img src = "%s" width="50" height = "50" />' % (self.image.url))     