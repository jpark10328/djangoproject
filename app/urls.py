from django.urls import path,include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("hotel_list/", views.hotel_list, name="hotel_list"),
    path("hotel_detail/", views.hotel_detail, name="hotel_list"),
]
