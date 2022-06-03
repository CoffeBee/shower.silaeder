from django.shortcuts import render
from .models import Student

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def add(request):
    # S
    Student.objects.create(id = 1, position =1)
    return HttpResponse(status=200)
