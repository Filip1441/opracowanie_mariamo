import marimo

__generated_with = "0.17.6"
app = marimo.App()

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `import marimo as mo`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`marimo`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`as`**: Słowo kluczowe języka Python: 'as'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`mo`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
""")
    return
@app.cell
def _():
    import marimo as mo
    return mo,

@app.cell
def _(mo):
    mo.md(r"""# Wykład 7: Systemy Współbieżne i CV""")
    return

@app.cell
def _():
    pass
    return

@app.cell
def _(mo):
    mo.md(r"""## Tworzenie Wątków""")
    return

@app.cell
def _(mo):
    mo.md(r"""Definicja wątku:


Wątek (ang. thread) – część programu wykonywana współbieżnie w obrębie jednego procesu.

Różnica między zwykłym procesem a wątkiem polega na współdzieleniu przez wszystkie wątki działające w danym procesie przestrzeni adresowej oraz wszystkich innych struktur systemowych (np. listy otwartych plików, gniazd itp.) – z kolei procesy posiadają niezależne zasoby.

Ta cecha ma dwie ważne konsekwencje:


Dzięki współdzieleniu przestrzeni adresowej (pamięci) wątki jednego zadania mogą się między sobą komunikować w bardzo łatwy sposób. Przekazanie dowolnie dużej ilości danych wymaga przesłania jedynie wskaźnika, zaś odczyt (a niekiedy zapis) danych o rozmiarze nie większym od słowa maszynowego nie wymaga synchronizacji (procesor gwarantuje atomowość takiej operacji).""")
    return

