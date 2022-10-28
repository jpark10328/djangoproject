from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from app import views

urlpatterns = [
    path("admin/", admin.site.urls),

    # http://127.0.0.1:8000/app
    path("app/", include("app.urls")),

    # http://127.0.0.1:8000/
    path("", views.home, name="index"),

    path("user/", include("user.urls")),

    path("accounts/",include('allauth.urls')),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
