from django.urls import re_path

from .views import join, login, logout

urlpatterns = [
    re_path(r"/join/?$", join, name="join"),
    re_path(r"/login/?$", login, name="login"),
    re_path(r"/logout/?$", logout, name="logout"),
]
