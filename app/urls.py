from django.urls import path
from app.views import home,TaskCreateView, TaskUpdateView, TaskDetailView, My_Task, TaskDeleteView, TaskCompleteView

urlpatterns = [
    path('',home,name='Home'),
    path('MyTask',My_Task, name='My Task'),

    path('create',TaskCreateView.as_view(),name='Create'),
    path('<int:pk>',TaskDetailView.as_view(),name='Details'),
    path('Update/<int:pk>',TaskUpdateView.as_view(),name='Update'),
    path('Delete/<int:pk>',TaskDeleteView.as_view(),name='Delete'),
    path('complete/<int:id>',TaskCompleteView.as_view(),name='Complete'),
]