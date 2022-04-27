from django.http import HttpResponse

def index(request):
    return HttpResponse('Главная страница')


def group_posts(request):
    return HttpResponse('Группы')


def group_filter(request, slug):
    return HttpResponse(f'Подборка {slug}')
