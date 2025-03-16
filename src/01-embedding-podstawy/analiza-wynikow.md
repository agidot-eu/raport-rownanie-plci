# Analiza wyników

## Wynik programu 01

model[word_king] - model[word_man] + model[word_woman]
Top 8 similar words:
king: 0.8449
queen: 0.7301
monarch: 0.6455
princess: 0.6156
crown_prince: 0.5819
prince: 0.5777
kings: 0.5614
sultan: 0.5377

model[word_queen] - model[word_woman] + model[word_man] 
Top 8 similar words:
queen: 0.8393
king: 0.7046
queens: 0.6253
kings: 0.5997
monarch: 0.5615
princess: 0.5421
prince: 0.5246
royal: 0.5168


1. Dlaczego „king” jest na pierwszym miejscu? 👑
king: 0.8449
Model nadal widzi king jako najbardziej podobne słowo, ponieważ operacje na wektorach nie zawsze prowadzą do idealnie nowego wektora – czasem wynik jest wciąż bardzo bliski pierwotnemu punktowi (king).
Może to oznaczać, że różnica między „king” a „man” w modelu nie jest wystarczająco duża, by stworzyć wyraźnie nowy wektor.
2. „queen” jako drugi wynik – sukces! 👸
queen: 0.7301
To wskazuje, że model rzeczywiście wychwycił relację płciową – queen (królowa) to najlepszy kobiecy odpowiednik king.
Jest to potwierdzenie, że Word2Vec rozpoznaje różnice między płciami w języku i ich zastosowanie w tytułach.


## wynik programu 02
Top 10 similar words:
king: 0.9152
queen: 0.8844
female: 0.8156
monarch: 0.8124
empress: 0.8097
princess: 0.8090
royal: 0.7962
throne: 0.7933
duchess: 0.7889
lady: 0.7796
ruler: 0.7698
crown_prince: 0.7688

## wynik programu 03

Top 10 podobnych słów:
król: 0.8782
kobieta: 0.8678
królowa: 0.8402
królewski: 0.8011
księżna: 0.7908
księżniczka: 0.7830
monarcha: 0.7522
cesarzowa: 0.7512
dama: 0.7375
następca_tronu: 0.7281
władca: 0.7249
tron: 0.6908


## wynik programu 04
Top 8 similar words for 'work - man + woman':
work: 0.7426
she: 0.5016
working: 0.4849
works: 0.4611
Work: 0.4587
towork: 0.4365
blog_Nikanor_Inn: 0.4288
her: 0.4256

==================================================

Top 8 similar words for 'work - woman + man':
work: 0.7427
working: 0.5282
worked: 0.4296
job: 0.4204
works: 0.4046
Working: 0.3921
tinkering: 0.3785
toiling: 0.3739