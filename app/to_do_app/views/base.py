from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from to_do_app.models import Task


def index_view(request: WSGIRequest):
    return render(request, 'index.html')


def tasks_list(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'index.html', context=context)
