from . import views
from django.urls import path

app_name = 'evaluations'
urlpatterns = [
    path('home/', views.Home.as_view()),
]