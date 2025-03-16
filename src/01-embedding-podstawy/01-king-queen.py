import gensim.downloader as api

# Wczytaj wstępnie wytrenowany model Word2Vec
model = api.load("word2vec-google-news-300")

# Zdefiniuj słowa do równania
word_king = "king"
word_man = "man"
word_woman = "woman"

# Wykonaj operację na wektorach
# Odejmujemy "man" od "king" → To jak pytanie: Co sprawia, że "king" (król) jest mężczyzną? Odejmuje się więc cechy związane z męskością.
# Dodajemy "woman" → Teraz model zastępuje utraconą „męskość” cechami kobiecymi.
result_vector = model[word_king] - model[word_man] + model[word_woman]  

# Znajdź 8 najbardziej podobnych słów
similar_words = model.similar_by_vector(result_vector, topn=8)

# Wyświetl wyniki
print("Top 8 similar words:")
for word, similarity in similar_words:
    print(f"{word}: {similarity:.4f}")



####################

# Zdefiniuj słowa do równania
word_queen = "queen"
word_woman = "woman"
word_man = "man"

# Wykonaj operację na wektorach
# Odejmujemy "woman" od "queen" → To jak pytanie: Co sprawia, że "queen" (królowa) jest kobietą? Odejmuje się więc cechy związane z kobiecością.
# Dodajemy "man" → Teraz model zastępuje utraconą „kobiecość” cechami męskimi.
result_vector = model[word_queen] - model[word_woman] + model[word_man]  

# Znajdź 8 najbardziej podobnych słów
similar_words = model.similar_by_vector(result_vector, topn=8)

# Wyświetl wyniki
print("Top 8 similar words:")
for word, similarity in similar_words:
    print(f"{word}: {similarity:.4f}")