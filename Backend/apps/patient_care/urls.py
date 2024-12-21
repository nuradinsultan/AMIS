# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('patient/<int:patient_id>/', views.patient_detail, name='patient_detail'),
]
