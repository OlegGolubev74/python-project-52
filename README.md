### Hexlet tests and linter status:
[![Actions Status](https://github.com/OlegGolubev74/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/OlegGolubev74/python-project-52/actions)

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=OlegGolubev74_python-project-52&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=OlegGolubev74_python-project-52)

[![Quality gate](https://sonarcloud.io/api/project_badges/quality_gate?project=OlegGolubev74_python-project-52)](https://sonarcloud.io/summary/new_code?id=OlegGolubev74_python-project-52)

[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=OlegGolubev74_python-project-52&metric=coverage)](https://sonarcloud.io/summary/new_code?id=OlegGolubev74_python-project-52)


### Демонстрационный проект
https://python-project-52-vc5e.onrender.com


# Менеджер задач (Task Manager) — веб-приложение для управления задачами
Менеджер задач — система управления проектами, позволяющая пользователям создавать, распределять и отслеживать выполнение задач с возможностью установки статусов и меток для удобства организации рабочего процесса.

Проект был построен и использует следующие инструменты:

* Python
* Django
* SQLite
* PostgreSQL
* Bootstrap 5
* Gunicorn
* Ruff
* Rollbar
* Render.com

### Установка и запуск
1. Клонирование репозитория:
```
git clone https://github.com/OlegGolubev74/python-project-52
cd python-project-52
```

2. Установка зависимостей
Используется менеджер пакетов uv:
```
make install
```

3. Применение миграций:
```
make migrate
```

4. Запуск локального сервера:
```
make start
```