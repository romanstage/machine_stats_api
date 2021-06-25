from django.urls import path
from stats import views

urlpatterns = [

    path('current', views.CurrentStats, name='current-stats'),              #GET, POST with options
    path('history', views.HistoryStats, name='history-stats'),  #GET
    path('clear', views.ClearStats, name='clear-stats'),    #POST with range
    #REDIS
    path('current/redis', views.current_redis_view, name='current-redis-stats'),
    path('history/redis', views.history_redis_view, name='history-redis-stats'),
    path('clear/redis', views.clear_redis_view, name='clear-redis-stats'),


]
