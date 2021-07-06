from django.contrib import admin
from module.fb88.models import Fb88,Question,Answer


class Fb88Admin(admin.ModelAdmin):
    list_display = ('id','name','created','updated')
    list_filter = ('id','name','created','updated')
    search_fields = ('id','name')


admin.site.register(Fb88,Fb88Admin)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id','name','created','update')
    list_filter = ('id','name','created','update')
    search_fields = ('id','name')

# admin.site.register(Question, QuestionAdmin)

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created', 'updated')
    list_filter = ('id', 'name', 'created', 'updated')
    search_fields = ('id', 'name')
# Register your models here.
