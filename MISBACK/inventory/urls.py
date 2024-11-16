# backend/inventory/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.InventoryListView.as_view(), name='inventory_list'),
    path('add/', views.InventoryCreateView.as_view(), name='inventory_add'),
    path('<int:pk>/', views.InventoryDetailView.as_view(), name='inventory_detail'),
    path('<int:pk>/edit/', views.InventoryUpdateView.as_view(), name='inventory_edit'),
    path('<int:pk>/delete/', views.InventoryDeleteView.as_view(), name='inventory_delete'),
]
