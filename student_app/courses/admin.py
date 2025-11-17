from django.contrib import admin
from .models import Course

# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """
    Admin interface for managing courses.
    Displays: name, instructor, and credits in the list view.
    """
    list_display = ['name', 'instructor', 'credits', 'created_at']
    list_filter = ['credits', 'created_at']
    search_fields = ['name', 'instructor', 'description']
    readonly_fields = ['created_at']
