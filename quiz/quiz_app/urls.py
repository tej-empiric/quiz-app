from django.urls import path
from . import views

urlpatterns = [
    path("accounts/signup/", views.SignUpView.as_view(), name="signup"),
    path("", views.home, name="home"),
    path("play/", views.play, name="play"),
]
