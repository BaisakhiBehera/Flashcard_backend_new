from django.urls import path
from .views import add_flashcard, get_flashcards

urlpatterns = [
    path('flashcard', add_flashcard, name='add_flashcard'),
    path('get-subject', get_flashcards, name='get_flashcards'),
]
