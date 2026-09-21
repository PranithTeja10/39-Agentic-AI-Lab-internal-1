# ============================================================
# EXPERIMENT 2
# RAG-BASED QUESTION ANSWERING SYSTEM
# ============================================================

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


print("=" * 60)
print("        RAG-BASED QUESTION ANSWERING SYSTEM")
print("=" * 60)


# ============================================================
# 1. KNOWLEDGE BASE
# ============================================================

documents = [

    """
    Artificial Intelligence (AI) is a branch of computer science
    that develops systems capable of performing tasks that normally
    require human intelligence. AI applications include healthcare,
    finance, education, robotics, natural language processing and
    computer vision.
    """,

    """
    Internet of Things (IoT) is a technology in which physical
    devices are connected to the internet and communicate with
    each other. IoT devices use sensors to collect data and can
    be monitored or controlled remotely. IoT is used in smart homes,
    smart cities, healthcare, agriculture and industrial automation.
    """,

    """
    Machine Learning (ML) is a subset of Artificial Intelligence
    that enables computers to learn patterns from data and make
    predictions or decisions without being explicitly programmed.
    Machine Learning is used in recommendation systems, fraud
    detection, image recognition and prediction.
    """,

    """
    Data Science is an interdisciplinary field that uses statistics,
    mathematics, programming and machine learning to analyze data
    and extract useful insights. Data Science is used in healthcare,
    finance, business analytics, marketing and scientific research.
    """,

    """
    Cloud Computing provides computing resources such as servers,
    storage, databases and software over the internet. Cloud
    computing allows organizations to access resources on demand
    without maintaining all physical infrastructure locally.
    """
]


print("\nKnowledge base loaded:", len(documents), "documents")


# ============================================================
# 2. INDEXING
# ============================================================

print("\n===== 1. INDEXING =====")

vectorizer = TfidfVectorizer(
    stop_words="english"
)

document_vectors = vectorizer.fit_transform(documents)

print("Documents converted into TF-IDF vectors.")
print("Index created successfully.")


# ============================================================
# 3. USER QUESTION
# ============================================================

question = input("\nEnter your question: ").strip()


# ============================================================
# 4. RETRIEVAL
# ============================================================

print("\n===== 2. RETRIEVAL =====")

question_vector = vectorizer.transform([question])

similarity_scores = cosine_similarity(
    question_vector,
    document_vectors
)[0]

ranked_documents = similarity_scores.argsort()[::-1]

best_index = ranked_documents[0]
best_score = similarity_scores[best_index]


# Threshold prevents unrelated answers
if best_score < 0.10:

    print("No sufficiently relevant document was found.")
    print("Similarity score:", round(best_score, 3))

    answer = """
Sorry, the knowledge base does not contain enough
information to answer this question.
"""

else:

    print("Most relevant document:")
    print(documents[best_index])

    print("Similarity score:", round(best_score, 3))


    # ========================================================
    # 5. RESPONSE GENERATION
    # ========================================================

    print("\n===== 3. RESPONSE GENERATION =====")

    retrieved_text = documents[best_index].strip()

    answer = (
        "Based on the retrieved information:\n\n"
        + retrieved_text
    )


print(answer)


# ============================================================
# 6. FINAL RESULT
# ============================================================

print("\n===== RAG COMPLETED =====")

print("""
The system successfully performed:

1. Document indexing using TF-IDF
2. Query processing
3. Similarity-based retrieval
4. Relevant document selection
5. Response generation
""")