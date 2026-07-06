import random

def generate_mcqs(sentences, keywords, count=10):

    mcqs = []

    # Sirf achhe sentences lo
    valid_sentences = []

    for s in sentences:
        s = s.strip()

        if (
            len(s.split()) >= 8
            and len(s.split()) <= 35
            and "include" not in s.lower()
            and "printf" not in s.lower()
            and "void" not in s.lower()
            and "main" not in s.lower()
            and "{" not in s
            and "}" not in s
        ):
            valid_sentences.append(s)

    for sentence in valid_sentences:

        for keyword in keywords:

            if keyword.lower() in sentence.lower():

                question = sentence.replace(keyword, "_____")

                options = [keyword]

                distractors = [k for k in keywords if k != keyword]

                if len(distractors) >= 3:
                    options.extend(random.sample(distractors, 3))

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
