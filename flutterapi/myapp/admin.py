from django.contrib import admin
from .models import Todolist


class TodolistAddmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'detail']


admin.site.register(Todolist, TodolistAddmin)
