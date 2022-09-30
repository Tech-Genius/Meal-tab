# from django.contrib import admin
from django.urls import path 
from shop import views

urlpatterns = [
    path('shop/', views.shop, name='shop'),
    # path('category/<slug:slug>/', views.category, name = 'category'),
    path('item/<slug:slug>/', views.item, name = 'item'),
    path('filter-category/', views.filter_category, name='filter-category'),
    path('add-to-cart',views.add_to_cart,name='add_to_cart'),
    path('cart_view',views.cart_view,name='cart_view'),
    path('delete-from-cart',views.delete_cart_item,name='delete-from-cart'),
    path('update-cart',views.update_cart_item,name='update-cart'),
]

