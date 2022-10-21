from django.shortcuts import redirect, render
from django.conf import settings

from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "home.html")

def maps_view(request):       
    return render(request, 'googleMap.html', {'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY})

def maps_kakao(request):
    return render (request, 'maps.html', {'kakao_maps_api_key': settings.KAKAO_MAPS_API_KEY})

def hotel_list(request):
    return render(request, "hotel_list.html")

def hotel_detail(request):
    return render(request, "hotel_detail.html")