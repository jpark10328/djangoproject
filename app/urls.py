from django.urls import path,include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('map/', views.maps_view, name="maps_view"),
    path('kakao/',views.maps_kakao, name="maps_kakao"),
    path('hotel_list/', views.hotel_list, name="hotel_list"),
    path('hotel_list/<int:pk>/', views.hotel_detail, name="hotel_detail"),
]
