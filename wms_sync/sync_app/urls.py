from django.urls import path
from .views import health_check, create_order, update_inventory

urlpatterns = [
    path('health-check/', health_check),
    path('api/orders', create_order),
    path('api/inventory', update_inventory),
]
