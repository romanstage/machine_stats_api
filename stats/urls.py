from django.urls import path
from stats import views

urlpatterns = [

    path('current', views.CurrentStats, name='current-stats'),              #GET, POST with options
    path('history', views.HistoryStats, name='history-stats'),  #GET
    path('clear', views.ClearStats, name='clear-stats'),    #POST with range
    #REDIS
    path('clear/redis', views.redis_view, name='redis-stats'),


]
