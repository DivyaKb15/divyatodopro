from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.task_view, name='task_view'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cvtask/',views.TaskListView.as_view(),name='cvtask'),
    path('cvdetail/<int:pk>/', views.TaskDetailView.as_view(), name='cvdetail'),
    path('cvupdate/<int:pk>/', views.TaskUpdateView.as_view(), name='cvupdate'),
    path('cvdelete/<int:pk>/', views.TaskDeletelView.as_view(), name='cvdelete'),
]
