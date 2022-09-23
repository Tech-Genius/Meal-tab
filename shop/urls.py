from django.contrib import admin
from django.urls import path 
from shop import views

urlpatterns = [
    path('shop/', views.shop, name='shop'),
    # path('category/<slug:slug>/', views.category, name = 'category'),
    path('item/<slug:slug>/', views.item, name = 'item'),
    path('filter-category/', views.filter_category, name='filter-category'),
]
