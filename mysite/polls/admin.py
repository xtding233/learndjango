from django.contrib import admin
from .models import Question, Choice
# Register your models here.

class ChocieInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    #field = ["pub_date", "question_text"]
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date Information", {"fields" : ["pub_date"]}),
    ]
    inlines = [ChocieInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]

admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)
