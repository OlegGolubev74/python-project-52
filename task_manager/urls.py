"""
URL configuration for task_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from task_manager import views #шаг 2, 16.01.2026

urlpatterns = [
    #path("", views.index), #шаг 2, 16.01.2026
    path('', views.HomePageView.as_view(), name='start_page'),#шаг 2, 17.01.2026
    path('admin/', admin.site.urls),
    path('users/', include('task_manager.users.urls'), name='users_list'),
    path('login/', views.LoginView.as_view(), name='login'), #шаг 3 
    path('logout/', views.LogoutView.as_view(), name='logout'), #шаг 3
    path('statuses/', include('task_manager.statuses.urls'), name='statuses_list'), #шаг4 23.01.2025
    path('tasks/', include('task_manager.tasks.urls'), name='tasks_list'),#шаг5 24.01.2025
    path('labels/', include('task_manager.labels.urls'), name='labels_list'), #шаг 6
]
