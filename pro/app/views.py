from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import fitz

from app.ai_engine.preprocess import (
    clean_text,
    sentence_split,
    word_split,
    remove_stopwords,
    lemmatize,
)

from app.ai_engine.keyword_extractor import extract_keywords
from app.ai_engine.mcq_generator import generate_mcqs


def home(request):

    mcqs = []

    if request.method == "POST":

        pdf = request.FILES.get("pdf_file")
        difficulty = request.POST.get("difficulty")
        mcq_count = request.POST.get("mcq_count")

        if pdf:

            fs = FileSystemStorage()
            filename = fs.save(pdf.name, pdf)
            file_path = fs.path(filename)

            pdf_document = fitz.open(file_path)

            extracted_text = ""

            for page in pdf_document:
                extracted_text += page.get_text()

            pdf_document.close()

            cleaned_text = clean_text(extracted_text)

            sentences = sentence_split(cleaned_text)

            words = word_split(cleaned_text)

            filtered_words = remove_stopwords(words)

            lemmatized_words = lemmatize(filtered_words)

            keywords = extract_keywords(cleaned_text)

            mcqs = generate_mcqs(
                sentences,
                keywords,
                int(mcq_count)
            )

    return render(request, "home.html", {
        "mcqs": mcqs
    })
