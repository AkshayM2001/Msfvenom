# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('receive_data/', views.receive_data, name='receive_data'),
    path('', views.display_data, name='display_data'),
    path('test_connection/', views.test_connection, name='test_connection'),
    path('start_listener/', views.start_listener, name='start_listener'),
]
