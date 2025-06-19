from django.urls import path

from .views import home, register

urlpatterns = [
    path("", home, name="users-home"),
    path("register/", register, name="users-register"),
]
