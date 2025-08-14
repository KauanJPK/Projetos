from django.contrib import admin
from django.urls import path, include
from home.views import entrada

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', entrada),
]
