import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from .models import Order, Inventory
from .messaging import publish

def health_check(request):
    return JsonResponse({"status":"OK"})

@csrf_exempt
def create_order(request):
    if request.method != 'POST': return HttpResponseBadRequest("POST only")
    data = json.loads(request.body or "{}")
    order = Order.objects.create(
        status=data.get("status","CREATED"),
        total=float(data.get("total",0))
    )
    publish("orders.created", {"id":order.id,"total":order.total,"status":order.status})
    return JsonResponse({"id":order.id})

@csrf_exempt
def update_inventory(request):
    if request.method != 'POST': return HttpResponseBadRequest("POST only")
    data = json.loads(request.body or "{}")
    inv = Inventory.objects.create(product=data["product"], quantity=int(data["quantity"]))
    publish("inventory.updated", {"id":inv.id,"product":inv.product,"quantity":inv.quantity})
    return JsonResponse({"id":inv.id})
