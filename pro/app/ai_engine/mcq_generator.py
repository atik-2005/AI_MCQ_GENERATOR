import random


def generate_mcqs(
    sentences,
    keywords,
    count,
    difficulty="Low",
    excluded_questions=None,
):
    excluded_questions = excluded_questions or set()

    usable_sentences = [
        sentence
        for sentence in sentences
        if len(sentence.split()) > 6
        and len(sentence.split()) < 40
        and "include" not in sentence.lower()
        and "printf" not in sentence.lower()
        and "void" not in sentence.lower()
        and "main" not in sentence.lower()
    ]

    random.shuffle(usable_sentences)
    shuffled_keywords = list(keywords)
    random.shuffle(shuffled_keywords)

    candidates = []
    seen_questions = set()

    for sentence in usable_sentences:
        for keyword in shuffled_keywords:
            if keyword.lower() not in sentence.lower():
                continue

            question = sentence.replace(keyword, "_____")
            if question in seen_questions:
                continue

            seen_questions.add(question)
            distractors = [
                item for item in shuffled_keywords
                if item.lower() != keyword.lower()
            ]
            random.shuffle(distractors)

            options = [keyword, *distractors[:3]]
            while len(options) < 4:
                options.append("None of the above")

            random.shuffle(options)
            answer_index = options.index(keyword)

            candidates.append(
                {
                    "question": question,
                    "options": options,
                    "answer": keyword,
                    "answer_letter": "ABCD"[answer_index],
                }
            )

    random.shuffle(candidates)

    fresh_candidates = [
        mcq
        for mcq in candidates
        if mcq["question"] not in excluded_questions
    ]
    previous_candidates = [
        mcq
        for mcq in candidates
        if mcq["question"] in excluded_questions
    ]

    return (fresh_candidates + previous_candidates)[: int(count)]
