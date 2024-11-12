from django.shortcuts import render


def platform_page(request):
    title = 'Лучшее описание игр!'
    page = "Главная страница"
    context = {
        'title': title,
        'page': page
    }
    return render(request, 'fourth_task/platform.html', context)


def card_page(request):
    title = 'Тут ты кое что узнаешь!'
    page = "Рубрика: 'А ты знал Чтоооо...'"
    context = {
        'title': title,
        'page': page
    }
    return render(request, "fourth_task/card.html", context)


def games_page(request):
    title = 'Игры игрульки'
    page = "Игры"
    context = {
        'title': title,
        'page': page,
        'games': ['Baldur`s Gate 3','Pathfinder: Wrath of the Righteous','State of Decay']
    }
    return render(request, 'fourth_task/games.html', context)


