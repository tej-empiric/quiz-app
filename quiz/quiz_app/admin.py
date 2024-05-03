from django.contrib import admin
from .models import *


class AnswerAdmin(admin.StackedInline):
    model = Choices
    extra = 1
    max_num = 1


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin]

    search_fields = [
        "question",
        "que_ans__choice_1",
        "que_ans__choice_2",
        "que_ans__choice_3",
        "que_ans__choice_4",
    ]

    list_filter = ["has_published"]

    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.has_published:
            return False
        return True


admin.site.register(Question, QuestionAdmin)
admin.site.register(Quiz)


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):

    list_display = ["user", "score"]
    ordering = ["-score"]


@admin.register(Attempted)
class AttemptedAdmin(admin.ModelAdmin):
    list_display = ["user", "question", "choice"]
