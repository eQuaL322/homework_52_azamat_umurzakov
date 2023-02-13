from django.urls import path

from to_do_app.views.tasks import add_view
from to_do_app.views.base import index_view, detail_view

urlpatterns = [
    path('', index_view),
    path('task/add', add_view),
    path('task/', detail_view),
]