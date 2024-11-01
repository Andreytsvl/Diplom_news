from django.shortcuts import render

def apteks(request):


    context: dict = {
        'title': 'Торговая точка(V)(Это учебный сайт)',
        'content': 'Аптека (V)(Это учебный сайт)',

    }
    return render(request, 'apteks/apteka.html', context)