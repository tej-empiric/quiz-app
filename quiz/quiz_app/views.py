from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import (
    CustomUserCreationForm,
)
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def home(request):
    # TODO : display leaderboard information
    # ordey by score desc of users with users
    return render(request, "quiz_app/home.html")


def play(request):
    # if request.method == "POST":
    #     form = QuestionForm(request.POST)
    # form.is_valid():
    # fetch answer and match it with choice.
    # if choice is equal ans than display message correct
    # if choice is not equal ans than display message incorrect
    # return redirect(request.path)
    # only show 10 random questions to user per quiz, question should not repeat to user, then finish quiz and display the score to user.
    # display timer to user, quiz should end in 10 minutes.
    # form = QuestionForm()
    # context = {"form": form}
    return render(request, "quiz_app/play.html")
