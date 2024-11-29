from django.urls import path
from . import views


urlpatterns = [
    path('', views.execute_query, name='execute_query'),
    path('download-csv/', views.download_csv, name='download_csv'),
    path('auto_search/', views.auto_search, name='auto_search'),

   
]
