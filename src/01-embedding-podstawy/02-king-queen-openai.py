import os
from openai import OpenAI
import numpy as np


apikey_openai = "";
# Wczytanie klucza API z pliku
with open(r"C:\\ag\\licencje\\apikey-openai.txt", "r") as file:
    apikey_openai = file.read().strip()



client = OpenAI(api_key=apikey_openai)

# Funkcja generująca embeddingi słów
def get_embedding(text, model="text-embedding-ada-002"):
    response = client.embeddings.create(input=[text], model=model)
    return response.data[0].embedding

# Funkcja analogii słownej
def find_analogy(word_a, word_b, word_c):
    vector_a = np.array(get_embedding(word_a))
    vector_b = np.array(get_embedding(word_b))
    vector_c = np.array(get_embedding(word_c))

    # Operacja na wektorach: king - man + woman
    result_vector = vector_a - vector_b + vector_c

    return result_vector

# Przykładowe słowa
word_king = "king"
word_man = "man"
word_woman = "woman"

result_vector = find_analogy(word_king, word_man, word_woman)

# Lista słów do porównania - tu nie możemy przeszukać wszystkich słów- więc dajemy nasz zbiór
candidate_words = ["queen", "princess", "duchess", "lady", "female", "empress", "monarch", "ruler", "throne", "royal", "king", "crown_prince"]

# Pobierz embeddingi dla kandydatów
candidate_embeddings = [np.array(get_embedding(word)) for word in candidate_words]

# Oblicz podobieństwo kosinusowe
cosine_similarity = lambda a, b: np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

similarities = [(word, cosine_similarity(result_vector, embedding)) for word, embedding in zip(candidate_words, candidate_embeddings)]

# Sortowanie wyników
similarities.sort(key=lambda x: x[1], reverse=True)

# Wyświetl 10 najbardziej podobnych słów
print("Top 10 similar words:")
for word, similarity in similarities:
    print(f"{word}: {similarity:.4f}")