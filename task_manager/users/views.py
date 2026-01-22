from django.shortcuts import render, redirect
#from django.http import HttpResponse
#from django.views.generic import TemplateView
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from task_manager.users.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib import messages  # Добавили импорт сообщений
#from django.utils.translation import gettext_lazy as _
from .forms import MyUserCreationForm, UpdateUserForm #UserForm #, 

'''
def index(request):
    return HttpResponse("-------------users-------")
'''

#cсписок всех пользователей
class UsersListView(ListView):
    model = User
    template_name = "users/users_list.html"
    context_object_name = "users"


class UserCreateView(SuccessMessageMixin, CreateView):
    #print('запустили UserCreateView')
    model = User
    form_class = MyUserCreationForm
    template_name = "users/create.html"
    success_url = reverse_lazy("login")
    #success_message = _("User is successfully registered")
    success_message = 'Пользователь успешно зарегистрирован'

'''
class UserUpdateView(SuccessMessageMixin, UpdateView):
    model = User
    form_class = UpdateUserForm  
    template_name = 'users/update.html'
    success_url = reverse_lazy('users_list')
    success_message = "Профиль успешно обновлен"
'''

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
            
        # 2. Получаем объект, который хотим редактировать, и сравниваем с текущим пользователем
        if self.get_object() != request.user:
            messages.error(request, "У вас нет прав для изменения другого пользователя.")
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
            messages.error(request, "У вас нет прав для изменения другого пользователя.")
            return redirect('users_list')

        # 3. Если проверки пройдены — работаем дальше
        return super().dispatch(request, *args, **kwargs)








'''
class UsersListView(TemplateView):
    """
    Класс-представление для главной страницы приложения users.
    Наследует TemplateView и переопределяет контекст.
    """
    #Указываем, какой шаблон использовать
    #Эквивалентно template_name="index.html" в render()
    template_name = "users/index1.html"
    
    #Переопределение контекста
    def get_context_data(self, **kwargs): #метод, который собирает контекст для шаблона
        """
        Переопределяем метод для добавления своего контекста.
        """
        # Получаем контекст родительского класса
        context = super().get_context_data(**kwargs)
        
        # Добавляем свои данные в контекст
        #context["who"] = "World! Это самая главная страница сайта."
        print('Показали стартовую страницу приложения users index1.html')
        return context
'''