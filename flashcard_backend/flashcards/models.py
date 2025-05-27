from django.db import models

# Create your models here.
class Flashcard(models.Model):
    student_id = models.CharField(max_length=100)
    question = models.TextField()
    answer = models.TextField()
    subject = models.CharField(max_length=100)
