#шаг 2, 16.01.2026
from django.shortcuts import render
from django.views.generic import TemplateView #шаг 2, 17.01.2026



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
        """
        Переопределяем метод для добавления своего контекста.
        """
        # Получаем контекст родительского класса
        context = super().get_context_data(**kwargs)
        
        # Добавляем свои данные в контекст
        context["who"] = "World! Это самая главная страница сайта."
        print('Показали стартовую страницу')
        return context
