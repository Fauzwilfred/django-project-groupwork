from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Course

# Create your views here.

def home(request):
    """
    Home view - displays the home page with course overview.
    """
    return render(request, 'courses/home.html')

def course_list(request):
    """
    View to display a list of all courses with course selection feature.
    """
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, course_id):
    """
    View to display details of a specific course.
    Includes credits, instructor, and other course information.
    """
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'courses/course_detail.html', {'course': course})
