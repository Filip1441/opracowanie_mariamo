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
    mo.md(r"""# Wykład 2: Kolekcje i Logika""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `a="100"`
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`"100"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 2**: `b="200"`
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`"200"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 3**: `print(a+b)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _a="100"
    _b="200"
    print(_a+_b)
    return

@app.cell
def _(mo):
    mo.md(r"""Operacje w klasie str



*   len -  określenie długości
*   pobieranie konkretnego znaku, jest takie jak pobieranie elementu tablicy


""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `a="abcd"`
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`"abcd"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 2**: `print("długość ",len(a))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"długość "`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`len`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 3**: `print("drugi znak ",a[3])`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"drugi znak "`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _a="abcd"
    print("długość ",len(_a))
    print("drugi znak ",_a[3])
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `# pobieranie fragmentu`
- **Komentarz `[ # pobieranie fragmentu ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 3**: `a="abcd"`
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`"abcd"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 4**: `b=a[1:3]`
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 5**: `print(b)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    # pobieranie fragmentu
    
    _a="abcd"
    _b=_a[1:3]
    print(_b)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `a="abcdefgh"`
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`"abcdefgh"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 2**: `b=a[0:-2]`
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Znak **`-`**: Operator odejmowania.
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 3**: `print(b)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _a="abcdefgh"
    _b=_a[0:-2]
    print(_b)
    return

@app.cell
def _(mo):
    mo.md(r"""Rzutowanie typów sczególnie ze string na liczby jest łatwiejsze niż np. w Javie.
""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `a="100"`
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`"100"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 2**: `b="200"`
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`"200"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 3**: `print(a+b)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 4**: `print(int(a)+int(b))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`int`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Nazwa **`int`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _a="100"
    _b="200"
    print(_a+_b)
    print(int(_a)+int(_b))
    return

@app.cell
def _(mo):
    mo.md(r"""Sprawdzenie typu""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `a="100"`
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`"100"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 2**: `b=100`
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`100`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 3**: `print(type(a))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`type`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 4**: `print(type(b))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`type`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _a="100"
    _b=100
    print(type(_a))
    print(type(_b))
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `a=100`
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`100`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 2**: `if isinstance(a,int): print("int")`
- Słowo kluczowe **`if`**: Słowo kluczowe 'if' (jeśli). Rozpoczyna instrukcję warunkową. Komputer sprawdzi postawiony warunek - jeśli jest on prawdziwy, wykona kod pod spodem.
- Nazwa **`isinstance`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`int`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"int"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 3**: `else: print("not int")`
- Słowo kluczowe **`else`**: Słowo kluczowe 'else' (w przeciwnym razie). Używane na samym końcu. Oznacza: 'Jeśli ŻADEN z wcześniejszych warunków nie był prawdziwy, wykonaj ostatecznie ten kod'.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"not int"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _a=100
    if isinstance(_a,int): print("int")
    else: print("not int")
    return

@app.cell
def _(mo):
    mo.md(r"""# Kolekcje

## Listy

Przypominają tablice z innych języków lub wektory z C++. Mogą skłądać się z elementów różnego typu.""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `lista = [7, 2, 5, 4]`
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Liczba **`7`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`5`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`4`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 2**: `print(lista)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _lista = [7, 2, 5, 4]
    print(_lista)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `lista_1 = [1, 'a', 2, 'b']`
- Nazwa **`lista_1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'a'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'b'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 2**: `print(lista_1)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`lista_1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 3**: `print(lista_1[0])`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`lista_1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 4**: `print(lista_1[-1])  # Python umożliwia liczenie elementów od końca`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`lista_1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Znak **`-`**: Operator odejmowania.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- **Komentarz `[ # Python umożliwia liczenie elementów od końca ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 5**: `print(lista_1[1:3])`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`lista_1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 6**: `print(len(lista_1))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`len`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`lista_1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _lista_1 = [1, 'a', 2, 'b']
    print(_lista_1)
    print(_lista_1[0])
    print(_lista_1[-1])  # Python umożliwia liczenie elementów od końca
    print(_lista_1[1:3])
    print(len(_lista_1))
    return

@app.cell
def _(mo):
    mo.md(r"""Dodanie elementu do listy""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `lista_1 = [1, 'a', 2, 'b']`
- Nazwa **`lista_1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'a'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'b'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 2**: `lista_1.append(3)`
- Nazwa **`lista_1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`append`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 3**: `print(lista_1)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`lista_1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _lista_1 = [1, 'a', 2, 'b']
    _lista_1.append(3)
    print(_lista_1)
    return

@app.cell
def _(mo):
    mo.md(r"""Połączenie list""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `lista_1 = [1, 'a', 2, 'b']`
- Nazwa **`lista_1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'a'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'b'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 2**: `lista = [3, 'x', 2, 'b']`
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'x'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'b'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 3**: `lista_1.extend(lista)`
- Nazwa **`lista_1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`extend`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 4**: `print(lista_1)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`lista_1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _lista_1 = [1, 'a', 2, 'b']
    _lista = [3, 'x', 2, 'b']
    _lista_1.extend(_lista)
    print(_lista_1)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `lista_1 = [1, 'a', 2, 'b']`
- Nazwa **`lista_1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'a'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'b'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 2**: `lista = [3, 'x', 2, 'b']`
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'x'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'b'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 3**: `lista_1 += lista`
- Nazwa **`lista_1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`+=`**: Znak interpunkcyjny lub operator: '+='. Służy do organizacji struktury kodu.
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 4**: `print(lista_1)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`lista_1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _lista_1 = [1, 'a', 2, 'b']
    _lista = [3, 'x', 2, 'b']
    _lista_1 += _lista
    print(_lista_1)
    return

@app.cell
def _(mo):
    mo.md(r"""Sortowanie""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `lista = ['x', 'u', 'b']`
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Tekst (String) **`'x'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'u'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'b'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 2**: `lista.sort()`
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`sort`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 3**: `print(lista)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _lista = ['x', 'u', 'b']
    _lista.sort()
    print(_lista)
    return

@app.cell
def _(mo):
    mo.md(r"""Zmiana kolejności""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `lista = ['z', 'x', 'u', 'b']`
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Tekst (String) **`'z'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'x'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'u'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'b'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 2**: `lista.reverse()`
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`reverse`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 3**: `print(lista)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _lista = ['z', 'x', 'u', 'b']
    _lista.reverse()
    print(_lista)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `lista = ['z', 'x', 'u', 'b']`
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Tekst (String) **`'z'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'x'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'u'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'b'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 2**: `lista.pop(2)`
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`pop`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 3**: `print(lista)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _lista = ['z', 'x', 'u', 'b']
    _lista.pop(2)
    print(_lista)
    return

@app.cell
def _(mo):
    mo.md(r"""### Przypisanie wartości

Jeśli a i b są listami, to instrukcja a = b powoduje przypisanie referencji, zmiany listy a będą powodowały zmiany listy b i odwrotnie. Jeśli chcemy kopiować listy, to uzywamy a = b[:]
_Instrukcja == porównuje zawartość, instrukcja is sprawdza referencję.""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `a = [1, 2, 3, 4, 5]`
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`4`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`5`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 2**: `b = a  #  przypisanie referencji`
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- **Komentarz `[ #  przypisanie referencji ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 3**: `print(a == b)  # porównanie wartości`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`==`**: Podwójny znak równości to 'operator porównania'. Komputer sprawdza, czy to co po lewej jest DOKŁADNIE TAKIE SAMO jak to po prawej. Zwraca odpowiedź Prawda (True) lub Fałsz (False).
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- **Komentarz `[ # porównanie wartości ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 4**: `print(a is b)  # porównanie referencji`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`is`**: Słowo kluczowe języka Python: 'is'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- **Komentarz `[ # porównanie referencji ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.
""")
    return
@app.cell
def _():
    _a = [1, 2, 3, 4, 5]
    _b = _a  #  przypisanie referencji
    print(_a == _b)  # porównanie wartości
    print(_a is _b)  # porównanie referencji
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `b = a[:]  #kopiowanie tablic, powstanie nowa tablica`
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- **Komentarz `[ #kopiowanie tablic, powstanie nowa tablica ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `print(a == b)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`==`**: Podwójny znak równości to 'operator porównania'. Komputer sprawdza, czy to co po lewej jest DOKŁADNIE TAKIE SAMO jak to po prawej. Zwraca odpowiedź Prawda (True) lub Fałsz (False).
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 3**: `print(a is b)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`is`**: Słowo kluczowe języka Python: 'is'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _b = a[:]  #kopiowanie tablic, powstanie nowa tablica
    print(a == _b)
    print(a is _b)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `print(a[0:3])`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 2**: `print(a[0:-2])`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Znak **`-`**: Operator odejmowania.
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 3**: `print(a[-3:-1])`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Znak **`-`**: Operator odejmowania.
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Znak **`-`**: Operator odejmowania.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    print(a[0:3])
    print(a[0:-2])
    print(a[-3:-1])
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `print(list(range(1,5,2)))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`list`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`range`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`5`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    print(list(range(1,5,2)))
    return

@app.cell
def _(mo):
    mo.md(r"""## Krotki (ang. tuple)

Przypominają listy, ale są niezmienne (nie mozna zmieniać ich elementów, nie są jednak odpwiednikiem stałych z C, bo jako całość mogą ulec zmianie).""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `ip_address = ('10.20.30.40', 8080)`
- Nazwa **`ip_address`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'10.20.30.40'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`8080`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 2**: `print(ip_address)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`ip_address`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _ip_address = ('10.20.30.40', 8080)
    print(_ip_address)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `ip_address = ('10.20.30.40', 8080)`
- Nazwa **`ip_address`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'10.20.30.40'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`8080`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 2**: `print(ip_address[0])`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`ip_address`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _ip_address = ('10.20.30.40', 8080)
    print(_ip_address[0])
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `#próba zmiany, błąd`
- **Komentarz `[ #próba zmiany, błąd ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `ip_address = ('10.20.30.40', 8080)`
- Nazwa **`ip_address`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'10.20.30.40'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`8080`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 3**: `ip_address[0] = '10.20.30.250'`
- Nazwa **`ip_address`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'10.20.30.250'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
""")
    return
@app.cell
def _():
    #próba zmiany, błąd
    _ip_address = ('10.20.30.40', 8080)
    _ip_address[0] = '10.20.30.250'
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `# a to jest poprawne`
- **Komentarz `[ # a to jest poprawne ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `ip_address1 = ('10.20.30.40', 8080)`
- Nazwa **`ip_address1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'10.20.30.40'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`8080`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 3**: `ip_address1 = ('10.20.30.50', 8082)`
- Nazwa **`ip_address1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'10.20.30.50'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`8082`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 4**: `print(ip_address1)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`ip_address1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    # a to jest poprawne
    _ip_address1 = ('10.20.30.40', 8080)
    _ip_address1 = ('10.20.30.50', 8082)
    print(_ip_address1)
    return

@app.cell
def _(mo):
    mo.md(r"""## Zbiory

Zawieraja elementy unikalne i nie są uporządkowane.""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `duze_miasta = {'Warszawa', 'Kraków', 'Gdańsk'}`
- Nazwa **`duze_miasta`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`{`**: Lewy nawias klamrowy. Rozpoczyna słownik (zbiór par 'klucz: wartość') lub zbiór unikalnych elementów (set).
- Tekst (String) **`'Warszawa'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'Kraków'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'Gdańsk'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`}`**: Prawy nawias klamrowy. Kończy słownik lub zbiór.

#### 👉 **Linia 2**: `miasta_mazowsza = {'Radom', 'Płock', 'Warszawa'}`
- Nazwa **`miasta_mazowsza`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`{`**: Lewy nawias klamrowy. Rozpoczyna słownik (zbiór par 'klucz: wartość') lub zbiór unikalnych elementów (set).
- Tekst (String) **`'Radom'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'Płock'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'Warszawa'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`}`**: Prawy nawias klamrowy. Kończy słownik lub zbiór.

#### 👉 **Linia 3**: `stolice_europy = {'Paryż', 'Berlin', 'Warszawa'}`
- Nazwa **`stolice_europy`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`{`**: Lewy nawias klamrowy. Rozpoczyna słownik (zbiór par 'klucz: wartość') lub zbiór unikalnych elementów (set).
- Tekst (String) **`'Paryż'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'Berlin'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'Warszawa'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`}`**: Prawy nawias klamrowy. Kończy słownik lub zbiór.
""")
    return
@app.cell
def _():
    _duze_miasta = {'Warszawa', 'Kraków', 'Gdańsk'}
    _miasta_mazowsza = {'Radom', 'Płock', 'Warszawa'}
    _stolice_europy = {'Paryż', 'Berlin', 'Warszawa'}
    return

@app.cell
def _(mo):
    mo.md(r"""Iloczyn zbiorów
""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `duze_miasta = {'Warszawa', 'Kraków', 'Gdańsk'}`
- Nazwa **`duze_miasta`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`{`**: Lewy nawias klamrowy. Rozpoczyna słownik (zbiór par 'klucz: wartość') lub zbiór unikalnych elementów (set).
- Tekst (String) **`'Warszawa'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'Kraków'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'Gdańsk'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`}`**: Prawy nawias klamrowy. Kończy słownik lub zbiór.

#### 👉 **Linia 2**: `miasta_mazowsza = {'Radom', 'Płock', 'Warszawa'}`
- Nazwa **`miasta_mazowsza`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`{`**: Lewy nawias klamrowy. Rozpoczyna słownik (zbiór par 'klucz: wartość') lub zbiór unikalnych elementów (set).
- Tekst (String) **`'Radom'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'Płock'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'Warszawa'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`}`**: Prawy nawias klamrowy. Kończy słownik lub zbiór.

#### 👉 **Linia 3**: `stolice_europy = {'Paryż', 'Berlin', 'Warszawa'}`
- Nazwa **`stolice_europy`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`{`**: Lewy nawias klamrowy. Rozpoczyna słownik (zbiór par 'klucz: wartość') lub zbiór unikalnych elementów (set).
- Tekst (String) **`'Paryż'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'Berlin'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'Warszawa'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`}`**: Prawy nawias klamrowy. Kończy słownik lub zbiór.

#### 👉 **Linia 4**: `duze_miasta_mazowsza = duze_miasta.intersection(miasta_mazowsza)`
- Nazwa **`duze_miasta_mazowsza`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`duze_miasta`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`intersection`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`miasta_mazowsza`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 5**: `print(duze_miasta_mazowsza)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`duze_miasta_mazowsza`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _duze_miasta = {'Warszawa', 'Kraków', 'Gdańsk'}
    _miasta_mazowsza = {'Radom', 'Płock', 'Warszawa'}
    _stolice_europy = {'Paryż', 'Berlin', 'Warszawa'}
    _duze_miasta_mazowsza = _duze_miasta.intersection(_miasta_mazowsza)
    print(_duze_miasta_mazowsza)
    return

@app.cell
def _(mo):
    mo.md(r"""Różnica zbiorów""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `duze_miasta = {'Warszawa', 'Kraków', 'Gdańsk'}`
- Nazwa **`duze_miasta`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`{`**: Lewy nawias klamrowy. Rozpoczyna słownik (zbiór par 'klucz: wartość') lub zbiór unikalnych elementów (set).
- Tekst (String) **`'Warszawa'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'Kraków'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'Gdańsk'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`}`**: Prawy nawias klamrowy. Kończy słownik lub zbiór.

#### 👉 **Linia 2**: `miasta_mazowsza = {'Radom', 'Płock', 'Warszawa'}`
- Nazwa **`miasta_mazowsza`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`{`**: Lewy nawias klamrowy. Rozpoczyna słownik (zbiór par 'klucz: wartość') lub zbiór unikalnych elementów (set).
- Tekst (String) **`'Radom'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'Płock'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'Warszawa'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`}`**: Prawy nawias klamrowy. Kończy słownik lub zbiór.

#### 👉 **Linia 3**: `stolice_europy = {'Paryż', 'Berlin', 'Warszawa'}`
- Nazwa **`stolice_europy`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`{`**: Lewy nawias klamrowy. Rozpoczyna słownik (zbiór par 'klucz: wartość') lub zbiór unikalnych elementów (set).
- Tekst (String) **`'Paryż'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'Berlin'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'Warszawa'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`}`**: Prawy nawias klamrowy. Kończy słownik lub zbiór.

#### 👉 **Linia 4**: `male_miasta_mazowsza = miasta_mazowsza.difference(duze_miasta)`
- Nazwa **`male_miasta_mazowsza`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`miasta_mazowsza`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`difference`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`duze_miasta`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 5**: `print(male_miasta_mazowsza)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`male_miasta_mazowsza`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _duze_miasta = {'Warszawa', 'Kraków', 'Gdańsk'}
    _miasta_mazowsza = {'Radom', 'Płock', 'Warszawa'}
    _stolice_europy = {'Paryż', 'Berlin', 'Warszawa'}
    _male_miasta_mazowsza = _miasta_mazowsza.difference(_duze_miasta)
    print(_male_miasta_mazowsza)
    return

@app.cell
def _(mo):
    mo.md(r"""Sprawdzenie podzbiorów i rozłączności""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `duze_miasta = {'Warszawa', 'Kraków', 'Gdańsk'}`
- Nazwa **`duze_miasta`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`{`**: Lewy nawias klamrowy. Rozpoczyna słownik (zbiór par 'klucz: wartość') lub zbiór unikalnych elementów (set).
- Tekst (String) **`'Warszawa'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'Kraków'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'Gdańsk'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`}`**: Prawy nawias klamrowy. Kończy słownik lub zbiór.

#### 👉 **Linia 2**: `miasta_mazowsza = {'Radom', 'Płock', 'Warszawa'}`
- Nazwa **`miasta_mazowsza`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`{`**: Lewy nawias klamrowy. Rozpoczyna słownik (zbiór par 'klucz: wartość') lub zbiór unikalnych elementów (set).
- Tekst (String) **`'Radom'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'Płock'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'Warszawa'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`}`**: Prawy nawias klamrowy. Kończy słownik lub zbiór.

#### 👉 **Linia 3**: `stolice_europy = {'Paryż', 'Berlin', 'Warszawa'}`
- Nazwa **`stolice_europy`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`{`**: Lewy nawias klamrowy. Rozpoczyna słownik (zbiór par 'klucz: wartość') lub zbiór unikalnych elementów (set).
- Tekst (String) **`'Paryż'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'Berlin'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'Warszawa'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`}`**: Prawy nawias klamrowy. Kończy słownik lub zbiór.

#### 👉 **Linia 4**: `male_miasta_mazowsza = miasta_mazowsza.difference(duze_miasta)`
- Nazwa **`male_miasta_mazowsza`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`miasta_mazowsza`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`difference`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`duze_miasta`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 5**: `print(duze_miasta_mazowsza.issubset(stolice_europy))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`duze_miasta_mazowsza`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`issubset`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`stolice_europy`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 6**: `print(male_miasta_mazowsza.isdisjoint(stolice_europy))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`male_miasta_mazowsza`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`isdisjoint`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`stolice_europy`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _duze_miasta = {'Warszawa', 'Kraków', 'Gdańsk'}
    _miasta_mazowsza = {'Radom', 'Płock', 'Warszawa'}
    _stolice_europy = {'Paryż', 'Berlin', 'Warszawa'}
    _male_miasta_mazowsza = _miasta_mazowsza.difference(_duze_miasta)
    print(duze_miasta_mazowsza.issubset(_stolice_europy))
    print(_male_miasta_mazowsza.isdisjoint(_stolice_europy))
    return

@app.cell
def _(mo):
    mo.md(r"""Sprawdzanie przynależności elementu do zbioru (uwaga - ta sama składnia działa też dla innych kolekcji)""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `stolice_europy = {'Paryż', 'Berlin', 'Warszawa'}`
- Nazwa **`stolice_europy`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`{`**: Lewy nawias klamrowy. Rozpoczyna słownik (zbiór par 'klucz: wartość') lub zbiór unikalnych elementów (set).
- Tekst (String) **`'Paryż'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'Berlin'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'Warszawa'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`}`**: Prawy nawias klamrowy. Kończy słownik lub zbiór.

#### 👉 **Linia 2**: `print('Berlin' in stolice_europy)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'Berlin'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`stolice_europy`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _stolice_europy = {'Paryż', 'Berlin', 'Warszawa'}
    print('Berlin' in _stolice_europy)
    return

@app.cell
def _(mo):
    mo.md(r"""Sprawdzenia nieobecności elementu w zbiorze najlepiej dokonać przez operator not in:""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `stolice_europy = {'Paryż', 'Berlin', 'Warszawa'}`
- Nazwa **`stolice_europy`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`{`**: Lewy nawias klamrowy. Rozpoczyna słownik (zbiór par 'klucz: wartość') lub zbiór unikalnych elementów (set).
- Tekst (String) **`'Paryż'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'Berlin'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'Warszawa'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`}`**: Prawy nawias klamrowy. Kończy słownik lub zbiór.

#### 👉 **Linia 2**: `print('Radom' not in stolice_europy)  # Zalecane`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'Radom'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Słowo kluczowe **`not`**: Słowo 'not' (nie). Odwraca logiczną wartość na przeciwną. Z Prawdy robi Fałsz, a z Fałszu Prawdę.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`stolice_europy`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- **Komentarz `[ # Zalecane ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 3**: `print(not 'Radom' in stolice_europy)  # Niezalecane, ale też działa`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Słowo kluczowe **`not`**: Słowo 'not' (nie). Odwraca logiczną wartość na przeciwną. Z Prawdy robi Fałsz, a z Fałszu Prawdę.
- Tekst (String) **`'Radom'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`stolice_europy`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- **Komentarz `[ # Niezalecane, ale też działa ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.
""")
    return
@app.cell
def _():
    _stolice_europy = {'Paryż', 'Berlin', 'Warszawa'}
    print('Radom' not in _stolice_europy)  # Zalecane
    print(not 'Radom' in _stolice_europy)  # Niezalecane, ale też działa
    return

@app.cell
def _(mo):
    mo.md(r"""Rozmiar zbioru (ponownie - ta sama składnia dla innych kolekcji)""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `miasta_mazowsza = {'Radom', 'Płock', 'Warszawa'}`
- Nazwa **`miasta_mazowsza`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`{`**: Lewy nawias klamrowy. Rozpoczyna słownik (zbiór par 'klucz: wartość') lub zbiór unikalnych elementów (set).
- Tekst (String) **`'Radom'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'Płock'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'Warszawa'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`}`**: Prawy nawias klamrowy. Kończy słownik lub zbiór.

#### 👉 **Linia 2**: `print(len(miasta_mazowsza))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`len`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`miasta_mazowsza`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _miasta_mazowsza = {'Radom', 'Płock', 'Warszawa'}
    print(len(_miasta_mazowsza))
    return

@app.cell
def _(mo):
    mo.md(r"""## Słowniki

Słownik to zbiór par klucz-wartość.""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `ludnosc = {'Warszawa': 1777972,`
- Nazwa **`ludnosc`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`{`**: Lewy nawias klamrowy. Rozpoczyna słownik (zbiór par 'klucz: wartość') lub zbiór unikalnych elementów (set).
- Tekst (String) **`'Warszawa'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Liczba **`1777972`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).

#### 👉 **Linia 2**: `'Radom': 213715,`
- Tekst (String) **`'Radom'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Liczba **`213715`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).

#### 👉 **Linia 3**: `'Płock': 327027}`
- Tekst (String) **`'Płock'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Liczba **`327027`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`}`**: Prawy nawias klamrowy. Kończy słownik lub zbiór.

#### 👉 **Linia 4**: `print(ludnosc.keys())`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`ludnosc`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`keys`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 5**: `print(ludnosc.values())`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`ludnosc`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`values`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 6**: `print(ludnosc['Warszawa'])`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`ludnosc`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Tekst (String) **`'Warszawa'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _ludnosc = {'Warszawa': 1777972,
               'Radom': 213715,
               'Płock': 327027}
    print(_ludnosc.keys())
    print(_ludnosc.values())
    print(_ludnosc['Warszawa'])
    return

@app.cell
def _(mo):
    mo.md(r"""**Zmiana zmiennych powoduje zarezerwowanie nowego miejsca w pamięci**""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `a="dane"`
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`"dane"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 2**: `print(type(a),"  ",id(a))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`type`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`"  "`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`id`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 3**: `a+="  test"`
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`+=`**: Znak interpunkcyjny lub operator: '+='. Służy do organizacji struktury kodu.
- Tekst (String) **`"  test"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 4**: `print(type(a),"  ",id(a))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`type`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`"  "`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`id`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _a="dane"
    print(type(_a),"  ",id(_a))
    _a+="  test"
    print(type(_a),"  ",id(_a))
    return

@app.cell
def _(mo):
    mo.md(r"""## Quiz""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `# Jaki będzie wynik działania kodu:`
- **Komentarz `[ # Jaki będzie wynik działania kodu: ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `aTuple = (1, 'Jhon', 1+3j)`
- Nazwa **`aTuple`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'Jhon'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Liczba **`3j`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 3**: `print(type(aTuple[2:3]))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`type`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`aTuple`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    # Jaki będzie wynik działania kodu:
    _aTuple = (1, 'Jhon', 1+3j)
    print(type(_aTuple[2:3]))
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `# Jaki będzie wynik działania kodu:`
- **Komentarz `[ # Jaki będzie wynik działania kodu: ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `print(bool(0.0), bool(3.14159), bool(-3), bool(1.0+1j))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`bool`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`0.0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`bool`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`3.14159`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`bool`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`-`**: Operator odejmowania.
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`bool`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`1.0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Liczba **`1j`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    # Jaki będzie wynik działania kodu:
    print(bool(0.0), bool(3.14159), bool(-3), bool(1.0+1j))
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `print(type(10))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`type`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`10`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    print(type(10))
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `print(type({}) is set)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`type`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`{`**: Lewy nawias klamrowy. Rozpoczyna słownik (zbiór par 'klucz: wartość') lub zbiór unikalnych elementów (set).
- Znak **`}`**: Prawy nawias klamrowy. Kończy słownik lub zbiór.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Słowo kluczowe **`is`**: Słowo kluczowe języka Python: 'is'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`set`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 2**: `print(type({}))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`type`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`{`**: Lewy nawias klamrowy. Rozpoczyna słownik (zbiór par 'klucz: wartość') lub zbiór unikalnych elementów (set).
- Znak **`}`**: Prawy nawias klamrowy. Kończy słownik lub zbiór.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    print(type({}) is set)
    print(type({}))
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `aTuple = (1, 'Jhon', 1+3j)`
- Nazwa **`aTuple`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'Jhon'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Liczba **`3j`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 2**: `print(type(aTuple[2:3]))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`type`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`aTuple`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _aTuple = (1, 'Jhon', 1+3j)
    print(type(_aTuple[2:3]))
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `a = [1, 2, 3, 4, 5]`
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`4`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`5`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 2**: `b = a`
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 3**: `print(a == b)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`==`**: Podwójny znak równości to 'operator porównania'. Komputer sprawdza, czy to co po lewej jest DOKŁADNIE TAKIE SAMO jak to po prawej. Zwraca odpowiedź Prawda (True) lub Fałsz (False).
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 4**: `print(a is b)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`is`**: Słowo kluczowe języka Python: 'is'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _a = [1, 2, 3, 4, 5]
    _b = _a 
    print(_a == _b)
    print(_a is _b)
    return

@app.cell
def _():
    pass
    return

@app.cell
def _(mo):
    mo.md(r"""# Instrukcje

Instrukcje języka Python są elastyczne. Można wyróznić instrukcje związane ze składnią języka (np. if, for while), wykorzystanie operatorów (np. =, ==, +, **) i metod/funkcji. W jednej linii można łaczyc instrukcje róznego rodzaju, co przy dobrym wykorzystaniu sprzyja czytelności kodu.

## Podstawienie

Może dotyczyc jednego argumentu lub kilku, dzięki czemu np. operacja zamiany zmiennych jest łatwiejsza niż w C.""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `a = 3`
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 2**: `b, c = 5, 7`
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`c`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`5`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`7`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 3**: `print(a, b, c)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`c`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 4**: `b, c = c, b`
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`c`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`c`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 5**: `print(a, b, c)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`c`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _a = 3
    b, c = 5, 7
    print(_a, b, c)
    b, c = c, b
    print(_a, b, c)
    return

@app.cell
def _(mo):
    mo.md(r"""## Instrukcja if""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `x = int(input('Please enter an integer'))`
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`int`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`input`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'Please enter an integer'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 2**: `if x < 0:`
- Słowo kluczowe **`if`**: Słowo kluczowe 'if' (jeśli). Rozpoczyna instrukcję warunkową. Komputer sprawdzi postawiony warunek - jeśli jest on prawdziwy, wykona kod pod spodem.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`<`**: Znak mniejszości. Pyta: 'czy to po lewej jest mniejsze niż to po prawej?'.
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 3**: `print('Negative')`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'Negative'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 4**: `else:`
- Słowo kluczowe **`else`**: Słowo kluczowe 'else' (w przeciwnym razie). Używane na samym końcu. Oznacza: 'Jeśli ŻADEN z wcześniejszych warunków nie był prawdziwy, wykonaj ostatecznie ten kod'.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 5**: `print('Positive or zero')`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'Positive or zero'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _x = int(input('Please enter an integer'))
    if _x < 0:
      print('Negative')
    else:
      print('Positive or zero')
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `x = int(input('Please enter an integer'))`
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`int`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`input`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'Please enter an integer'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 2**: `if x < 0:`
- Słowo kluczowe **`if`**: Słowo kluczowe 'if' (jeśli). Rozpoczyna instrukcję warunkową. Komputer sprawdzi postawiony warunek - jeśli jest on prawdziwy, wykona kod pod spodem.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`<`**: Znak mniejszości. Pyta: 'czy to po lewej jest mniejsze niż to po prawej?'.
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 3**: `print('Negative')`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'Negative'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 4**: `elif x == 0:`
- Słowo kluczowe **`elif`**: Słowo kluczowe 'elif' (w przeciwnym razie jeśli). Używane po 'if'. Jeśli pierwszy warunek się nie spełnił, komputer sprawdza ten kolejny warunek zastępczy.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`==`**: Podwójny znak równości to 'operator porównania'. Komputer sprawdza, czy to co po lewej jest DOKŁADNIE TAKIE SAMO jak to po prawej. Zwraca odpowiedź Prawda (True) lub Fałsz (False).
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 5**: `print('Zero')`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'Zero'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 6**: `else:`
- Słowo kluczowe **`else`**: Słowo kluczowe 'else' (w przeciwnym razie). Używane na samym końcu. Oznacza: 'Jeśli ŻADEN z wcześniejszych warunków nie był prawdziwy, wykonaj ostatecznie ten kod'.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 7**: `print('Positive')`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'Positive'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _x = int(input('Please enter an integer'))
    if _x < 0:
      print('Negative')
    elif _x == 0:
      print('Zero')
    else:
      print('Positive')
    return

@app.cell
def _(mo):
    mo.md(r"""W Pythonie istnieje również odpowiednik operatora trójarguemntowego C o bardziej czytelnym zapisie:""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `x = int(input('Please enter an integer'))`
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`int`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`input`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'Please enter an integer'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 2**: `print( 'Negative' if x < 0 else 'Positive or zero' )`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'Negative'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Słowo kluczowe **`if`**: Słowo kluczowe 'if' (jeśli). Rozpoczyna instrukcję warunkową. Komputer sprawdzi postawiony warunek - jeśli jest on prawdziwy, wykona kod pod spodem.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`<`**: Znak mniejszości. Pyta: 'czy to po lewej jest mniejsze niż to po prawej?'.
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Słowo kluczowe **`else`**: Słowo kluczowe 'else' (w przeciwnym razie). Używane na samym końcu. Oznacza: 'Jeśli ŻADEN z wcześniejszych warunków nie był prawdziwy, wykonaj ostatecznie ten kod'.
- Tekst (String) **`'Positive or zero'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _x = int(input('Please enter an integer'))
    print( 'Negative' if _x < 0 else 'Positive or zero' )
    return

@app.cell
def _(mo):
    mo.md(r"""Warunki logiczne łączymy operatorami and i or. Negacje wykonuje operator not.""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `wiek = 27`
- Nazwa **`wiek`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`27`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 2**: `if wiek < 30 or wiek % 10 == 0:`
- Słowo kluczowe **`if`**: Słowo kluczowe 'if' (jeśli). Rozpoczyna instrukcję warunkową. Komputer sprawdzi postawiony warunek - jeśli jest on prawdziwy, wykona kod pod spodem.
- Nazwa **`wiek`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`<`**: Znak mniejszości. Pyta: 'czy to po lewej jest mniejsze niż to po prawej?'.
- Liczba **`30`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Słowo kluczowe **`or`**: Słowo 'or' (lub). Łączy dwa warunki. Całość jest prawdziwa, gdy PRZYNAJMNIEJ JEDEN z warunków jest prawdziwy.
- Nazwa **`wiek`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`%`**: Operator modulo (zwraca samą resztę z dzielenia dwóch liczb).
- Liczba **`10`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`==`**: Podwójny znak równości to 'operator porównania'. Komputer sprawdza, czy to co po lewej jest DOKŁADNIE TAKIE SAMO jak to po prawej. Zwraca odpowiedź Prawda (True) lub Fałsz (False).
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 3**: `print('Możesz zorganizować huczne urodziny')`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'Możesz zorganizować huczne urodziny'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 4**: `else:`
- Słowo kluczowe **`else`**: Słowo kluczowe 'else' (w przeciwnym razie). Używane na samym końcu. Oznacza: 'Jeśli ŻADEN z wcześniejszych warunków nie był prawdziwy, wykonaj ostatecznie ten kod'.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 5**: `print('Wystarczy ciasto dla najbliższych, masz kredyt hipoteczny')`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'Wystarczy ciasto dla najbliższych, masz kredyt hipoteczny'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _wiek = 27
    if _wiek < 30 or _wiek % 10 == 0:
      print('Możesz zorganizować huczne urodziny')
    else:
      print('Wystarczy ciasto dla najbliższych, masz kredyt hipoteczny')
    return

@app.cell
def _(mo):
    mo.md(r"""## Instrukcja for

Pozwala na iterację po dowolnym obiekcie iterowalnym (np. liście, krotce, słowniku, ale i Stringu)""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `for i in [0, 4, 7, 12]:`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`i`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`4`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`7`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`12`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 2**: `print(i)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`i`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    for i in [0, 4, 7, 12]:
      print(i)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `for letter in 'Radom':`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`letter`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Tekst (String) **`'Radom'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 2**: `print(letter)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`letter`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    for letter in 'Radom':
      print(letter)
    return

@app.cell
def _(mo):
    mo.md(r"""Instrukcja for jest często łaczona z range(), tworzącą w Python iterowalny obiekt (nie mylić z iteratorem).
range ma w ogólności postać: range(start, stop, krok)""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `lista = range(1,10,3)`
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`range`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`10`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 2**: `print(lista)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 3**: `for i in lista:`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`i`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 4**: `print(i)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`i`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _lista = range(1,10,3)
    print(_lista)
    for i in _lista:
      print(i)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `for i in range(4, 10, 2):`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`i`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`range`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`4`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`10`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 2**: `print(i)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`i`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    for i in range(4, 10, 2):
      print(i)
    return

@app.cell
def _(mo):
    mo.md(r"""Jeśli oprócz wartosci elementu listy chcemy znać jego pozycję na tej lisćie, wykorzystujemy enumerate().""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `najwieksze_kraje = ['Rosja', 'Kanada', 'USA']`
- Nazwa **`najwieksze_kraje`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Tekst (String) **`'Rosja'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'Kanada'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'USA'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 2**: `for idx, item in enumerate(najwieksze_kraje):`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`idx`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`item`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`enumerate`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`najwieksze_kraje`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 3**: `print(idx, item)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`idx`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`item`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _najwieksze_kraje = ['Rosja', 'Kanada', 'USA']
    for idx, item in enumerate(_najwieksze_kraje):
      print(idx, item)
    return

@app.cell
def _(mo):
    mo.md(r"""Do sterowania przebiegiem pętli można wykorzystywać instrukcje break i continue.""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `for num in range(2, 10):`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`num`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`range`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`10`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 2**: `print(num)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`num`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 3**: `if num % 2 == 0:`
- Słowo kluczowe **`if`**: Słowo kluczowe 'if' (jeśli). Rozpoczyna instrukcję warunkową. Komputer sprawdzi postawiony warunek - jeśli jest on prawdziwy, wykona kod pod spodem.
- Nazwa **`num`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`%`**: Operator modulo (zwraca samą resztę z dzielenia dwóch liczb).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`==`**: Podwójny znak równości to 'operator porównania'. Komputer sprawdza, czy to co po lewej jest DOKŁADNIE TAKIE SAMO jak to po prawej. Zwraca odpowiedź Prawda (True) lub Fałsz (False).
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 4**: `print('Found an even number -', num)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'Found an even number -'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`num`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 5**: `break`
- Słowo kluczowe **`break`**: Słowo kluczowe języka Python: 'break'. Jest to wbudowane polecenie o specjalnym znaczeniu.
""")
    return
@app.cell
def _():
    for num in range(2, 10):
      print(num)
      if num % 2 == 0:
        print('Found an even number -', num)
        break
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `for num in range(2, 10):`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`num`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`range`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`10`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 2**: `if num % 2 == 0:`
- Słowo kluczowe **`if`**: Słowo kluczowe 'if' (jeśli). Rozpoczyna instrukcję warunkową. Komputer sprawdzi postawiony warunek - jeśli jest on prawdziwy, wykona kod pod spodem.
- Nazwa **`num`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`%`**: Operator modulo (zwraca samą resztę z dzielenia dwóch liczb).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`==`**: Podwójny znak równości to 'operator porównania'. Komputer sprawdza, czy to co po lewej jest DOKŁADNIE TAKIE SAMO jak to po prawej. Zwraca odpowiedź Prawda (True) lub Fałsz (False).
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 3**: `print('Found an even number -', num)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'Found an even number -'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`num`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 4**: `continue`
- Słowo kluczowe **`continue`**: Słowo kluczowe języka Python: 'continue'. Jest to wbudowane polecenie o specjalnym znaczeniu.

#### 👉 **Linia 5**: `x = 10 / (num % 2)`
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`10`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`/`**: Operator dzielenia.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`num`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`%`**: Operator modulo (zwraca samą resztę z dzielenia dwóch liczb).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    for num in range(2, 10):
      if num % 2 == 0:
        print('Found an even number -', num)
        continue
      _x = 10 / (num % 2)
    return

@app.cell
def _(mo):
    mo.md(r"""Z instrukcją for możemy wiązać instrukcję else, chociaż nie działa ona zgodnie z intuicją, bo instrukcje po else wykonywane są zawsze bez wzgledu na działanie for""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `for i in range (0,2):`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`i`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`range`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 2**: `print(i)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`i`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 3**: `else:`
- Słowo kluczowe **`else`**: Słowo kluczowe 'else' (w przeciwnym razie). Używane na samym końcu. Oznacza: 'Jeśli ŻADEN z wcześniejszych warunków nie był prawdziwy, wykonaj ostatecznie ten kod'.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 4**: `print("koniec")`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"koniec"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    for i in range (0,2):
      print(i)
    else:
      print("koniec")
    return

@app.cell
def _(mo):
    mo.md(r"""W języku Python istnieje instrukcja pusta pass, wykorzystywana głównie jako tymczasowa zaślepka lub przy tworzeniu funkcji wirtualnych - składnia Pythona nie pozwala powiem na tworzenie pustych bloków, analogicznych jak {} w C/C++""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `x=10`
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`10`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 2**: `if x>100:`
- Słowo kluczowe **`if`**: Słowo kluczowe 'if' (jeśli). Rozpoczyna instrukcję warunkową. Komputer sprawdzi postawiony warunek - jeśli jest on prawdziwy, wykona kod pod spodem.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`>`**: Znak większości. Pyta: 'czy to po lewej jest większe?'.
- Liczba **`100`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 3**: `pass`
- Słowo kluczowe **`pass`**: Słowo kluczowe języka Python: 'pass'. Jest to wbudowane polecenie o specjalnym znaczeniu.

#### 👉 **Linia 4**: `else:`
- Słowo kluczowe **`else`**: Słowo kluczowe 'else' (w przeciwnym razie). Używane na samym końcu. Oznacza: 'Jeśli ŻADEN z wcześniejszych warunków nie był prawdziwy, wykonaj ostatecznie ten kod'.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 5**: `print(x)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _x=10
    if _x>100:
        pass
    else:
        print(_x)
    return

@app.cell
def _(mo):
    mo.md(r"""Bardzo interesującą własnoscią języka Python jest inicjalizacja całych list w jednej instrukcji (podobna składnia również dla innych kolekcji)""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `kwadraty = [x**2 for x in range(10)]  # tworzenie listy kwadratów liczb od 1 do 9`
- Nazwa **`kwadraty`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`**`**: Operator potęgowania (liczba do potęgi).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`range`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`10`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- **Komentarz `[ # tworzenie listy kwadratów liczb od 1 do 9 ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `print(kwadraty)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`kwadraty`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _kwadraty = [x**2 for x in range(10)]  # tworzenie listy kwadratów liczb od 1 do 9
    print(_kwadraty)
    return

@app.cell
def _(mo):
    mo.md(r"""Analogiczne operacje można wykonać dla słowników.""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `kwadraty_dict = {x: x**2 for x in range(10)}`
- Nazwa **`kwadraty_dict`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`{`**: Lewy nawias klamrowy. Rozpoczyna słownik (zbiór par 'klucz: wartość') lub zbiór unikalnych elementów (set).
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`**`**: Operator potęgowania (liczba do potęgi).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`range`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`10`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`}`**: Prawy nawias klamrowy. Kończy słownik lub zbiór.

#### 👉 **Linia 2**: `for liczba, kwadrat in kwadraty_dict.items():`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`liczba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`kwadrat`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`kwadraty_dict`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`items`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 3**: `print(liczba, kwadrat)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`liczba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`kwadrat`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _kwadraty_dict = {x: x**2 for x in range(10)}
    for liczba, kwadrat in _kwadraty_dict.items():
      print(liczba, kwadrat)
    return

@app.cell
def _(mo):
    mo.md(r"""Do nowo tworzonej kolekcji można wybrać wszystkie (jak wyżej) lub tylko część spośród elementów:""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `kwadraty_parzyste_dict = {x: x**2 for x in range(10) if x%2 == 0}`
- Nazwa **`kwadraty_parzyste_dict`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`{`**: Lewy nawias klamrowy. Rozpoczyna słownik (zbiór par 'klucz: wartość') lub zbiór unikalnych elementów (set).
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`**`**: Operator potęgowania (liczba do potęgi).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`range`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`10`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Słowo kluczowe **`if`**: Słowo kluczowe 'if' (jeśli). Rozpoczyna instrukcję warunkową. Komputer sprawdzi postawiony warunek - jeśli jest on prawdziwy, wykona kod pod spodem.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`%`**: Operator modulo (zwraca samą resztę z dzielenia dwóch liczb).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`==`**: Podwójny znak równości to 'operator porównania'. Komputer sprawdza, czy to co po lewej jest DOKŁADNIE TAKIE SAMO jak to po prawej. Zwraca odpowiedź Prawda (True) lub Fałsz (False).
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`}`**: Prawy nawias klamrowy. Kończy słownik lub zbiór.

#### 👉 **Linia 2**: `for liczba, kwadrat in kwadraty_parzyste_dict.items():`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`liczba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`kwadrat`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`kwadraty_parzyste_dict`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`items`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 3**: `print(liczba, kwadrat)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`liczba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`kwadrat`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _kwadraty_parzyste_dict = {x: x**2 for x in range(10) if x%2 == 0}
    for liczba, kwadrat in _kwadraty_parzyste_dict.items():
      print(liczba, kwadrat)
    return

@app.cell
def _(mo):
    mo.md(r"""Możliwe jest również stosowanie pętli podwójnych:""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `tabliczka_mnozenia = [{'czynnik_1': x, 'czynnik_2': y, 'iloczyn': x * y}`
- Nazwa **`tabliczka_mnozenia`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Znak **`{`**: Lewy nawias klamrowy. Rozpoczyna słownik (zbiór par 'klucz: wartość') lub zbiór unikalnych elementów (set).
- Tekst (String) **`'czynnik_1'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'czynnik_2'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'iloczyn'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`*`**: Operator mnożenia (gwiazdka).
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`}`**: Prawy nawias klamrowy. Kończy słownik lub zbiór.

#### 👉 **Linia 2**: `for x in range(1, 5) for y in range(1, x+1)]`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`range`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`5`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`range`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 3**: `for item in tabliczka_mnozenia:`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`item`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`tabliczka_mnozenia`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 4**: `print(item)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`item`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _tabliczka_mnozenia = [{'czynnik_1': x, 'czynnik_2': y, 'iloczyn': x * y}
                          for x in range(1, 5) for y in range(1, x+1)]
    for item in _tabliczka_mnozenia:
      print(item)
    return

@app.cell
def _(mo):
    mo.md(r"""Podstawienie wielu wartości (ścisle - krotki) moze być wykorzystane w dowolnym miejscu, np:""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `lista_krotek = [('a', 'b', 'c'), ('x', 'y', 'z'), ('1', '2', '3')]`
- Nazwa **`lista_krotek`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'a'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'b'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'c'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'x'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'y'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'z'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'1'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'2'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'3'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 2**: `for item in lista_krotek:`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`item`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`lista_krotek`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 3**: `print(item)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`item`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _lista_krotek = [('a', 'b', 'c'), ('x', 'y', 'z'), ('1', '2', '3')]
    for item in _lista_krotek:
      print(item)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `for i1, i2, i3 in lista_krotek:`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`i1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`i2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`i3`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`lista_krotek`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 2**: `print(i1, i2, i3)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`i1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`i2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`i3`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    for i1, i2, i3 in lista_krotek:
      print(i1, i2, i3)
    return

@app.cell
def _(mo):
    mo.md(r"""## Instrukcja while""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `i = 0`
- Nazwa **`i`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 2**: `while i**2 < 30:`
- Słowo kluczowe **`while`**: Słowo kluczowe 'while' (dopóki). Rozpoczyna pętlę warunkową. Komputer będzie powtarzał kod pod spodem TAK DŁUGO, dopóki sprawdzany warunek jest wciąż prawdziwy.
- Nazwa **`i`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`**`**: Operator potęgowania (liczba do potęgi).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`<`**: Znak mniejszości. Pyta: 'czy to po lewej jest mniejsze niż to po prawej?'.
- Liczba **`30`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 3**: `i = i+1`
- Nazwa **`i`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`i`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 4**: `print(i)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`i`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _i = 0
    while _i**2 < 30:
      _i = _i+1
      print(_i)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `i = 2`
- Nazwa **`i`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 2**: `while 1 < i**2 < 30:`
- Słowo kluczowe **`while`**: Słowo kluczowe 'while' (dopóki). Rozpoczyna pętlę warunkową. Komputer będzie powtarzał kod pod spodem TAK DŁUGO, dopóki sprawdzany warunek jest wciąż prawdziwy.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`<`**: Znak mniejszości. Pyta: 'czy to po lewej jest mniejsze niż to po prawej?'.
- Nazwa **`i`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`**`**: Operator potęgowania (liczba do potęgi).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`<`**: Znak mniejszości. Pyta: 'czy to po lewej jest mniejsze niż to po prawej?'.
- Liczba **`30`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 3**: `i = i+1`
- Nazwa **`i`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`i`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 4**: `print(i)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`i`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _i = 2
    while 1 < _i**2 < 30:
      _i = _i+1
      print(_i)
    return

@app.cell
def _(mo):
    mo.md(r"""## Zakres zmiennych

Zmienne w języku Python są widoczne poza blokiem w którym zostały zdefiniowane. Nie są widoczne poza funkcją w której zostały zdefiniowane, ale to zostanie omówione po wprowadzeniu funkcji. Pozwala to na pisanie bardziej zwięzłego kodu, trzeba jednak pamietać o ryzyku odwołania  do niezainicjalizowanej zmiennej.""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `x=1`
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 2**: `if x>0:`
- Słowo kluczowe **`if`**: Słowo kluczowe 'if' (jeśli). Rozpoczyna instrukcję warunkową. Komputer sprawdzi postawiony warunek - jeśli jest on prawdziwy, wykona kod pod spodem.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`>`**: Znak większości. Pyta: 'czy to po lewej jest większe?'.
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 3**: `y=1`
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 4**: `print(y)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    _x=1
    if _x>0:
        _y=1
    print(_y)
    return

@app.cell
def _(mo):
    mo.md(r"""""")
    return

@app.cell
def _(mo):
    mo.md(r"""##Quiz""")
    return

@app.cell
def _(mo):
    mo.md(r"""""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `# Jaki jest wynik uruchomienia programu`
- **Komentarz `[ # Jaki jest wynik uruchomienia programu ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 3**: `for i in range(1,5,1):`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`i`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`range`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`5`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 4**: `print(i)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`i`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 5**: `else: print("koniec")`
- Słowo kluczowe **`else`**: Słowo kluczowe 'else' (w przeciwnym razie). Używane na samym końcu. Oznacza: 'Jeśli ŻADEN z wcześniejszych warunków nie był prawdziwy, wykonaj ostatecznie ten kod'.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"koniec"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    # Jaki jest wynik uruchomienia programu
    
    for i in range(1,5,1):
      print(i)
    else: print("koniec")
    return

@app.cell
def _(mo):
    mo.md(r"""Jak napisać instrukcję:

if x%2==0: print(Parzyste)
else print("nieparzyste")

w sposób bardziej "pythonowy" """)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `x=2`
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
""")
    return
@app.cell
def _():
    _x=2
    return

@app.cell
def _(mo):
    mo.md(r"""## Praca domowa (termin oddania 12.03.2023)""")
    return

@app.cell
def _(mo):
    mo.md(r"""Napisać program, który wczytuje kilka par nazwisko, wiek (instrukcja input), tworzy słownik i wypisuje komórki słownika, dla których wiek przekracza zadaną wartość, proszę napisać jak najbardziej związły kod. (minimum linii)
""")
    return

if __name__ == "__main__":
    app.run()