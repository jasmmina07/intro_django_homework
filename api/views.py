from django.http import HttpRequest, JsonResponse
import json
from tinydb import TinyDB,Query
from tinydb.database import Document

db=TinyDB("db.json",indent=4)
data=db.table("grocery")

# Grocery store API
# GET /grocery - this endpoint will display a list of fruits.
# POST /grocery/add - this endpoint will display a form that allows users to add new fruits to the list.
# GET /grocery/type/<type> - this endpoint will display a list of fruits by specifying the fruit type in the URL.
# GET /grocery/name/<name> - this endpoint will display a list of fruits by specifying the fruit name in the URL.
# GET /grocery/price/<price> - this endpoint will display a list of fruits by specifying the fruit price in the URL.

def home(request: HttpRequest):
    return JsonResponse({"message":"Welcome!"})

def get_all_items(request: HttpRequest):
    return JsonResponse({"response":data.all()})

def grocery_by_type(request: HttpRequest,type):
    return JsonResponse({"response":data.search(Query().type==type)})

def grocery_by_price(request: HttpRequest,price):
    return JsonResponse({"response":data.search(Query().price<=float(price))})

def grocery_by_name(request: HttpRequest,name):
    return JsonResponse({"response":data.search(Query().name==name)})

def grocery(request: HttpRequest):
    arr=[]
    for i in data:
        arr.append(data[i]["name"])
    return JsonResponse({"products":arr})

def add_item(request: HttpRequest):
    if request.method=='POST':
        item=request.body
        item=json.loads(item)
        doc=Document(value=item)
        data.insert(doc)
        return JsonResponse(data)
    else:
        return JsonResponse({'status':'method is not POST'})


