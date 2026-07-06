======================================================================
                    AI MCQ GENERATOR
======================================================================

Developer
---------
Name : Atik
Course : B.Sc. Computer Science
Field of Interest :
Artificial Intelligence | Machine Learning | NLP | Django

----------------------------------------------------------------------
PROJECT OVERVIEW
----------------------------------------------------------------------

AI MCQ Generator is an intelligent web application that automatically
generates Multiple Choice Questions (MCQs) from PDF documents.

Users can upload any educational PDF, choose the difficulty level,
select the number of MCQs, and the system automatically generates
MCQs using Natural Language Processing (NLP) and Machine Learning
techniques.

The generated MCQs can also be downloaded as a PDF.

----------------------------------------------------------------------
MAIN FEATURES
----------------------------------------------------------------------

✔ Upload PDF Files

✔ Extract Text from PDF

✔ NLP Text Preprocessing
   • Text Cleaning
   • Sentence Tokenization
   • Word Tokenization
   • Stopword Removal
   • Lemmatization

✔ Keyword Extraction

✔ AI-based MCQ Generation

✔ Difficulty Selection
   • Low
   • Medium
   • High

✔ Select Number of Questions

✔ Display Generated MCQs

✔ Download Generated MCQs as PDF

✔ Clean and Responsive User Interface

----------------------------------------------------------------------
TECH STACK
----------------------------------------------------------------------

Backend
-------
• Python
• Django

Artificial Intelligence
-----------------------
• Machine Learning
• Natural Language Processing (NLP)

Libraries
---------
• PyMuPDF (PDF Processing)
• ReportLab (PDF Generation)
• NLTK
• Random

Frontend
--------
• HTML5
• CSS3

----------------------------------------------------------------------
PROJECT WORKFLOW
----------------------------------------------------------------------

Step 1
------
User uploads a PDF.

↓

Step 2
------
Text is extracted from the PDF.

↓

Step 3
------
NLP preprocessing is applied.

↓

Step 4
------
Important keywords are extracted.

↓

Step 5
------
MCQs are generated automatically.

↓

Step 6
------
Generated MCQs are displayed.

↓

Step 7
------
User downloads MCQs as a PDF.

----------------------------------------------------------------------
PROJECT STRUCTURE
----------------------------------------------------------------------

AI_MCQ_GENERATOR

│
├── app
│   ├── ai_engine
│   │   ├── preprocess.py
│   │   ├── keyword_extractor.py
│   │   └── mcq_generator.py
│   │
│   ├── templates
│   │   └── home.html
│   │
│   ├── static
│   │
│   ├── views.py
│   ├── urls.py
│   └── models.py
│
├── media
├── manage.py
├── requirements.txt
└── README.md

----------------------------------------------------------------------
HOW TO RUN
----------------------------------------------------------------------

1. Clone Repository

git clone <repository_link>

2. Move into Project Folder

cd AI_MCQ_GENERATOR

3. Install Dependencies

pip install -r requirements.txt

4. Apply Migrations

python manage.py migrate

5. Run Server

python manage.py runserver

6. Open Browser

http://127.0.0.1:8000/

----------------------------------------------------------------------
SCREENSHOTS
----------------------------------------------------------------------

• Home Page

• Upload PDF

• Generated MCQs

• Downloaded PDF

(Add screenshots inside GitHub README)

----------------------------------------------------------------------
FUTURE IMPROVEMENTS
----------------------------------------------------------------------

• Login & Registration

• Database Storage

• Quiz Mode

• Timer Based Exam

• Answer Key Download

• AI-based Better Distractor Generation

• Deep Learning Model Integration

• Multi-language Support

• Performance Analytics

• Cloud Deployment

----------------------------------------------------------------------
PROJECT OBJECTIVE
----------------------------------------------------------------------

The objective of this project is to automate MCQ generation from
educational PDF documents using Artificial Intelligence and Natural
Language Processing. This system helps students and teachers quickly
create quizzes while reducing manual effort.

----------------------------------------------------------------------
AUTHOR
----------------------------------------------------------------------

Atik

B.Sc. Computer Science

Interested in

• Artificial Intelligence
• Machine Learning
• Deep Learning
• Natural Language Processing
• Django Development
• Software Engineering

GitHub :
(Add Your GitHub Profile Link)

LinkedIn :
(Add Your LinkedIn Profile Link)

======================================================================
Thank you for visiting this repository.
If you found this project useful, please consider giving it a ⭐.
======================================================================
