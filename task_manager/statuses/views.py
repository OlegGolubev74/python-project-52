# from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

# шаг 6, добавили импорты для защиты от удаления
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from task_manager.statuses.models import Status

from .forms import StatusForm

'''
def index(request):
    return HttpResponse("-------------Главная страница приложения Статусы-----")
'''


class StatusListView(LoginRequiredMixin, ListView):
    model = Status
    template_name = 'statuses/statuses_list.html'
    context_object_name = 'statuses'


class StatusCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/create.html'
    success_url = reverse_lazy('statuses_list')
    success_message = 'Статус успешно создан'


class StatusUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/update.html'
    success_url = reverse_lazy('statuses_list')
    success_message = 'Статус успешно изменен'


class StatusDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Status
    template_name = 'statuses/delete.html'
    success_url = reverse_lazy('statuses_list')
    success_message = 'Статус успешно удален'

    # отрабатываем, что нельзя удалять статус, 
    # если он связан с какой-либо задачей
    def form_valid(self, form):
        if self.get_object().task_set.exists():
            messages.error(
                self.request,
                'Невозможно удалить статус, потому что он используется',
            )
            return redirect('statuses_list')
        
        return super().form_valid(form)