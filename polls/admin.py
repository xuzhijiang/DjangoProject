from django.contrib import admin
from .models import Question, Choice


# class ChoiceAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {'fields': ['choice_text']})
#     ]

# class ChoickInline(admin.StackedInline):
class ChoickInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Data information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoickInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice, ChoiceAdmin)
