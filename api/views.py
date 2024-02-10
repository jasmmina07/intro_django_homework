from django.http import HttpRequest, JsonResponse
import json
data = {
    1: {
        'name': 'Milk',
        'price': 2.5,
        'quantity': 10
    },
    2: {
        'name': 'Bread',
        'price': 1.5,
        'quantity': 20
    },
}
# Grocery store API
# GET /grocery - this endpoint will display a list of fruits.
# POST /grocery/add - this endpoint will display a form that allows users to add new fruits to the list.
# GET /grocery/type/<type> - this endpoint will display a list of fruits by specifying the fruit type in the URL.
# GET /grocery/name/<name> - this endpoint will display a list of fruits by specifying the fruit name in the URL.
# GET /grocery/price/<price> - this endpoint will display a list of fruits by specifying the fruit price in the URL.

def get_all_items(request: HttpRequest):
    return JsonResponse(data)

def add_item(request: HttpRequest):
    if request.method=='POST':
        item=request.body
        item=json.loads(item)
        data[len(data)+1]=item
        return JsonResponse(data)
    else:
        return JsonResponse({'status':'method is not POST'})


