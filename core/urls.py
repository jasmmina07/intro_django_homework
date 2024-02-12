# from django.contrib import admin
from django.urls import path
from api.views import (
                       get_all_items,
                       add_item,
                       home,
                       grocery,
                       grocery_by_type,
                       grocery_by_name,
                       grocery_by_price
                       )

urlpatterns = [
    path('items/',get_all_items),
    path('additem/',add_item),
    path("",home),
    path("grocery/",grocery),
    path("grocery/type/<type>",grocery_by_type),
    path("grocery/name/<name>",grocery_by_name),
    path("grocery/price/<price>",grocery_by_price)
]
