from django.contrib import admin
from .models import Todo
# Register your models here.
@admin.register(Todo)
class TODOAdmin(admin.ModelAdmin):
    pass