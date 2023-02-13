from django.urls import path

from to_do_app.views.base import index_view, tasks_list

urlpatterns = [
    path('', index_view),
    path('tasks', tasks_list)
]
