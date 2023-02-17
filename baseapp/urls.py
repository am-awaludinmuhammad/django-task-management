from django.urls import path, include
from .views import task

urlpatterns = [
    path('tasks/', include([
        path('', task.index, name='tasks'),
        path('create/', task.create, name='tasks.create'),
        path('detail/<int:id>/', task.update, name='tasks.detail'),
        path('detail/<int:id>/', task.index, name='tasks.update'),
    ]))
]