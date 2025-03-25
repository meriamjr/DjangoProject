from django.urls import path
from . import views

app_name = 'reservation'

urlpatterns = [
    path('reserver/', views.reserver_table, name='reserver_table'),
    path('confirmation/', views.confirmation_reservation,
    name='confirmation_reservation'),
]