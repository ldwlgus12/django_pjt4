from django.urls import path
from . import views

app_name = 'balances'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/delete', views.delete, name='delete'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/answer/<str:balance_answer>', views.answer, name='answer'),
    path('<int:pk>/comment_create/', views.comment_create, name='comment_create'),
    path('<int:pk>/likes/', views.likes, name='likes'),
    path('search/', views.search, name='search'),
]
