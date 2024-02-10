# from django.contrib import admin
from django.urls import path
from api.views import get_all_items,add_item

urlpatterns = [
    path('items/',get_all_items),
    path('additem/',add_item)
]
