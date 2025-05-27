#  Smart Flashcard Backend API
This is a Django REST Framework (DRF) project for a **Smart Flashcard System**. Users can add flashcards with questions and answers. The system automatically **infers the subject** based on keywords. Later, users can fetch flashcards grouped across different subjects.
**Live API Base URL**  [https://flashcard-backend-new-ca69.onrender.com](https://flashcard-backend-new-ca69.onrender.com)

## 🚀 Features

-  Add flashcards with automatic **subject classification** (rule-based)
-  Fetch a **mix of flashcards from different subjects**
-  Supports multiple students (`student_id`)
-  Built with **Django**, **DRF**, and **PostgreSQL**
- Deployed on **Render**

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/BaisakhiBehera/Flashcard_backend_new.git
cd Flashcard_backend_new

### 2. Create and activate Virtual Environment (for Windows)
python -m venv venv
venv\Scripts\activate

### 3. Install Dependencies
pip install -r requirements.txt

⚙️ Database Setup (PostgreSQL)
Create a PostgreSQL database (e.g., flashcard_db)
You can use Supabase, ElephantSQL, or local PostgreSQL.

Update settings.py:DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'flashcard_db',
        'USER': 'your_postgres_username',
        'PASSWORD': 'your_postgres_password',
        'HOST': 'your_db_host',
        'PORT': '5432',
    }
}
Apply Migrations and 🏃 Run the Server Locally : python manage.py runserver

API Endpoints:
1️⃣ Add Flashcard
POST /flashcard

Live URL: https://flashcard-backend-new-ca69.onrender.com/flashcard
Request:{
  "student_id": "stu001",
  "question": "What is photosynthesis?",
  "answer": "A process used by plants to convert light into energy"
}
Response:{
  "message": "Flashcard added successfully",
  "subject": "Biology"
}

Get Flashcards
GET /get-subject?student_id=stu001&limit=4

Live URL: https://flashcard-backend-new-ca69.onrender.com/get-subject?student_id=stu001&limit=2

🔼 Sample Response:[
    {
        "student_id": "stu001",
        "question": "State Newton's first law of motion.",
        "answer": "An object remains at rest or in uniform motion unless acted upon by an external force.",
        "subject": "Physics"
    },
    {
        "student_id": "stu001",
        "question": "What is the process of photosynthesis in plants?",
        "answer": "Photosynthesis is the process where green plants use sunlight to make food from carbon dioxide and water.",
        "subject": "Biology"
    }
]
