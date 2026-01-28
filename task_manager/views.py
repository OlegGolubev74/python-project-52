#шаг 2, 16.01.2026
from django.shortcuts import render
from django.views.generic import TemplateView #шаг 2, 17.01.2026
from django.contrib.messages.views import SuccessMessageMixin #шаг 3, 21.01.2026
from django.contrib.auth.views import LoginView, LogoutView #шаг 3, 21.01.2026
from django.contrib import messages #шаг 3, 21.01.2026



'''
def index(request):
    return render(
        request,
        "index.html",
        context={
            "who": "Oleg Golubev",
        },
    )
'''


#шаг 2 17.01.2025
class HomePageView(TemplateView):

    """
    Класс-представление для главной страницы.
    Наследует TemplateView и переопределяет контекст.
    """
    #Указываем, какой шаблон использовать
    #Эквивалентно template_name="index.html" в render()
    template_name = "index.html"
    
    #Переопределение контекста
    def get_context_data(self, **kwargs): #метод, который собирает контекст для шаблона
        #division_by_zero = 1 / 0 
        """
        Переопределяем метод для добавления своего контекста.
        """
        # Получаем контекст родительского класса
        context = super().get_context_data(**kwargs)
        
        # Добавляем свои данные в контекст
        #context["who"] = "World! Это самая главная страница сайта."
        print('Показали стартовую страницу')
        
        return context
    

#шаг 3
class LoginView(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    success_message = 'Вы залогинены'

'''
class LogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.info(request, 'Вы разлогинены')
        return super().dispatch(request, *args, **kwargs)
'''
         
class LogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, 'Вы разлогинены')
        return super().dispatch(request, *args, **kwargs)
