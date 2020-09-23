from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from . import views
urlpatterns = [
    path('admin_console', views.admin_console, name="admin_console"),
]