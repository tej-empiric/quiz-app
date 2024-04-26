from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *
import random


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )


# class QuestionForm(forms.Form):
#     choices1 = Choices.objects.all()
#     ANS_CHOICES = [
#         ("1", "1"),
#         ("2", "2"),
#         ("3", "3"),
#         ("4", "4"),
#     ]

#     question = forms.CharField(
#         label=choices1.question, widget=forms.RadioSelect(choices=ANS_CHOICES)
#     )
