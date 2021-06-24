from django.urls import path
from stats import views

urlpatterns = [

    path('current', views.CurrentStats, name='current-stats'),              #GET, POST with options
    # path('history', views.TodoRetrieveUpdateDestroy.as_view()),  #GET
    # path('clear', views.TodoComplete.as_view()),    #POST with range

]
