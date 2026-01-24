from django.db import models
from task_manager.statuses.models import Status
from task_manager.users.models import User

class Task(models.Model):
    name = models.CharField("Имя", max_length=150)
    description = models.TextField("Описание", blank=True)
    
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name="Статус")
    
    author = models.ForeignKey(
        User, 
        on_delete=models.PROTECT, 
        related_name='created_tasks',
        verbose_name="Автор"
    )
    
    executor = models.ForeignKey(
        User, 
        on_delete=models.PROTECT, 
        related_name='executed_tasks',
        null=True,
        blank=True, #Может быть пустым
        verbose_name="Исполнитель"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
