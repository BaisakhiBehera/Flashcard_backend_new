from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Flashcard
from .serializers import FlashcardSerializer
from .utils import infer_subject
import random



@api_view(['POST'])
def add_flashcard(request):
    data = request.data
    student_id = data.get('student_id')
    question = data.get('question')
    answer = data.get('answer')

    if not student_id or not question or not answer:
        return Response({"error": "student_id, question and answer are required"}, status=400)

    subject = infer_subject(question)

    flashcard = Flashcard.objects.create(
        student_id=student_id,
        question=question,
        answer=answer,
        subject=subject
    )

    return Response({
        "message": "Flashcard added successfully",
        "subject": subject
    })


@api_view(['GET'])
def get_flashcards(request):
    student_id = request.query_params.get('student_id')
    limit = request.query_params.get('limit')

    if not student_id:
        return Response({"error": "student_id query param is required"}, status=400)

    try:
        limit = int(limit)
    except (TypeError, ValueError):
        limit = 5  # default limit if not provided or invalid

    flashcards = Flashcard.objects.filter(student_id=student_id)

    # Group flashcards by subject, pick one per subject
    subject_map = {}
    for fc in flashcards:
        if fc.subject not in subject_map:
            subject_map[fc.subject] = fc
        if len(subject_map) >= limit:
            break

    selected_flashcards = list(subject_map.values())

    # Shuffle the list to mix subjects
    random.shuffle(selected_flashcards)

    serializer = FlashcardSerializer(selected_flashcards, many=True)
    return Response(serializer.data)

