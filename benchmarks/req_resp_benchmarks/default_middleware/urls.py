from django.urls import path
from .views import index

urlpatterns = [
    path('inx-pg', index),
]
