from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def text_similarity(text1: str, text2: str) -> float:
    vectorizer = CountVectorizer()

    vectors = vectorizer.fit_transform([text1, text2])
    cosine_sim = cosine_similarity(vectors[0], vectors[1])

    return cosine_sim[0][0]


def find_closest_match(word: str, words: list) -> str:
    closest = float("-inf")
    closest_word = ""

    for w in words:
        score = text_similarity(w, word)

        if score > closest:
            closest = score
            closest_word = w

    return closest_word
