from django.urls import path
from apps.project.views import get_all_tasks

appname='tasks'
urlpatterns=[
    path('', get_all_tasks, name='get_all_tasks')


]