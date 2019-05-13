from django.http import HttpResponse


def index(request):
    return HttpResponse('click here to enter game --><a href="localhost:8000/game"> GO </a>')
