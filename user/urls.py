from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from . import views

app_name="user"

urlpatterns = [

    # http://127.0.0.1:8000/user/register

    path("register/", views.user_register, name="user_register"),

    path('login/', auth_views.LoginView.as_view(template_name="user/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
]