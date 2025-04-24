# 🌳 Django Tree Menu

Простое и эффективное Django-приложение для построения древовидных меню с поддержкой вложенности, активных элементов и удобной админкой.

---

## 🚀 Быстрый старт

### 📥 Клонирование проекта

```bash
git clone https://github.com/baxtdev/menu_app.git
cd menu_app
```

### 🐍 2. Установка зависимостей

Создай виртуальное окружение и установи зависимости:

```bash
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
pip install -r requirements.txt
```

#### Пример `requirements.txt`:

```
Django>=4.0,<5.0
```

---

### ⚙️ 3. Применение миграций и запуск проекта

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser  # Создай администратора
python manage.py runserver
```

---

## 🛠️ 4. Добавление меню (через Django shell)

Если ты не хочешь заходить в админку, можно добавить меню и пункты напрямую:

```bash
python manage.py shell
```

```python
from menu.models import Menu, MenuItem

menu = Menu.objects.create(name='main_menu')

home = MenuItem.objects.create(menu=menu, title='Главная', named_url='home', order=0)
about = MenuItem.objects.create(menu=menu, title='О нас', named_url='about', order=1)
team = MenuItem.objects.create(menu=menu, title='Команда', url='/about/team/', parent=about, order=0)
history = MenuItem.objects.create(menu=menu, title='История', url='/about/history/', parent=about, order=1)
```

> Не забудь, что `named_url` должен существовать в `urls.py`, например:
> `path('about/', views.about, name='about')`

---