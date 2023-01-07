from django.urls import path

from .views import test_view

urlpatterns = [path("/get", test_view), path("/post", test_view)]
