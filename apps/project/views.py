from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from apps.project.models import Task, Project
from apps.project.forms import CreateProjectForm, ProjectUpdateForm
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

def get_project_info_by_id(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    context = {
        "project": project
    }

    return render(
        request=request,
        template_name='project/project_info.html',
        context=context
    )


def update_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)


    if request.method == 'POST':
        form = ProjectUpdateForm(request.POST, instance=project)

        if form.is_valid():
            form.save()
            return redirect('/project')

        context = {
            "form": form,
            "project": project,

        }
    else:
        form = ProjectUpdateForm(instance=project)

        context = {
            "form": form,
            "task": project,

        }

    return render(
        request=request,
        template_name='project/update_project.html',
        context=context
    )

def delete_project(request, project_id):
    task = get_object_or_404(Project, id=project_id)

    task.delete()
    return redirect('/project')
def create_new_project(request):
    if request.method == "POST":
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            project_data = form.cleaned_data
            Project.objects.create(**project_data)
            return redirect('/project')

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