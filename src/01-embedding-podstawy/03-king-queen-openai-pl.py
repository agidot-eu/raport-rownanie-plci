import os
from openai import OpenAI
import numpy as np

apikey_openai = ""
# Wczytanie klucza API z pliku
with open(r"C:\\ag\\licencje\\apikey-openai.txt", "r") as file:
    apikey_openai = file.read().strip()

client = OpenAI(api_key=apikey_openai)

# Funkcja generująca embeddingi słów
def get_embedding(text, model="text-embedding-ada-002"):
    response = client.embeddings.create(input=[text], model=model)
    return response.data[0].embedding

# Funkcja analogii słownej
def znajdz_analogie(slowo_a, slowo_b, slowo_c):
    wektor_a = np.array(get_embedding(slowo_a))
    wektor_b = np.array(get_embedding(slowo_b))
    wektor_c = np.array(get_embedding(slowo_c))

    # Operacja na wektorach: król - mężczyzna + kobieta
    wynikowy_wektor = wektor_a - wektor_b + wektor_c

    return wynikowy_wektor

# Przykładowe słowa
slowo_krol = "król"
slowo_mezczyzna = "mężczyzna"
slowo_kobieta = "kobieta"

wynikowy_wektor = znajdz_analogie(slowo_krol, slowo_mezczyzna, slowo_kobieta)

# Lista słów do porównania
slowa_kandydaci = ["królowa", "księżniczka", "księżna", "dama", "kobieta", "cesarzowa", "monarcha", "władca", "tron", "królewski", "król", "następca_tronu"]

# Pobierz embeddingi dla kandydatów
embeddingi_kandydatow = [np.array(get_embedding(slowo)) for slowo in slowa_kandydaci]

# Oblicz podobieństwo kosinusowe
podobienstwo_kosinusowe = lambda a, b: np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

podobienstwa = [(slowo, podobienstwo_kosinusowe(wynikowy_wektor, embedding)) for slowo, embedding in zip(slowa_kandydaci, embeddingi_kandydatow)]

# Sortowanie wyników
podobienstwa.sort(key=lambda x: x[1], reverse=True)

# Wyświetl 10 najbardziej podobnych słów
print("Top 10 podobnych słów:")
for slowo, podobienstwo in podobienstwa:
    print(f"{slowo}: {podobienstwo:.4f}")
