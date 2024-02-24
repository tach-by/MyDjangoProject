from django.contrib.auth.models import User
from django.forms import fields, widgets, Form
from django.forms import ModelForm

from apps.project.choises import STATUS_CHOICES, PRIORITY_CHOICES
from apps.project.models import (
    Task,
    Project
)



class CreateProjectForm(Form):
    name = fields.CharField(max_length=200)
    description = fields.CharField(max_length=2000)

    class Meta:
        model=Project
        fields=[
            'name',
            'discription'
        ]


class ProjectUpdateForm(ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'description', )