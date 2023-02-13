from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect

from to_do_app.models import Task


def add_task(request: WSGIRequest):
    if request.method == "GET":
        return render(request, 'add_new_task.html')
    task_data = {
        'description': request.POST.get('description'),
        'status': request.POST.get('status'),
        'complete_date': request.POST.get('complete_date')
    }
    task = Task.objects.create(**task_data)

    return redirect(f'/task/?pk={task.pk}')
