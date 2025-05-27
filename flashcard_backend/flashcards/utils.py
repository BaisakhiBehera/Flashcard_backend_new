def infer_subject(question):
    question_lower = question.lower()

    if any(keyword in question_lower for keyword in ['photosynthesis', 'plant', 'biology', 'cell']):
        return "Biology"
    elif any(keyword in question_lower for keyword in ['newton', 'force', 'velocity', 'physics', 'acceleration']):
        return "Physics"
    elif any(keyword in question_lower for keyword in ['algebra', 'geometry', 'math', 'calculus']):
        return "Math"
    elif any(keyword in question_lower for keyword in ['revolution', 'war', 'history', 'empire']):
        return "History"
    elif any(keyword in question_lower for keyword in ['atom', 'chemical', 'reaction', 'chemistry']):
        return "Chemistry"
    else:
        return "General"
