from django.urls import path
from . import views

urlpatterns = [
    path('', views.paper_list, name='paper_list'),
    path('create/', views.paper_create, name='paper_create'),
    path('update/<str:paper_id>/', views.paper_update, name='paper_update'),
    path('delete/<str:paper_id>/', views.paper_delete, name='paper_delete'),
]