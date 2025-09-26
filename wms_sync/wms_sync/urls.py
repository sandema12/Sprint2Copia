from django.contrib import admin
from django.urls import path, include  # incluye include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sync_app.urls')),  # <- agrega esta línea
]
