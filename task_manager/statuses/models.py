from django.db import models


class Status(models.Model):
    name = models.CharField("Имя", max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name






'''
самое простое создание модели
from django.db import models
class Status(models.Model):
    # Поле для названия статуса
    name = models.CharField(max_length=100, unique=True)
    
    # Дата создания
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
'''