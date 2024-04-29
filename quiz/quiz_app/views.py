from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import (
    CustomUserCreationForm,
)
from django.contrib import messages
from .models import *
from .forms import *
import random


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def home(request):
    # TODO : display leaderboard information
    # ordey by score desc of users with users
    return render(request, "quiz_app/home.html")


def play(request):

    # validate form, fetch selected choice and match it with answer.
    # if choice is equal ans than display message correct
    # if choice is not equal ans than display message incorrect
    # attempted question should be saved in attempted model
    # return redirect(request.path)
    # only show 10 random questions to user per quiz, question should not repeat to user, then finish quiz.
    # save score in Leaderboard model and display the score to user.
    # display timer to user, quiz should end in 10 minutes.

    if request.method == "POST":
        selected_choice = request.POST.get("choice")

    random_question = random.choice(Question.objects.filter(has_published=True))
    choices = Choices.objects.filter(question=random_question)

    context = {
        "question": random_question,
        "choices": choices,
    }

    return render(request, "quiz_app/play.html", context)
