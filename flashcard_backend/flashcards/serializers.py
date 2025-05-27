from rest_framework import serializers
from .models import Flashcard

class FlashcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = ['student_id', 'question', 'answer', 'subject']
