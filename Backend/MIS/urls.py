from django.urls import path
from . import views

urlpatterns = [
    path('api/inventory/', views.InventoryItemListCreateView.as_view(), name='inventory-list-create'),
    path('api/financial/', views.FinancialRecordListView.as_view(), name='financial-list'),
    # Other API routes for different modules
]
