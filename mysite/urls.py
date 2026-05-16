
from django.contrib import admin
from django.urls import path, include
# app_name = 'cadastro'

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('cadastro.urls')),
    
]
