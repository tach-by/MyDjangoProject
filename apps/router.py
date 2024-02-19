from django.urls import path, include
from apps.project.views import home

app_name= 'router'

urlpatterns=[
    path('', home, name='home'),
    path('tasks/',include('apps.project.urls'))

]