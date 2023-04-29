from django.contrib import admin
from .models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'important', 'user']
    list_editable = ['important']
    readonly_fields = ['created']
