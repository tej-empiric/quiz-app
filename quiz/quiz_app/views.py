from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import (
    CustomUserCreationForm,
)
from django.contrib import messages
from .models import *
from .forms import *
import random
from datetime import datetime, timedelta
from django.utils import timezone


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def home(request):
    leaderboard = Leaderboard.objects.all().order_by("-score", "user_id", "-created_at")
    context = {"leaderboard": leaderboard}
    try:

        leaderboard1 = Leaderboard.objects.filter(user=request.user).order_by(
            "-created_at"
        )
        context = {"leaderboard1": leaderboard1}
    except Exception as e:
        print(f"Error displaying leaderboard {str(e)} ")

    return render(request, "quiz_app/home.html", context)


def quiz(request):
    try:
        quizzes = Quiz.objects.all()
    except Exception as e:
        print(f"Error displaying leaderboard {str(e)} ")

    context = {"quizzes": quizzes}
    return render(request, "quiz_app/quiz.html", context)


def play(request, id):
    try:
        if request.method == "POST":
            try:
                selected_choice = request.POST.get("choice")
                question_id = request.POST.get("question_id")
                question = Question.objects.get(
                    pk=question_id,
                )

                correct_answer = Choices.objects.filter(
                    question=question, answer=selected_choice
                ).exists()

                # Attempted.objects.create(
                #     user=request.user,
                #     question=question,
                #     choice=selected_choice,
                # )

                if correct_answer:
                    request.session["marks"] = (
                        request.session.get("marks", 0) + question.marks
                    )
                    if request.session["question_count"] < 5:
                        messages.success(request, "Correct Answer!")
                else:
                    if request.session["question_count"] < 5:
                        messages.error(request, "Incorrect Answer!")

                if request.session[
                    "question_count"
                ] >= 5 or timezone.now() > timezone.datetime.fromisoformat(
                    request.session["quiz_end_time"]
                ):
                    try:
                        leaderboard = Leaderboard.objects.create(user=request.user)
                        leaderboard.score = (leaderboard.score or 0) + request.session[
                            "marks"
                        ]
                        leaderboard.save()
                        request.session["quiz_started"] = False
                        request.session["question_count"] = 0
                        request.session["marks"] = 0
                    except Exception as e:
                        print(f"Error passing score {str(e)} ")
                    return redirect("score")

            except Exception as e:
                print(f"Error submitting answer {str(e)} ")

            return redirect(request.path)

        if (
            "quiz_started" not in request.session
            or timezone.now()
            > timezone.datetime.fromisoformat(request.session["quiz_end_time"])
        ):
            request.session["quiz_started"] = True
            request.session["quiz_end_time"] = (
                timezone.now() + timedelta(seconds=300)
            ).isoformat()
            request.session["question_count"] = 0
            request.session["marks"] = 0

        if request.session[
            "question_count"
        ] >= 5 or timezone.now() > timezone.datetime.fromisoformat(
            request.session["quiz_end_time"]
        ):
            try:
                leaderboard = Leaderboard.objects.create(user=request.user)
                leaderboard.score = (leaderboard.score or 0) + request.session["marks"]
                leaderboard.save()
                request.session["quiz_started"] = False
                request.session["question_count"] = 0
                request.session["marks"] = 0
            except Exception as e:
                print(f"Error passing score {str(e)} ")
            return redirect("score")

        attempted_questions = Attempted.objects.filter(user=request.user).values_list(
            "question__id", flat=True
        )
        available_questions = Question.objects.filter(
            has_published=True, quiz_id__id=id
        ).exclude(id__in=attempted_questions)

        random_question = random.choice(available_questions)

        choices = Choices.objects.filter(question=random_question)

        request.session["question_count"] += 1

        context = {
            "question": random_question,
            "choices": choices,
            "question_count": request.session["question_count"],
        }

    except Exception as e:
        print(f"Error in play function {str(e)} ")

    return render(request, "quiz_app/play.html", context)


def score(request):
    try:
        leaderboard = Leaderboard.objects.filter(user=request.user).last()
        context = {"leaderboard": leaderboard}

    except Exception as e:
        print(f"Error displaying score {str(e)} ")

    return render(request, "quiz_app/score.html", context)
