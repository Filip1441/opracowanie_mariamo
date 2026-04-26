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
    mo.md(r"""# Wykład 5: Programowanie Obiektowe""")
    return

@app.cell
def _(mo):
    mo.md(r"""### TEORIA: OOP
`class Nazwa:` definiuje wzorzec. `self` to odwołanie do konkretnego egzemplarza obiektu.""")
    return

@app.cell
def _(mo):
    mo.md(r"""# Pytania po wykładzie 4""")
    return

@app.cell
def _(mo):
    mo.md(r"""# Jeśli f to funkcja, to jaka jest różnica między: f2=f, a f2=f()?""")
    return

@app.cell
def _(mo):
    mo.md(r"""# Co oznacza @log_input, umieszczone przed deklaracją funkcji?


""")
    return

@app.cell
def _(mo):
    mo.md(r"""# Co to są wartości domyślne argumentów i jak się je ustawia?""")
    return

@app.cell
def _(mo):
    mo.md(r"""# Co oznacza słowo global wewnątrz funkcji""")
    return

@app.cell
def _(mo):
    mo.md(r"""# Co to jest wyrażenie lambda?""")
    return

@app.cell
def _(mo):
    mo.md(r"""# Napisz wyrażenie lambda, umożliwia znalezienie najdłuższego słowa z listy""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `words = ["kot", "hipopotam", "pies"]`
- Nazwa **`words`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Tekst (String) **`"kot"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`"hipopotam"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`"pies"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 2**: `longest = max(words, key=lambda x: len(x))`
- Nazwa **`longest`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`max`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`words`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`key`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Słowo kluczowe **`lambda`**: Słowo kluczowe języka Python: 'lambda'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Nazwa **`len`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _words = ["kot", "hipopotam", "pies"]
    _longest = max(_words, key=lambda x: len(x))
    return

@app.cell
def _(mo):
    mo.md(r"""# Napisz wyrażenie lambda, które zwraca większą z dwóch liczb""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `max=lambda x,y:x if x>y else y`
- Nazwa **`max`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Słowo kluczowe **`lambda`**: Słowo kluczowe języka Python: 'lambda'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`if`**: Słowo kluczowe 'if' (jeśli). Rozpoczyna instrukcję warunkową. Komputer sprawdzi postawiony warunek - jeśli jest on prawdziwy, wykona kod pod spodem.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`>`**: Znak większości. Pyta: 'czy to po lewej jest większe?'.
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`else`**: Słowo kluczowe 'else' (w przeciwnym razie). Używane na samym końcu. Oznacza: 'Jeśli ŻADEN z wcześniejszych warunków nie był prawdziwy, wykonaj ostatecznie ten kod'.
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
""")
    return
@app.cell
def _():
    _max=lambda x,y:x if x>y else y
    return

@app.cell
def _(mo):
    mo.md(r"""# Napisz lambda, króra sprawdz czy liczba jest ujemna""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `ujemna=lambda x: x<0`
- Nazwa **`ujemna`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Słowo kluczowe **`lambda`**: Słowo kluczowe języka Python: 'lambda'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`<`**: Znak mniejszości. Pyta: 'czy to po lewej jest mniejsze niż to po prawej?'.
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 2**: `ujemna(1)`
- Nazwa **`ujemna`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _ujemna=lambda x: x<0
    _ujemna(1)
    return

@app.cell
def _(mo):
    mo.md(r"""# Napisz lambdę, która:
# zwraca „duża” jeśli liczba > 10, inaczej „mała”""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `wielkosc = lambda x: 'duża' if x > 10 else 'mała'`
- Nazwa **`wielkosc`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Słowo kluczowe **`lambda`**: Słowo kluczowe języka Python: 'lambda'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Tekst (String) **`'duża'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Słowo kluczowe **`if`**: Słowo kluczowe 'if' (jeśli). Rozpoczyna instrukcję warunkową. Komputer sprawdzi postawiony warunek - jeśli jest on prawdziwy, wykona kod pod spodem.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`>`**: Znak większości. Pyta: 'czy to po lewej jest większe?'.
- Liczba **`10`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Słowo kluczowe **`else`**: Słowo kluczowe 'else' (w przeciwnym razie). Używane na samym końcu. Oznacza: 'Jeśli ŻADEN z wcześniejszych warunków nie był prawdziwy, wykonaj ostatecznie ten kod'.
- Tekst (String) **`'mała'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
""")
    return
@app.cell
def _():
    _wielkosc = lambda x: 'duża' if x > 10 else 'mała'
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `# Posortować listę słów w kolejności alfabetycznej ostatniej litery`
- **Komentarz `[ # Posortować listę słów w kolejności alfabetycznej ostatniej litery ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.
""")
    return
@app.cell
def _():
    # Posortować listę słów w kolejności alfabetycznej ostatniej litery
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `posort = lambda x: x[-1]`
- Nazwa **`posort`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Słowo kluczowe **`lambda`**: Słowo kluczowe języka Python: 'lambda'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Znak **`-`**: Operator odejmowania.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 2**: `lista = ['kot', 'pies', 'kura']`
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Tekst (String) **`'kot'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'pies'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'kura'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 3**: `print(sorted(lista, key=posort))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`sorted`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`key`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`posort`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _posort = lambda x: x[-1]
    _lista = ['kot', 'pies', 'kura']
    print(sorted(_lista, key=_posort))
    return

@app.cell
def _(mo):
    mo.md(r"""# Programowanie obiektowe""")
    return

@app.cell
def _(mo):
    mo.md(r"""Programowanie obiektowe (ang. Object-Oriented Programming, OOP) to jeden z najpopularniejszych i najbardziej efektywnych paradygmatów programowania.

Kluczową ideą OOP jest modelowanie  poprzez klasy i obiekty. Klasa to wzorzec, który definiuje strukturę i zachowanie obiektów, natomiast obiekt to konkretny egzemplarz klasy z własnym zestawem danych. Dzięki temu podejściu kod jest bardziej przejrzysty, modułowy i łatwiejszy do ponownego wykorzystania.

Programowanie obiektowe bazuje na czterech fundamentalnych zasadach:

* Enkapsulacja – ukrywanie wewnętrznych szczegółów implementacji obiektu i udostępnianie tylko niezbędnych interfejsów.
* Dziedziczenie – możliwość tworzenia nowych klas na podstawie już istniejących, co ułatwia ponowne użycie kodu.
* Polimorfizm – zdolność obiektów do przyjmowania różnych form, co pozwala na elastyczne używanie metod w różnych kontekstach.
* Abstrakcja – upraszczanie skomplikowanych systemów poprzez ukrywanie zbędnych szczegółów i eksponowanie istotnych funkcji.""")
    return

@app.cell
def _(mo):
    mo.md(r"""
# Zalety programowania obiektowego (OOP)
* Modularność i ponowne użycie kodu

* Kod jest podzielony na klasy i obiekty, co ułatwia jego organizację.
* Klasy mogą być wielokrotnie używane w różnych częściach programu lub w innych projektach.
* Enkapsulacja (ukrywanie szczegółów implementacji)
* Dzięki mechanizmowi prywatnych i publicznych metod oraz pól, dane mogą być ukrywane przed nieautoryzowanym dostępem.
* Zwiększa bezpieczeństwo i minimalizuje ryzyko błędów wynikających z niepożądanego modyfikowania danych.
* Łatwiejsze zmiany i rozwój kodu
* Użytkownik klasy może korzystać z jej metod bez znajomości szczegółów implementacji.
* Dziedziczenie ozwala na ponowne wykorzystanie kodu przez rozszerzanie istniejących klas.
* Ułatwia tworzenie hierarchii klas i organizację kodu.
* Polimorfizm pozwala na tworzenie uniwersalnych interfejsów dla różnych typów obiektów.
* Ułatwia rozbudowę kodu i pozwala na elastyczniejsze implementowanie funkcji.
* Struktura obiektowa ułatwia podział projektu na mniejsze części, co jest przydatne zwłaszcza w zespołowym programowaniu.
* Każdy moduł może być rozwijany niezależnie.

# Wady programowania obiektowego


* Tworzenie klas, obiektów i hierarchii dziedziczenia może być bardziej skomplikowane niż proste podejście proceduralne.
* Wymaga większej ilości kodu, co może utrudniać naukę i implementację.
* Większe zużycie pamięci i mniejsza wydajność
* Tworzenie obiektów, dziedziczenie i dynamiczne wywoływanie metod mogą powodować większe zużycie zasobów w porównaniu do programowania proceduralnego.
* Ukrywanie implementacji przez enkapsulację może sprawić, że znalezienie problemu będzie bardziej czasochłonne.
* W prostych programach stosowanie OOP może być przesadą i niepotrzebnie komplikować kod.
* Tworzenie dobrze zaprojektowanych systemów OOP wymaga większego doświadczenia i przemyślanego projektowania.""")
    return

@app.cell
def _(mo):
    mo.md(r"""# Klasy wbudowane
1. Typy liczbowe
Klasy proste liczby całkowite, zmiennoprzecinkowe, zespolone i logiczne.
2. Typy sekwencyjne
Klasy reprezentujące struktury danych przechowujące elementy w określonym porządku (np. listy, krotki).
3. Typy zbiorów
Klasy reprezentujące zbiór unikalnych elementów.
4. Typy do pracy z danymi binarnymi
Klasy do przechowywania i manipulowania danymi w formie bajtów.
5. Typy do pracy z tekstem
Klasy reprezentujące ciągi znaków i operacje na nich.
6. Typy do obsługi plików i wejścia/wyjścia
Klasy umożliwiające operacje na plikach, strumieniach danych i wejściu/wyjściu.
7. Typy do obsługi wyjątków
Klasy reprezentujące różne wyjątki i błędy w Pythonie.
8. Typy do programowania obiektowego
Klasy wspomagające tworzenie i zarządzanie obiektami w Pythonie.
9. Typy do współbieżności i wielowątkowości
Klasy umożliwiające programowanie współbieżne i wielowątkowe.
10. Typy matematyczne
Klasy umożliwiające operacje na liczbach dziesiętnych, ułamkach i liczbach zespolonych.
11. Typy do pracy z czasem
Klasy do obsługi daty, czasu i związanych z nimi operacji.
12. Typy pomocnicze
Klasy wspomagające różne operacje, takie jak range do generowania sekwencji liczb, czy property do definiowania właściwości w klasach.
""")
    return

@app.cell
def _(mo):
    mo.md(r"""# Klasa str""")
    return

@app.cell
def _(mo):
    mo.md(r"""Podstawowe operacje na ciągach znaków:
* str.upper() - zamienia wszystkie litery na wielkie.
* str.lower() - zamienia wszystkie litery na małe.
* str.capitalize() - zamienia pierwszą literę na wielką, resztę na małe.
* str.title() - zamienia pierwsze litery wszystkich słów na wielkie.
* str.swapcase() - zamienia wielkie litery na małe i odwrotnie.

Sprawdzanie zawartości ciągu znaków:

* str.startswith(prefix) - sprawdza, czy ciąg zaczyna się od prefix.
* str.endswith(suffix) - sprawdza, czy ciąg kończy się na suffix.
* str.isalpha() - sprawdza, czy ciąg zawiera tylko litery.
* str.isdigit() - sprawdza, czy ciąg zawiera tylko cyfry.
* str.isalnum() - sprawdza, czy ciąg zawiera tylko litery i cyfry.
* str.isspace() - sprawdza, czy ciąg zawiera tylko białe znaki.
* str.islower() - sprawdza, czy wszystkie litery są małe.
* str.isupper() - sprawdza, czy wszystkie litery są wielkie.

Operacje na białych znakach:

* str.strip([chars]) -  usuwa białe znaki (lub podane znaki) z początku i końca ciągu.
* str.lstrip([chars]) - usuwa białe znaki (lub podane znaki) z początku ciągu.
* str.rstrip([chars]) - usuwa białe znaki (lub podane znaki) z końca ciągu.

Zastępowanie i modyfikowanie tekstu:

* str.replace(old, new[, count]) - zamienia wszystkie (lub określoną liczbę) wystąpienia old na new.
* str.translate(table) - tłumaczy znaki zgodnie z podaną tabelą (stosowane z str.maketrans).
* str.zfill(width) - dodaje zera na początku, aby osiągnąć określoną długość.

Wyszukiwanie i dzielenie tekstu:

* str.find(sub[, start[, end]]) – zwraca indeks pierwszego wystąpienia sub lub -1, jeśli nie znaleziono.
* str.rfind(sub[, start[, end]]) – zwraca indeks ostatniego wystąpienia sub.
* str.index(sub[, start[, end]]) – jak find(), ale rzuca wyjątek ValueError, jeśli sub nie występuje.
* str.rindex(sub[, start[, end]]) – jak rfind(), ale rzuca wyjątek ValueError, jeśli sub nie występuje.
* str.count(sub[, start[, end]]) – zwraca liczbę wystąpień sub w ciągu.
* str.split([sep[, maxsplit]]) – dzieli ciąg według sep, zwracając listę części.
* str.rsplit([sep[, maxsplit]]) – jak split(), ale dzielenie zaczyna się od końca.
* str.splitlines([keepends]) – dzieli tekst na linie.
* str.partition(sep) – dzieli ciąg na trzyczęściową krotkę: (przed, sep, po).
* str.rpartition(sep) – podobne do partition(), ale szuka sep od końca.

Formatowanie tekstu:

* str.center(width[, fillchar]) – centruje ciąg w polu o szerokości width.
* str.ljust(width[, fillchar]) – wyrównuje ciąg do lewej.
* str.rjust(width[, fillchar]) – wyrównuje ciąg do prawej.
* str.format(*args, **kwargs) – formatuje ciąg według podanych argumentów.
* str.format_map(mapping) – jak format(), ale używa słownika.
* str.join(iterable) – łączy elementy iterowalnej kolekcji w jeden ciąg, używając ciągu jako separatora.""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `str = "Ala ma kota {}"`
- Nazwa **`str`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`"Ala ma kota {}"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 2**: `print(str.upper())`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`str`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`upper`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 3**: `print(str.lower())`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`str`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`lower`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 4**: `text1 = "Produkt: {produkt}, cena: {cena} zł"`
- Nazwa **`text1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`"Produkt: {produkt}, cena: {cena} zł"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 5**: `print(text1)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`text1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 6**: `text=text1.format(produkt="Chleb", cena=4.5)`
- Nazwa **`text`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`text1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`format`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`produkt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`"Chleb"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`cena`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`4.5`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 7**: `print(text)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`text`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    str = "Ala ma kota {}"
    print(str.upper())
    print(str.lower())
    _text1 = "Produkt: {produkt}, cena: {cena} zł"
    print(_text1)
    _text=_text1.format(produkt="Chleb", cena=4.5)
    print(_text)
    return

@app.cell
def _(mo):
    mo.md(r"""## Świat bez klas""")
    return

@app.cell
def _(mo):
    mo.md(r"""## Chcemy zbudować zbiór danych o osobach.
* Co powinniśmy zrobić?
* Jakie struktury danych należu użyć?""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `osoba1={'name':'ALA','age':15}`
- Nazwa **`osoba1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`{`**: Lewy nawias klamrowy. Rozpoczyna słownik (zbiór par 'klucz: wartość') lub zbiór unikalnych elementów (set).
- Tekst (String) **`'name'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Tekst (String) **`'ALA'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'age'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Liczba **`15`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`}`**: Prawy nawias klamrowy. Kończy słownik lub zbiór.

#### 👉 **Linia 2**: `def getname(osoba):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`getname`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 3**: `return osoba['name']`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Nazwa **`osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Tekst (String) **`'name'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 4**: `def getage(osoba):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`getage`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 5**: `return osoba['age']`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Nazwa **`osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Tekst (String) **`'age'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 6**: `print(getname(osoba1))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`getname`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`osoba1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 7**: `print(getage(osoba1))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`getage`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`osoba1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _osoba1={'name':'ALA','age':15}
    def getname(osoba):
      return osoba['name']
    def getage(osoba):
      return osoba['age']
    print(getname(_osoba1))
    print(getage(_osoba1))
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `osoba2={'name':'TOMEK','age':85}`
- Nazwa **`osoba2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`{`**: Lewy nawias klamrowy. Rozpoczyna słownik (zbiór par 'klucz: wartość') lub zbiór unikalnych elementów (set).
- Tekst (String) **`'name'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Tekst (String) **`'TOMEK'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'age'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Liczba **`85`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`}`**: Prawy nawias klamrowy. Kończy słownik lub zbiór.

#### 👉 **Linia 2**: `lista=[osoba1,osoba2]`
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Nazwa **`osoba1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`osoba2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 3**: `for os in lista: print(getname(os))`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`os`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`getname`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`os`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _osoba2={'name':'TOMEK','age':85}
    _lista=[osoba1,_osoba2]
    for os in _lista: print(getname(os))
    return

@app.cell
def _(mo):
    mo.md(r"""## Z tekstu nie wynika jednoznacznie, że dwa obiekty należą do tej samej klasy, lista obiektów nie jest związana w sposób widoczny z klasami, liczba elementów przechowywana w oddzielnej zmiennej""")
    return

@app.cell
def _(mo):
    mo.md(r"""## Programowanie obiektowe""")
    return

@app.cell
def _(mo):
    mo.md(r"""W klasycznych językach programowania klasa składa się


* Opisu atrybutów klasy (argumentów, nazw pól)
* Konstruktora
* Metod

Dodatkowe pojęcia:

* argumenty prywatne
* argumenty statyczne
* metody statyczne
* polimorfizm
* dziedziczenie

""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `# klasa Osoba  - konstruktor`
- **Komentarz `[ # klasa Osoba  - konstruktor ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 3**: `class Osoba:`
- Słowo kluczowe **`class`**: Słowo kluczowe 'class' (klasa). Oznacza tworzenie nowego, złożonego typu danych (obiektu). To tak, jakbyś tworzył własną foremkę, z której potem będziesz 'wypiekać' konkretne obiekty (ciastka) o określonych cechach.
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 4**: `def  __init__(self, name, age):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 5**: `self.name=name`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 6**: `self.age=age`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 8**: `o1=Osoba("Ania",50)`
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Ania"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`50`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 9**: `print(o1.name,o1.age)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    # klasa Osoba  - konstruktor
    
    class Osoba:
     def  __init__(self, name, age):
      self.name=name
      self.age=age
    
    _o1=Osoba("Ania",50)
    print(_o1.name,_o1.age)
    return

@app.cell
def _(mo):
    mo.md(r"""# Nie definiujemy pól w nagłówku, są one definiowane w konstruktorze""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `# klasa Osoba, dodajemy metody`
- **Komentarz `[ # klasa Osoba, dodajemy metody ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 3**: `class Osoba:`
- Słowo kluczowe **`class`**: Słowo kluczowe 'class' (klasa). Oznacza tworzenie nowego, złożonego typu danych (obiektu). To tak, jakbyś tworzył własną foremkę, z której potem będziesz 'wypiekać' konkretne obiekty (ciastka) o określonych cechach.
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 4**: `def  __init__(self, name, age):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 5**: `self.name=name`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 6**: `self.age=age`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 7**: `def  druk(self):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`druk`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 8**: `print(self.name,self.age)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 10**: `o1=Osoba("Ania",50)`
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Ania"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`50`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 11**: `o1.druk()`
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`druk`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    # klasa Osoba, dodajemy metody
    
    class Osoba:
     def  __init__(self, name, age):
      self.name=name
      self.age=age
     def  druk(self):
      print(self.name,self.age)
    
    _o1=Osoba("Ania",50)
    _o1.druk()
    return

@app.cell
def _(mo):
    mo.md(r"""## Pola statyczne""")
    return

@app.cell
def _(mo):
    mo.md(r"""pola statyczne są powiązane z klasą, a nie z obiektem, nie mamy słów kluczowych, decyduje miejsce deklaracji""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `class Osoba:`
- Słowo kluczowe **`class`**: Słowo kluczowe 'class' (klasa). Oznacza tworzenie nowego, złożonego typu danych (obiektu). To tak, jakbyś tworzył własną foremkę, z której potem będziesz 'wypiekać' konkretne obiekty (ciastka) o określonych cechach.
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 2**: `liczba=0              #liczba elementów            #miejsce deklaracji`
- Nazwa **`liczba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- **Komentarz `[ #liczba elementów            #miejsce deklaracji ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 3**: `lista=[]              #lista elementów`
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- **Komentarz `[ #lista elementów ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 4**: `def  __init__(self, name, age):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 5**: `self.name=name`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 6**: `self.age=age`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 7**: `Osoba.liczba+=1`
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`liczba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`+=`**: Znak interpunkcyjny lub operator: '+='. Służy do organizacji struktury kodu.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 8**: `Osoba.lista.append(self)`
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`append`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 9**: `def  druk(self):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`druk`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 10**: `print(self.name,self.age,Osoba.liczba)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`liczba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 12**: `o1=Osoba("Ania",50)`
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Ania"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`50`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 13**: `o1.druk()`
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`druk`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 14**: `o2=Osoba("Agata",50)`
- Nazwa **`o2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Agata"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`50`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 15**: `o2.druk()`
- Nazwa **`o2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`druk`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 16**: `o1.druk()`
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`druk`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    class Osoba:
     _liczba=0              #_liczba elementów            #miejsce deklaracji
     _lista=[]              #_lista elementów
     def  __init__(self, name, age):
      self.name=name
      self.age=age
      Osoba._liczba+=1
      Osoba._lista.append(self)
     def  druk(self):
      print(self.name,self.age,Osoba._liczba)
    
    _o1=Osoba("Ania",50)
    _o1.druk()
    _o2=Osoba("Agata",50)
    _o2.druk()
    _o1.druk()
    return

@app.cell
def _(mo):
    mo.md(r"""Pobieranie informacji o instancji lub klasie""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `print(isinstance(o1,Osoba))  #sprawdzenie czy o1 jest instancją klasy`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`isinstance`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- **Komentarz `[ #sprawdzenie czy o1 jest instancją klasy ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `print(type(o1))  #sprawdzenie instancją jakiej klasy jest o1`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`type`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- **Komentarz `[ #sprawdzenie instancją jakiej klasy jest o1 ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 3**: `print(o1.__class__)  # __cos__  - specjalne metody lub pola`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`__class__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- **Komentarz `[ # __cos__  - specjalne metody lub pola ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.
""")
    return
@app.cell
def _():
    print(isinstance(o1,Osoba))  #sprawdzenie czy o1 jest instancją klasy
    print(type(o1))  #sprawdzenie instancją jakiej klasy jest o1
    print(o1.__class__)  # __cos__  - specjalne metody lub pola
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `# dokładniejsze informacje o obiekcie`
- **Komentarz `[ # dokładniejsze informacje o obiekcie ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.
""")
    return
@app.cell
def _():
    # dokładniejsze informacje o obiekcie
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `print(vars(o1))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`vars`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    print(vars(o1))
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `print(vars(Osoba))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`vars`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    print(vars(Osoba))
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `dir(vars(Osoba))`
- Nazwa **`dir`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`vars`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    dir(vars(Osoba))
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `class Osoba:`
- Słowo kluczowe **`class`**: Słowo kluczowe 'class' (klasa). Oznacza tworzenie nowego, złożonego typu danych (obiektu). To tak, jakbyś tworzył własną foremkę, z której potem będziesz 'wypiekać' konkretne obiekty (ciastka) o określonych cechach.
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 2**: `def  __init__(self, name, age, sex):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`sex`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 3**: `self.name=name`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 4**: `self.age=age`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 5**: `self.__sex=sex`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`__sex`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`sex`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 6**: `o1=Osoba("Ania",50,"women")`
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Ania"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`50`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`"women"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 7**: `print(o1.name,o1.age,o1.__sex)    #próba dostępu do pola prywatnego, błąd`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`__sex`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- **Komentarz `[ #próba dostępu do pola prywatnego, błąd ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.
""")
    return
@app.cell
def _():
    class Osoba:
     def  __init__(self, name, age, sex):
      self.name=name
      self.age=age
      self.__sex=sex
    _o1=Osoba("Ania",50,"women")
    print(_o1.name,_o1.age,_o1.__sex)    #próba dostępu do pola prywatnego, błąd
    return

@app.cell
def _(mo):
    mo.md(r"""Pola prywatne - brak dostępu poza klasą""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `class Osoba:`
- Słowo kluczowe **`class`**: Słowo kluczowe 'class' (klasa). Oznacza tworzenie nowego, złożonego typu danych (obiektu). To tak, jakbyś tworzył własną foremkę, z której potem będziesz 'wypiekać' konkretne obiekty (ciastka) o określonych cechach.
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 2**: `l=1`
- Nazwa **`l`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 3**: `def  __init__(self, name, age,sex,l):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`sex`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`l`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 4**: `self.name=name`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 5**: `self.age=age`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 6**: `self.__l=l`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`__l`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`l`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 7**: `o1=Osoba("Ania",50,"women",2)`
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Ania"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`50`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`"women"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 8**: `o1.__l=8        #powstaje nowe pole`
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`__l`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`8`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- **Komentarz `[ #powstaje nowe pole ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 9**: `print(vars(o1))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`vars`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    class Osoba:
     _l=1
     def  __init__(self, name, age,sex,_l):
      self.name=name
      self.age=age
      self.__l=_l
    _o1=Osoba("Ania",50,"women",2)
    _o1.__l=8        #powstaje nowe pole
    print(vars(_o1))
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `class Osoba:`
- Słowo kluczowe **`class`**: Słowo kluczowe 'class' (klasa). Oznacza tworzenie nowego, złożonego typu danych (obiektu). To tak, jakbyś tworzył własną foremkę, z której potem będziesz 'wypiekać' konkretne obiekty (ciastka) o określonych cechach.
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 2**: `def  __init__(self, name, age, sex):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`sex`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 3**: `self.name=name`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 4**: `self.age=age`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 5**: `self.__sex=sex`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`__sex`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`sex`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 6**: `o1=Osoba("Ania",50,"women")`
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Ania"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`50`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`"women"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 7**: `o1.__sex="mmm"                             #powstaje nowe pole`
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`__sex`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`"mmm"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- **Komentarz `[ #powstaje nowe pole ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 8**: `print(o1.name,o1.age,o1.__sex)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`__sex`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 9**: `print(vars(o1))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`vars`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    class Osoba:
     def  __init__(self, name, age, sex):
      self.name=name
      self.age=age
      self.__sex=sex
    _o1=Osoba("Ania",50,"women")
    _o1.__sex="mmm"                             #powstaje nowe pole
    print(_o1.name,_o1.age,_o1.__sex)
    print(vars(_o1))
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `#dodawanie pól poza klasą`
- **Komentarz `[ #dodawanie pól poza klasą ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 4**: `class Osoba:`
- Słowo kluczowe **`class`**: Słowo kluczowe 'class' (klasa). Oznacza tworzenie nowego, złożonego typu danych (obiektu). To tak, jakbyś tworzył własną foremkę, z której potem będziesz 'wypiekać' konkretne obiekty (ciastka) o określonych cechach.
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 5**: `def  __init__(self, name, age):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 6**: `self.name=name`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 7**: `self.age=age`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 8**: `o1=Osoba("Ania",50)`
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Ania"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`50`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 9**: `print(vars(o1))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`vars`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 10**: `o1.sex="Women"                         #powstaje nowe pole`
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`sex`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`"Women"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- **Komentarz `[ #powstaje nowe pole ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 11**: `print(o1.name,o1.age,o1.sex)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`sex`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 12**: `print(vars(o1))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`vars`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    #dodawanie pól poza klasą
    
    
    class Osoba:
     def  __init__(self, name, age):
      self.name=name
      self.age=age
    _o1=Osoba("Ania",50)
    print(vars(_o1))
    _o1.sex="Women"                         #powstaje nowe pole
    print(_o1.name,_o1.age,_o1.sex)
    print(vars(_o1))
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `# usuwanie atrybutu`
- **Komentarz `[ # usuwanie atrybutu ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 3**: `class Osoba:`
- Słowo kluczowe **`class`**: Słowo kluczowe 'class' (klasa). Oznacza tworzenie nowego, złożonego typu danych (obiektu). To tak, jakbyś tworzył własną foremkę, z której potem będziesz 'wypiekać' konkretne obiekty (ciastka) o określonych cechach.
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 4**: `def  __init__(self, name, age):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 5**: `self.name=name`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 6**: `self.age=age`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 7**: `o1=Osoba("Ania",50)`
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Ania"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`50`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 8**: `o1.sex="Women"`
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`sex`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`"Women"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 9**: `print(vars(o1))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`vars`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 10**: `del o1.sex`
- Słowo kluczowe **`del`**: Słowo kluczowe języka Python: 'del'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`sex`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 11**: `print(vars(o1))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`vars`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    # usuwanie atrybutu
    
    class Osoba:
     def  __init__(self, name, age):
      self.name=name
      self.age=age
    _o1=Osoba("Ania",50)
    _o1.sex="Women"
    print(vars(_o1))
    del _o1.sex
    print(vars(_o1))
    return

@app.cell
def _(mo):
    mo.md(r"""## Funkcja setattr       umożliwia zmianę wartości pól, kolejność jak w konstruktorze""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `class Osoba1:`
- Słowo kluczowe **`class`**: Słowo kluczowe 'class' (klasa). Oznacza tworzenie nowego, złożonego typu danych (obiektu). To tak, jakbyś tworzył własną foremkę, z której potem będziesz 'wypiekać' konkretne obiekty (ciastka) o określonych cechach.
- Nazwa **`Osoba1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 2**: `def  __init__(self, name, age):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 3**: `self.name=name`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 4**: `self.age=age`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 5**: `o2=Osoba1("Ania",50)`
- Nazwa **`o2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`Osoba1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Ania"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`50`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 6**: `# print(o2.name,o2.age,o2.sex)`
- **Komentarz `[ # print(o2.name,o2.age,o2.sex) ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 7**: `setattr(o2,"sex","woman")    #o2 musi istnieć`
- Nazwa **`setattr`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`o2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`"sex"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`"woman"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- **Komentarz `[ #o2 musi istnieć ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 8**: `print(o2.name,o2.age,o2.sex)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`o2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`o2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`o2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`sex`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 9**: `print(vars(o2))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`vars`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`o2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 10**: `delattr(o2,"sex")             #tu usuwamy atrybut`
- Nazwa **`delattr`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`o2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`"sex"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- **Komentarz `[ #tu usuwamy atrybut ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.
""")
    return
@app.cell
def _():
    class Osoba1:
     def  __init__(self, name, age):
      self.name=name
      self.age=age
    _o2=Osoba1("Ania",50)
    # print(_o2.name,_o2.age,_o2.sex)
    setattr(_o2,"sex","woman")    #_o2 musi istnieć
    print(_o2.name,_o2.age,_o2.sex)
    print(vars(_o2))
    delattr(_o2,"sex")             #tu usuwamy atrybut
    return

@app.cell
def _(mo):
    mo.md(r"""## Metody statyczne, to metody związane z klasą, a nie z pojedynczym obiektem""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `#metody klasy`
- **Komentarz `[ #metody klasy ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 3**: `class Osoba:`
- Słowo kluczowe **`class`**: Słowo kluczowe 'class' (klasa). Oznacza tworzenie nowego, złożonego typu danych (obiektu). To tak, jakbyś tworzył własną foremkę, z której potem będziesz 'wypiekać' konkretne obiekty (ciastka) o określonych cechach.
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 4**: `def  __init__(self, name, age):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 5**: `self.name=name`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 6**: `self.age=age`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 7**: `#definiujemy metodę statyczną`
- **Komentarz `[ #definiujemy metodę statyczną ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 8**: `@classmethod             #metoda statyczna`
- Znak **`@`**: Znak interpunkcyjny lub operator: '@'. Służy do organizacji struktury kodu.
- Nazwa **`classmethod`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- **Komentarz `[ #metoda statyczna ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 9**: `def nag(cls):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`nag`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`cls`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 10**: `print("klasa osoba")`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"klasa osoba"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 11**: `o1=Osoba("Ania",50)`
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Ania"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`50`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 12**: `o1.sex="Women"`
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`sex`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`"Women"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 13**: `Osoba.nag()`
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`nag`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 14**: `print(o1.name,o1.age,o1.sex)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`sex`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 15**: `print(vars(o1))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`vars`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    #metody klasy
    
    class Osoba:
     def  __init__(self, name, age):
      self.name=name
      self.age=age
    #definiujemy metodę statyczną
     @classmethod             #metoda statyczna
     def nag(cls):
      print("klasa osoba")
    _o1=Osoba("Ania",50)
    _o1.sex="Women"
    Osoba.nag()
    print(_o1.name,_o1.age,_o1.sex)
    print(vars(_o1))
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `# metoda split, będzie potrzebna w kolejnym przykładzie`
- **Komentarz `[ # metoda split, będzie potrzebna w kolejnym przykładzie ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `tekst="jan ma"`
- Nazwa **`tekst`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`"jan ma"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 3**: `print(*tekst.split(' '))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`*`**: Operator mnożenia (gwiazdka).
- Nazwa **`tekst`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`split`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`' '`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    # metoda split, będzie potrzebna w kolejnym przykładzie
    _tekst="jan ma"
    print(*_tekst.split(' '))
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `#metody klasy trochę bardziej skomplikowane, tworzenie obiektu bez konstruktora`
- **Komentarz `[ #metody klasy trochę bardziej skomplikowane, tworzenie obiektu bez konstruktora ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 3**: `class Osoba:`
- Słowo kluczowe **`class`**: Słowo kluczowe 'class' (klasa). Oznacza tworzenie nowego, złożonego typu danych (obiektu). To tak, jakbyś tworzył własną foremkę, z której potem będziesz 'wypiekać' konkretne obiekty (ciastka) o określonych cechach.
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 4**: `def  __init__(self, name, age):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 5**: `self.name=name`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 6**: `self.age=age`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 7**: `#definiujemy metodę statyczną`
- **Komentarz `[ #definiujemy metodę statyczną ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 8**: `@classmethod`
- Znak **`@`**: Znak interpunkcyjny lub operator: '@'. Służy do organizacji struktury kodu.
- Nazwa **`classmethod`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 9**: `def newob(cls,tekst):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`newob`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`cls`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`tekst`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 10**: `print(tekst)   #tekst, wartości argumentów`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`tekst`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- **Komentarz `[ #tekst, wartości argumentów ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 11**: `print(*tekst)  #ciąg znaków`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`*`**: Operator mnożenia (gwiazdka).
- Nazwa **`tekst`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- **Komentarz `[ #ciąg znaków ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 12**: `o2=cls(*tekst.split(' '))`
- Nazwa **`o2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cls`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`*`**: Operator mnożenia (gwiazdka).
- Nazwa **`tekst`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`split`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`' '`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 13**: `return(o2)`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`o2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 14**: `o1=Osoba("Ania",50)`
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Ania"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`50`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 15**: `o2=Osoba.newob("Jan 100")`
- Nazwa **`o2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`newob`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Jan 100"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 16**: `print('o2', o2.name,o2.age)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'o2'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`o2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`o2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 17**: `print('vars o2', vars(o2))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'vars o2'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`vars`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`o2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    #metody klasy trochę bardziej skomplikowane, tworzenie obiektu bez konstruktora
    
    class Osoba:
     def  __init__(self, name, age):
      self.name=name
      self.age=age
    #definiujemy metodę statyczną
     @classmethod
     def newob(cls,tekst):
      print(tekst)   #tekst, wartości argumentów
      print(*tekst)  #ciąg znaków
      _o2=cls(*tekst.split(' '))
      return(_o2)
    _o1=Osoba("Ania",50)
    _o2=Osoba.newob("Jan 100")
    print('_o2', _o2.name,_o2.age)
    print('vars _o2', vars(_o2))
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `# Dekoratory - property, odwołujemy się do metody jak do pola klasy`
- **Komentarz `[ # Dekoratory - property, odwołujemy się do metody jak do pola klasy ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `class Osoba:`
- Słowo kluczowe **`class`**: Słowo kluczowe 'class' (klasa). Oznacza tworzenie nowego, złożonego typu danych (obiektu). To tak, jakbyś tworzył własną foremkę, z której potem będziesz 'wypiekać' konkretne obiekty (ciastka) o określonych cechach.
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 3**: `def  __init__(self, name, age, sex):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`sex`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 4**: `self.name=name`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 5**: `self.age=age`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 6**: `self.sex=sex`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`sex`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`sex`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 7**: `@property       #możemy się odwoływać do metody jak do pola klasy`
- Znak **`@`**: Znak interpunkcyjny lub operator: '@'. Służy do organizacji struktury kodu.
- Nazwa **`property`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- **Komentarz `[ #możemy się odwoływać do metody jak do pola klasy ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 8**: `def prints(self):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`prints`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 9**: `print(self.sex)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`sex`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 10**: `o1=Osoba("Ania",50,"women")`
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Ania"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`50`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`"women"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 11**: `print(o1.name,o1.age)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 12**: `o1.prints              # to jest poprawne`
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`prints`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- **Komentarz `[ # to jest poprawne ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 13**: `print(vars(o1))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`vars`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 14**: `print(vars(Osoba))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`vars`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    # Dekoratory - property, odwołujemy się do metody jak do pola klasy
    class Osoba:
     def  __init__(self, name, age, sex):
      self.name=name
      self.age=age
      self.sex=sex
     @property       #możemy się odwoływać do metody jak do pola klasy
     def prints(self):
       print(self.sex)
    _o1=Osoba("Ania",50,"women")
    print(_o1.name,_o1.age)
    _o1.prints              # to jest poprawne
    print(vars(_o1))
    print(vars(Osoba))
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `# Dekoratory ustawianie wartości`
- **Komentarz `[ # Dekoratory ustawianie wartości ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `class Osoba:`
- Słowo kluczowe **`class`**: Słowo kluczowe 'class' (klasa). Oznacza tworzenie nowego, złożonego typu danych (obiektu). To tak, jakbyś tworzył własną foremkę, z której potem będziesz 'wypiekać' konkretne obiekty (ciastka) o określonych cechach.
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 3**: `def  __init__(self, name, age, sex):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`sex`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 4**: `self.name=name`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 5**: `self.age=age`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 6**: `self.__sex=sex`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`__sex`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`sex`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 7**: `@property                           # umożliwia pobranie wartości pola prywatnego`
- Znak **`@`**: Znak interpunkcyjny lub operator: '@'. Służy do organizacji struktury kodu.
- Nazwa **`property`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- **Komentarz `[ # umożliwia pobranie wartości pola prywatnego ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 8**: `def sex(self):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`sex`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 9**: `return self.__sex`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`__sex`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 10**: `@sex.setter                         # umożliwia zmianę wartości pola prywatnego`
- Znak **`@`**: Znak interpunkcyjny lub operator: '@'. Służy do organizacji struktury kodu.
- Nazwa **`sex`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`setter`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- **Komentarz `[ # umożliwia zmianę wartości pola prywatnego ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 11**: `def sex(self,newval):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`sex`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`newval`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 12**: `self.__sex=newval`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`__sex`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`newval`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 13**: `o1=Osoba("Ania",50,"women")`
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Ania"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`50`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`"women"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 14**: `print(o1.name,o1.age,o1.sex)             # sex to funkcja, a nie pole klasy`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`sex`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- **Komentarz `[ # sex to funkcja, a nie pole klasy ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 15**: `o1.sex="man"`
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`sex`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`"man"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 16**: `print(vars(o1))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`vars`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 19**: `o2=Osoba("Tom",50,"women")`
- Nazwa **`o2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Tom"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`50`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`"women"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 20**: `print(o2.name,o1.age)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`o2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 21**: `o2.sex="man"`
- Nazwa **`o2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`sex`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`"man"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 22**: `print(vars(o2))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`vars`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`o2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    # Dekoratory ustawianie wartości
    class Osoba:
     def  __init__(self, name, age, sex):
      self.name=name
      self.age=age
      self.__sex=sex
     @property                           # umożliwia pobranie wartości pola prywatnego
     def sex(self):
       return self.__sex
     @sex.setter                         # umożliwia zmianę wartości pola prywatnego
     def sex(self,newval):
       self.__sex=newval
    _o1=Osoba("Ania",50,"women")
    print(_o1.name,_o1.age,_o1.sex)             # sex to funkcja, a nie pole klasy
    _o1.sex="man"
    print(vars(_o1))
    
    
    _o2=Osoba("Tom",50,"women")
    print(_o2.name,_o1.age)
    _o2.sex="man"
    print(vars(_o2))
    return

@app.cell
def _(mo):
    mo.md(r"""Metody prywatne, podobnie jak pola zaczynają się od __""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `class Osoba:`
- Słowo kluczowe **`class`**: Słowo kluczowe 'class' (klasa). Oznacza tworzenie nowego, złożonego typu danych (obiektu). To tak, jakbyś tworzył własną foremkę, z której potem będziesz 'wypiekać' konkretne obiekty (ciastka) o określonych cechach.
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 2**: `def  __init__(self, name, age, sex):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`sex`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 3**: `self.name=name`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 4**: `self.age=age`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 5**: `self.__sex=sex`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`__sex`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`sex`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 6**: `def __getname(self):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__getname`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 7**: `return self.name`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 8**: `def printname(self):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`printname`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 9**: `print(self.__getname())`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`__getname`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 10**: `o1=Osoba("Basia",100,"nn")`
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Basia"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`100`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`"nn"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 11**: `o1.printname()`
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`printname`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    class Osoba:
     def  __init__(self, name, age, sex):
      self.name=name
      self.age=age
      self.__sex=sex
     def __getname(self):
      return self.name
     def printname(self):
       print(self.__getname())
    _o1=Osoba("Basia",100,"nn")
    _o1.printname()
    return

@app.cell
def _(mo):
    mo.md(r"""# Klasy collable, obiekty tych klas możemy wyoływać jak funkcje""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `# sprawdzamy`
- **Komentarz `[ # sprawdzamy ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `print(callable(len))          # True (funkcja wbudowana)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`callable`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`len`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- **Komentarz `[ # True (funkcja wbudowana) ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 3**: `print(callable(42))           # False (liczba nie jest callable)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`callable`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`42`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- **Komentarz `[ # False (liczba nie jest callable) ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 4**: `print(callable(lambda x: x))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`callable`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Słowo kluczowe **`lambda`**: Słowo kluczowe języka Python: 'lambda'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 5**: `a1=lambda x:x`
- Nazwa **`a1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Słowo kluczowe **`lambda`**: Słowo kluczowe języka Python: 'lambda'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 6**: `print(callable(a1))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`callable`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`a1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    # sprawdzamy
    print(callable(len))          # True (funkcja wbudowana)
    print(callable(42))           # False (liczba nie jest callable)
    print(callable(lambda x: x))
    _a1=lambda x:x
    print(callable(_a1))
    return

@app.cell
def _():
    pass
    return

@app.cell
def _():
    pass
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `#klasyczne podejście`
- **Komentarz `[ #klasyczne podejście ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `class Osoba:`
- Słowo kluczowe **`class`**: Słowo kluczowe 'class' (klasa). Oznacza tworzenie nowego, złożonego typu danych (obiektu). To tak, jakbyś tworzył własną foremkę, z której potem będziesz 'wypiekać' konkretne obiekty (ciastka) o określonych cechach.
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 3**: `def  __init__(self, name, lista):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 4**: `self.name=name`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 5**: `self.lista=lista`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 6**: `o1=Osoba("Basia",[])`
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Basia"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 7**: `o1.lista.append("Basia")`
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`append`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Basia"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 8**: `print(o1.lista)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    #klasyczne podejście
    class Osoba:
     def  __init__(self, name, lista):
      self.name=name
      self.lista=lista
    _o1=Osoba("Basia",[])
    _o1.lista.append("Basia")
    print(_o1.lista)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `#nowe podejście rozszerzania listy, kod jest bardziej czytelny, odzielamy inicjalizację od wykonania`
- **Komentarz `[ #nowe podejście rozszerzania listy, kod jest bardziej czytelny, odzielamy inicjalizację od wykonania ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `class Osoba:`
- Słowo kluczowe **`class`**: Słowo kluczowe 'class' (klasa). Oznacza tworzenie nowego, złożonego typu danych (obiektu). To tak, jakbyś tworzył własną foremkę, z której potem będziesz 'wypiekać' konkretne obiekty (ciastka) o określonych cechach.
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 3**: `def  __init__(self, name, lista):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 4**: `self.name=name`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 5**: `self.lista=lista`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 6**: `def __call__(self, item):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__call__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`item`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 7**: `self.lista.append(item)`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`append`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`item`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 8**: `print("dodaję",item)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"dodaję"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`item`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 9**: `o1=Osoba("Basia",[])`
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Basia"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 10**: `o2=o1(" xxxx")`
- Nazwa **`o2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`" xxxx"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 11**: `o1(" yyy")`
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`" yyy"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 12**: `print(o1.lista)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 13**: `print(callable(o1),callable(o2))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`callable`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`callable`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`o2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    #nowe podejście rozszerzania listy, kod jest bardziej czytelny, odzielamy inicjalizację od wykonania
    class Osoba:
     def  __init__(self, name, lista):
      self.name=name
      self.lista=lista
     def __call__(self, item):
       self.lista.append(item)
       print("dodaję",item)
    _o1=Osoba("Basia",[])
    _o2=_o1(" xxxx")
    _o1(" yyy")
    print(_o1.lista)
    print(callable(_o1),callable(_o2))
    return

@app.cell
def _(mo):
    mo.md(r"""## Do konstruktora możemy przekazać funkcję, tak jak pole klasy""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `class Osoba:`
- Słowo kluczowe **`class`**: Słowo kluczowe 'class' (klasa). Oznacza tworzenie nowego, złożonego typu danych (obiektu). To tak, jakbyś tworzył własną foremkę, z której potem będziesz 'wypiekać' konkretne obiekty (ciastka) o określonych cechach.
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 2**: `lista=[]`
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 3**: `def  __init__(self, func):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`func`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 4**: `self.func=func`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`func`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`func`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 5**: `def test():`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`test`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 6**: `print("test")`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"test"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 7**: `o1=Osoba(test)`
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`test`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 8**: `o1.func()`
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`func`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    class Osoba:
     _lista=[]
     def  __init__(self, func):
      self.func=func
    def test():
      print("test")
    _o1=Osoba(test)
    _o1.func()
    return

@app.cell
def _(mo):
    mo.md(r"""Operatory, operacje na obiektach""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `class Osoba:`
- Słowo kluczowe **`class`**: Słowo kluczowe 'class' (klasa). Oznacza tworzenie nowego, złożonego typu danych (obiektu). To tak, jakbyś tworzył własną foremkę, z której potem będziesz 'wypiekać' konkretne obiekty (ciastka) o określonych cechach.
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 2**: `def  __init__(self, name,lista):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 3**: `self.name=name`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 4**: `self.lista=lista`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 5**: `def __add__(self,other):           #zwracamy String`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__add__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`other`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- **Komentarz `[ #zwracamy String ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 6**: `return self.name+" "+other.name`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Tekst (String) **`" "`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Nazwa **`other`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 7**: `o1=Osoba("Basia",[])`
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Basia"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 8**: `o2=Osoba("Adam",[])`
- Nazwa **`o2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Adam"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 9**: `print(o1+o2)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Nazwa **`o2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    class Osoba:
     def  __init__(self, name,lista):
      self.name=name
      self.lista=lista
     def __add__(self,other):           #zwracamy String
       return self.name+" "+other.name
    _o1=Osoba("Basia",[])
    _o2=Osoba("Adam",[])
    print(_o1+_o2)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `class MyClass:`
- Słowo kluczowe **`class`**: Słowo kluczowe 'class' (klasa). Oznacza tworzenie nowego, złożonego typu danych (obiektu). To tak, jakbyś tworzył własną foremkę, z której potem będziesz 'wypiekać' konkretne obiekty (ciastka) o określonych cechach.
- Nazwa **`MyClass`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 2**: `def __init__(self, value):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`value`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 3**: `self.value = value`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`value`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`value`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 5**: `def __mul__(self, other):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__mul__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`other`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 6**: `if isinstance(other, int):`
- Słowo kluczowe **`if`**: Słowo kluczowe 'if' (jeśli). Rozpoczyna instrukcję warunkową. Komputer sprawdzi postawiony warunek - jeśli jest on prawdziwy, wykona kod pod spodem.
- Nazwa **`isinstance`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`other`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`int`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 7**: `return MyClass(self.value * other) # zwracamy obieky klasy`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Nazwa **`MyClass`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`value`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`*`**: Operator mnożenia (gwiazdka).
- Nazwa **`other`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- **Komentarz `[ # zwracamy obieky klasy ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 8**: `else:`
- Słowo kluczowe **`else`**: Słowo kluczowe 'else' (w przeciwnym razie). Używane na samym końcu. Oznacza: 'Jeśli ŻADEN z wcześniejszych warunków nie był prawdziwy, wykonaj ostatecznie ten kod'.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 9**: `return 0`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 10**: `m1 = MyClass(5)`
- Nazwa **`m1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`MyClass`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`5`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 11**: `m2=m1*3`
- Nazwa **`m2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`m1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`*`**: Operator mnożenia (gwiazdka).
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 12**: `print(m2.value)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`m2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`value`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    class MyClass:
        def __init__(self, value):
            self.value = value
    
        def __mul__(self, other):
            if isinstance(other, int):
                return MyClass(self.value * other) # zwracamy obieky klasy
            else:
                return 0
    _m1 = MyClass(5)
    _m2=_m1*3
    print(_m2.value)
    return

@app.cell
def _(mo):
    mo.md(r"""## Przykładowe nazwy:

* __add__ - Przeciąża operator dodawania +.
* __sub__ - Przeciąża operator odejmowania -.
* __div__ - Przeciąża operator dzielenia / (w starszych wersjach Pythona, w Pythonie 3.x należy używać __truediv__).
* __floordiv__ - Przeciąża operator dzielenia całkowitego //.
* __mod__ - Przeciąża operator modulo %.
* __pow__ - Przeciąża operator potęgowania **.
* __lt__ - Przeciąża operator < (mniejsze niż).
* __le__ - Przeciąża operator <= (mniejsze niż lub równe).
* __eq__ - Przeciąża operator == (równe).
* __ne__ - Przeciąża operator != (różne).
* __gt__ - Przeciąża operator > (większe niż).
* __ge__ - Przeciąża operator >= (większe niż lub równe).
* __getitem__ - Przeciąża operator indeksowania [].
* __setitem__ - Przeciąża operator przypisania wartości dla indeksu [].
* __len__ - Przeciąża funkcję len().
* __str__ - Przeciąża funkcję str().""")
    return

@app.cell
def _(mo):
    mo.md(r"""Dziedziczenie""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `#metoda1`
- **Komentarz `[ #metoda1 ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 3**: `class Osoba:`
- Słowo kluczowe **`class`**: Słowo kluczowe 'class' (klasa). Oznacza tworzenie nowego, złożonego typu danych (obiektu). To tak, jakbyś tworzył własną foremkę, z której potem będziesz 'wypiekać' konkretne obiekty (ciastka) o określonych cechach.
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 4**: `def  __init__(self, name):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 5**: `self.name=name`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 6**: `class Student(Osoba):`
- Słowo kluczowe **`class`**: Słowo kluczowe 'class' (klasa). Oznacza tworzenie nowego, złożonego typu danych (obiektu). To tak, jakbyś tworzył własną foremkę, z której potem będziesz 'wypiekać' konkretne obiekty (ciastka) o określonych cechach.
- Nazwa **`Student`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 7**: `def __init__(self,name,id):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`id`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 8**: `super().__init__(name)`
- Nazwa **`super`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 9**: `self.id=id`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`id`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`id`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 10**: `o1=Osoba("Basia")`
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Basia"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 11**: `o2=Student("Adam","sdsdsd")`
- Nazwa **`o2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`Student`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Adam"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`"sdsdsd"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 12**: `print(o2.id)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`o2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`id`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    #metoda1
    
    class Osoba:
     def  __init__(self, name):
      self.name=name
    class Student(Osoba):
      def __init__(self,name,id):
       super().__init__(name)
       self.id=id
    _o1=Osoba("Basia")
    _o2=Student("Adam","sdsdsd")
    print(_o2.id)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `#metoda2`
- **Komentarz `[ #metoda2 ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 3**: `class Osoba:`
- Słowo kluczowe **`class`**: Słowo kluczowe 'class' (klasa). Oznacza tworzenie nowego, złożonego typu danych (obiektu). To tak, jakbyś tworzył własną foremkę, z której potem będziesz 'wypiekać' konkretne obiekty (ciastka) o określonych cechach.
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 4**: `def  __init__(self, name):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 5**: `self.name=name`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 6**: `class Student(Osoba):                           #  Student dziedziczy po klasie Osoba`
- Słowo kluczowe **`class`**: Słowo kluczowe 'class' (klasa). Oznacza tworzenie nowego, złożonego typu danych (obiektu). To tak, jakbyś tworzył własną foremkę, z której potem będziesz 'wypiekać' konkretne obiekty (ciastka) o określonych cechach.
- Nazwa **`Student`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- **Komentarz `[ #  Student dziedziczy po klasie Osoba ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 7**: `def __init__(self,name,id):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`id`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 8**: `Osoba.__init__(self,name)`
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 9**: `self.id=id`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`id`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`id`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 10**: `o1=Osoba("Basia")`
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Basia"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 11**: `o2=Student("Adam","sdsdsd")`
- Nazwa **`o2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`Student`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Adam"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`"sdsdsd"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 12**: `print(o2.id)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`o2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`id`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    #metoda2
    
    class Osoba:
     def  __init__(self, name):
      self.name=name
    class Student(Osoba):                           #  Student dziedziczy po klasie Osoba
      def __init__(self,name,id):
       Osoba.__init__(self,name)
       self.id=id
    _o1=Osoba("Basia")
    _o2=Student("Adam","sdsdsd")
    print(_o2.id)
    return

@app.cell
def _(mo):
    mo.md(r"""## Polimorfizm  - różne zachowanie metody, zależnie od kontekstu""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `class Kot:`
- Słowo kluczowe **`class`**: Słowo kluczowe 'class' (klasa). Oznacza tworzenie nowego, złożonego typu danych (obiektu). To tak, jakbyś tworzył własną foremkę, z której potem będziesz 'wypiekać' konkretne obiekty (ciastka) o określonych cechach.
- Nazwa **`Kot`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 2**: `def dzwiek(self):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`dzwiek`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 3**: `return "Miau!"`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Tekst (String) **`"Miau!"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 5**: `class Pies:`
- Słowo kluczowe **`class`**: Słowo kluczowe 'class' (klasa). Oznacza tworzenie nowego, złożonego typu danych (obiektu). To tak, jakbyś tworzył własną foremkę, z której potem będziesz 'wypiekać' konkretne obiekty (ciastka) o określonych cechach.
- Nazwa **`Pies`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 6**: `def dzwiek(self):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`dzwiek`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 7**: `return "Hau!"`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Tekst (String) **`"Hau!"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 9**: `# Funkcja wykorzystująca polimorfizm`
- **Komentarz `[ # Funkcja wykorzystująca polimorfizm ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 10**: `def wydaj_dzwiek(zwierze):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`wydaj_dzwiek`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`zwierze`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 11**: `print(zwierze.dzwiek())`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`zwierze`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`dzwiek`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 13**: `# Tworzenie obiektów`
- **Komentarz `[ # Tworzenie obiektów ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 14**: `kot = Kot()`
- Nazwa **`kot`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`Kot`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 15**: `pies = Pies()`
- Nazwa **`pies`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`Pies`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 17**: `# Wywołanie tej samej metody na różnych obiektach, a właściwie metody statycznej klasy`
- **Komentarz `[ # Wywołanie tej samej metody na różnych obiektach, a właściwie metody statycznej klasy ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 18**: `wydaj_dzwiek(kot)  # Miau!`
- Nazwa **`wydaj_dzwiek`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`kot`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- **Komentarz `[ # Miau! ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 19**: `wydaj_dzwiek(pies)  # Hau!`
- Nazwa **`wydaj_dzwiek`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`pies`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- **Komentarz `[ # Hau! ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 20**: `lista=[kot,pies]   #  Mamy elementy różnych klas`
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Nazwa **`kot`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`pies`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- **Komentarz `[ #  Mamy elementy różnych klas ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 21**: `for zwierze in lista:`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`zwierze`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 22**: `wydaj_dzwiek(zwierze)`
- Nazwa **`wydaj_dzwiek`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`zwierze`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    class Kot:
        def dzwiek(self):
            return "Miau!"
    
    class Pies:
        def dzwiek(self):
            return "Hau!"
    
    # Funkcja wykorzystująca polimorfizm
    def wydaj_dzwiek(zwierze):
        print(zwierze.dzwiek())
    
    # Tworzenie obiektów
    _kot = Kot()
    _pies = Pies()
    
    # Wywołanie tej samej metody na różnych obiektach, a właściwie metody statycznej klasy
    wydaj_dzwiek(_kot)  # Miau!
    wydaj_dzwiek(_pies)  # Hau!
    _lista=[_kot,_pies]   #  Mamy elementy różnych klas
    for zwierze in _lista:
      wydaj_dzwiek(zwierze)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `class Osoba:`
- Słowo kluczowe **`class`**: Słowo kluczowe 'class' (klasa). Oznacza tworzenie nowego, złożonego typu danych (obiektu). To tak, jakbyś tworzył własną foremkę, z której potem będziesz 'wypiekać' konkretne obiekty (ciastka) o określonych cechach.
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 2**: `def  __init__(self, name):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 3**: `self.name=name`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 4**: `def druk(self):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`druk`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 5**: `print(self.name)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 6**: `class Student(Osoba):`
- Słowo kluczowe **`class`**: Słowo kluczowe 'class' (klasa). Oznacza tworzenie nowego, złożonego typu danych (obiektu). To tak, jakbyś tworzył własną foremkę, z której potem będziesz 'wypiekać' konkretne obiekty (ciastka) o określonych cechach.
- Nazwa **`Student`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 7**: `def __init__(self,name,id):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`id`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 8**: `Osoba.__init__(self,name)`
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 9**: `self.id=id`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`id`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`id`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 10**: `def druk(self):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`druk`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 11**: `print(self.name,"  ",self.id)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`"  "`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`id`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 12**: `def druk(self,tekst):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`druk`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`tekst`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 13**: `print(tekst,"  ",self.name,"  ",self.id)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`tekst`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`"  "`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`"  "`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`id`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 14**: `o1=Osoba("Basia")`
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`Osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Basia"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 15**: `o1.druk()`
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`druk`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 16**: `o2=Student("Adam","indeks")`
- Nazwa **`o2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`Student`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Adam"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`"indeks"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 17**: `o2.druk("tekst")`
- Nazwa **`o2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`druk`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"tekst"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    class Osoba:
     def  __init__(self, name):
      self.name=name
     def druk(self):
       print(self.name)
    class Student(Osoba):
      def __init__(self,name,id):
       Osoba.__init__(self,name)
       self.id=id
      def druk(self):
       print(self.name,"  ",self.id)
      def druk(self,tekst):
       print(tekst,"  ",self.name,"  ",self.id)
    _o1=Osoba("Basia")
    _o1.druk()
    _o2=Student("Adam","indeks")
    _o2.druk("tekst")
    return

@app.cell
def _(mo):
    mo.md(r"""## Dziedziczenie po wielu klasach""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `class Color:`
- Słowo kluczowe **`class`**: Słowo kluczowe 'class' (klasa). Oznacza tworzenie nowego, złożonego typu danych (obiektu). To tak, jakbyś tworzył własną foremkę, z której potem będziesz 'wypiekać' konkretne obiekty (ciastka) o określonych cechach.
- Nazwa **`Color`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 2**: `def __init__(self,color):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`color`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 3**: `self.color=color`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`color`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`color`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 4**: `class Punkt:`
- Słowo kluczowe **`class`**: Słowo kluczowe 'class' (klasa). Oznacza tworzenie nowego, złożonego typu danych (obiektu). To tak, jakbyś tworzył własną foremkę, z której potem będziesz 'wypiekać' konkretne obiekty (ciastka) o określonych cechach.
- Nazwa **`Punkt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 5**: `def __init__(self,x,y):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 6**: `self.x=x`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 7**: `self.y=y`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 8**: `class Cpunkt(Color,Punkt):`
- Słowo kluczowe **`class`**: Słowo kluczowe 'class' (klasa). Oznacza tworzenie nowego, złożonego typu danych (obiektu). To tak, jakbyś tworzył własną foremkę, z której potem będziesz 'wypiekać' konkretne obiekty (ciastka) o określonych cechach.
- Nazwa **`Cpunkt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`Color`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`Punkt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 9**: `def __init__(self,x,y,color):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`color`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 10**: `Color.__init__(self,color)`
- Nazwa **`Color`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`color`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 11**: `Punkt.__init__(self,x,y)`
- Nazwa **`Punkt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 12**: `o1=Cpunkt(1,2,"red")`
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`Cpunkt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`"red"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 13**: `print(vars(o1))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`vars`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    class Color:
      def __init__(self,color):
        self.color=color
    class Punkt:
      def __init__(self,x,y):
        self.x=x
        self.y=y
    class Cpunkt(Color,Punkt):
      def __init__(self,x,y,color):
        Color.__init__(self,color)
        Punkt.__init__(self,x,y)
    _o1=Cpunkt(1,2,"red")
    print(vars(_o1))
    return

@app.cell
def _():
    pass
    return

@app.cell
def _(mo):
    mo.md(r"""W przypadku wielodziedziczenia mamy problem funkcja z jakiej klasy będzie wywoływana, jeśli nazwy i argumenty są takie same, tu decyduje kolejność klas podana w konstruktorze""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `class Color:`
- Słowo kluczowe **`class`**: Słowo kluczowe 'class' (klasa). Oznacza tworzenie nowego, złożonego typu danych (obiektu). To tak, jakbyś tworzył własną foremkę, z której potem będziesz 'wypiekać' konkretne obiekty (ciastka) o określonych cechach.
- Nazwa **`Color`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 2**: `def __init__(self,color):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`color`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 3**: `self.color=color`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`color`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`color`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 4**: `def printn(self,ttt):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`printn`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`ttt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 5**: `print("Color")`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Color"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 6**: `print(ttt)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`ttt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 7**: `class Punkt:`
- Słowo kluczowe **`class`**: Słowo kluczowe 'class' (klasa). Oznacza tworzenie nowego, złożonego typu danych (obiektu). To tak, jakbyś tworzył własną foremkę, z której potem będziesz 'wypiekać' konkretne obiekty (ciastka) o określonych cechach.
- Nazwa **`Punkt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 8**: `def __init__(self,x,y):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 9**: `self.x=x`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 10**: `self.y=y`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 11**: `def printn(self,ttt):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`printn`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`ttt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 12**: `print("Punkt")`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Punkt"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 13**: `print(ttt)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`ttt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 14**: `class Cpunkt(Punkt,Color):`
- Słowo kluczowe **`class`**: Słowo kluczowe 'class' (klasa). Oznacza tworzenie nowego, złożonego typu danych (obiektu). To tak, jakbyś tworzył własną foremkę, z której potem będziesz 'wypiekać' konkretne obiekty (ciastka) o określonych cechach.
- Nazwa **`Cpunkt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`Punkt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`Color`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 15**: `def __init__(self,x,y,color):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`color`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 16**: `Color.__init__(self,color)`
- Nazwa **`Color`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`color`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 17**: `Punkt.__init__(self,x,y)`
- Nazwa **`Punkt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 18**: `o1=Cpunkt(1,1,"red")`
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`Cpunkt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`"red"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 19**: `o1.printn("test")`
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`printn`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"test"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    class Color:
      def __init__(self,color):
        self.color=color
      def printn(self,ttt):
        print("Color")
        print(ttt)
    class Punkt:
      def __init__(self,x,y):
        self.x=x
        self.y=y
      def printn(self,ttt):
        print("Punkt")
        print(ttt)
    class Cpunkt(Punkt,Color):
      def __init__(self,x,y,color):
        Color.__init__(self,color)
        Punkt.__init__(self,x,y)
    _o1=Cpunkt(1,1,"red")
    _o1.printn("test")
    return

@app.cell
def _():
    pass
    return

@app.cell
def _():
    pass
    return

@app.cell
def _(mo):
    mo.md(r"""Jeśli funkcja występuje tylko w jednej klasie nadrzędnej to problemu nie mamy""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 2**: `class Color:`
- Słowo kluczowe **`class`**: Słowo kluczowe 'class' (klasa). Oznacza tworzenie nowego, złożonego typu danych (obiektu). To tak, jakbyś tworzył własną foremkę, z której potem będziesz 'wypiekać' konkretne obiekty (ciastka) o określonych cechach.
- Nazwa **`Color`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 3**: `def __init__(self,color):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`color`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 4**: `self.color=color`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`color`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`color`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 5**: `def mprint(self,ttt):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`mprint`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`ttt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 6**: `print("Color")`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Color"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 7**: `print(ttt)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`ttt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 8**: `class Punkt:`
- Słowo kluczowe **`class`**: Słowo kluczowe 'class' (klasa). Oznacza tworzenie nowego, złożonego typu danych (obiektu). To tak, jakbyś tworzył własną foremkę, z której potem będziesz 'wypiekać' konkretne obiekty (ciastka) o określonych cechach.
- Nazwa **`Punkt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 9**: `def __init__(self,x,y):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 10**: `self.x=x`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 11**: `self.y=y`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 12**: `def xmprint(self,ttt):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`xmprint`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`ttt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 13**: `print("Punkt")`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Punkt"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 14**: `print(ttt)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`ttt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 15**: `class Cpunkt(Punkt,Color):`
- Słowo kluczowe **`class`**: Słowo kluczowe 'class' (klasa). Oznacza tworzenie nowego, złożonego typu danych (obiektu). To tak, jakbyś tworzył własną foremkę, z której potem będziesz 'wypiekać' konkretne obiekty (ciastka) o określonych cechach.
- Nazwa **`Cpunkt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`Punkt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`Color`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 16**: `def __init__(self,x,y,color):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`color`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 17**: `Color.__init__(self,color)`
- Nazwa **`Color`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`color`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 18**: `Punkt.__init__(self,x,y)`
- Nazwa **`Punkt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 19**: `def mprint(self,ttt):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`mprint`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`ttt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 20**: `super().mprint(ttt)`
- Nazwa **`super`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`mprint`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`ttt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 21**: `o1=Cpunkt(1,1,"red")`
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`Cpunkt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`"red"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 22**: `o1.mprint("test")`
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`mprint`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"test"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    
    class Color:
      def __init__(self,color):
        self.color=color
      def mprint(self,ttt):
        print("Color")
        print(ttt)
    class Punkt:
      def __init__(self,x,y):
        self.x=x
        self.y=y
      def xmprint(self,ttt):
        print("Punkt")
        print(ttt)
    class Cpunkt(Punkt,Color):
      def __init__(self,x,y,color):
        Color.__init__(self,color)
        Punkt.__init__(self,x,y)
      def mprint(self,ttt):
        super().mprint(ttt)
    _o1=Cpunkt(1,1,"red")
    _o1.mprint("test")
    return

@app.cell
def _(mo):
    mo.md(r"""Warto jest dokumentować kod, a w szczególności klasę którą się zbudowało. Dokumentowanie klasy polega na opisaniu, czym jest klasa, jakie ma atrybuty i metody, jakich typów są argumenty i zwracane wartości, jakie są założenia i wymagania co do poprawności danych wejściowych oraz ogólnie jak korzystać z klasy.

Zwykle dokumentacja klas jest pisana w tzw. Docstrings, czyli w specjalnym komentarzu umieszczonym na początku definicji klasy, metody lub funkcji. Docstrings są specjalnymi ciągami znaków umieszczonymi w trzech cudzysłowach.""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `help(Punkt)`
- Nazwa **`help`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`Punkt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    help(Punkt)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `class Color:`
- Słowo kluczowe **`class`**: Słowo kluczowe 'class' (klasa). Oznacza tworzenie nowego, złożonego typu danych (obiektu). To tak, jakbyś tworzył własną foremkę, z której potem będziesz 'wypiekać' konkretne obiekty (ciastka) o określonych cechach.
- Nazwa **`Color`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 2**: `\"\"\"`
- Tekst (String) **`\"\"\"
    Przykład opisu klasy kolor
  \"\"\"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 4**: `\"\"\"`

#### 👉 **Linia 5**: `def __init__(self,color):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`color`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 6**: `\"\"\"`
- Tekst (String) **`\"\"\"
    Do konstruktora przekazujemy kolor
    \"\"\"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 8**: `\"\"\"`

#### 👉 **Linia 9**: `self.color=color`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`color`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`color`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 10**: `def mprint(self,ttt):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`mprint`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`ttt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 11**: `print("Color")`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Color"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 12**: `print(ttt)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`ttt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 13**: `class Punkt:`
- Słowo kluczowe **`class`**: Słowo kluczowe 'class' (klasa). Oznacza tworzenie nowego, złożonego typu danych (obiektu). To tak, jakbyś tworzył własną foremkę, z której potem będziesz 'wypiekać' konkretne obiekty (ciastka) o określonych cechach.
- Nazwa **`Punkt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 14**: `def __init__(self,x,y):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 15**: `self.x=x`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 16**: `self.y=y`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 17**: `def xmprint(self,ttt):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`xmprint`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`ttt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 18**: `print("Punkt")`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Punkt"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 19**: `print(ttt)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`ttt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 20**: `class Cpunkt(Punkt,Color):`
- Słowo kluczowe **`class`**: Słowo kluczowe 'class' (klasa). Oznacza tworzenie nowego, złożonego typu danych (obiektu). To tak, jakbyś tworzył własną foremkę, z której potem będziesz 'wypiekać' konkretne obiekty (ciastka) o określonych cechach.
- Nazwa **`Cpunkt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`Punkt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`Color`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 21**: `def __init__(self,x,y,color):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`color`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 22**: `Color.__init__(self,color)`
- Nazwa **`Color`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`color`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 23**: `Punkt.__init__(self,x,y)`
- Nazwa **`Punkt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 24**: `def mprint(self,ttt):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`mprint`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`ttt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 25**: `super().mprint(ttt)`
- Nazwa **`super`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`mprint`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`ttt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 26**: `o1=Cpunkt(1,1,"red")`
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`Cpunkt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`"red"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 27**: `o1.mprint("test")`
- Nazwa **`o1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`mprint`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"test"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    class Color:
      """
        Przykład opisu klasy kolor
      """
      def __init__(self,color):
        """
        Do konstruktora przekazujemy kolor
        """
        self.color=color
      def mprint(self,ttt):
        print("Color")
        print(ttt)
    class Punkt:
      def __init__(self,x,y):
        self.x=x
        self.y=y
      def xmprint(self,ttt):
        print("Punkt")
        print(ttt)
    class Cpunkt(Punkt,Color):
      def __init__(self,x,y,color):
        Color.__init__(self,color)
        Punkt.__init__(self,x,y)
      def mprint(self,ttt):
        super().mprint(ttt)
    _o1=Cpunkt(1,1,"red")
    _o1.mprint("test")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `help(Color)`
- Nazwa **`help`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`Color`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    help(Color)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `## przykład wykorzystania na wykładzie`
- **Komentarz `[ ## przykład wykorzystania na wykładzie ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.
""")
    return
@app.cell
def _():
    ## przykład wykorzystania na wykładzie
    return

@app.cell
def _(mo):
    mo.md(r"""## Obsługa wyjątków (błędów)""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `x=0`
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 2**: `z=1/x`
- Nazwa **`z`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`/`**: Operator dzielenia.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 3**: `print(z)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`z`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _x=0
    _z=1/_x
    print(_z)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `x=0`
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 2**: `try:`
- Słowo kluczowe **`try`**: Słowo kluczowe 'try' (próbuj). Rozpoczyna niebezpieczny blok kodu, w którym komputer ma 'spróbować' wykonać operację, spodziewając się, że może pojawić się awaria/błąd.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 3**: `z=1/x`
- Nazwa **`z`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`/`**: Operator dzielenia.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 4**: `except:`
- Słowo kluczowe **`except`**: Słowo kluczowe 'except' (za wyjątkiem / przechwyć). Określa ratunek: co komputer ma awaryjnie zrobić, jeśli w bloku 'try' faktycznie wystąpił błąd. Zapobiega to gwałtownemu wyłączeniu się programu.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 5**: `print("dzielenie przez zero")`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"dzielenie przez zero"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 6**: `else:`
- Słowo kluczowe **`else`**: Słowo kluczowe 'else' (w przeciwnym razie). Używane na samym końcu. Oznacza: 'Jeśli ŻADEN z wcześniejszych warunków nie był prawdziwy, wykonaj ostatecznie ten kod'.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 7**: `print(z)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`z`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _x=0
    try:
      _z=1/_x
    except:
      print("dzielenie przez zero")
    else:
      print(_z)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `x=1`
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 2**: `try:`
- Słowo kluczowe **`try`**: Słowo kluczowe 'try' (próbuj). Rozpoczyna niebezpieczny blok kodu, w którym komputer ma 'spróbować' wykonać operację, spodziewając się, że może pojawić się awaria/błąd.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 3**: `z=1/x`
- Nazwa **`z`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`/`**: Operator dzielenia.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 4**: `except:`
- Słowo kluczowe **`except`**: Słowo kluczowe 'except' (za wyjątkiem / przechwyć). Określa ratunek: co komputer ma awaryjnie zrobić, jeśli w bloku 'try' faktycznie wystąpił błąd. Zapobiega to gwałtownemu wyłączeniu się programu.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 5**: `print("dzielenie przez zero")`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"dzielenie przez zero"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 6**: `else:`
- Słowo kluczowe **`else`**: Słowo kluczowe 'else' (w przeciwnym razie). Używane na samym końcu. Oznacza: 'Jeśli ŻADEN z wcześniejszych warunków nie był prawdziwy, wykonaj ostatecznie ten kod'.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 7**: `print(z)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`z`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 8**: `finally:`
- Słowo kluczowe **`finally`**: Słowo kluczowe języka Python: 'finally'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 9**: `print("koniec")`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"koniec"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _x=1
    try:
      _z=1/_x
    except:
      print("dzielenie przez zero")
    else:
      print(_z)
    finally:
      print("koniec")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `x=0`
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 2**: `try:`
- Słowo kluczowe **`try`**: Słowo kluczowe 'try' (próbuj). Rozpoczyna niebezpieczny blok kodu, w którym komputer ma 'spróbować' wykonać operację, spodziewając się, że może pojawić się awaria/błąd.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 3**: `z=1/x`
- Nazwa **`z`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`/`**: Operator dzielenia.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 4**: `except Exception as e:`
- Słowo kluczowe **`except`**: Słowo kluczowe 'except' (za wyjątkiem / przechwyć). Określa ratunek: co komputer ma awaryjnie zrobić, jeśli w bloku 'try' faktycznie wystąpił błąd. Zapobiega to gwałtownemu wyłączeniu się programu.
- Nazwa **`Exception`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`as`**: Słowo kluczowe języka Python: 'as'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`e`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 5**: `print("dzielenie przez zero",e)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"dzielenie przez zero"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`e`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 6**: `else:`
- Słowo kluczowe **`else`**: Słowo kluczowe 'else' (w przeciwnym razie). Używane na samym końcu. Oznacza: 'Jeśli ŻADEN z wcześniejszych warunków nie był prawdziwy, wykonaj ostatecznie ten kod'.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 7**: `print(z)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`z`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 8**: `finally:`
- Słowo kluczowe **`finally`**: Słowo kluczowe języka Python: 'finally'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 9**: `print("koniec")`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"koniec"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _x=0
    try:
      _z=1/_x
    except Exception as e:
      print("dzielenie przez zero",e)
    else:
      print(_z)
    finally:
      print("koniec")
    return

@app.cell
def _(mo):
    mo.md(r"""W bloku try możemy wykryć różne rodzaje błędów, które mogą wystąpić podczas wykonywania kodu.



1.    Błędy składniowe (SyntaxError) - wykrywane przez interpreter podczas analizowania składni kodu.
Wyjątki związane z typami danych (TypeError, ValueError) - np. próba wykonania
operacji nieobsługiwanej przez dany typ danych, przekroczenie zakresu itp.
2.   Wyjątki związane z plikami (FileNotFoundError, PermissionError) - np. próba otwarcia nieistniejącego pliku, brak uprawnień do odczytu/zapisu pliku itp.
3.   Wyjątki związane z innymi błędami wykonania (RuntimeError) - np. próba wykonania niepoprawnej operacji, przekroczenie stosu, itp.
4.   Wyjątki związane z siecią (ConnectionError) - np. błędy połączenia, przekroczenie czasu oczekiwania itp.
Istnieją też inne wyjątki, takie jak ZeroDivisionError, IndexError, KeyError, ImportError, AssertionError, oraz wiele innych.""")
    return

@app.cell
def _(mo):
    mo.md(r"""* Exception: Bazowa klasa dla wszystkich wyjątków.
* AttributeError: Występuje, gdy atrybut obiektu nie istnieje.
* IndexError: Występuje, gdy indeks listy lub innej sekwencji jest poza zakresem.
* KeyError: Występuje, gdy klucz nie istnieje w słowniku.
* ValueError: Występuje, gdy funkcja otrzymuje argument o niewłaściwej wartości.
* TypeError: Występuje, gdy operacja lub funkcja jest stosowana do obiektu niewłaściwego typu.
* NameError: Występuje, gdy zmienna lub nazwa funkcji nie jest zdefiniowana.
* ZeroDivisionError: Występuje, gdy próbujesz podzielić przez zero.
* FileNotFoundError: Występuje, gdy próba otwarcia pliku, który nie istnieje, kończy się niepowodzeniem.
* ImportError: Występuje, gdy moduł nie może zostać zaimportowany.
* IOError: Występuje, gdy operacja wejścia/wyjścia (np. otwarcie pliku) kończy się niepowodzeniem.
* RuntimeError: Występuje, gdy błąd nie pasuje do żadnej innej kategorii wyjątków.""")
    return

@app.cell
def _(mo):
    mo.md(r"""## Własne wyjątki""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `class Kwadrat:`
- Słowo kluczowe **`class`**: Słowo kluczowe 'class' (klasa). Oznacza tworzenie nowego, złożonego typu danych (obiektu). To tak, jakbyś tworzył własną foremkę, z której potem będziesz 'wypiekać' konkretne obiekty (ciastka) o określonych cechach.
- Nazwa **`Kwadrat`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 2**: `def  __init__(self,x,y):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 3**: `self.x=x`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 4**: `self.y=y`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 5**: `def pole(self):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`pole`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 6**: `return self.x*self.y       #tu musi być self`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`*`**: Operator mnożenia (gwiazdka).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- **Komentarz `[ #tu musi być self ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 7**: `k1=Kwadrat(2,2)`
- Nazwa **`k1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`Kwadrat`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 8**: `print(k1.pole())`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`k1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`pole`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    class Kwadrat:
     def  __init__(self,x,y):
        self.x=x
        self.y=y
     def pole(self):
       return self.x*self.y       #tu musi być self
    _k1=Kwadrat(2,2)
    print(_k1.pole())
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `# Tu zgłaszamy własny wyjątek`
- **Komentarz `[ # Tu zgłaszamy własny wyjątek ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 3**: `class Kwadrat:`
- Słowo kluczowe **`class`**: Słowo kluczowe 'class' (klasa). Oznacza tworzenie nowego, złożonego typu danych (obiektu). To tak, jakbyś tworzył własną foremkę, z której potem będziesz 'wypiekać' konkretne obiekty (ciastka) o określonych cechach.
- Nazwa **`Kwadrat`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 4**: `def  __init__(self,x,y):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 5**: `self.x=x`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 6**: `self.y=y`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 7**: `def pole(self):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`pole`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 8**: `if self.x < 0 or self.y <0:`
- Słowo kluczowe **`if`**: Słowo kluczowe 'if' (jeśli). Rozpoczyna instrukcję warunkową. Komputer sprawdzi postawiony warunek - jeśli jest on prawdziwy, wykona kod pod spodem.
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`<`**: Znak mniejszości. Pyta: 'czy to po lewej jest mniejsze niż to po prawej?'.
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Słowo kluczowe **`or`**: Słowo 'or' (lub). Łączy dwa warunki. Całość jest prawdziwa, gdy PRZYNAJMNIEJ JEDEN z warunków jest prawdziwy.
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`<`**: Znak mniejszości. Pyta: 'czy to po lewej jest mniejsze niż to po prawej?'.
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 9**: `raise Exception("Złe wymiary")`
- Słowo kluczowe **`raise`**: Słowo kluczowe języka Python: 'raise'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`Exception`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Złe wymiary"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 10**: `else:`
- Słowo kluczowe **`else`**: Słowo kluczowe 'else' (w przeciwnym razie). Używane na samym końcu. Oznacza: 'Jeśli ŻADEN z wcześniejszych warunków nie był prawdziwy, wykonaj ostatecznie ten kod'.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 11**: `return self.x*self.y       #tu musi być self`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`*`**: Operator mnożenia (gwiazdka).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- **Komentarz `[ #tu musi być self ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 12**: `k1=Kwadrat(2,2)`
- Nazwa **`k1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`Kwadrat`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 13**: `print(k1.pole())`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`k1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`pole`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    # Tu zgłaszamy własny wyjątek
    
    class Kwadrat:
     def  __init__(self,x,y):
        self.x=x
        self.y=y
     def pole(self):
       if self.x < 0 or self.y <0:
         raise Exception("Złe wymiary")
       else:
        return self.x*self.y       #tu musi być self
    _k1=Kwadrat(2,2)
    print(_k1.pole())
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `# No to jescze musimy obsłużyć ten wyjątek`
- **Komentarz `[ # No to jescze musimy obsłużyć ten wyjątek ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 3**: `class Kwadrat:`
- Słowo kluczowe **`class`**: Słowo kluczowe 'class' (klasa). Oznacza tworzenie nowego, złożonego typu danych (obiektu). To tak, jakbyś tworzył własną foremkę, z której potem będziesz 'wypiekać' konkretne obiekty (ciastka) o określonych cechach.
- Nazwa **`Kwadrat`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 4**: `def  __init__(self,x,y):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 5**: `self.x=x`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 6**: `self.y=y`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 7**: `def pole(self):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`pole`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 8**: `if self.x < 0 or self.y <0:`
- Słowo kluczowe **`if`**: Słowo kluczowe 'if' (jeśli). Rozpoczyna instrukcję warunkową. Komputer sprawdzi postawiony warunek - jeśli jest on prawdziwy, wykona kod pod spodem.
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`<`**: Znak mniejszości. Pyta: 'czy to po lewej jest mniejsze niż to po prawej?'.
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Słowo kluczowe **`or`**: Słowo 'or' (lub). Łączy dwa warunki. Całość jest prawdziwa, gdy PRZYNAJMNIEJ JEDEN z warunków jest prawdziwy.
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`<`**: Znak mniejszości. Pyta: 'czy to po lewej jest mniejsze niż to po prawej?'.
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 9**: `raise Exception("Złe wymiary")`
- Słowo kluczowe **`raise`**: Słowo kluczowe języka Python: 'raise'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`Exception`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Złe wymiary"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 10**: `else:`
- Słowo kluczowe **`else`**: Słowo kluczowe 'else' (w przeciwnym razie). Używane na samym końcu. Oznacza: 'Jeśli ŻADEN z wcześniejszych warunków nie był prawdziwy, wykonaj ostatecznie ten kod'.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 11**: `return self.x*self.y       #tu musi być self`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`*`**: Operator mnożenia (gwiazdka).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- **Komentarz `[ #tu musi być self ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 13**: `k1=Kwadrat(2,2)`
- Nazwa **`k1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`Kwadrat`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 14**: `try:`
- Słowo kluczowe **`try`**: Słowo kluczowe 'try' (próbuj). Rozpoczyna niebezpieczny blok kodu, w którym komputer ma 'spróbować' wykonać operację, spodziewając się, że może pojawić się awaria/błąd.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 15**: `k=k1.pole()`
- Nazwa **`k`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`k1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`pole`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 16**: `except Exception as e:`
- Słowo kluczowe **`except`**: Słowo kluczowe 'except' (za wyjątkiem / przechwyć). Określa ratunek: co komputer ma awaryjnie zrobić, jeśli w bloku 'try' faktycznie wystąpił błąd. Zapobiega to gwałtownemu wyłączeniu się programu.
- Nazwa **`Exception`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`as`**: Słowo kluczowe języka Python: 'as'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`e`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 17**: `print(e)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`e`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 18**: `else:`
- Słowo kluczowe **`else`**: Słowo kluczowe 'else' (w przeciwnym razie). Używane na samym końcu. Oznacza: 'Jeśli ŻADEN z wcześniejszych warunków nie był prawdziwy, wykonaj ostatecznie ten kod'.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 19**: `print(k)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`k`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    # No to jescze musimy obsłużyć ten wyjątek
    
    class Kwadrat:
     def  __init__(self,x,y):
        self.x=x
        self.y=y
     def pole(self):
       if self.x < 0 or self.y <0:
          raise Exception("Złe wymiary")
       else:
        return self.x*self.y       #tu musi być self
    
    _k1=Kwadrat(2,2)
    try:
     _k=_k1.pole()
    except Exception as e:
      print(e)
    else:
      print(_k)
    
    return

@app.cell
def _(mo):
    mo.md(r"""Bardziej elegancko będzie wyglądać kod w którym mamy własną klasę np. BadDimensionError . Klasa BadDimensionError powinna dziedziczyć po wbudowanej klasie wyjątków ValueError, ponieważ ten wyjątek jest przeznaczony do sygnalizowania błędów związanych z nieprawidłowymi wartościami argumentów.""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `# przykład klasy`
- **Komentarz `[ # przykład klasy ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `class BadDimensionError(ValueError):`
- Słowo kluczowe **`class`**: Słowo kluczowe 'class' (klasa). Oznacza tworzenie nowego, złożonego typu danych (obiektu). To tak, jakbyś tworzył własną foremkę, z której potem będziesz 'wypiekać' konkretne obiekty (ciastka) o określonych cechach.
- Nazwa **`BadDimensionError`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`ValueError`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 3**: `def __init__(self, message):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`message`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 4**: `super().__init__(message)`
- Nazwa **`super`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`message`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    # przykład klasy
    class BadDimensionError(ValueError):
        def __init__(self, message):
            super().__init__(message)
    return

@app.cell
def _(mo):
    mo.md(r"""A pełny kod będzie wyglądał następująco:""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `#ValueError`
- **Komentarz `[ #ValueError ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `class BadDimensionError(ValueError):`
- Słowo kluczowe **`class`**: Słowo kluczowe 'class' (klasa). Oznacza tworzenie nowego, złożonego typu danych (obiektu). To tak, jakbyś tworzył własną foremkę, z której potem będziesz 'wypiekać' konkretne obiekty (ciastka) o określonych cechach.
- Nazwa **`BadDimensionError`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`ValueError`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 3**: `def __init__(self, message):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`message`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 4**: `super().__init__(message)`
- Nazwa **`super`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`message`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 6**: `class Kwadrat:`
- Słowo kluczowe **`class`**: Słowo kluczowe 'class' (klasa). Oznacza tworzenie nowego, złożonego typu danych (obiektu). To tak, jakbyś tworzył własną foremkę, z której potem będziesz 'wypiekać' konkretne obiekty (ciastka) o określonych cechach.
- Nazwa **`Kwadrat`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 7**: `def  __init__(self,x,y):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 8**: `self.x=x`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 9**: `self.y=y`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 10**: `def pole(self):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`pole`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 11**: `if self.x < 0 or self.y <0:`
- Słowo kluczowe **`if`**: Słowo kluczowe 'if' (jeśli). Rozpoczyna instrukcję warunkową. Komputer sprawdzi postawiony warunek - jeśli jest on prawdziwy, wykona kod pod spodem.
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`<`**: Znak mniejszości. Pyta: 'czy to po lewej jest mniejsze niż to po prawej?'.
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Słowo kluczowe **`or`**: Słowo 'or' (lub). Łączy dwa warunki. Całość jest prawdziwa, gdy PRZYNAJMNIEJ JEDEN z warunków jest prawdziwy.
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`<`**: Znak mniejszości. Pyta: 'czy to po lewej jest mniejsze niż to po prawej?'.
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 12**: `raise BadDimensionError("Złe wymiary")`
- Słowo kluczowe **`raise`**: Słowo kluczowe języka Python: 'raise'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`BadDimensionError`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Złe wymiary"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 13**: `else:`
- Słowo kluczowe **`else`**: Słowo kluczowe 'else' (w przeciwnym razie). Używane na samym końcu. Oznacza: 'Jeśli ŻADEN z wcześniejszych warunków nie był prawdziwy, wykonaj ostatecznie ten kod'.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 14**: `return self.x*self.y       #tu musi być self`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`*`**: Operator mnożenia (gwiazdka).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- **Komentarz `[ #tu musi być self ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 16**: `k1=Kwadrat(-2,2)`
- Nazwa **`k1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`Kwadrat`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`-`**: Operator odejmowania.
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 17**: `try:`
- Słowo kluczowe **`try`**: Słowo kluczowe 'try' (próbuj). Rozpoczyna niebezpieczny blok kodu, w którym komputer ma 'spróbować' wykonać operację, spodziewając się, że może pojawić się awaria/błąd.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 18**: `k=k1.pole()`
- Nazwa **`k`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`k1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`pole`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 19**: `except Exception as e:`
- Słowo kluczowe **`except`**: Słowo kluczowe 'except' (za wyjątkiem / przechwyć). Określa ratunek: co komputer ma awaryjnie zrobić, jeśli w bloku 'try' faktycznie wystąpił błąd. Zapobiega to gwałtownemu wyłączeniu się programu.
- Nazwa **`Exception`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`as`**: Słowo kluczowe języka Python: 'as'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`e`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 20**: `print(e.args)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`e`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`args`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 21**: `else:`
- Słowo kluczowe **`else`**: Słowo kluczowe 'else' (w przeciwnym razie). Używane na samym końcu. Oznacza: 'Jeśli ŻADEN z wcześniejszych warunków nie był prawdziwy, wykonaj ostatecznie ten kod'.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 22**: `print(k)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`k`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    #ValueError
    class BadDimensionError(ValueError):
        def __init__(self, message):
            super().__init__(message)
    
    class Kwadrat:
     def  __init__(self,x,y):
        self.x=x
        self.y=y
     def pole(self):
       if self.x < 0 or self.y <0:
          raise BadDimensionError("Złe wymiary")
       else:
        return self.x*self.y       #tu musi być self
    
    _k1=Kwadrat(-2,2)
    try:
     _k=_k1.pole()
    except Exception as e:
      print(e.args)
    else:
      print(_k)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `# kilka wyjątków`
- **Komentarz `[ # kilka wyjątków ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `try:`
- Słowo kluczowe **`try`**: Słowo kluczowe 'try' (próbuj). Rozpoczyna niebezpieczny blok kodu, w którym komputer ma 'spróbować' wykonać operację, spodziewając się, że może pojawić się awaria/błąd.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 3**: `x = int("abc")  # Spowoduje ValueError`
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`int`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"abc"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- **Komentarz `[ # Spowoduje ValueError ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 4**: `#y=1/0`
- **Komentarz `[ #y=1/0 ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 5**: `except ValueError:`
- Słowo kluczowe **`except`**: Słowo kluczowe 'except' (za wyjątkiem / przechwyć). Określa ratunek: co komputer ma awaryjnie zrobić, jeśli w bloku 'try' faktycznie wystąpił błąd. Zapobiega to gwałtownemu wyłączeniu się programu.
- Nazwa **`ValueError`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 6**: `print("Błąd: Nie można przekonwertować na liczbę.")`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Błąd: Nie można przekonwertować na liczbę."`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 7**: `except ZeroDivisionError:`
- Słowo kluczowe **`except`**: Słowo kluczowe 'except' (za wyjątkiem / przechwyć). Określa ratunek: co komputer ma awaryjnie zrobić, jeśli w bloku 'try' faktycznie wystąpił błąd. Zapobiega to gwałtownemu wyłączeniu się programu.
- Nazwa **`ZeroDivisionError`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 8**: `print("Błąd: Dzielenie przez zero.")`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Błąd: Dzielenie przez zero."`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 9**: `except FileNotFoundError:`
- Słowo kluczowe **`except`**: Słowo kluczowe 'except' (za wyjątkiem / przechwyć). Określa ratunek: co komputer ma awaryjnie zrobić, jeśli w bloku 'try' faktycznie wystąpił błąd. Zapobiega to gwałtownemu wyłączeniu się programu.
- Nazwa **`FileNotFoundError`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 10**: `print("Błąd: Plik nie istnieje.")`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Błąd: Plik nie istnieje."`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    # kilka wyjątków
    try:
        _x = int("abc")  # Spowoduje ValueError
        #y=1/0
    except ValueError:
        print("Błąd: Nie można przekonwertować na liczbę.")
    except ZeroDivisionError:
        print("Błąd: Dzielenie przez zero.")
    except FileNotFoundError:
        print("Błąd: Plik nie istnieje.")
    return

@app.cell
def _(mo):
    mo.md(r"""Obiekt wyjątku zawiera wiele informacji, które mogą pomóc w diagnozowaniu i rozwiązywaniu problemu, w tym:

typ wyjątku (BadDimensionError)
pełną ścieżkę do modułu i pliku, w którym został zgłoszony wyjątek
numer linii, w której został zgłoszony wyjątek
stos wywołań, czyli kolejność wywołania funkcji prowadząca do miejsca zgłoszenia wyjątku
Można wykorzystać te informacje do znalezienia źródła problemu i naprawienia go. Na przykład, patrząc na numer linii, można znaleźć miejsce w kodzie, gdzie wystąpił problem. Patrząc na stos wywołań, można znaleźć, która funkcja lub metoda była odpowiedzialna za wystąpienie wyjątku.

Aby wyświetlić więcej informacji o obiekcie wyjątku, można użyć funkcji traceback.print_exception() z modułu traceback. Ta funkcja wyświetla szczegółowe informacje o wyjątku, w tym stos wywołań, na standardowym strumieniu błędów.""")
    return

@app.cell
def _(mo):
    mo.md(r"""# Zadanie:

# Zbudować klasę Auto, wczytać dane: marka, rokp, cena, przebieg, typ (jedna linia, metoda input), zrobić obsługę wyjatków: rokp, cena, przebieg [liczby], marka, typ [dane z listy].""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `class Auto:`
- Słowo kluczowe **`class`**: Słowo kluczowe 'class' (klasa). Oznacza tworzenie nowego, złożonego typu danych (obiektu). To tak, jakbyś tworzył własną foremkę, z której potem będziesz 'wypiekać' konkretne obiekty (ciastka) o określonych cechach.
- Nazwa **`Auto`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 2**: `DOZWOLONE_MARKI = ["Toyota", "BMW", "Audi", "Ford"]`
- Nazwa **`DOZWOLONE_MARKI`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Tekst (String) **`"Toyota"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`"BMW"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`"Audi"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`"Ford"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 3**: `DOZWOLONE_TYPY = ["sedan", "suv", "hatchback", "kombi"]`
- Nazwa **`DOZWOLONE_TYPY`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Tekst (String) **`"sedan"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`"suv"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`"hatchback"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`"kombi"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 5**: `def __init__(self, marka, rokp, cena, przebieg, typ):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`marka`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`rokp`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`cena`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`przebieg`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`typ`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 6**: `self.marka = marka`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`marka`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`marka`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 7**: `self.rokp = rokp`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`rokp`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`rokp`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 8**: `self.cena = cena`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`cena`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cena`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 9**: `self.przebieg = przebieg`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`przebieg`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`przebieg`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 10**: `self.typ = typ`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`typ`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`typ`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 12**: `def __str__(self):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__str__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 13**: `return f"{self.marka}, rok: {self.rokp}, cena: {self.cena}, przebieg: {self.przebieg}, typ: {self.typ}"`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Tekst (String) **`f"{self.marka}, rok: {self.rokp}, cena: {self.cena}, przebieg: {self.przebieg}, typ: {self.typ}"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 16**: `while True:`
- Słowo kluczowe **`while`**: Słowo kluczowe 'while' (dopóki). Rozpoczyna pętlę warunkową. Komputer będzie powtarzał kod pod spodem TAK DŁUGO, dopóki sprawdzany warunek jest wciąż prawdziwy.
- Słowo kluczowe **`True`**: Wartość logiczna 'True' (Prawda). Oznacza stan włączenia, potwierdzenie, że coś jest zgodne z prawdą (w pamięci komputera to jedynka: 1).
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 17**: `try:`
- Słowo kluczowe **`try`**: Słowo kluczowe 'try' (próbuj). Rozpoczyna niebezpieczny blok kodu, w którym komputer ma 'spróbować' wykonać operację, spodziewając się, że może pojawić się awaria/błąd.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 18**: `dane = input("Podaj: marka rok cena przebieg typ: ").split()`
- Nazwa **`dane`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`input`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Podaj: marka rok cena przebieg typ: "`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`split`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 20**: `if len(dane) != 5:`
- Słowo kluczowe **`if`**: Słowo kluczowe 'if' (jeśli). Rozpoczyna instrukcję warunkową. Komputer sprawdzi postawiony warunek - jeśli jest on prawdziwy, wykona kod pod spodem.
- Nazwa **`len`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`dane`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`!=`**: Operator 'różne od'. Sprawdza czy dwie rzeczy NIE SĄ takie same.
- Liczba **`5`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 21**: `raise ValueError("Musisz podać dokładnie 5 wartości")`
- Słowo kluczowe **`raise`**: Słowo kluczowe języka Python: 'raise'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`ValueError`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Musisz podać dokładnie 5 wartości"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 23**: `marka, rokp, cena, przebieg, typ = dane`
- Nazwa **`marka`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`rokp`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`cena`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`przebieg`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`typ`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`dane`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 25**: `# konwersja liczb`
- **Komentarz `[ # konwersja liczb ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 26**: `rokp = int(rokp)`
- Nazwa **`rokp`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`int`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`rokp`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 27**: `cena = float(cena)`
- Nazwa **`cena`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`float`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`cena`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 28**: `przebieg = int(przebieg)`
- Nazwa **`przebieg`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`int`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`przebieg`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 30**: `# walidacja marki`
- **Komentarz `[ # walidacja marki ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 31**: `if marka not in Auto.DOZWOLONE_MARKI:`
- Słowo kluczowe **`if`**: Słowo kluczowe 'if' (jeśli). Rozpoczyna instrukcję warunkową. Komputer sprawdzi postawiony warunek - jeśli jest on prawdziwy, wykona kod pod spodem.
- Nazwa **`marka`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`not`**: Słowo 'not' (nie). Odwraca logiczną wartość na przeciwną. Z Prawdy robi Fałsz, a z Fałszu Prawdę.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`Auto`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`DOZWOLONE_MARKI`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 32**: `raise ValueError(f"Nieznana marka! Dozwolone: {Auto.DOZWOLONE_MARKI}")`
- Słowo kluczowe **`raise`**: Słowo kluczowe języka Python: 'raise'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`ValueError`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`f"Nieznana marka! Dozwolone: {Auto.DOZWOLONE_MARKI}"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 34**: `# walidacja typu`
- **Komentarz `[ # walidacja typu ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 35**: `if typ not in Auto.DOZWOLONE_TYPY:`
- Słowo kluczowe **`if`**: Słowo kluczowe 'if' (jeśli). Rozpoczyna instrukcję warunkową. Komputer sprawdzi postawiony warunek - jeśli jest on prawdziwy, wykona kod pod spodem.
- Nazwa **`typ`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`not`**: Słowo 'not' (nie). Odwraca logiczną wartość na przeciwną. Z Prawdy robi Fałsz, a z Fałszu Prawdę.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`Auto`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`DOZWOLONE_TYPY`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 36**: `raise ValueError(f"Nieznany typ! Dozwolone: {Auto.DOZWOLONE_TYPY}")`
- Słowo kluczowe **`raise`**: Słowo kluczowe języka Python: 'raise'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`ValueError`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`f"Nieznany typ! Dozwolone: {Auto.DOZWOLONE_TYPY}"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 38**: `auto = Auto(marka, rokp, cena, przebieg, typ)`
- Nazwa **`auto`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`Auto`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`marka`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`rokp`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`cena`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`przebieg`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`typ`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 39**: `print("Dodano auto:")`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Dodano auto:"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 40**: `print(auto)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`auto`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 41**: `break`
- Słowo kluczowe **`break`**: Słowo kluczowe języka Python: 'break'. Jest to wbudowane polecenie o specjalnym znaczeniu.

#### 👉 **Linia 43**: `except ValueError as e:`
- Słowo kluczowe **`except`**: Słowo kluczowe 'except' (za wyjątkiem / przechwyć). Określa ratunek: co komputer ma awaryjnie zrobić, jeśli w bloku 'try' faktycznie wystąpił błąd. Zapobiega to gwałtownemu wyłączeniu się programu.
- Nazwa **`ValueError`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`as`**: Słowo kluczowe języka Python: 'as'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`e`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 44**: `print("Błąd:", e)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Błąd:"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`e`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 45**: `except Exception:`
- Słowo kluczowe **`except`**: Słowo kluczowe 'except' (za wyjątkiem / przechwyć). Określa ratunek: co komputer ma awaryjnie zrobić, jeśli w bloku 'try' faktycznie wystąpił błąd. Zapobiega to gwałtownemu wyłączeniu się programu.
- Nazwa **`Exception`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 46**: `print("Nieprawidłowe dane wejściowe!")`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Nieprawidłowe dane wejściowe!"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    class Auto:
        _DOZWOLONE_MARKI = ["Toyota", "BMW", "Audi", "Ford"]
        _DOZWOLONE_TYPY = ["sedan", "suv", "hatchback", "kombi"]
    
        def __init__(self, marka, _rokp, _cena, _przebieg, typ):
            self.marka = marka
            self._rokp = _rokp
            self._cena = _cena
            self._przebieg = _przebieg
            self.typ = typ
    
        def __str__(self):
            return f"{self.marka}, rok: {self._rokp}, _cena: {self._cena}, _przebieg: {self._przebieg}, typ: {self.typ}"
    
    
    while True:
        try:
            _dane = input("Podaj: marka rok _cena _przebieg typ: ").split()
    
            if len(_dane) != 5:
                raise ValueError("Musisz podać dokładnie 5 wartości")
    
            marka, _rokp, _cena, _przebieg, typ = _dane
    
            # konwersja liczb
            _rokp = int(_rokp)
            _cena = float(_cena)
            _przebieg = int(_przebieg)
    
            # walidacja marki
            if marka not in Auto._DOZWOLONE_MARKI:
                raise ValueError(f"Nieznana marka! Dozwolone: {Auto._DOZWOLONE_MARKI}")
    
            # walidacja typu
            if typ not in Auto._DOZWOLONE_TYPY:
                raise ValueError(f"Nieznany typ! Dozwolone: {Auto._DOZWOLONE_TYPY}")
    
            _auto = Auto(marka, _rokp, _cena, _przebieg, typ)
            print("Dodano _auto:")
            print(_auto)
            break
    
        except ValueError as e:
            print("Błąd:", e)
        except Exception:
            print("Nieprawidłowe _dane wejściowe!")
    return

@app.cell
def _(mo):
    mo.md(r"""# Zbować listę samochodów, posortować listę według wybranego kryterium np. rokp, cena, typ""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `class Auto:`
- Słowo kluczowe **`class`**: Słowo kluczowe 'class' (klasa). Oznacza tworzenie nowego, złożonego typu danych (obiektu). To tak, jakbyś tworzył własną foremkę, z której potem będziesz 'wypiekać' konkretne obiekty (ciastka) o określonych cechach.
- Nazwa **`Auto`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 2**: `DOZWOLONE_MARKI = ["Toyota", "BMW", "Audi", "Ford"]`
- Nazwa **`DOZWOLONE_MARKI`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Tekst (String) **`"Toyota"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`"BMW"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`"Audi"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`"Ford"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 3**: `DOZWOLONE_TYPY = ["sedan", "suv", "hatchback", "kombi"]`
- Nazwa **`DOZWOLONE_TYPY`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Tekst (String) **`"sedan"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`"suv"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`"hatchback"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`"kombi"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 4**: `lista_aut = []`
- Nazwa **`lista_aut`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 5**: `def __init__(self, marka, rokp, cena):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__init__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`marka`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`rokp`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`cena`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 6**: `self.marka = marka`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`marka`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`marka`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 7**: `self.rokp = rokp`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`rokp`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`rokp`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 8**: `self.cena = cena`
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`cena`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`cena`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 11**: `def __str__(self):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`__str__`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`self`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 12**: `return f"{self.marka}, rok: {self.rokp}, cena: {self.cena}"`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Tekst (String) **`f"{self.marka}, rok: {self.rokp}, cena: {self.cena}"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 14**: `# Tu zaczyna się program`
- **Komentarz `[ # Tu zaczyna się program ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 15**: `lista_aut = [Auto("BMW",2022,12000),Auto("Ford",2010,10000),Auto("Audi",1990,8000)]`
- Nazwa **`lista_aut`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Nazwa **`Auto`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"BMW"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`2022`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`12000`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`Auto`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Ford"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`2010`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`10000`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`Auto`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Audi"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`1990`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`8000`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 16**: `lista_aut.sort(key=lambda x: x.cena)`
- Nazwa **`lista_aut`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`sort`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`key`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Słowo kluczowe **`lambda`**: Słowo kluczowe języka Python: 'lambda'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`cena`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 18**: `#lista_aut.sort(key=lambda x: [-ord(c) for c in x.marka])`
- **Komentarz `[ #lista_aut.sort(key=lambda x: [-ord(c) for c in x.marka]) ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 19**: `for auto in lista_aut:`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`auto`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`lista_aut`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 20**: `print(auto)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`auto`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    class Auto:
        _DOZWOLONE_MARKI = ["Toyota", "BMW", "Audi", "Ford"]
        _DOZWOLONE_TYPY = ["sedan", "suv", "hatchback", "kombi"]
        _lista_aut = []
        def __init__(self, marka, rokp, cena):
            self.marka = marka
            self.rokp = rokp
            self.cena = cena
    
    
        def __str__(self):
            return f"{self.marka}, rok: {self.rokp}, cena: {self.cena}"
    
    # Tu zaczyna się program
    _lista_aut = [Auto("BMW",2022,12000),Auto("Ford",2010,10000),Auto("Audi",1990,8000)]
    _lista_aut.sort(key=lambda x: x.cena)
    
    #_lista_aut.sort(key=lambda x: [-ord(c) for c in x.marka])
    for auto in _lista_aut:
        print(auto)
    return

if __name__ == "__main__":
    app.run()