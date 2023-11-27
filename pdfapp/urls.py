from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_pdf, name='upload_pdf'),
    path('show-csv/', views.show_csv, name='show_csv'),
]
