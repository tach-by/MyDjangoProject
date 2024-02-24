from django.urls import path
from apps.project.views import get_all_tasks,\
    create_new_project, \
    get_all_projects, \
    get_project_info_by_id, \
    update_project

appname='project'
urlpatterns=[
    path('', get_all_projects, name='get-all-projects'),
    path('task/', get_all_tasks, name='get-all-tasks'),
    path('create/', create_new_project, name='create'),
    path('<int:project_id>/', get_project_info_by_id, name='project-info'),
    path("<int:project_id>/update/", update_project, name='update-project'),


]