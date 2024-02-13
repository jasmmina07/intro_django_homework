from django.urls import include,path
from .views import (
                       get_all_items,
                       add_item,
                       home,
                       grocery,
                       grocery_by_type,
                       grocery_by_name,
                       grocery_by_price
                       )

urlpatterns = [
    path("",get_all_items),
    path('add/',add_item),
    # path("",home),
    # path("grocery/",grocery),
    path("type/<type>",grocery_by_type),
    path("name/<name>",grocery_by_name),
    path("price/<price>",grocery_by_price)
]