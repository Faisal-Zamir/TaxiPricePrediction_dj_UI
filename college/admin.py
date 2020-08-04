from django.contrib import admin
from . models import Notice, Branch, Profile, Question
from django.contrib.admin.options import ModelAdmin


class NoticeAdmin(ModelAdmin):
    list_display = ["subject", "cr_date"]
    search_fields = ["subject", "msg"]
    list_filter = ["cr_date"]

admin.site.register(Notice, NoticeAdmin)
admin.site.register(Branch)
admin.site.register(Profile)

class QuestionAdmin(ModelAdmin):
    list_display = ["subject", "cr_date"]
    search_fields = ["subject", "msg"]
    list_filter = ["cr_date"]
admin.site.register(Question, QuestionAdmin)

