from django.urls import path
from .views import TaskView,TaskUpdate,TaskDelete,TaskCreate,TaskStatus
urlpatterns = [
    path('', TaskView.as_view(), name='task-list'),
    path('<int:pk>/update', TaskUpdate.as_view(), name='task-update'),
    path('<int:pk>/delete', TaskDelete.as_view(), name='task-delete'),
    path('create/', TaskCreate.as_view(), name='task-create'),
    path('<int:pk>/status/', TaskStatus.as_view(), name='task-status'),
]