@app.cell
def _(mo):
    mo.md(r"""W Pythonie mamy następujące metody tworzenia wątków:

* użycie klasy Thread
* dziedziczenie po Thread
""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `import time`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`time`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 2**: `from threading import Thread`
- Słowo kluczowe **`from`**: Słowo kluczowe 'from' (z). Używane przy importowaniu, oznacza 'Z tej konkretnej, dużej biblioteki załaduj tylko ten jeden określony fragment'.
- Nazwa **`threading`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`Thread`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 4**: `def druk():`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`druk`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 5**: `for i in range (0,5):`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`i`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`range`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`5`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 6**: `print(i)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`i`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 7**: `t1=Thread(target=druk)`
- Nazwa **`t1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`Thread`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`target`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`druk`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 8**: `t2=Thread(target=druk)`
- Nazwa **`t2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`Thread`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`target`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`druk`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 9**: `t1.start()`
- Nazwa **`t1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`start`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 10**: `t2.start()`
- Nazwa **`t2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`start`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    import time
    from threading import Thread
    
    def druk():
      for i in range (0,5):
        print(i)
    t1=Thread(target=druk)
    t2=Thread(target=druk)
    t1.start()
    t2.start()
    
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `import time`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`time`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 2**: `from threading import Thread`
- Słowo kluczowe **`from`**: Słowo kluczowe 'from' (z). Używane przy importowaniu, oznacza 'Z tej konkretnej, dużej biblioteki załaduj tylko ten jeden określony fragment'.
- Nazwa **`threading`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`Thread`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 4**: `def druk():`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`druk`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 5**: `for i in range (0,5):`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`i`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`range`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`5`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 6**: `print(i)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`i`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 7**: `time.sleep(1)`
- Nazwa **`time`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`sleep`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 8**: `t1=Thread(target=druk)`
- Nazwa **`t1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`Thread`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`target`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`druk`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 9**: `t2=Thread(target=druk)`
- Nazwa **`t2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`Thread`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`target`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`druk`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 10**: `t1.start()`
- Nazwa **`t1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`start`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 11**: `t2.start()`
- Nazwa **`t2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`start`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 12**: `t1.join()`
- Nazwa **`t1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`join`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 13**: `t2.join()`
- Nazwa **`t2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`join`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    import time
    from threading import Thread
    
    def druk():
      for i in range (0,5):
        print(i)
        time.sleep(1)
    t1=Thread(target=druk)
    t2=Thread(target=druk)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    return

@app.cell
def _(mo):
    mo.md(r"""Wątek nadrzędny czeka na zakończenie działania wątków""")
    return

@app.cell
def _():
    pass
    return

@app.cell
def _(mo):
    mo.md(r"""Dodanie argumentów""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `from threading import Thread`
- Słowo kluczowe **`from`**: Słowo kluczowe 'from' (z). Używane przy importowaniu, oznacza 'Z tej konkretnej, dużej biblioteki załaduj tylko ten jeden określony fragment'.
- Nazwa **`threading`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`Thread`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 3**: `def druk(n):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`druk`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`n`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 4**: `for i in range(n):`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`i`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`range`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`n`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 5**: `print(i)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`i`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 7**: `t1 = Thread(target=druk, args=(3,))`
- Nazwa **`t1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`Thread`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`target`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`druk`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`args`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 8**: `t2 = Thread(target=druk, args=(5,))`
- Nazwa **`t2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`Thread`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`target`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`druk`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`args`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`5`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 10**: `t1.start()`
- Nazwa **`t1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`start`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 11**: `t2.start()`
- Nazwa **`t2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`start`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 13**: `t1.join()`
- Nazwa **`t1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`join`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 14**: `t2.join()`
- Nazwa **`t2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`join`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    from threading import Thread
    
    def druk(n):
        for i in range(n):
            print(i)
    
    t1 = Thread(target=druk, args=(3,))
    t2 = Thread(target=druk, args=(5,))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `import threading`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`threading`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 3**: `saldo = 100`
- Nazwa **`saldo`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`100`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 5**: `def wyplata(name):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`wyplata`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 6**: `global saldo`
- Słowo kluczowe **`global`**: Słowo kluczowe języka Python: 'global'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`saldo`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 7**: `for _ in range(5):`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`_`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`range`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`5`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 8**: `if saldo > 0:`
- Słowo kluczowe **`if`**: Słowo kluczowe 'if' (jeśli). Rozpoczyna instrukcję warunkową. Komputer sprawdzi postawiony warunek - jeśli jest on prawdziwy, wykona kod pod spodem.
- Nazwa **`saldo`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`>`**: Znak większości. Pyta: 'czy to po lewej jest większe?'.
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 9**: `saldo1 = saldo-1`
- Nazwa **`saldo1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`saldo`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`-`**: Operator odejmowania.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 10**: `time.sleep(1)`
- Nazwa **`time`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`sleep`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 11**: `saldo = saldo1`
- Nazwa **`saldo`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`saldo1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 12**: `print(name, saldo)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`saldo`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 13**: `t1 = threading.Thread(target=wyplata, args=("w1",))`
- Nazwa **`t1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`threading`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`Thread`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`target`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`wyplata`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`args`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"w1"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 14**: `t2 = threading.Thread(target=wyplata, args=("w2",))`
- Nazwa **`t2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`threading`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`Thread`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`target`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`wyplata`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`args`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"w2"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 16**: `t1.start()`
- Nazwa **`t1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`start`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 17**: `t2.start()`
- Nazwa **`t2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`start`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 19**: `t1.join()`
- Nazwa **`t1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`join`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 20**: `t2.join()`
- Nazwa **`t2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`join`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 22**: `print("Saldo końcowe:", saldo)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Saldo końcowe:"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`saldo`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    import threading
    
    saldo = 100
    
    def wyplata(name):
        global saldo
        for _ in range(5):
           if saldo > 0:
            saldo1 = saldo-1
           time.sleep(1)
           saldo = saldo1
           print(name, saldo)
    t1 = threading.Thread(target=wyplata, args=("w1",))
    t2 = threading.Thread(target=wyplata, args=("w2",))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print("Saldo końcowe:", saldo)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `import threading`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`threading`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 3**: `saldo = 100`
- Nazwa **`saldo`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`100`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 4**: `lock = threading.Lock()`
- Nazwa **`lock`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`threading`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`Lock`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 5**: `def wyplata(name):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`wyplata`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 6**: `global saldo`
- Słowo kluczowe **`global`**: Słowo kluczowe języka Python: 'global'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`saldo`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 7**: `for _ in range(10):`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`_`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`range`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`10`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 8**: `with lock:`
- Słowo kluczowe **`with`**: Słowo kluczowe języka Python: 'with'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`lock`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 9**: `if saldo > 0:`
- Słowo kluczowe **`if`**: Słowo kluczowe 'if' (jeśli). Rozpoczyna instrukcję warunkową. Komputer sprawdzi postawiony warunek - jeśli jest on prawdziwy, wykona kod pod spodem.
- Nazwa **`saldo`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`>`**: Znak większości. Pyta: 'czy to po lewej jest większe?'.
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 10**: `saldo1 = saldo-1`
- Nazwa **`saldo1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`saldo`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`-`**: Operator odejmowania.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 11**: `time.sleep(1)`
- Nazwa **`time`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`sleep`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 12**: `saldo = saldo1`
- Nazwa **`saldo`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`saldo1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 13**: `print(name, saldo)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`saldo`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 14**: `t1 = threading.Thread(target=wyplata, args=("w1",))`
- Nazwa **`t1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`threading`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`Thread`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`target`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`wyplata`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`args`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"w1"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 15**: `t2 = threading.Thread(target=wyplata, args=("w2",))`
- Nazwa **`t2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`threading`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`Thread`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`target`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`wyplata`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`args`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"w2"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 17**: `t1.start()`
- Nazwa **`t1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`start`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 18**: `t2.start()`
- Nazwa **`t2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`start`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 20**: `t1.join()`
- Nazwa **`t1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`join`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 21**: `t2.join()`
- Nazwa **`t2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`join`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 23**: `print("Saldo końcowe:", saldo)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Saldo końcowe:"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`saldo`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    import threading
    
    saldo = 100
    lock = threading.Lock()
    def wyplata(name):
        global saldo
        for _ in range(10):
           with lock:
            if saldo > 0:
             saldo1 = saldo-1
            time.sleep(1)
            saldo = saldo1
            print(name, saldo)
    t1 = threading.Thread(target=wyplata, args=("w1",))
    t2 = threading.Thread(target=wyplata, args=("w2",))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print("Saldo końcowe:", saldo)
    return

@app.cell
def _(mo):
    mo.md(r"""## Dziedziczenie po klasie Thread""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `class MyThread(Thread):`
- Słowo kluczowe **`class`**: Słowo kluczowe 'class' (klasa). Oznacza tworzenie nowego, złożonego typu danych (obiektu). To tak, jakbyś tworzył własną foremkę, z której potem będziesz 'wypiekać' konkretne obiekty (ciastka) o określonych cechach.
- Nazwa **`MyThread`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`Thread`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 2**: `def __init__(self, num,name):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`num`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 3**: `super().__init__()`
- Nazwa **`super`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 4**: `self._num = num`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`_num`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`num`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 5**: `self._name = name`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`_name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 7**: `def run(self):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`run`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 8**: `for i in range(0,self._num):`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`i`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`range`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`_num`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 9**: `print(self._name," ",i)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`_name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`" "`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`i`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 10**: `time.sleep(1)`
- Nazwa **`time`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`sleep`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 12**: `t1=MyThread(2,"w1")`
- Nazwa **`t1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`MyThread`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`"w1"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 13**: `t2=MyThread(3,"w2")`
- Nazwa **`t2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`MyThread`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`"w2"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 14**: `t1.start()`
- Nazwa **`t1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`start`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 15**: `t2.start()`
- Nazwa **`t2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`start`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 16**: `t1.join()`
- Nazwa **`t1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`join`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 17**: `t2.join()`
- Nazwa **`t2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`join`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    class MyThread(Thread):
        def __init__(self, num,name):
            super().__init__()
            self._num = num
            self._name = name
    
        def run(self):
          for i in range(0,self._num):
            print(self._name," ",i)
            time.sleep(1)
    
    t1=MyThread(2,"w1")
    t2=MyThread(3,"w2")
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    return

@app.cell
def _(mo):
    mo.md(r"""Synchronizacja wątków,  zwiększamy wartość wspólnej zmiennej o 1, wynik jest niedeterministyczny""")
    return

@app.cell
def _(mo):
    mo.md(r"""## Nowe zalecenia - określenie typów,  niestety nie mamy kontroli edydtora""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `def func(x: int) -> int:`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`func`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Nazwa **`int`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`->`**: Znak interpunkcyjny lub operator: '->'. Służy do organizacji struktury kodu.
- Nazwa **`int`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 2**: `return x + 1`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 3**: `print(func(2.0))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`func`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`2.0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    def func(x: int) -> int:
        return x + 1
    print(func(2.0))
    return

@app.cell
def _(mo):
    mo.md(r"""## Oczekiwania od aplikacji przetwarzania obrazów



1.  Wczytywanie obrazów i filmów
2.  Pobieranie obrazów z kamery
3. Zapisywanie obrazów i tworzenie filmów
4. Poprawa jakości obrazu ´
5. Wykrywanie cech obrazu
6. Operacje geometryczne - obrót, przesunięcie
7. Zmiana przestrzenie barw
8. Klasyfikacja obiektów widocznych na obrazie
9. Wykrywanie cech""")
    return

@app.cell
def _(mo):
    mo.md(r"""## Pakiety umożliwiające analizę obrazów



1. OpenCV
2. NumPy
3. SciPy
4. Pillow
5. SimplyCV
6. SimpleITK
7. pgmagick
8. scikit-image
9. ImageAI
10. Mahotas
11. OpenAI

""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `#import cv2`
- **Komentarz `[ #import cv2 ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `from google.colab import drive`
- Słowo kluczowe **`from`**: Słowo kluczowe 'from' (z). Używane przy importowaniu, oznacza 'Z tej konkretnej, dużej biblioteki załaduj tylko ten jeden określony fragment'.
- Nazwa **`google`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`colab`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`drive`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 3**: `from google.colab.patches import cv2_imshow`
- Słowo kluczowe **`from`**: Słowo kluczowe 'from' (z). Używane przy importowaniu, oznacza 'Z tej konkretnej, dużej biblioteki załaduj tylko ten jeden określony fragment'.
- Nazwa **`google`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`colab`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`patches`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`cv2_imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 4**: `import os`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`os`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 5**: `# Zamontuj dysk Google Drive`
- **Komentarz `[ # Zamontuj dysk Google Drive ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 6**: `drive.mount('/content/drive')`
- Nazwa **`drive`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`mount`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'/content/drive'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 9**: `# Ścieżka do pliku na dysku Google Drive`
- **Komentarz `[ # Ścieżka do pliku na dysku Google Drive ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 10**: `katalog = '/content/drive/MyDrive/pliki'`
- Nazwa **`katalog`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'/content/drive/MyDrive/pliki'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 14**: `# Wypisanie zawartości katalogu`
- **Komentarz `[ # Wypisanie zawartości katalogu ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 15**: `for folder, podfoldery, pliki in os.walk(katalog):`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`folder`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`podfoldery`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`pliki`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`os`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`walk`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`katalog`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 16**: `for plik in pliki:`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`plik`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`pliki`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 17**: `pelna_sciezka = os.path.join(folder, plik)`
- Nazwa **`pelna_sciezka`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`os`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`path`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`join`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`folder`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`plik`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 18**: `print(pelna_sciezka)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`pelna_sciezka`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 19**: `#path2 = '/content/drive/MyDrive/l2.png'`
- **Komentarz `[ #path2 = '/content/drive/MyDrive/l2.png' ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.
""")
    return
@app.cell
def _():
    #import cv2
    from google.colab import drive
    from google.colab.patches import cv2_imshow
    import os
    # Zamontuj dysk Google Drive
    drive.mount('/content/drive')
    
    
    # Ścieżka do pliku na dysku Google Drive
    katalog = '/content/drive/MyDrive/pliki'
    
    
    
    # Wypisanie zawartości katalogu
    for folder, podfoldery, pliki in os.walk(katalog):
        for plik in pliki:
            pelna_sciezka = os.path.join(folder, plik)
            print(pelna_sciezka)
    #path2 = '/content/drive/MyDrive/l2.png'
    return

@app.cell
def _(mo):
    mo.md(r"""## Jeśli korzystamy z google collab to musimy zamontować dysk googla, aby mieć dostęp do plików i dodatkowo zaimportować odpowiednie pakiety""")
    return

@app.cell
def _(mo):
    mo.md(r"""## Obraz jako tablica liczb""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `import cv2`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 2**: `import numpy as np`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`numpy`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`as`**: Słowo kluczowe języka Python: 'as'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`np`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 3**: `from google.colab.patches import cv2_imshow  #potrzebne w google colab`
- Słowo kluczowe **`from`**: Słowo kluczowe 'from' (z). Używane przy importowaniu, oznacza 'Z tej konkretnej, dużej biblioteki załaduj tylko ten jeden określony fragment'.
- Nazwa **`google`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`colab`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`patches`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`cv2_imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- **Komentarz `[ #potrzebne w google colab ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 4**: `# Ścieżka do pliku na dysku Google Drive`
- **Komentarz `[ # Ścieżka do pliku na dysku Google Drive ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 5**: `path = '/content/drive/MyDrive/pliki/l1.png'`
- Nazwa **`path`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'/content/drive/MyDrive/pliki/l1.png'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 6**: `img=cv2.imread(filename=path)`
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`imread`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`filename`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`path`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 7**: `#cv2_imshow(img)`
- **Komentarz `[ #cv2_imshow(img) ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 8**: `print(img)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    import cv2
    import numpy as np
    from google.colab.patches import cv2_imshow  #potrzebne w google colab
    # Ścieżka do pliku na dysku Google Drive
    path = '/content/drive/MyDrive/pliki/l1.png'
    img=cv2.imread(filename=path)
    #cv2_imshow(img)
    print(img)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `cv2_imshow(img)`
- Nazwa **`cv2_imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    cv2_imshow(img)
    return

@app.cell
def _(mo):
    mo.md(r"""
## Pakiet numpy

biblioteka obliczeń numerycznych, ale ponieważ obraz jest tablicą więc w wielu przypadkach może być przydatna""")
    return

@app.cell
def _(mo):
    mo.md(r"""## Przykładowe operacje""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `import numpy as np`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`numpy`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`as`**: Słowo kluczowe języka Python: 'as'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`np`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 2**: `a=np.array([1,2,3])`
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`np`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`array`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 3**: `print(a.min(),a.max())`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`min`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`max`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 4**: `print(any(a==1))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`any`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`==`**: Podwójny znak równości to 'operator porównania'. Komputer sprawdza, czy to co po lewej jest DOKŁADNIE TAKIE SAMO jak to po prawej. Zwraca odpowiedź Prawda (True) lub Fałsz (False).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 5**: `print(all(a==1))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`all`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`==`**: Podwójny znak równości to 'operator porównania'. Komputer sprawdza, czy to co po lewej jest DOKŁADNIE TAKIE SAMO jak to po prawej. Zwraca odpowiedź Prawda (True) lub Fałsz (False).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    import numpy as np
    a=np.array([1,2,3])
    print(a.min(),a.max())
    print(any(a==1))
    print(all(a==1))
    return

@app.cell
def _(mo):
    mo.md(r"""## OpenCV

biblioteka funkcji wykorzystywanych podczas obróbki obrazu, oparta
na otwartym kodzie. Zaletą jest to ze została zoptymalizowana, tak aby ˙
obraz przetwarzac w czasie rzeczywistym, jest możliwość
wykorzystania karty graficznej w procesie przetwarzania.
Niektóre moduły openCV wymagają dodatkowo instalacji
opencv-contrib-python

pip install opencv-contrib-python
""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `# import bibliotek`
- **Komentarz `[ # import bibliotek ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 3**: `import cv2`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 4**: `import numpy as np`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`numpy`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`as`**: Słowo kluczowe języka Python: 'as'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`np`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 5**: `from google.colab.patches import cv2_imshow  #potrzebne w google colab`
- Słowo kluczowe **`from`**: Słowo kluczowe 'from' (z). Używane przy importowaniu, oznacza 'Z tej konkretnej, dużej biblioteki załaduj tylko ten jeden określony fragment'.
- Nazwa **`google`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`colab`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`patches`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`cv2_imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- **Komentarz `[ #potrzebne w google colab ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.
""")
    return
@app.cell
def _():
    # import bibliotek
    
    import cv2
    import numpy as np
    from google.colab.patches import cv2_imshow  #potrzebne w google colab
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `# Ścieżka do pliku na dysku Google Drive`
- **Komentarz `[ # Ścieżka do pliku na dysku Google Drive ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `path = '/content/drive/MyDrive/pliki/irys.jpg'`
- Nazwa **`path`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'/content/drive/MyDrive/pliki/irys.jpg'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 3**: `img=cv2.imread(filename=path)`
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`imread`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`filename`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`path`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 4**: `cv2_imshow(img)`
- Nazwa **`cv2_imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    # Ścieżka do pliku na dysku Google Drive
    path = '/content/drive/MyDrive/pliki/irys.jpg'
    img=cv2.imread(filename=path)
    cv2_imshow(img)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 2**: `# imread nie sygnalizuje braku pliku`
- **Komentarz `[ # imread nie sygnalizuje braku pliku ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 3**: `path = '/content/drive/MyDrive/l3.png'`
- Nazwa **`path`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'/content/drive/MyDrive/l3.png'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 4**: `img=cv2.imread(filename=path)`
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`imread`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`filename`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`path`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 5**: `cv2_imshow(img)`
- Nazwa **`cv2_imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    
    # imread nie sygnalizuje braku pliku
    path = '/content/drive/MyDrive/l3.png'
    img=cv2.imread(filename=path)
    cv2_imshow(img)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `# brak pliku musimy sprawdzić sami`
- **Komentarz `[ # brak pliku musimy sprawdzić sami ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `import os`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`os`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 4**: `path = '/content/drive/MyDrive/l3.png'`
- Nazwa **`path`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'/content/drive/MyDrive/l3.png'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 5**: `if os.path.isfile(path):`
- Słowo kluczowe **`if`**: Słowo kluczowe 'if' (jeśli). Rozpoczyna instrukcję warunkową. Komputer sprawdzi postawiony warunek - jeśli jest on prawdziwy, wykona kod pod spodem.
- Nazwa **`os`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`path`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`isfile`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`path`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 6**: `img=cv2.imread(filename=path)`
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`imread`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`filename`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`path`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 7**: `cv2_imshow(img)`
- Nazwa **`cv2_imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 8**: `else:`
- Słowo kluczowe **`else`**: Słowo kluczowe 'else' (w przeciwnym razie). Używane na samym końcu. Oznacza: 'Jeśli ŻADEN z wcześniejszych warunków nie był prawdziwy, wykonaj ostatecznie ten kod'.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 9**: `print("blad")`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"blad"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    # brak pliku musimy sprawdzić sami
    import os
    
    path = '/content/drive/MyDrive/l3.png'
    if os.path.isfile(path):
     img=cv2.imread(filename=path)
     cv2_imshow(img)
    else:
      print("blad")
    return

@app.cell
def _(mo):
    mo.md(r"""Korzystając z OpenCV możemy umieszczać rysunki w nazwanych oknach i przesuwać te okna, ale jest to trudne w środowisku google collab, zostanie pokazane później""")
    return

@app.cell
def _(mo):
    mo.md(r"""# Parametry dodatkowe imread

* cv2.IMREAD_COLOR = 1
* cv2.IMREAD_GRAYSCALE =0
* cv2.IMREAD_UNCHANGED = -1""")
    return

@app.cell
def _(mo):
    mo.md(r"""## Formaty które możemy czytać:

* Portable Network Graphics – *.png
* Portable image format – *.pbm, *.pgm, *.ppm *.pxm, *.pnm
* Windows bitmaps – *.bmp
* JPEG files – *.jpeg, *.jpg, *.jpe
* JPEG 2000 files – *.jp2
* WebP – *.webp
* PFM files – *.pfm
* Sun rasters – *.sr, *.ras
* Image files – *.exr
* Radiance HDR – *.hdr, *.pic
* TIFF files – *.tiff, *.tif
""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `# pliku video`
- **Komentarz `[ # pliku video ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `import time`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`time`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 3**: `path2 = '/content/drive/MyDrive/pliki/Shrimp.avi'`
- Nazwa **`path2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'/content/drive/MyDrive/pliki/Shrimp.avi'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 4**: `cap = cv2.VideoCapture(path2)`
- Nazwa **`cap`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`VideoCapture`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`path2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 5**: `frame_width = int(cap.get(3))`
- Nazwa **`frame_width`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`int`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`cap`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`get`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 6**: `frame_height = int(cap.get(4))`
- Nazwa **`frame_height`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`int`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`cap`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`get`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`4`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 7**: `for _ in range(3):`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`_`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`range`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 8**: `# Capture frame−by−frame`
- **Komentarz `[ # Capture frame−by−frame ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 9**: `ret , frame = cap.read( )`
- Nazwa **`ret`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`frame`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cap`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`read`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 10**: `print(ret)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`ret`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 11**: `img = cv2.cvtColor(frame, 1)`
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`cvtColor`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`frame`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 12**: `cv2_imshow(img)`
- Nazwa **`cv2_imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 13**: `time.sleep(5)`
- Nazwa **`time`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`sleep`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`5`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    # pliku video
    import time
    path2 = '/content/drive/MyDrive/pliki/Shrimp.avi'
    cap = cv2.VideoCapture(path2)
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    for _ in range(3):
       # Capture frame−by−frame
     ret , frame = cap.read( )
     print(ret)
     img = cv2.cvtColor(frame, 1)
     cv2_imshow(img)
     time.sleep(5)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `#Odczytywanie dodatkowych parametrów`
- **Komentarz `[ #Odczytywanie dodatkowych parametrów ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `path2 = '/content/drive/MyDrive/pliki/Shrimp.avi'`
- Nazwa **`path2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'/content/drive/MyDrive/pliki/Shrimp.avi'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 3**: `cap = cv2.VideoCapture(path2)`
- Nazwa **`cap`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`VideoCapture`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`path2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 4**: `w=cap.get(cv2.CAP_PROP_FRAME_WIDTH)`
- Nazwa **`w`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cap`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`get`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`CAP_PROP_FRAME_WIDTH`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 5**: `h=cap.get (cv2.CAP_PROP_FRAME_HEIGHT)`
- Nazwa **`h`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cap`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`get`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`CAP_PROP_FRAME_HEIGHT`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 6**: `fps=cap.get (cv2.CAP_PROP_FPS)`
- Nazwa **`fps`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cap`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`get`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`CAP_PROP_FPS`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 7**: `fc=cap.get (cv2.CAP_PROP_FRAME_COUNT)`
- Nazwa **`fc`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cap`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`get`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`CAP_PROP_FRAME_COUNT`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 8**: `print('w=',w,' h=',h, ' fps=',int(fps),' fc=',int(fc))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'w='`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`w`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`' h='`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`h`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`' fps='`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`int`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`fps`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`' fc='`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`int`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`fc`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    #Odczytywanie dodatkowych parametrów
    path2 = '/content/drive/MyDrive/pliki/Shrimp.avi'
    cap = cv2.VideoCapture(path2)
    w=cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    h=cap.get (cv2.CAP_PROP_FRAME_HEIGHT)
    fps=cap.get (cv2.CAP_PROP_FPS)
    fc=cap.get (cv2.CAP_PROP_FRAME_COUNT)
    print('w=',w,' h=',h, ' fps=',int(fps),' fc=',int(fc))
    return

@app.cell
def _(mo):
    mo.md(r"""## Operacje na obrazach""")
    return

@app.cell
def _(mo):
    mo.md(r"""## zmiana wymiarów""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `import cv2`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 2**: `import numpy as np`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`numpy`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`as`**: Słowo kluczowe języka Python: 'as'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`np`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 3**: `import matplotlib.pyplot as plt`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`matplotlib`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`pyplot`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`as`**: Słowo kluczowe języka Python: 'as'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`plt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 4**: `#p1 = '/content/drive/MyDrive/pliki/rys.png'`
- **Komentarz `[ #p1 = '/content/drive/MyDrive/pliki/rys.png' ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 5**: `p2 = '/content/drive/MyDrive/pliki/irys.jpg'`
- Nazwa **`p2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'/content/drive/MyDrive/pliki/irys.jpg'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 6**: `image = cv2.imread(p2)`
- Nazwa **`image`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`imread`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`p2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 7**: `# Loading the image`
- **Komentarz `[ # Loading the image ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 8**: `half = cv2.resize(image, (0, 0), fx = 0.5, fy = 0.5)`
- Nazwa **`half`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`resize`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`image`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`fx`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`0.5`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`fy`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`0.5`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 9**: `cv2_imshow(image)`
- Nazwa **`cv2_imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`image`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 10**: `cv2_imshow(half)`
- Nazwa **`cv2_imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`half`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    import cv2
    import numpy as np
    import matplotlib.pyplot as plt
    #p1 = '/content/drive/MyDrive/pliki/rys.png'
    p2 = '/content/drive/MyDrive/pliki/irys.jpg'
    image = cv2.imread(p2)
    # Loading the image
    half = cv2.resize(image, (0, 0), fx = 0.5, fy = 0.5)
    cv2_imshow(image)
    cv2_imshow(half)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `img200 = cv2.resize(image, (200, 200))`
- Nazwa **`img200`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`resize`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`image`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`200`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`200`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 2**: `cv2_imshow(img200)`
- Nazwa **`cv2_imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`img200`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 3**: `img500 = cv2.resize(image, (500, 500),`
- Nazwa **`img500`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`resize`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`image`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`500`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`500`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).

#### 👉 **Linia 4**: `interpolation = cv2.INTER_NEAREST)`
- Nazwa **`interpolation`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`INTER_NEAREST`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 5**: `cv2_imshow(img500)`
- Nazwa **`cv2_imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`img500`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    img200 = cv2.resize(image, (200, 200))
    cv2_imshow(img200)
    img500 = cv2.resize(image, (500, 500),
                  interpolation = cv2.INTER_NEAREST)
    cv2_imshow(img500)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `# zmiana wymiarów bardziej inteligentna, konieczny import imutils`
- **Komentarz `[ # zmiana wymiarów bardziej inteligentna, konieczny import imutils ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 3**: `import imutils`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`imutils`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 4**: `p1 = '/content/drive/MyDrive/pliki/irys.jpg'`
- Nazwa **`p1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'/content/drive/MyDrive/pliki/irys.jpg'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 6**: `#chcemy zmienić jeden wymiar, a pozostałe powinny się dostosować`
- **Komentarz `[ #chcemy zmienić jeden wymiar, a pozostałe powinny się dostosować ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 7**: `img = cv2.imread(p1, 1)`
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`imread`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`p1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 8**: `res=imutils.resize(image=img, width=100)`
- Nazwa **`res`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`imutils`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`resize`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`image`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`width`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`100`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 9**: `cv2_imshow(img)`
- Nazwa **`cv2_imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 10**: `cv2_imshow(res)`
- Nazwa **`cv2_imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`res`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    # zmiana wymiarów bardziej inteligentna, konieczny import imutils
    
    import imutils
    p1 = '/content/drive/MyDrive/pliki/irys.jpg'
    
    #chcemy zmienić jeden wymiar, a pozostałe powinny się dostosować
    img = cv2.imread(p1, 1)
    res=imutils.resize(image=img, width=100)
    cv2_imshow(img)
    cv2_imshow(res)
    
    
    return

@app.cell
def _(mo):
    mo.md(r"""## Generowanie losowych obrazów""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `array=np.random.randint(low=0,high=256,size=(300,300,3))`
- Nazwa **`array`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`np`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`random`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`randint`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`low`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`high`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`256`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`size`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`300`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`300`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 2**: `cv2_imshow(array)`
- Nazwa **`cv2_imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`array`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    array=np.random.randint(low=0,high=256,size=(300,300,3))
    cv2_imshow(array)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `array=np.full((300,300,3),fill_value=200)`
- Nazwa **`array`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`np`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`full`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`300`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`300`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`fill_value`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`200`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 2**: `cv2_imshow(array)`
- Nazwa **`cv2_imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`array`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 3**: `p1 = '/content/drive/MyDrive/pliki/test.jpg'`
- Nazwa **`p1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'/content/drive/MyDrive/pliki/test.jpg'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 4**: `cv2.imwrite(p1, array)`
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`imwrite`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`p1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`array`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    array=np.full((300,300,3),fill_value=200)
    cv2_imshow(array)
    p1 = '/content/drive/MyDrive/pliki/test.jpg'
    cv2.imwrite(p1, array)
    
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `p2='/content/drive/MyDrive/pliki/test.jpg'`
- Nazwa **`p2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'/content/drive/MyDrive/pliki/test.jpg'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 2**: `cv2.imread(p2,-1)`
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`imread`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`p2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Znak **`-`**: Operator odejmowania.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    p2='/content/drive/MyDrive/pliki/test.jpg'
    cv2.imread(p2,-1)
    return

@app.cell
def _(mo):
    mo.md(r"""## Proste operacje rysowania""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `p1 = '/content/drive/MyDrive/pliki/rys2.png'`
- Nazwa **`p1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'/content/drive/MyDrive/pliki/rys2.png'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 3**: `img = cv2.imread(p1, 1)`
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`imread`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`p1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 4**: `cv2_imshow(img)`
- Nazwa **`cv2_imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 5**: `cv2.line(img, pt1=(0,0),pt2=(100,100), color=(0,0,255),thickness=3)`
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`line`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`pt1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`pt2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`100`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`100`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`color`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`255`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`thickness`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 6**: `cv2.rectangle(img, pt1=(100,100),pt2=(200,200), color=(255,0,0),thickness=2)`
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`rectangle`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`pt1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`100`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`100`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`pt2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`200`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`200`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`color`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`255`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`thickness`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 7**: `cv2_imshow(img)`
- Nazwa **`cv2_imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    p1 = '/content/drive/MyDrive/pliki/rys2.png'
    
    img = cv2.imread(p1, 1)
    cv2_imshow(img)
    cv2.line(img, pt1=(0,0),pt2=(100,100), color=(0,0,255),thickness=3)
    cv2.rectangle(img, pt1=(100,100),pt2=(200,200), color=(255,0,0),thickness=2)
    cv2_imshow(img)
    return

@app.cell
def _(mo):
    mo.md(r"""## Dodawanie i odejmowanie obrazów

Aby dodać lub odjąć obrazy muszą mieć takie same wymiary""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `import cv2`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 2**: `import numpy as np`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`numpy`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`as`**: Słowo kluczowe języka Python: 'as'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`np`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 3**: `img=cv2.imread(p1,1)`
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`imread`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`p1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 4**: `p2 = '/content/drive/MyDrive/pliki/irys.jpg'`
- Nazwa **`p2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'/content/drive/MyDrive/pliki/irys.jpg'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 5**: `img1=cv2.imread(p2,1)`
- Nazwa **`img1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`imread`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`p2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 6**: `img = cv2.resize(img, (200, 200))    # zmiana rozmiaru`
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`resize`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`200`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`200`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- **Komentarz `[ # zmiana rozmiaru ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 7**: `img1 = cv2.resize(img1, (200, 200))`
- Nazwa **`img1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`resize`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`img1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`200`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`200`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 8**: `img3 = cv2.addWeighted(img, 1.0, img1, 1.0, 0)  #dodawanie obrazów`
- Nazwa **`img3`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`addWeighted`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`1.0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`img1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`1.0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- **Komentarz `[ #dodawanie obrazów ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 9**: `#img3=cv2.subtract(img,img1)`
- **Komentarz `[ #img3=cv2.subtract(img,img1) ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 10**: `combined = cv2.hconcat([img,img1,img3])    #łączenie obrazów`
- Nazwa **`combined`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`hconcat`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`img1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`img3`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- **Komentarz `[ #łączenie obrazów ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 11**: `cv2_imshow(combined)`
- Nazwa **`cv2_imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`combined`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    import cv2
    import numpy as np
    img=cv2.imread(p1,1)
    p2 = '/content/drive/MyDrive/pliki/irys.jpg'
    img1=cv2.imread(p2,1)
    img = cv2.resize(img, (200, 200))    # zmiana rozmiaru
    img1 = cv2.resize(img1, (200, 200))
    img3 = cv2.addWeighted(img, 1.0, img1, 1.0, 0)  #dodawanie obrazów
    #img3=cv2.subtract(img,img1)
    combined = cv2.hconcat([img,img1,img3])    #łączenie obrazów
    cv2_imshow(combined)
    return

@app.cell
def _(mo):
    mo.md(r"""## Przekształcenia geometryczne""")
    return

@app.cell
def _(mo):
    mo.md(r"""## Obrót""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `img=cv2.imread(p2,1)`
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`imread`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`p2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 2**: `(rows, cols) = img.shape[:2]  #pobieramy wymiary obrazu`
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`rows`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`cols`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`shape`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- **Komentarz `[ #pobieramy wymiary obrazu ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 3**: `print(rows,cols)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`rows`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`cols`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 4**: `#help(cv2.getRotationMatrix2D)`
- **Komentarz `[ #help(cv2.getRotationMatrix2D) ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 5**: `# tworzymy macierz rotacji, środek obrotu, kąt obrotu, skalowanie`
- **Komentarz `[ # tworzymy macierz rotacji, środek obrotu, kąt obrotu, skalowanie ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 6**: `M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)`
- Nazwa **`M`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`getRotationMatrix2D`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`cols`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`/`**: Operator dzielenia.
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`rows`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`/`**: Operator dzielenia.
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`45`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 7**: `#dokonujemy przekształcenia`
- **Komentarz `[ #dokonujemy przekształcenia ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 8**: `res = cv2.warpAffine(img, M, (cols, rows))`
- Nazwa **`res`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`warpAffine`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`M`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`cols`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`rows`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 9**: `combined = cv2.hconcat([img,res])`
- Nazwa **`combined`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`hconcat`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`res`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 10**: `cv2_imshow(combined)`
- Nazwa **`cv2_imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`combined`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    img=cv2.imread(p2,1)
    (rows, cols) = img.shape[:2]  #pobieramy wymiary obrazu
    print(rows,cols)
    #help(cv2.getRotationMatrix2D)
    # tworzymy macierz rotacji, środek obrotu, kąt obrotu, skalowanie
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
    #dokonujemy przekształcenia
    res = cv2.warpAffine(img, M, (cols, rows))
    combined = cv2.hconcat([img,res])
    cv2_imshow(combined)
    return

@app.cell
def _(mo):
    mo.md(r"""## Przesunięcie""")
    return

@app.cell
def _(mo):
    mo.md(r"""""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `M = np.float32([ [ 0,1,50],[1,0,50]])`
- Nazwa **`M`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`np`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`float32`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`50`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`50`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 2**: `res = cv2.warpAffine(img, M, (cols, rows))`
- Nazwa **`res`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`warpAffine`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`M`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`cols`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`rows`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 3**: `combined = cv2.hconcat([img,res])`
- Nazwa **`combined`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`hconcat`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`res`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 4**: `cv2_imshow(combined)`
- Nazwa **`cv2_imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`combined`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    M = np.float32([ [ 0,1,50],[1,0,50]])
    res = cv2.warpAffine(img, M, (cols, rows))
    combined = cv2.hconcat([img,res])
    cv2_imshow(combined)
    return

@app.cell
def _(mo):
    mo.md(r"""## Wycinanie fragmentów obrazu""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `import cv2`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 2**: `import numpy as np`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`numpy`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`as`**: Słowo kluczowe języka Python: 'as'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`np`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 3**: `import matplotlib.pyplot as plt`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`matplotlib`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`pyplot`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`as`**: Słowo kluczowe języka Python: 'as'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`plt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 4**: `p1 = '/content/drive/MyDrive/pliki/irys.jpg'`
- Nazwa **`p1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'/content/drive/MyDrive/pliki/irys.jpg'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 5**: `p2 = '/content/drive/MyDrive/rys2.png'`
- Nazwa **`p2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'/content/drive/MyDrive/rys2.png'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 6**: `image = cv2.imread(p1, 1)`
- Nazwa **`image`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`imread`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`p1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 7**: `img=image[100:200,100:200]`
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`image`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Liczba **`100`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Liczba **`200`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`100`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Liczba **`200`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 8**: `#cv2_imshow(image)`
- **Komentarz `[ #cv2_imshow(image) ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 9**: `cv2_imshow(img)`
- Nazwa **`cv2_imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    import cv2
    import numpy as np
    import matplotlib.pyplot as plt
    p1 = '/content/drive/MyDrive/pliki/irys.jpg'
    p2 = '/content/drive/MyDrive/rys2.png'
    image = cv2.imread(p1, 1)
    img=image[100:200,100:200]
    #cv2_imshow(image)
    cv2_imshow(img)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `import cv2`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 2**: `import numpy as np`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`numpy`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`as`**: Słowo kluczowe języka Python: 'as'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`np`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 3**: `import matplotlib.pyplot as plt`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`matplotlib`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`pyplot`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`as`**: Słowo kluczowe języka Python: 'as'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`plt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 4**: `p1 = '/content/drive/MyDrive/pliki/irys.jpg'`
- Nazwa **`p1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'/content/drive/MyDrive/pliki/irys.jpg'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 5**: `p2 = '/content/drive/MyDrive/rys2.png'`
- Nazwa **`p2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'/content/drive/MyDrive/rys2.png'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 6**: `image = cv2.imread(p1, 1)`
- Nazwa **`image`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`imread`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`p1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 7**: `img=image[-250:,-250:]      #uwaga na położenie :`
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`image`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Znak **`-`**: Operator odejmowania.
- Liczba **`250`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Znak **`-`**: Operator odejmowania.
- Liczba **`250`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- **Komentarz `[ #uwaga na położenie : ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 8**: `#cv2_imshow(image)`
- **Komentarz `[ #cv2_imshow(image) ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 9**: `cv2_imshow(img)`
- Nazwa **`cv2_imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    import cv2
    import numpy as np
    import matplotlib.pyplot as plt
    p1 = '/content/drive/MyDrive/pliki/irys.jpg'
    p2 = '/content/drive/MyDrive/rys2.png'
    image = cv2.imread(p1, 1)
    img=image[-250:,-250:]      #uwaga na położenie :
    #cv2_imshow(image)
    cv2_imshow(img)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `import cv2`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 2**: `import numpy as np`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`numpy`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`as`**: Słowo kluczowe języka Python: 'as'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`np`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 3**: `import matplotlib.pyplot as plt`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`matplotlib`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`pyplot`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`as`**: Słowo kluczowe języka Python: 'as'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`plt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 4**: `p1 = '/content/drive/MyDrive/pliki/irys.jpg'`
- Nazwa **`p1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'/content/drive/MyDrive/pliki/irys.jpg'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 5**: `p2 = '/content/drive/MyDrive/rys2.png'`
- Nazwa **`p2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'/content/drive/MyDrive/rys2.png'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 6**: `image = cv2.imread(p1, 1)`
- Nazwa **`image`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`imread`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`p1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 7**: `img=image[100:200,100:200]`
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`image`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Liczba **`100`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Liczba **`200`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`100`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Liczba **`200`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 8**: `#cv2_imshow(image)`
- **Komentarz `[ #cv2_imshow(image) ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 9**: `cv2_imshow(img)`
- Nazwa **`cv2_imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    import cv2
    import numpy as np
    import matplotlib.pyplot as plt
    p1 = '/content/drive/MyDrive/pliki/irys.jpg'
    p2 = '/content/drive/MyDrive/rys2.png'
    image = cv2.imread(p1, 1)
    img=image[100:200,100:200]
    #cv2_imshow(image)
    cv2_imshow(img)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `import cv2`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 2**: `import numpy as np`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`numpy`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`as`**: Słowo kluczowe języka Python: 'as'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`np`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 3**: `import matplotlib.pyplot as plt`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`matplotlib`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`pyplot`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`as`**: Słowo kluczowe języka Python: 'as'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`plt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 4**: `p1 = '/content/drive/MyDrive/pliki/irys.jpg'`
- Nazwa **`p1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'/content/drive/MyDrive/pliki/irys.jpg'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 5**: `p2 = '/content/drive/MyDrive/rys2.png'`
- Nazwa **`p2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'/content/drive/MyDrive/rys2.png'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 6**: `image = cv2.imread(p1, 1)`
- Nazwa **`image`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`imread`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`p1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 7**: `img=image[100:200,100:200]`
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`image`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Liczba **`100`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Liczba **`200`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`100`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Liczba **`200`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 8**: `#cv2_imshow(image)`
- **Komentarz `[ #cv2_imshow(image) ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 9**: `cv2_imshow(img)`
- Nazwa **`cv2_imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    import cv2
    import numpy as np
    import matplotlib.pyplot as plt
    p1 = '/content/drive/MyDrive/pliki/irys.jpg'
    p2 = '/content/drive/MyDrive/rys2.png'
    image = cv2.imread(p1, 1)
    img=image[100:200,100:200]
    #cv2_imshow(image)
    cv2_imshow(img)
    return

@app.cell
def _(mo):
    mo.md(r"""## jak wyciąć środkowy fragment obrazka?""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `# musimy znać wymiary`
- **Komentarz `[ # musimy znać wymiary ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `x,y,_= image.shape`
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`_`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`image`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`shape`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 3**: `print(x,y)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    # musimy znać wymiary
    x,y,_= image.shape
    print(x,y)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `# określamy środek`
- **Komentarz `[ # określamy środek ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `xs=x//2   # dzielenie całkowite`
- Nazwa **`xs`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`//`**: Operator dzielenia całkowitego (dzieli i odrzuca resztę, zostawiając samą całość).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- **Komentarz `[ # dzielenie całkowite ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 3**: `ys=y//2`
- Nazwa **`ys`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`//`**: Operator dzielenia całkowitego (dzieli i odrzuca resztę, zostawiając samą całość).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 4**: `dl=50  #długość to 100`
- Nazwa **`dl`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`50`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- **Komentarz `[ #długość to 100 ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 5**: `# współrzędne prawego górnego i lewego dolengo rogu`
- **Komentarz `[ # współrzędne prawego górnego i lewego dolengo rogu ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 6**: `xp=xs-dl`
- Nazwa **`xp`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`xs`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`-`**: Operator odejmowania.
- Nazwa **`dl`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 7**: `yp=ys-dl`
- Nazwa **`yp`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`ys`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`-`**: Operator odejmowania.
- Nazwa **`dl`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 8**: `xl=xs+dl`
- Nazwa **`xl`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`xs`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Nazwa **`dl`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 9**: `yl=ys+dl`
- Nazwa **`yl`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`ys`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Nazwa **`dl`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 10**: `img=image[xp:xl,yp:yl]`
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`image`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Nazwa **`xp`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Nazwa **`xl`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`yp`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Nazwa **`yl`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 11**: `cv2_imshow(img)`
- Nazwa **`cv2_imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    # określamy środek
    xs=x//2   # dzielenie całkowite
    ys=y//2
    dl=50  #długość to 100
    # współrzędne prawego górnego i lewego dolengo rogu
    xp=xs-dl
    yp=ys-dl
    xl=xs+dl
    yl=ys+dl
    img=image[xp:xl,yp:yl]
    cv2_imshow(img)
    
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `## Zmiana barw wybranego fragmentu`
- **Komentarz `[ ## Zmiana barw wybranego fragmentu ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 3**: `image[xp:xl,yp:yl]=(0,100,0)`
- Nazwa **`image`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Nazwa **`xp`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Nazwa **`xl`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`yp`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Nazwa **`yl`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`100`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 4**: `cv2_imshow(image)`
- Nazwa **`cv2_imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`image`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    ## Zmiana barw wybranego fragmentu
    
    image[xp:xl,yp:yl]=(0,100,0)
    cv2_imshow(image)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `# określamy środek`
- **Komentarz `[ # określamy środek ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `image = cv2.imread(p1, 1)`
- Nazwa **`image`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`imread`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`p1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 3**: `xs=x//2   # dzielenie całkowite`
- Nazwa **`xs`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`//`**: Operator dzielenia całkowitego (dzieli i odrzuca resztę, zostawiając samą całość).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- **Komentarz `[ # dzielenie całkowite ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 4**: `ys=y//2`
- Nazwa **`ys`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`//`**: Operator dzielenia całkowitego (dzieli i odrzuca resztę, zostawiając samą całość).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 5**: `dl=50  #długość to 100`
- Nazwa **`dl`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`50`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- **Komentarz `[ #długość to 100 ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 6**: `# współrzędne prawego górnego i lewego dolengo rogu`
- **Komentarz `[ # współrzędne prawego górnego i lewego dolengo rogu ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 7**: `xp=xs-dl`
- Nazwa **`xp`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`xs`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`-`**: Operator odejmowania.
- Nazwa **`dl`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 8**: `yp=ys-dl`
- Nazwa **`yp`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`ys`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`-`**: Operator odejmowania.
- Nazwa **`dl`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 9**: `oko=image[xp:xs,yp:ys]`
- Nazwa **`oko`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`image`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Nazwa **`xp`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Nazwa **`xs`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`yp`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Nazwa **`ys`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 10**: `cv2_imshow(oko)`
- Nazwa **`cv2_imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`oko`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    # określamy środek
    image = cv2.imread(p1, 1)
    xs=x//2   # dzielenie całkowite
    ys=y//2
    dl=50  #długość to 100
    # współrzędne prawego górnego i lewego dolengo rogu
    xp=xs-dl
    yp=ys-dl
    oko=image[xp:xs,yp:ys]
    cv2_imshow(oko)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `#A teraz możemy powielić fragment w kilku miejscach`
- **Komentarz `[ #A teraz możemy powielić fragment w kilku miejscach ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `image[xp-40:xs-40,yp-40:ys-40]=oko`
- Nazwa **`image`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Nazwa **`xp`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`-`**: Operator odejmowania.
- Liczba **`40`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Nazwa **`xs`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`-`**: Operator odejmowania.
- Liczba **`40`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`yp`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`-`**: Operator odejmowania.
- Liczba **`40`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Nazwa **`ys`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`-`**: Operator odejmowania.
- Liczba **`40`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`oko`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 3**: `image[xp+40:xs+40,yp+40:ys+40]=oko`
- Nazwa **`image`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Nazwa **`xp`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Liczba **`40`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Nazwa **`xs`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Liczba **`40`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`yp`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Liczba **`40`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Nazwa **`ys`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Liczba **`40`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`oko`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 4**: `p=60`
- Nazwa **`p`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`60`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 5**: `image[xp+40+p:xs+40+p,yp+40+p:ys+40+p]=oko`
- Nazwa **`image`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Nazwa **`xp`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Liczba **`40`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Nazwa **`p`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Nazwa **`xs`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Liczba **`40`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Nazwa **`p`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`yp`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Liczba **`40`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Nazwa **`p`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Nazwa **`ys`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Liczba **`40`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Nazwa **`p`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`oko`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 6**: `p=-160`
- Nazwa **`p`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`-`**: Operator odejmowania.
- Liczba **`160`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 7**: `image[xp+40+p:xs+40+p,yp+40+p:ys+40+p]=oko`
- Nazwa **`image`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Nazwa **`xp`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Liczba **`40`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Nazwa **`p`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Nazwa **`xs`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Liczba **`40`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Nazwa **`p`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`yp`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Liczba **`40`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Nazwa **`p`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Nazwa **`ys`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Liczba **`40`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Nazwa **`p`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`oko`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 8**: `cv2_imshow(image)`
- Nazwa **`cv2_imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`image`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    #A teraz możemy powielić fragment w kilku miejscach
    image[xp-40:xs-40,yp-40:ys-40]=oko
    image[xp+40:xs+40,yp+40:ys+40]=oko
    p=60
    image[xp+40+p:xs+40+p,yp+40+p:ys+40+p]=oko
    p=-160
    image[xp+40+p:xs+40+p,yp+40+p:ys+40+p]=oko
    cv2_imshow(image)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `## Tworzenie ramek na około obrazka`
- **Komentarz `[ ## Tworzenie ramek na około obrazka ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `p1 = '/content/drive/MyDrive/pliki/irys.jpg'`
- Nazwa **`p1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'/content/drive/MyDrive/pliki/irys.jpg'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 3**: `image=cv2.imread(p1,1)`
- Nazwa **`image`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`imread`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`p1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 4**: `ramka=cv2.copyMakeBorder(image,20,20,20,20,borderType=cv2.BORDER_REPLICATE)`
- Nazwa **`ramka`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`copyMakeBorder`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`image`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`20`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`20`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`20`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`20`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`borderType`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`BORDER_REPLICATE`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 5**: `cv2_imshow(image)`
- Nazwa **`cv2_imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`image`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 6**: `cv2_imshow(ramka)`
- Nazwa **`cv2_imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`ramka`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    ## Tworzenie ramek na około obrazka
    p1 = '/content/drive/MyDrive/pliki/irys.jpg'
    image=cv2.imread(p1,1)
    ramka=cv2.copyMakeBorder(image,20,20,20,20,borderType=cv2.BORDER_REPLICATE)
    cv2_imshow(image)
    cv2_imshow(ramka)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `## Tworzenie ramek na około obrazka`
- **Komentarz `[ ## Tworzenie ramek na około obrazka ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `p1 = '/content/drive/MyDrive/pliki/irys.jpg'`
- Nazwa **`p1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'/content/drive/MyDrive/pliki/irys.jpg'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 3**: `image=cv2.imread(p1,1)`
- Nazwa **`image`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`imread`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`p1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 4**: `ramka=cv2.copyMakeBorder(image,20,20,20,20,borderType=cv2.BORDER_WRAP)`
- Nazwa **`ramka`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`copyMakeBorder`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`image`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`20`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`20`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`20`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`20`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`borderType`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`BORDER_WRAP`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 5**: `cv2_imshow(ramka)`
- Nazwa **`cv2_imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`ramka`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    ## Tworzenie ramek na około obrazka
    p1 = '/content/drive/MyDrive/pliki/irys.jpg'
    image=cv2.imread(p1,1)
    ramka=cv2.copyMakeBorder(image,20,20,20,20,borderType=cv2.BORDER_WRAP)
    cv2_imshow(ramka)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `## Tworzenie ramek na około obrazka`
- **Komentarz `[ ## Tworzenie ramek na około obrazka ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `p1 = '/content/drive/MyDrive/pliki/irys.jpg'`
- Nazwa **`p1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'/content/drive/MyDrive/pliki/irys.jpg'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 3**: `image=cv2.imread(p1,1)`
- Nazwa **`image`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`imread`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`p1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 4**: `ramka=cv2.copyMakeBorder(image,20,20,20,20,borderType=cv2.BORDER_ISOLATED)`
- Nazwa **`ramka`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`copyMakeBorder`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`image`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`20`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`20`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`20`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`20`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`borderType`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`BORDER_ISOLATED`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 5**: `cv2_imshow(ramka)`
- Nazwa **`cv2_imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`ramka`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    ## Tworzenie ramek na około obrazka
    p1 = '/content/drive/MyDrive/pliki/irys.jpg'
    image=cv2.imread(p1,1)
    ramka=cv2.copyMakeBorder(image,20,20,20,20,borderType=cv2.BORDER_ISOLATED)
    cv2_imshow(ramka)
    return

@app.cell
def _(mo):
    mo.md(r"""## Poprawa jakości

* filtr mediamowy
* filtr uśredniający
* filtr Gaussa
* wyostrzanie obrazu""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `# filtr medianowy`
- **Komentarz `[ # filtr medianowy ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `img=cv2.imread(p1,1)`
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`imread`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`p1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 3**: `img1 = cv2.medianBlur(img,25)`
- Nazwa **`img1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`medianBlur`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`25`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 4**: `combined = cv2.hconcat([img,img1])`
- Nazwa **`combined`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`hconcat`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`img1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 5**: `cv2_imshow(combined)`
- Nazwa **`cv2_imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`combined`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    # filtr medianowy
    img=cv2.imread(p1,1)
    img1 = cv2.medianBlur(img,25)
    combined = cv2.hconcat([img,img1])
    cv2_imshow(combined)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `# filtr uredniający`
- **Komentarz `[ # filtr uredniający ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 3**: `kernel = np.array([[0.1, 0.1, 0.1],`
- Nazwa **`kernel`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`np`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`array`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Liczba **`0.1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`0.1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`0.1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).

#### 👉 **Linia 4**: `[0.1, 0.2, 0.1],`
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Liczba **`0.1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`0.2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`0.1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).

#### 👉 **Linia 5**: `[0.1, 0.1, 0.1]])`
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Liczba **`0.1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`0.1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`0.1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 7**: `#filter the source image`
- **Komentarz `[ #filter the source image ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 8**: `img1 = cv2.filter2D(img,-1,kernel)`
- Nazwa **`img1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`filter2D`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Znak **`-`**: Operator odejmowania.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`kernel`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 9**: `combined = cv2.hconcat([img,img1])`
- Nazwa **`combined`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`hconcat`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`img1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 10**: `cv2_imshow(combined)`
- Nazwa **`cv2_imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`combined`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    # filtr uredniający
    
    kernel = np.array([[0.1, 0.1, 0.1],
                       [0.1, 0.2, 0.1],
                       [0.1, 0.1, 0.1]])
    
    #filter the source image
    img1 = cv2.filter2D(img,-1,kernel)
    combined = cv2.hconcat([img,img1])
    cv2_imshow(combined)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `# filtr Gaussa`
- **Komentarz `[ # filtr Gaussa ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `import cv2`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 3**: `import numpy as np`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`numpy`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`as`**: Słowo kluczowe języka Python: 'as'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`np`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 4**: `path = '/content/drive/MyDrive/pliki/irys.jpg'`
- Nazwa **`path`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'/content/drive/MyDrive/pliki/irys.jpg'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 5**: `img=cv2.imread(filename=path)`
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`imread`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`filename`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`path`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 6**: `cv2_imshow(img)`
- Nazwa **`cv2_imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 7**: `img1=cv2.GaussianBlur(img,[7,7],0.7)`
- Nazwa **`img1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`GaussianBlur`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Liczba **`7`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`7`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`0.7`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 8**: `edge=cv2.Canny(img1,100,270)`
- Nazwa **`edge`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`Canny`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`img1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`100`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`270`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 9**: `cv2_imshow(edge)`
- Nazwa **`cv2_imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`edge`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    # filtr Gaussa
    import cv2
    import numpy as np
    path = '/content/drive/MyDrive/pliki/irys.jpg'
    img=cv2.imread(filename=path)
    cv2_imshow(img)
    img1=cv2.GaussianBlur(img,[7,7],0.7)
    edge=cv2.Canny(img1,100,270)
    cv2_imshow(edge)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `# wyostrzanie`
- **Komentarz `[ # wyostrzanie ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `kernel = np.array([[-1, -1, -1],`
- Nazwa **`kernel`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`np`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`array`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Znak **`-`**: Operator odejmowania.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Znak **`-`**: Operator odejmowania.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Znak **`-`**: Operator odejmowania.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).

#### 👉 **Linia 3**: `[-1, 9, -1],`
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Znak **`-`**: Operator odejmowania.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`9`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Znak **`-`**: Operator odejmowania.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).

#### 👉 **Linia 4**: `[-1, -1, -1]])`
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Znak **`-`**: Operator odejmowania.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Znak **`-`**: Operator odejmowania.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Znak **`-`**: Operator odejmowania.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 6**: `#filter the source image`
- **Komentarz `[ #filter the source image ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 7**: `img1 = cv2.filter2D(img,-1,kernel)`
- Nazwa **`img1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`filter2D`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Znak **`-`**: Operator odejmowania.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`kernel`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 8**: `combined = cv2.hconcat([img,img1])`
- Nazwa **`combined`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`hconcat`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`img1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 9**: `cv2_imshow(combined)`
- Nazwa **`cv2_imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`combined`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    # wyostrzanie
    kernel = np.array([[-1, -1, -1],
                       [-1, 9, -1],
                       [-1, -1, -1]])
    
    #filter the source image
    img1 = cv2.filter2D(img,-1,kernel)
    combined = cv2.hconcat([img,img1])
    cv2_imshow(combined)
    return

@app.cell
def _(mo):
    mo.md(r"""# Operacje progowania

Progowanie to proces podziału obrazu na obszary o różnych poziomach jasności. Progowanie często jest stosowane w celu poprawy kontrastu obrazu i wyróżnienia cech, takich jak krawędzie.
W bibliotece OpenCV, funkcja cv2.threshold() służy do progowania obrazu, opcje:

1. cv2.THRESH_BINARY
2. cv2.THRESH_BINARY_INV
3. cv2.THRESH_TRUNC
4. cv2.THRESH_TOZERO
5. cv2.THRESH_TOZERO_INV""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `_, th0 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)`
- Nazwa **`_`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`th0`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`threshold`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`127`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`255`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`THRESH_BINARY`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 2**: `#img=cv2.imread(path,0)`
- **Komentarz `[ #img=cv2.imread(path,0) ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 3**: `#_, th0 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)  działa tylko dla obrazów w stpniach szarości`
- **Komentarz `[ #_, th0 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)  działa tylko dla obrazów w stpniach szarości ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 4**: `combined = cv2.hconcat([img,th0])`
- Nazwa **`combined`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`hconcat`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`th0`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 5**: `cv2_imshow(combined)`
- Nazwa **`cv2_imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`combined`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _, th0 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    #img=cv2.imread(path,0)
    #_, th0 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)  działa tylko dla obrazów w stpniach szarości
    combined = cv2.hconcat([img,th0])
    cv2_imshow(combined)
    return

@app.cell
def _(mo):
    mo.md(r"""## Zmiana barw""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `import cv2`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 2**: `import numpy as np`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`numpy`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`as`**: Słowo kluczowe języka Python: 'as'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`np`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 3**: `path2 = '/content/drive/MyDrive/pliki/blb.png'`
- Nazwa **`path2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'/content/drive/MyDrive/pliki/blb.png'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 4**: `img = cv2.imread(path2, 1)`
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`imread`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`path2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 5**: `cv2_imshow(img)`
- Nazwa **`cv2_imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 6**: `# axis=2 - sprawdzane są wszystkie kanały`
- **Komentarz `[ # axis=2 - sprawdzane są wszystkie kanały ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 7**: `img[np.where((img == [0,0,0]).all(axis = 2))] = [0,255,0]    #zmieniamy czarny na zielony`
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Nazwa **`np`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`where`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`==`**: Podwójny znak równości to 'operator porównania'. Komputer sprawdza, czy to co po lewej jest DOKŁADNIE TAKIE SAMO jak to po prawej. Zwraca odpowiedź Prawda (True) lub Fałsz (False).
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`all`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`axis`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`255`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- **Komentarz `[ #zmieniamy czarny na zielony ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 8**: `cv2_imshow(img)`
- Nazwa **`cv2_imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    import cv2
    import numpy as np
    path2 = '/content/drive/MyDrive/pliki/blb.png'
    img = cv2.imread(path2, 1)
    cv2_imshow(img)
    # axis=2 - sprawdzane są wszystkie kanały
    img[np.where((img == [0,0,0]).all(axis = 2))] = [0,255,0]    #zmieniamy czarny na zielony
    cv2_imshow(img)
    return

@app.cell
def _(mo):
    mo.md(r"""## Zmiana przestrzeni barw""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `import cv2`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 2**: `import numpy as np`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`numpy`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`as`**: Słowo kluczowe języka Python: 'as'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`np`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 3**: `import matplotlib.pyplot as plt`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`matplotlib`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`pyplot`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`as`**: Słowo kluczowe języka Python: 'as'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`plt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 4**: `path2 = '/content/drive/MyDrive/pliki/blb.png'`
- Nazwa **`path2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'/content/drive/MyDrive/pliki/blb.png'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 5**: `img = cv2.imread(path2, 1)`
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`imread`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`path2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 6**: `cv2_imshow(img)`
- Nazwa **`cv2_imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 7**: `hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)`
- Nazwa **`hsv`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`cvtColor`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`COLOR_BGR2HSV`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 8**: `h,s,v = cv2.split(hsv)`
- Nazwa **`h`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`s`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`v`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`split`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`hsv`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 9**: `combined = cv2.hconcat([h,s,v])`
- Nazwa **`combined`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`hconcat`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Nazwa **`h`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`s`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`v`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 10**: `cv2_imshow(combined)`
- Nazwa **`cv2_imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`combined`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 12**: `# odcień - h`
- **Komentarz `[ # odcień - h ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 13**: `# nasycenie - s`
- **Komentarz `[ # nasycenie - s ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 14**: `# jasność - v`
- **Komentarz `[ # jasność - v ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.
""")
    return
@app.cell
def _():
    import cv2
    import numpy as np
    import matplotlib.pyplot as plt
    path2 = '/content/drive/MyDrive/pliki/blb.png'
    img = cv2.imread(path2, 1)
    cv2_imshow(img)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h,s,v = cv2.split(hsv)
    combined = cv2.hconcat([h,s,v])
    cv2_imshow(combined)
    
    # odcień - h
    # nasycenie - s
    # jasność - v
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `path2 = '/content/drive/MyDrive/pliki/blb.png'`
- Nazwa **`path2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'/content/drive/MyDrive/pliki/blb.png'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 2**: `img = cv2.imread(path2, 1)`
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`imread`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`path2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 4**: `lower_black = np.array([0,0,0])`
- Nazwa **`lower_black`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`np`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`array`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 5**: `upper_black = np.array([10,10,10])`
- Nazwa **`upper_black`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`np`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`array`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Liczba **`10`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`10`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`10`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 6**: `mask0 = cv2.inRange(hsv, lower_black, upper_black)`
- Nazwa **`mask0`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`inRange`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`hsv`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`lower_black`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`upper_black`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 8**: `cv2_imshow(mask0)`
- Nazwa **`cv2_imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`mask0`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    path2 = '/content/drive/MyDrive/pliki/blb.png'
    img = cv2.imread(path2, 1)
    
    lower_black = np.array([0,0,0])
    upper_black = np.array([10,10,10])
    mask0 = cv2.inRange(hsv, lower_black, upper_black)
    
    cv2_imshow(mask0)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `import cv2`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 2**: `import numpy as np`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`numpy`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`as`**: Słowo kluczowe języka Python: 'as'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`np`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 3**: `path2 = '/content/drive/MyDrive/pliki/testl.png'`
- Nazwa **`path2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'/content/drive/MyDrive/pliki/testl.png'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 4**: `img = cv2.imread(path2)`
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`imread`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`path2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 5**: `gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   #zamiana na odcienie szarości`
- Nazwa **`gray`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`cvtColor`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`COLOR_BGR2GRAY`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- **Komentarz `[ #zamiana na odcienie szarości ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 6**: `#Create default Fast Line Detector (FSD)`
- **Komentarz `[ #Create default Fast Line Detector (FSD) ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 7**: `fld = cv2.ximgproc.createFastLineDetector()   #generowanie matody wykrywania linii`
- Nazwa **`fld`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`ximgproc`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`createFastLineDetector`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- **Komentarz `[ #generowanie matody wykrywania linii ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 9**: `#Detect lines in the image`
- **Komentarz `[ #Detect lines in the image ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 10**: `lines = fld.detect(gray)`
- Nazwa **`lines`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`fld`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`detect`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`gray`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 11**: `print(lines)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`lines`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 12**: `#Draw detected lines in the image`
- **Komentarz `[ #Draw detected lines in the image ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 13**: `dlimg = fld.drawSegments(gray,lines)`
- Nazwa **`dlimg`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`fld`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`drawSegments`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`gray`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`lines`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 15**: `combined = cv2.hconcat([img,dlimg])`
- Nazwa **`combined`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`hconcat`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`dlimg`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 16**: `cv2_imshow(combined)`
- Nazwa **`cv2_imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`combined`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    import cv2
    import numpy as np
    path2 = '/content/drive/MyDrive/pliki/testl.png'
    img = cv2.imread(path2)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   #zamiana na odcienie szarości
    #Create default Fast Line Detector (FSD)
    fld = cv2.ximgproc.createFastLineDetector()   #generowanie matody wykrywania linii
    
    #Detect lines in the image
    lines = fld.detect(gray)
    print(lines)
    #Draw detected lines in the image
    dlimg = fld.drawSegments(gray,lines)
    
    combined = cv2.hconcat([img,dlimg])
    cv2_imshow(combined)
    
    return

@app.cell
def _(mo):
    mo.md(r"""## Wykrywanie krawędzi""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `# Ścieżka do pliku na dysku Google Drive`
- **Komentarz `[ # Ścieżka do pliku na dysku Google Drive ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `import cv2`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 3**: `import numpy as np`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`numpy`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`as`**: Słowo kluczowe języka Python: 'as'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`np`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 4**: `path2 = '/content/drive/MyDrive/pliki/blb2.png'`
- Nazwa **`path2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'/content/drive/MyDrive/pliki/blb2.png'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 5**: `img = cv2.imread(path2, 0)`
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`imread`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`path2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 6**: `cv2_imshow(img)`
- Nazwa **`cv2_imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 7**: `edge=cv2.Canny(img,180,270)`
- Nazwa **`edge`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`Canny`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`180`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`270`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 8**: `cv2_imshow(edge)`
- Nazwa **`cv2_imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`edge`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    # Ścieżka do pliku na dysku Google Drive
    import cv2
    import numpy as np
    path2 = '/content/drive/MyDrive/pliki/blb2.png'
    img = cv2.imread(path2, 0)
    cv2_imshow(img)
    edge=cv2.Canny(img,180,270)
    cv2_imshow(edge)
    return

@app.cell
def _(mo):
    mo.md(r"""## Określanie krawędzi""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `import cv2`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 3**: `# Wczytanie obrazu z pliku`
- **Komentarz `[ # Wczytanie obrazu z pliku ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 4**: `#img = cv2.imread('nazwa_obrazu.jpg')`
- **Komentarz `[ #img = cv2.imread('nazwa_obrazu.jpg') ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 6**: `# Konwersja obrazu do odcieni szarości`
- **Komentarz `[ # Konwersja obrazu do odcieni szarości ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 7**: `gray = img.copy()`
- Nazwa **`gray`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`copy`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 10**: `# Znalezienie konturów na obrazie`
- **Komentarz `[ # Znalezienie konturów na obrazie ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 11**: `contours, hierarchy = cv2.findContours(edge, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)`
- Nazwa **`contours`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`hierarchy`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`findContours`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`edge`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`RETR_TREE`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`CHAIN_APPROX_SIMPLE`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 13**: `# Iteracja po wszystkich konturach`
- **Komentarz `[ # Iteracja po wszystkich konturach ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 14**: `for contour in contours:`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`contour`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`contours`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 15**: `# Obliczenie przybliżonego kształtu konturu`
- **Komentarz `[ # Obliczenie przybliżonego kształtu konturu ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 16**: `approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)`
- Nazwa **`approx`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`approxPolyDP`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`contour`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`0.01`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`*`**: Operator mnożenia (gwiazdka).
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`arcLength`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`contour`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Słowo kluczowe **`True`**: Wartość logiczna 'True' (Prawda). Oznacza stan włączenia, potwierdzenie, że coś jest zgodne z prawdą (w pamięci komputera to jedynka: 1).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Słowo kluczowe **`True`**: Wartość logiczna 'True' (Prawda). Oznacza stan włączenia, potwierdzenie, że coś jest zgodne z prawdą (w pamięci komputera to jedynka: 1).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 17**: `#   cv2.drawContours(img, [approx], 0, (0, 255, 0), 2)`
- **Komentarz `[ #   cv2.drawContours(img, [approx], 0, (0, 255, 0), 2) ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 18**: `# Sprawdzenie, czy kontur ma 4 boki (czyli czy jest kwadratem)`
- **Komentarz `[ # Sprawdzenie, czy kontur ma 4 boki (czyli czy jest kwadratem) ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 19**: `if len(approx) == 4:`
- Słowo kluczowe **`if`**: Słowo kluczowe 'if' (jeśli). Rozpoczyna instrukcję warunkową. Komputer sprawdzi postawiony warunek - jeśli jest on prawdziwy, wykona kod pod spodem.
- Nazwa **`len`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`approx`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`==`**: Podwójny znak równości to 'operator porównania'. Komputer sprawdza, czy to co po lewej jest DOKŁADNIE TAKIE SAMO jak to po prawej. Zwraca odpowiedź Prawda (True) lub Fałsz (False).
- Liczba **`4`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 20**: `# Narysowanie prostokąta wokół konturu`
- **Komentarz `[ # Narysowanie prostokąta wokół konturu ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 21**: `cv2.drawContours(img, [approx], 0, (0, 255, 0), 2)`
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`drawContours`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Nazwa **`approx`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`255`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 22**: `print("Na obrazie znaleziono prostokąt.")`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Na obrazie znaleziono prostokąt."`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 23**: `cv2_imshow(img)`
- Nazwa **`cv2_imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 24**: `break`
- Słowo kluczowe **`break`**: Słowo kluczowe języka Python: 'break'. Jest to wbudowane polecenie o specjalnym znaczeniu.

#### 👉 **Linia 25**: `else:`
- Słowo kluczowe **`else`**: Słowo kluczowe 'else' (w przeciwnym razie). Używane na samym końcu. Oznacza: 'Jeśli ŻADEN z wcześniejszych warunków nie był prawdziwy, wykonaj ostatecznie ten kod'.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 26**: `print("Na obrazie nie znaleziono kwadratu.")`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Na obrazie nie znaleziono kwadratu."`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    import cv2
    
    # Wczytanie obrazu z pliku
    #img = cv2.imread('nazwa_obrazu.jpg')
    
    # Konwersja obrazu do odcieni szarości
    gray = img.copy()
    
    
    # Znalezienie konturów na obrazie
    contours, hierarchy = cv2.findContours(edge, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Iteracja po wszystkich konturach
    for contour in contours:
        # Obliczenie przybliżonego kształtu konturu
        approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
     #   cv2.drawContours(img, [approx], 0, (0, 255, 0), 2)
        # Sprawdzenie, czy kontur ma 4 boki (czyli czy jest kwadratem)
        if len(approx) == 4:
            # Narysowanie prostokąta wokół konturu
            cv2.drawContours(img, [approx], 0, (0, 255, 0), 2)
            print("Na obrazie znaleziono prostokąt.")
            cv2_imshow(img)
            break
    else:
        print("Na obrazie nie znaleziono kwadratu.")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `# Wyznaczenie konturów`
- **Komentarz `[ # Wyznaczenie konturów ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `contours = cv2.findContours(image=edge.copy(),`
- Nazwa **`contours`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`findContours`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`image`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`edge`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`copy`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).

#### 👉 **Linia 3**: `mode=cv2.RETR_TREE,`
- Nazwa **`mode`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`RETR_TREE`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).

#### 👉 **Linia 4**: `method=cv2.CHAIN_APPROX_SIMPLE)`
- Nazwa **`method`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`CHAIN_APPROX_SIMPLE`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 5**: `contours = imutils.grab_contours(contours)`
- Nazwa **`contours`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`imutils`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`grab_contours`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`contours`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 7**: `contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]`
- Nazwa **`contours`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`sorted`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`contours`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`key`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`contourArea`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`reverse`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Słowo kluczowe **`True`**: Wartość logiczna 'True' (Prawda). Oznacza stan włączenia, potwierdzenie, że coś jest zgodne z prawdą (w pamięci komputera to jedynka: 1).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Liczba **`10`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 8**: `print(contours)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`contours`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    # Wyznaczenie konturów
    contours = cv2.findContours(image=edge.copy(),
                                mode=cv2.RETR_TREE,
                                method=cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
    print(contours)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `#rysujemy kontur`
- **Komentarz `[ #rysujemy kontur ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `cnt1 = cv2.drawContours(image=img.copy(), contours=[contours[0]], contourIdx=0,`
- Nazwa **`cnt1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`drawContours`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`image`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`copy`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`contours`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Nazwa **`contours`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`contourIdx`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).

#### 👉 **Linia 3**: `color=(0, 255, 0), thickness=3)`
- Nazwa **`color`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`255`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`thickness`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 4**: `cv2_imshow(cnt1)`
- Nazwa **`cv2_imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`cnt1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    #rysujemy kontur
    cnt1 = cv2.drawContours(image=img.copy(), contours=[contours[0]], contourIdx=0,
                            color=(0, 255, 0), thickness=3)
    cv2_imshow(cnt1)
    return

@app.cell
def _():
    pass
    return

@app.cell
def _(mo):
    mo.md(r"""## Przepływ optyczny""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `import cv2`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 2**: `import numpy as np`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`numpy`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`as`**: Słowo kluczowe języka Python: 'as'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`np`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 3**: `import cv2`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 4**: `from google.colab import drive`
- Słowo kluczowe **`from`**: Słowo kluczowe 'from' (z). Używane przy importowaniu, oznacza 'Z tej konkretnej, dużej biblioteki załaduj tylko ten jeden określony fragment'.
- Nazwa **`google`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`colab`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`drive`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 5**: `from google.colab.patches import cv2_imshow`
- Słowo kluczowe **`from`**: Słowo kluczowe 'from' (z). Używane przy importowaniu, oznacza 'Z tej konkretnej, dużej biblioteki załaduj tylko ten jeden określony fragment'.
- Nazwa **`google`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`colab`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`patches`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`cv2_imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 6**: `import os`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`os`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 7**: `import matplotlib.pyplot as plt`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`matplotlib`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`pyplot`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`as`**: Słowo kluczowe języka Python: 'as'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`plt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 8**: `# Zamontuj dysk Google Drive`
- **Komentarz `[ # Zamontuj dysk Google Drive ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 11**: `# rozpoznanie obiektu`
- **Komentarz `[ # rozpoznanie obiektu ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 12**: `def identify_shape(image_path):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`identify_shape`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`image_path`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 13**: `try:`
- Słowo kluczowe **`try`**: Słowo kluczowe 'try' (próbuj). Rozpoczyna niebezpieczny blok kodu, w którym komputer ma 'spróbować' wykonać operację, spodziewając się, że może pojawić się awaria/błąd.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 14**: `# ładujemy obraz`
- **Komentarz `[ # ładujemy obraz ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 15**: `img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)`
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`imread`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`image_path`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`IMREAD_GRAYSCALE`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 16**: `if img is None:`
- Słowo kluczowe **`if`**: Słowo kluczowe 'if' (jeśli). Rozpoczyna instrukcję warunkową. Komputer sprawdzi postawiony warunek - jeśli jest on prawdziwy, wykona kod pod spodem.
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`is`**: Słowo kluczowe języka Python: 'is'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Słowo kluczowe **`None`**: Słowo 'None' oznacza 'Nic'. Specjalna wartość mówiąca, że zmienna jest pusta, nie ma w niej zupełnie żadnej wartości, nawet zera.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 17**: `return "Error: Could not load image."`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Tekst (String) **`"Error: Could not load image."`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 19**: `# usuwamy szum`
- **Komentarz `[ # usuwamy szum ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 20**: `img = cv2.GaussianBlur(img, (5, 5), 0)`
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`GaussianBlur`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`5`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`5`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 21**: `_, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)`
- Nazwa **`_`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`thresh`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`threshold`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`img`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`127`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`255`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`THRESH_BINARY_INV`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 24**: `# Find contours`
- **Komentarz `[ # Find contours ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 25**: `contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)`
- Nazwa **`contours`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`_`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`findContours`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`thresh`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`RETR_EXTERNAL`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`CHAIN_APPROX_SIMPLE`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 27**: `if not contours:`
- Słowo kluczowe **`if`**: Słowo kluczowe 'if' (jeśli). Rozpoczyna instrukcję warunkową. Komputer sprawdzi postawiony warunek - jeśli jest on prawdziwy, wykona kod pod spodem.
- Słowo kluczowe **`not`**: Słowo 'not' (nie). Odwraca logiczną wartość na przeciwną. Z Prawdy robi Fałsz, a z Fałszu Prawdę.
- Nazwa **`contours`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 28**: `return "No shapes detected."`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Tekst (String) **`"No shapes detected."`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 31**: `for contour in contours:`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`contour`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`contours`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 32**: `# Approximate the contour to a polygon`
- **Komentarz `[ # Approximate the contour to a polygon ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 33**: `epsilon = 0.04 * cv2.arcLength(contour, True)`
- Nazwa **`epsilon`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`0.04`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`*`**: Operator mnożenia (gwiazdka).
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`arcLength`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`contour`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Słowo kluczowe **`True`**: Wartość logiczna 'True' (Prawda). Oznacza stan włączenia, potwierdzenie, że coś jest zgodne z prawdą (w pamięci komputera to jedynka: 1).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 34**: `approx = cv2.approxPolyDP(contour, epsilon, True)`
- Nazwa **`approx`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`approxPolyDP`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`contour`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`epsilon`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Słowo kluczowe **`True`**: Wartość logiczna 'True' (Prawda). Oznacza stan włączenia, potwierdzenie, że coś jest zgodne z prawdą (w pamięci komputera to jedynka: 1).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 36**: `# klasysfikacja na podstawie liczby wierzchołków`
- **Komentarz `[ # klasysfikacja na podstawie liczby wierzchołków ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 37**: `vertices = len(approx)`
- Nazwa **`vertices`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`len`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`approx`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 39**: `if vertices == 3:`
- Słowo kluczowe **`if`**: Słowo kluczowe 'if' (jeśli). Rozpoczyna instrukcję warunkową. Komputer sprawdzi postawiony warunek - jeśli jest on prawdziwy, wykona kod pod spodem.
- Nazwa **`vertices`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`==`**: Podwójny znak równości to 'operator porównania'. Komputer sprawdza, czy to co po lewej jest DOKŁADNIE TAKIE SAMO jak to po prawej. Zwraca odpowiedź Prawda (True) lub Fałsz (False).
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 40**: `return "Triangle"`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Tekst (String) **`"Triangle"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 41**: `elif vertices == 4:`
- Słowo kluczowe **`elif`**: Słowo kluczowe 'elif' (w przeciwnym razie jeśli). Używane po 'if'. Jeśli pierwszy warunek się nie spełnił, komputer sprawdza ten kolejny warunek zastępczy.
- Nazwa **`vertices`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`==`**: Podwójny znak równości to 'operator porównania'. Komputer sprawdza, czy to co po lewej jest DOKŁADNIE TAKIE SAMO jak to po prawej. Zwraca odpowiedź Prawda (True) lub Fałsz (False).
- Liczba **`4`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 42**: `# Further check for square/rectangle`
- **Komentarz `[ # Further check for square/rectangle ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 43**: `x, y, w, h = cv2.boundingRect(approx)`
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`w`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`h`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`boundingRect`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`approx`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 44**: `aspect_ratio = float(w) / h`
- Nazwa **`aspect_ratio`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`float`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`w`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`/`**: Operator dzielenia.
- Nazwa **`h`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 45**: `if 0.95 <= aspect_ratio <= 1.05:`
- Słowo kluczowe **`if`**: Słowo kluczowe 'if' (jeśli). Rozpoczyna instrukcję warunkową. Komputer sprawdzi postawiony warunek - jeśli jest on prawdziwy, wykona kod pod spodem.
- Liczba **`0.95`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`<=`**: Znak mniejszy lub równy.
- Nazwa **`aspect_ratio`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`<=`**: Znak mniejszy lub równy.
- Liczba **`1.05`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 46**: `return "Square"`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Tekst (String) **`"Square"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 47**: `else:`
- Słowo kluczowe **`else`**: Słowo kluczowe 'else' (w przeciwnym razie). Używane na samym końcu. Oznacza: 'Jeśli ŻADEN z wcześniejszych warunków nie był prawdziwy, wykonaj ostatecznie ten kod'.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 48**: `return "Rectangle"`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Tekst (String) **`"Rectangle"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 49**: `elif vertices == 5:`
- Słowo kluczowe **`elif`**: Słowo kluczowe 'elif' (w przeciwnym razie jeśli). Używane po 'if'. Jeśli pierwszy warunek się nie spełnił, komputer sprawdza ten kolejny warunek zastępczy.
- Nazwa **`vertices`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`==`**: Podwójny znak równości to 'operator porównania'. Komputer sprawdza, czy to co po lewej jest DOKŁADNIE TAKIE SAMO jak to po prawej. Zwraca odpowiedź Prawda (True) lub Fałsz (False).
- Liczba **`5`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 50**: `return "Pentagon"`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Tekst (String) **`"Pentagon"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 51**: `elif vertices == 6:`
- Słowo kluczowe **`elif`**: Słowo kluczowe 'elif' (w przeciwnym razie jeśli). Używane po 'if'. Jeśli pierwszy warunek się nie spełnił, komputer sprawdza ten kolejny warunek zastępczy.
- Nazwa **`vertices`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`==`**: Podwójny znak równości to 'operator porównania'. Komputer sprawdza, czy to co po lewej jest DOKŁADNIE TAKIE SAMO jak to po prawej. Zwraca odpowiedź Prawda (True) lub Fałsz (False).
- Liczba **`6`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 52**: `return "Hexagon"`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Tekst (String) **`"Hexagon"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 53**: `elif vertices == 8:  # Octagon`
- Słowo kluczowe **`elif`**: Słowo kluczowe 'elif' (w przeciwnym razie jeśli). Używane po 'if'. Jeśli pierwszy warunek się nie spełnił, komputer sprawdza ten kolejny warunek zastępczy.
- Nazwa **`vertices`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`==`**: Podwójny znak równości to 'operator porównania'. Komputer sprawdza, czy to co po lewej jest DOKŁADNIE TAKIE SAMO jak to po prawej. Zwraca odpowiedź Prawda (True) lub Fałsz (False).
- Liczba **`8`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- **Komentarz `[ # Octagon ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 54**: `return "Octagon"`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Tekst (String) **`"Octagon"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 55**: `elif vertices > 10 :`
- Słowo kluczowe **`elif`**: Słowo kluczowe 'elif' (w przeciwnym razie jeśli). Używane po 'if'. Jeśli pierwszy warunek się nie spełnił, komputer sprawdza ten kolejny warunek zastępczy.
- Nazwa **`vertices`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`>`**: Znak większości. Pyta: 'czy to po lewej jest większe?'.
- Liczba **`10`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 56**: `return "Circle"  # Approximate circle`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Tekst (String) **`"Circle"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- **Komentarz `[ # Approximate circle ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 57**: `else:`
- Słowo kluczowe **`else`**: Słowo kluczowe 'else' (w przeciwnym razie). Używane na samym końcu. Oznacza: 'Jeśli ŻADEN z wcześniejszych warunków nie był prawdziwy, wykonaj ostatecznie ten kod'.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 58**: `return "Unknown Polygon"`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Tekst (String) **`"Unknown Polygon"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 59**: `except Exception as e:`
- Słowo kluczowe **`except`**: Słowo kluczowe 'except' (za wyjątkiem / przechwyć). Określa ratunek: co komputer ma awaryjnie zrobić, jeśli w bloku 'try' faktycznie wystąpił błąd. Zapobiega to gwałtownemu wyłączeniu się programu.
- Nazwa **`Exception`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`as`**: Słowo kluczowe języka Python: 'as'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`e`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 60**: `return f"Error: {e}"`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Tekst (String) **`f"Error: {e}"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 63**: `drive.mount('/content/drive/')`
- Nazwa **`drive`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`mount`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'/content/drive/'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 65**: `# Ścieżka do pliku na dysku Google Drive`
- **Komentarz `[ # Ścieżka do pliku na dysku Google Drive ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 67**: `path2 = '/content/drive/MyDrive/sq.jpg'`
- Nazwa **`path2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'/content/drive/MyDrive/sq.jpg'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 68**: `image=cv2.imread(path2)`
- Nazwa **`image`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cv2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`imread`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`path2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 69**: `plt.imshow(image)`
- Nazwa **`plt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`image`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 70**: `shape = identify_shape(path2)`
- Nazwa **`shape`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`identify_shape`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`path2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 71**: `print(f"The identified shape is: {shape}")`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`f"The identified shape is: {shape}"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    import cv2
    import numpy as np
    import cv2
    from google.colab import drive
    from google.colab.patches import cv2_imshow
    import os
    import matplotlib.pyplot as plt
    # Zamontuj dysk Google Drive
    
    
    # rozpoznanie obiektu
    def identify_shape(image_path):
        try:
            # ładujemy obraz
            img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            if img is None:
                return "Error: Could not load image."
    
            # usuwamy szum
            img = cv2.GaussianBlur(img, (5, 5), 0)
            _, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
    
    
            # Find contours
            contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
            if not contours:
              return "No shapes detected."
    
    
            for contour in contours:
                # Approximate the contour to a polygon
                epsilon = 0.04 * cv2.arcLength(contour, True)
                approx = cv2.approxPolyDP(contour, epsilon, True)
    
                # klasysfikacja na podstawie liczby wierzchołków
                vertices = len(approx)
    
                if vertices == 3:
                    return "Triangle"
                elif vertices == 4:
                    # Further check for square/rectangle
                    x, y, w, h = cv2.boundingRect(approx)
                    aspect_ratio = float(w) / h
                    if 0.95 <= aspect_ratio <= 1.05:
                        return "Square"
                    else:
                        return "Rectangle"
                elif vertices == 5:
                    return "Pentagon"
                elif vertices == 6:
                    return "Hexagon"
                elif vertices == 8:  # Octagon
                  return "Octagon"
                elif vertices > 10 :
                    return "Circle"  # Approximate circle
                else:
                    return "Unknown Polygon"
        except Exception as e:
            return f"Error: {e}"
    
    
    drive.mount('/content/drive/')
    
    # Ścieżka do pliku na dysku Google Drive
    
    path2 = '/content/drive/MyDrive/sq.jpg'
    image=cv2.imread(path2)
    plt.imshow(image)
    shape = identify_shape(path2)
    print(f"The identified shape is: {shape}")
    return

@app.cell
def _(mo):
    mo.md(r"""Przykładowe cmap

viridis – Domyślna mapa kolorów w Matplotlib, dobrze nadaje się do wizualizacji.

plasma – Kolorowa skala o cieplejszych barwach, bardziej nasycona.

inferno – Ciemna skala kolorów z intensywnymi czerwonymi i żółtymi.

magma – Mapa cieplna o ciemniejszych barwach.

cividis – Kolorowa mapa dla osób z problemami z widzeniem kolorów.

Greys – Skala szarości.""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `import numpy as np`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`numpy`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`as`**: Słowo kluczowe języka Python: 'as'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`np`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 2**: `import matplotlib.pyplot as plt`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`matplotlib`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`pyplot`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`as`**: Słowo kluczowe języka Python: 'as'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`plt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 4**: `# Generowanie przykładowych danych`
- **Komentarz `[ # Generowanie przykładowych danych ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 5**: `x = np.linspace(0, 1, 300)`
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`np`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`linspace`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`300`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 6**: `y = np.linspace(0, 1, 300)`
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`np`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`linspace`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`300`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 7**: `X, Y = np.meshgrid(x, y)`
- Nazwa **`X`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`Y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`np`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`meshgrid`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 8**: `heatmap_data = np.sin(10*X) * np.cos(10*Y)  # Przykładowe dane sinusoidalne`
- Nazwa **`heatmap_data`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`np`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`sin`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`10`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`*`**: Operator mnożenia (gwiazdka).
- Nazwa **`X`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`*`**: Operator mnożenia (gwiazdka).
- Nazwa **`np`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`cos`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`10`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`*`**: Operator mnożenia (gwiazdka).
- Nazwa **`Y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- **Komentarz `[ # Przykładowe dane sinusoidalne ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 10**: `# Tworzenie mapy cieplnej`
- **Komentarz `[ # Tworzenie mapy cieplnej ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 11**: `plt.imshow(heatmap_data, cmap='cividis', interpolation='nearest')`
- Nazwa **`plt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`imshow`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`heatmap_data`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`cmap`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'cividis'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`interpolation`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'nearest'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 13**: `# Dodanie paska kolorów`
- **Komentarz `[ # Dodanie paska kolorów ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 14**: `plt.colorbar(label='Intensywność')`
- Nazwa **`plt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`colorbar`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`label`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'Intensywność'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 16**: `# Tytuł i etykiety`
- **Komentarz `[ # Tytuł i etykiety ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 17**: `plt.title('Mapa Cieplna z Paskiem Kolorów')`
- Nazwa **`plt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`title`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'Mapa Cieplna z Paskiem Kolorów'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 18**: `plt.xlabel('X')`
- Nazwa **`plt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`xlabel`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'X'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 19**: `plt.ylabel('Y')`
- Nazwa **`plt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`ylabel`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'Y'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 21**: `# Wyświetlanie obrazu`
- **Komentarz `[ # Wyświetlanie obrazu ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 22**: `plt.show()`
- Nazwa **`plt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`show`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt
    
    # Generowanie przykładowych danych
    x = np.linspace(0, 1, 300)
    y = np.linspace(0, 1, 300)
    X, Y = np.meshgrid(x, y)
    heatmap_data = np.sin(10*X) * np.cos(10*Y)  # Przykładowe dane sinusoidalne
    
    # Tworzenie mapy cieplnej
    plt.imshow(heatmap_data, cmap='cividis', interpolation='nearest')
    
    # Dodanie paska kolorów
    plt.colorbar(label='Intensywność')
    
    # Tytuł i etykiety
    plt.title('Mapa Cieplna z Paskiem Kolorów')
    plt.xlabel('X')
    plt.ylabel('Y')
    
    # Wyświetlanie obrazu
    plt.show()
    return

@app.cell
def _():
    pass
    return

@app.cell
def _(mo):
    mo.md(r"""Zaawansowane przetwarzanie obrazów wykorzystując skimage https://scikit-image.org/docs/stable/api/skimage.data.html

Rejestracja obrazów

Etapy:

określenie przesunięcia między obrazami (metodą przepływu optycznego)

przesunięcie obrazu

złożenie obrazu""")
    return

@app.cell
def _():
    pass
    return

@app.cell
def _(mo):
    mo.md(r"""https://pillow.readthedocs.io/en/stable/""")
    return

if __name__ == "__main__":
    app.run()