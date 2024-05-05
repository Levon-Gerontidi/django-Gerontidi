from django.urls import path
from tasks import views

app_name = 'tasks'

"""
Для задания №3 (лекция №6 Диспетчер URL Django)

urlpatterns = [
    path('', views.index, name='index'),
    path('another/', views.another_page, name='another_page'),
]
"""

urlpatterns = [
    # path('', views.index, name='index'),
    # path('projects/', views.projects_list, name='projects_list'),
    # path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    # path('projects/<int:project_id>/tasks/<int:task_id>/', views.task_detail, name='task_detail'),

    path('', views.IndexView.as_view(), name='index'),
    path('projects/', views.ProjectsListView.as_view(), name='projects_list'),
    path('projects/<int:project_id>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('projects/<int:project_id>/tasks/<int:task_id>/', views.TaskDetailView.as_view(), name='task_detail'),
]