from django.shortcuts import render, redirect
from django.http import HttpRequest
from apps.project.models import Task, Project
from apps.project.forms import CreateProjectForm
from apps.project.choises import STATUS_CHOICES, PRIORITY_CHOICES
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

def get_all_projects(request: HttpRequest, *args, **kwargs):
    projects = Project.objects.all()
    context = {
        "projects": projects
    }

    return render(
        request=request,
        template_name='project/all_projects.html',
        context=context
    )



def create_new_project(request):
    if request.method == "POST":
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            project_data = form.cleaned_data
            Project.objects.create(**project_data)
            return redirect('router:project:get_all_projects')

        context = {
            "form": form,

        }
    else:
        form = CreateProjectForm()
        context = {
            "form": form,
                    }

    return render(
        request=request,
        template_name='project/create_project.html',
        context=context
    )