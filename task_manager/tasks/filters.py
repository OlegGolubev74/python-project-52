import django_filters
from django import forms
from .models import Task
from task_manager.labels.models import Label

class TaskFilter(django_filters.FilterSet):
    # Поля для выпадающих списков
    labels = django_filters.ModelChoiceFilter(
        queryset=Label.objects.all(),
        label='Метка'
    )
    
    # Чекбокс 
    self_tasks = django_filters.BooleanFilter(
        widget=forms.CheckboxInput,
        method='filter_self_tasks',
        label='Только свои задачи'
    )

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']

    def filter_self_tasks(self, queryset, name, value):
        if value:
            # показываем только задачи, где автор — текущий пользователь
            return queryset.filter(author=self.request.user)
        return queryset
