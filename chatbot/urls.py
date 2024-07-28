from django.urls import path
from .views import GreetingsView

urlpatterns = [
    path('greetings/', GreetingsView.as_view()),
]