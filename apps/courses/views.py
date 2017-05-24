from django.shortcuts import render, redirect
from .models import *


# Create your views here.
def index(request):
    courses=Course.objects.all().order_by('-id')
    context={
        'courses': courses
    }
    return render(request, 'courses/index.html', context)

def create(request):
    Course.objects.create(name=request.POST['name'], description=request.POST['description'])
    return redirect('/')


def confirmation(request, id):
    Course.objects.filter(id=id).delete()
    return render(request, 'courses/delete.html', context)


def delete(request, id):
    Course.objects.filter(id=id).delete()
    return redirect('/')
