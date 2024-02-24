from django.urls import path
from apps.project.views import get_all_tasks, create_new_project, get_all_projects

appname='project'
urlpatterns=[
    path('', get_all_projects, name='get_all_projects'),
    path('task/', get_all_tasks, name='get_all_tasks'),
    path('create/', create_new_project, name='create')


]