import random

def generate_mcqs(sentences, keywords, count, difficulty="Low"):

    mcqs = []

    sentences = [
        s for s in sentences
        if len(s.split()) > 6 and len(s.split()) < 40
        and "include" not in s.lower()
        and "printf" not in s.lower()
        and "void" not in s.lower()
        and "main" not in s.lower()
    ]

    for sentence in sentences:

        for keyword in keywords:

            if keyword.lower() in sentence.lower():

                question = sentence.replace(keyword, "_____")

                options = [keyword]

                distractors = [k for k in keywords if k != keyword]

                if difficulty == "Low":
                    options += random.sample(distractors, min(2, len(distractors)))

                elif difficulty == "Medium":
                    options += random.sample(distractors, min(3, len(distractors)))

                else:
                    options += random.sample(distractors, min(3, len(distractors)))
                    options.append("None of the above")

                random.shuffle(options)

                mcqs.append({
                    "question": question,
                    "options": options,
                    "answer": keyword
                })

                break

        if len(mcqs) >= int(count):
            break

    return mcqs
