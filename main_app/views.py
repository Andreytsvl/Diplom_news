from django.shortcuts import render
from django.http import HttpResponse

from products_app.models import Categories

def index(request):


    context: dict = {
        'title': 'Главная страница магазина Аптека (V)(Это учебный сайт)',
        'content': 'Магазин Аптека (V)',

    }
    return render(request, 'main_app/index.html', context)

def about(request):
    context: dict = {
        'title': 'О нас  (Это учебный сайт)',
        'content_page': 'Адрес. Телефон.',
        'text': 'Наши преимущества',
    }
    return render(request, 'main_app/about.html', context)