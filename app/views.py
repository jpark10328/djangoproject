from django.shortcuts import redirect, render

from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "home.html")

def hotel_list(request):
    return render(request, "hotel_list.html")

def hotel_detail(request):
    return render(request, "hotel_detail.html")