from django.contrib import admin
from django.urls import path 
from general import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name = 'search'),
    path('table-reservation/', views.table_reservation, name = 'table-reservation'),
    path('event-reservation/', views.event_reservation, name = "event-reservation"),
]
