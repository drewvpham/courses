from django.shortcuts import render, redirect
from .models import *


def index(request):
    courses=Course.objects.all().order_by('-id')
    context={
        'courses': courses
    }
    return render(request, 'courses/index.html', context)

def create(request):
    course=Course.objects.create(name=request.POST['name'])
    Description.objects.create(content=request.POST['description'], course=course)
    return redirect('/')

def confirmation(request, id):
    course=Course.objects.filter(id=id)
    context={
        'course': course
    }
    print context
    return render(request, 'courses/destroy.html', context)


def destroy(request, id):
    Course.objects.filter(id=id).delete()
    return redirect('/')
