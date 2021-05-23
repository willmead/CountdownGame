from django.urls import path

from . import views

app_name = 'number_game'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
