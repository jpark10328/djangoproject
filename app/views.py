from django.shortcuts import redirect, render,get_object_or_404
from django.conf import settings

from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import Hotel, Room


def home(request):
    return render(request, "home.html")

def maps_view(request):       
    return render(request, 'googleMap.html', {'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY})

def maps_kakao(request):
    return render (request, 'maps.html', {'kakao_maps_api_key': settings.KAKAO_MAPS_API_KEY})

def hotel_list(request):
    """
    호텔 리스트 목록
    """
    hotels = Hotel.objects.order_by("id")


    return render(request, "hotel_list.html", {"hotels":hotels})

def hotel_detail(request,pk):

    hotel = get_object_or_404(Hotel, pk=pk)
    rooms = Room.objects.filter(hotel=hotel)

    return render(request, "hotel_detail.html",{"hotel":hotel,"rooms":rooms})