from django.shortcuts import render


def platform_page(request):
    title = 'Лучшее описание игр!'
    context = {'title': title}
    return render(request, 'third_task/platform.html', context)


def card_page(request):
    return render(request, "third_task/card.html")


def games_page(request):
    context = {
        'game_1': 'Baldur`s Gate 3',
        'game_2': 'Pathfinder: Wrath of the Righteous',
        'game_3': 'State of Decay'
    }
    return render(request, 'third_task/games.html', context)
# Create your views here.
