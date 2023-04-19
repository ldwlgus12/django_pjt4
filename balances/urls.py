from django.urls import path
from . import views

app_name = 'balances'
urlpatterns = [
    path('', views.index, name='index'),
]
