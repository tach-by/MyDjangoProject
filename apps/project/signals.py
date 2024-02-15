from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from apps.project.models import Project, Task




@receiver(post_delete, sender=Task)
def log_task_delete(sender, **kwargs):
    print(f'Удалён объект {sender.__name__}.')

@receiver(post_save, sender=Task)
def log_task_create(sender, **kwargs):
    print(f'Создан объект {sender.__name__}.')


@receiver(post_save, sender=Project)
def log_project_or_task_update(sender, **kwargs):
    print(f'Создан объект {sender.__name__}.')


@receiver(post_delete, sender=Project)
def log_project_or_task_update(sender, **kwargs):
    print(f'Удалён объект {sender.__name__}.')


@receiver(post_save, sender=User)
def log_superuser_creation(sender, instance, created, **kwargs):
    if created and instance.is_superuser:
        print('Создан суперпользователь.')
