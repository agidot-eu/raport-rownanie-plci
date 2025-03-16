import gensim.downloader as api

# Wczytaj wstępnie wytrenowany model Word2Vec
model = api.load("word2vec-google-news-300")
print("wczytany")

def calculate_analogy(base_word, remove_word, add_word):
    """
    Oblicza równanie wektorowe: base_word - remove_word + add_word
    i zwraca 8 najbardziej podobnych słów.
    """
    result_vector = model[base_word] - model[remove_word] + model[add_word]
    similar_words = model.similar_by_vector(result_vector, topn=8)
    return similar_words

# Obliczenia dla work - man + woman
similar_work_woman = calculate_analogy("work", "man", "woman")
print("Top 8 similar words for 'work - man + woman':")
for word, similarity in similar_work_woman:
    print(f"{word}: {similarity:.4f}")

print("\n" + "="*50 + "\n")

# Obliczenia dla work - woman + man
similar_work_man = calculate_analogy("work", "woman", "man")
print("Top 8 similar words for 'work - woman + man':")
for word, similarity in similar_work_man:
    print(f"{word}: {similarity:.4f}")
