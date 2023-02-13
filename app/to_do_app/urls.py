from django.urls import path

from to_do_app.views.base import tasks_list, task_view

urlpatterns = [
    path('', tasks_list),
    path('task/', task_view)
]
