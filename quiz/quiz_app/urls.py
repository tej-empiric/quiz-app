from django.urls import path
from . import views

urlpatterns = [
    path("accounts/signup/", views.SignUpView.as_view(), name="signup"),
    path("", views.home, name="home"),
    path("play/<int:id>/", views.play, name="play"),
    path("score/", views.score, name="score"),
    path("quiz/", views.quiz, name="quiz"),
]
