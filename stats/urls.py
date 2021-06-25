from django.urls import path
from stats import views

urlpatterns = [

    path('current', views.current, name='current-stats'),
    path('history', views.history, name='history-stats'),
    path('clear', views.clear, name='clear-stats'),


]
