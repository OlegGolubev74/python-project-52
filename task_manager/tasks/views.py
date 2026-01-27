from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from .models import Task
from .forms import TaskForm
from django_filters.views import FilterView #шаг 7
from .filters import TaskFilter #шаг 7

''' предыдущая версия класса до шага 7
class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/tasks_list.html'
    context_object_name = 'tasks'
'''
class TaskListView(LoginRequiredMixin, FilterView):
    model = Task
    template_name = 'tasks/tasks_list.html'
    context_object_name = 'tasks'
    filterset_class = TaskFilter # шаг 7, указываем класс фильтра
    
    def get_queryset(self):
        return Task.objects.select_related('status', 'author', 'executor').prefetch_related('labels')

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'

class TaskCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/create.html'
    success_url = reverse_lazy('tasks_list')
    success_message = 'Задача успешно создана'

    def form_valid(self, form):
        # Текущий пользователь становится автором автоматически
        form.instance.author = self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/update.html'
    success_url = reverse_lazy('tasks_list')
    success_message = 'Задача успешно изменена'

class TaskDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('tasks_list')
    success_message = 'Задача успешно удалена'

    def dispatch(self, request, *args, **kwargs):
        # Проверка: удалять может только автор
        if self.get_object().author != request.user:
            messages.error(request, 'Задачу может удалить только её автор')
            return redirect('tasks_list')
        return super().dispatch(request, *args, **kwargs)
