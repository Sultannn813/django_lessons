from django.contrib import admin
from django.urls import path

from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('sum/', views.sum, name="sum"),
    path('user/<int:user_id>/', views.user, name="user"),
]
