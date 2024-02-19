from django.shortcuts import render
from django.http import HttpRequest
from apps.project.models import Task
# Create your views here.
def home(request: HttpRequest, *args, **kwargs):
    contex = {
        "data": "Hello from context"
    }
    return render(
        request= request,
        template_name='project/home.html',
        context=contex

    )

def get_all_tasks(request: HttpRequest, *args, **kwargs):
    tasks = Task.objects.all()
    context = {
        "tasks": tasks
    }

    return render(
        request=request,
        template_name='project/all_tasks.html',
        context=context
    )