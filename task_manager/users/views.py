from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from task_manager.users.models import User

from .forms import MyUserCreationForm, UpdateUserForm


# cсписок всех пользователей
class UsersListView(ListView):
    model = User
    template_name = "users/users_list.html"
    context_object_name = "users"


class UserCreateView(SuccessMessageMixin, CreateView):
    # print('запустили UserCreateView')
    model = User
    form_class = MyUserCreationForm
    template_name = "users/create.html"
    success_url = reverse_lazy("login")
    success_message = 'Пользователь успешно зарегистрирован'


class UserUpdateView(SuccessMessageMixin, UpdateView):
    model = User
    form_class = UpdateUserForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users_list')
    success_message = 'Пользователь успешно изменен'

    def dispatch(self, request, *args, **kwargs):
        # 1. Сначала проверяем, залогинен ли пользователь вообще
        if not request.user.is_authenticated:
            return redirect('login')
            
        # 2. Получаем объект, который хотим редактировать, 
        # и сравниваем с текущим пользователем
        if self.get_object() != request.user:
            messages.error(
                request, 
                "У вас нет прав для изменения другого пользователя."
            )
            return redirect('users_list')

        # 3. Если всё в порядке, разрешаем стандартную работу метода dispatch
        return super().dispatch(request, *args, **kwargs)
    

class UserDeleteView(SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users_list')
    success_message = 'Пользователь успешно удален'

    def dispatch(self, request, *args, **kwargs):
        # 1. Проверка на авторизацию
        if not request.user.is_authenticated:
            return redirect('login')

        # 2. Проверка прав (только самого себя)
        if self.get_object() != request.user:
            messages.error(
                request, 
                "У вас нет прав для изменения другого пользователя."
            )
            return redirect('users_list')

        # 3. Если проверки пройдены — работаем дальше
        return super().dispatch(request, *args, **kwargs)