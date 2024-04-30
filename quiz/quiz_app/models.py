from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Question(BaseModel):
    question = models.CharField(max_length=150)
    marks = models.IntegerField()
    has_published = models.BooleanField(default=False)

    def __str__(self):
        return self.question


class Choices(BaseModel):
    question = models.ForeignKey(
        Question, related_name="que_ans", on_delete=models.CASCADE
    )
    choice_1 = models.CharField(max_length=150)
    choice_2 = models.CharField(max_length=150)
    choice_3 = models.CharField(max_length=150)
    choice_4 = models.CharField(max_length=150)
    answer = models.CharField(max_length=150)

    def __str__(self):
        return self.answer


class Leaderboard(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(null=True)


class Attempted(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, default=settings.AUTH_USER_MODEL
    )
    question = models.ForeignKey(
        Question, related_name="que_attempted", on_delete=models.CASCADE
    )
    choice = models.CharField(max_length=150)


