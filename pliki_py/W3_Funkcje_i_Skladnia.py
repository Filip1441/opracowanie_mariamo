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
    mo.md(r"""# Wykład 3: Funkcje i Pattern Matching""")
    return

@app.cell
def _(mo):
    mo.md(r"""### SKŁADNIA: Match-Case
Składnia `match x: case y:` pozwala na dopasowanie wartości. Znak `_` (podkreślenie) w `case _:` to 'wildcard' - wyłapuje wszystko inne.""")
    return

@app.cell
def _(mo):
    mo.md(r"""# Wykład 2

## Plan

*   Funkcje
*   Wyrażenie lambda
*   Funkcje specjalne
*   Dekoratory i generatory""")
    return

@app.cell
def _(mo):
    mo.md(r"""# Uzupełnienie wykładu 1""")
    return

@app.cell
def _(mo):
    mo.md(r"""Rozwiązanie zadania z wykładu 1""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `data = {input("Nazwisko: "): int(input("Wiek: ")) for i in range(int(input("Ile par wprowadzić? ")))}`
- Nazwa **`data`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`{`**: Lewy nawias klamrowy. Rozpoczyna słownik (zbiór par 'klucz: wartość') lub zbiór unikalnych elementów (set).
- Nazwa **`input`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Nazwisko: "`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Nazwa **`int`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`input`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Wiek: "`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`i`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`range`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`int`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`input`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Ile par wprowadzić? "`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`}`**: Prawy nawias klamrowy. Kończy słownik lub zbiór.

#### 👉 **Linia 2**: `limitAge = int(input("Podaj graniczny wiek: "))`
- Nazwa **`limitAge`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`int`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`input`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Podaj graniczny wiek: "`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 3**: `print({name: age for name, age in data.items() if age > limitAge})`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`{`**: Lewy nawias klamrowy. Rozpoczyna słownik (zbiór par 'klucz: wartość') lub zbiór unikalnych elementów (set).
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`data`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`items`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Słowo kluczowe **`if`**: Słowo kluczowe 'if' (jeśli). Rozpoczyna instrukcję warunkową. Komputer sprawdzi postawiony warunek - jeśli jest on prawdziwy, wykona kod pod spodem.
- Nazwa **`age`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`>`**: Znak większości. Pyta: 'czy to po lewej jest większe?'.
- Nazwa **`limitAge`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`}`**: Prawy nawias klamrowy. Kończy słownik lub zbiór.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    data = {input("Nazwisko: "): int(input("Wiek: ")) for i in range(int(input("Ile par wprowadzić? ")))}
    limitAge = int(input("Podaj graniczny wiek: "))
    print({name: age for name, age in data.items() if age > limitAge})
    return

@app.cell
def _(mo):
    mo.md(r"""W pythonie nie ma swich, ale od wersji 3.10 mamy match, który jest odpowiednikiem swich""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `dzien=input("Podaj dzień tygodnia: ")`
- Nazwa **`dzien`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`input`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Podaj dzień tygodnia: "`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 2**: `match dzien:`
- Nazwa **`match`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Nazwa **`dzien`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 3**: `case "poniedziałek":`
- Nazwa **`case`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Tekst (String) **`"poniedziałek"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 4**: `print("Początek tygodnia")`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Początek tygodnia"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 5**: `case "wtorek":`
- Nazwa **`case`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Tekst (String) **`"wtorek"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 6**: `print("Drugi dzień tygodnia")`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Drugi dzień tygodnia"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 7**: `case "środa":`
- Nazwa **`case`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Tekst (String) **`"środa"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 8**: `print("Połowa tygodnia")`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Połowa tygodnia"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 9**: `case _:`
- Nazwa **`case`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Nazwa **`_`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 10**: `print("Nieznany dzień")`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Nieznany dzień"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    dzien=input("Podaj dzień tygodnia: ")
    match dzien:
            case "poniedziałek":
               print("Początek tygodnia")
            case "wtorek":
               print("Drugi dzień tygodnia")
            case "środa":
                print("Połowa tygodnia")
            case _:
                print("Nieznany dzień")
    return

@app.cell
def _(mo):
    mo.md(r"""else po for""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `for i in range(3):`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`i`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`range`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 2**: `k=int(input('podaj k'))`
- Nazwa **`k`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`int`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`input`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'podaj k'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 3**: `if k<0: break`
- Słowo kluczowe **`if`**: Słowo kluczowe 'if' (jeśli). Rozpoczyna instrukcję warunkową. Komputer sprawdzi postawiony warunek - jeśli jest on prawdziwy, wykona kod pod spodem.
- Nazwa **`k`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`<`**: Znak mniejszości. Pyta: 'czy to po lewej jest mniejsze niż to po prawej?'.
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Słowo kluczowe **`break`**: Słowo kluczowe języka Python: 'break'. Jest to wbudowane polecenie o specjalnym znaczeniu.

#### 👉 **Linia 4**: `else: print('koniec')`
- Słowo kluczowe **`else`**: Słowo kluczowe 'else' (w przeciwnym razie). Używane na samym końcu. Oznacza: 'Jeśli ŻADEN z wcześniejszych warunków nie był prawdziwy, wykonaj ostatecznie ten kod'.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'koniec'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    for i in range(3):
      k=int(input('podaj k'))
      if k<0: break
    else: print('koniec')
    return

@app.cell
def _(mo):
    mo.md(r"""# Przykłady""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `#tworzymy listę składającą się z liczb od 0 do 9   kod w stylu C, ale nie pythona`
- **Komentarz `[ #tworzymy listę składającą się z liczb od 0 do 9   kod w stylu C, ale nie pythona ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `kw=[]`
- Nazwa **`kw`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 3**: `for i in range(10):`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`i`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`range`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`10`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 4**: `kw.append(i)`
- Nazwa **`kw`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`append`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`i`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 5**: `print(kw)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`kw`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    #tworzymy listę składającą się z liczb od 0 do 9   kod w stylu C, ale nie pythona
    kw=[]
    for i in range(10):
        kw.append(i)
    print(kw)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `#zapis bardziej pythonowy`
- **Komentarz `[ #zapis bardziej pythonowy ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `print(list([x for x in range(10)]))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`list`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`range`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`10`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    #zapis bardziej pythonowy
    print(list([x for x in range(10)]))
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `#zapis bardziej pythonowy`
- **Komentarz `[ #zapis bardziej pythonowy ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `print(list(range(10)))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`list`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`range`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`10`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    #zapis bardziej pythonowy
    print(list(range(10)))
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `a=True`
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Słowo kluczowe **`True`**: Wartość logiczna 'True' (Prawda). Oznacza stan włączenia, potwierdzenie, że coś jest zgodne z prawdą (w pamięci komputera to jedynka: 1).

#### 👉 **Linia 2**: `if a==True:`
- Słowo kluczowe **`if`**: Słowo kluczowe 'if' (jeśli). Rozpoczyna instrukcję warunkową. Komputer sprawdzi postawiony warunek - jeśli jest on prawdziwy, wykona kod pod spodem.
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`==`**: Podwójny znak równości to 'operator porównania'. Komputer sprawdza, czy to co po lewej jest DOKŁADNIE TAKIE SAMO jak to po prawej. Zwraca odpowiedź Prawda (True) lub Fałsz (False).
- Słowo kluczowe **`True`**: Wartość logiczna 'True' (Prawda). Oznacza stan włączenia, potwierdzenie, że coś jest zgodne z prawdą (w pamięci komputera to jedynka: 1).
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 3**: `b=1`
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 4**: `else:`
- Słowo kluczowe **`else`**: Słowo kluczowe 'else' (w przeciwnym razie). Używane na samym końcu. Oznacza: 'Jeśli ŻADEN z wcześniejszych warunków nie był prawdziwy, wykonaj ostatecznie ten kod'.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 5**: `b=2`
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 6**: `print(b)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    a=True
    if a==True:
        b=1
    else:
        b=2
    print(b)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `#zapis bardziej pythonowy`
- **Komentarz `[ #zapis bardziej pythonowy ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `a=True`
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Słowo kluczowe **`True`**: Wartość logiczna 'True' (Prawda). Oznacza stan włączenia, potwierdzenie, że coś jest zgodne z prawdą (w pamięci komputera to jedynka: 1).

#### 👉 **Linia 3**: `print(b := 1 if a else 2)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:=`**: Znak interpunkcyjny lub operator: ':='. Służy do organizacji struktury kodu.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Słowo kluczowe **`if`**: Słowo kluczowe 'if' (jeśli). Rozpoczyna instrukcję warunkową. Komputer sprawdzi postawiony warunek - jeśli jest on prawdziwy, wykona kod pod spodem.
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`else`**: Słowo kluczowe 'else' (w przeciwnym razie). Używane na samym końcu. Oznacza: 'Jeśli ŻADEN z wcześniejszych warunków nie był prawdziwy, wykonaj ostatecznie ten kod'.
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    #zapis bardziej pythonowy
    a=True
    print(b := 1 if a else 2)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `# zapis w stylu C`
- **Komentarz `[ # zapis w stylu C ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `lista=[1,2,3,4,5]`
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
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

#### 👉 **Linia 3**: `n=3`
- Nazwa **`n`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 4**: `for i in range(len(lista)):`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`i`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`range`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`len`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 5**: `if i > n: print(lista[i])`
- Słowo kluczowe **`if`**: Słowo kluczowe 'if' (jeśli). Rozpoczyna instrukcję warunkową. Komputer sprawdzi postawiony warunek - jeśli jest on prawdziwy, wykona kod pod spodem.
- Nazwa **`i`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`>`**: Znak większości. Pyta: 'czy to po lewej jest większe?'.
- Nazwa **`n`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Nazwa **`i`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    # zapis w stylu C
    lista=[1,2,3,4,5]
    n=3
    for i in range(len(lista)):
        if i > n: print(lista[i])
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `lista=[1,2,3,4,5]`
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
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

#### 👉 **Linia 2**: `n=3`
- Nazwa **`n`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 3**: `for x in lista: print(x if x>n else "")`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`if`**: Słowo kluczowe 'if' (jeśli). Rozpoczyna instrukcję warunkową. Komputer sprawdzi postawiony warunek - jeśli jest on prawdziwy, wykona kod pod spodem.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`>`**: Znak większości. Pyta: 'czy to po lewej jest większe?'.
- Nazwa **`n`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`else`**: Słowo kluczowe 'else' (w przeciwnym razie). Używane na samym końcu. Oznacza: 'Jeśli ŻADEN z wcześniejszych warunków nie był prawdziwy, wykonaj ostatecznie ten kod'.
- Tekst (String) **`""`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    lista=[1,2,3,4,5]
    n=3
    for x in lista: print(x if x>n else "")
    return

@app.cell
def _():
    pass
    return

@app.cell
def _(mo):
    mo.md(r"""Napisać kod w którym  wprowadzam z klawiatury nazwę funkcji,która jest następnie wykonywana""")
    return

@app.cell
def _(mo):
    mo.md(r"""Metoda eval - umieszczenie fragmentu kodu z zewnątrz""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `source='print("test eval xxxx")'`
- Nazwa **`source`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'print("test eval xxxx")'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 2**: `result=eval(source)`
- Nazwa **`result`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`eval`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`source`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    source='print("test eval xxxx")'
    result=eval(source)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `#wprowadzanie parametrów`
- **Komentarz `[ #wprowadzanie parametrów ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `var_x=55`
- Nazwa **`var_x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`55`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 3**: `source='print("test eval",var_x)'`
- Nazwa **`source`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'print("test eval",var_x)'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 4**: `print(source)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`source`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 5**: `result=eval(source)`
- Nazwa **`result`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`eval`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`source`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    #wprowadzanie parametrów
    var_x=55
    source='print("test eval",var_x)'
    print(source)
    result=eval(source)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `import math`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`math`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 2**: `x=2`
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 3**: `source='math.sqrt(x)'`
- Nazwa **`source`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'math.sqrt(x)'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 4**: `result=eval(source)`
- Nazwa **`result`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`eval`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`source`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 5**: `print(result)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`result`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    import math
    x=2
    source='math.sqrt(x)'
    result=eval(source)
    print(result)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `#wprowadzanie parametrów`
- **Komentarz `[ #wprowadzanie parametrów ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `x=20`
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`20`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 3**: `y=1000`
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`1000`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 4**: `source='x/y'`
- Nazwa **`source`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'x/y'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 5**: `result=eval(source)`
- Nazwa **`result`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`eval`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`source`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 6**: `print(result)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`result`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    #wprowadzanie parametrów
    x=20
    y=1000
    source='x/y'
    result=eval(source)
    print(result)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `# wprowadzenie instrukcji z klawiatury`
- **Komentarz `[ # wprowadzenie instrukcji z klawiatury ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `x=20`
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`20`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 3**: `y=30`
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`30`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 4**: `source=input("wprowadź instrukcję: ")`
- Nazwa **`source`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`input`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"wprowadź instrukcję: "`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 5**: `result=eval(source)`
- Nazwa **`result`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`eval`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`source`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 6**: `print(result)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`result`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    # wprowadzenie instrukcji z klawiatury
    x=20
    y=30
    source=input("wprowadź instrukcję: ")
    result=eval(source)
    print(result)
    return

@app.cell
def _(mo):
    mo.md(r"""Funkcja exec wykonuje blok kodu, ale nie zwraca żadnej wartości""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `var_x=20`
- Nazwa **`var_x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`20`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 2**: `source='var_x=30'          #próba zmiany wartości`
- Nazwa **`source`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'var_x=30'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- **Komentarz `[ #próba zmiany wartości ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 3**: `result=exec(source)        #nic nie zwraca`
- Nazwa **`result`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`exec`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`source`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- **Komentarz `[ #nic nie zwraca ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 4**: `print(result)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`result`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 5**: `print(var_x)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`var_x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    var_x=20
    source='var_x=30'          #próba zmiany wartości
    result=exec(source)        #nic nie zwraca
    print(result)
    print(var_x)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `var_x=20`
- Nazwa **`var_x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`20`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 2**: `source=input("podaj kod")          #próba zmiany wartości`
- Nazwa **`source`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`input`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"podaj kod"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- **Komentarz `[ #próba zmiany wartości ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 3**: `result=exec(source)                #nic nie zwraca`
- Nazwa **`result`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`exec`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`source`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- **Komentarz `[ #nic nie zwraca ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 4**: `print(var_x)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`var_x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    var_x=20
    source=input("podaj kod")          #próba zmiany wartości
    result=exec(source)                #nic nie zwraca
    print(var_x)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `var_x=20`
- Nazwa **`var_x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`20`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 2**: `source='''`
- Nazwa **`source`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'''
print("poprzednia wartość ",var_x)
var_x=10

'''`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 6**: `'''`

#### 👉 **Linia 7**: `csource=compile(source,'','exec')`
- Nazwa **`csource`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`compile`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`source`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`''`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'exec'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 8**: `result=exec(csource)`
- Nazwa **`result`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`exec`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`csource`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 9**: `print("nowa wartość ",var_x)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"nowa wartość "`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`var_x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 10**: `print(result)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`result`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    var_x=20
    source='''
    print("poprzednia wartość ",var_x)
    var_x=10
    
    '''
    csource=compile(source,'','exec')
    result=exec(csource)
    print("nowa wartość ",var_x)
    print(result)
    return

@app.cell
def _(mo):
    mo.md(r"""compile - tworzy kod wykonywalny (bytowy) z fragmentu kodu, ma to istotne znaczenie, jeśli dany fragment wykonujemy wiele razy.

Funkcja compile() w Pythonie służy do kompilowania kodu źródłowego Pythona do kodu bajtowego, który jest gotowy do wykonania przez interpreter. Funkcja ta przyjmuje trzy argumenty:


*   source - kod źródłowy Pythona, który ma być skompilowany. Może to być napis, plik lub obiekt typu code.
*  filename - opcjonalny argument, który określa nazwę pliku, z którego został wczytany kod źródłowy. Jeśli argument ten nie jest przekazany, funkcja przyjmuje nazwę "<string>".
* mode - tryb kompilacji, określający typ kodu źródłowego, który jest
kompilowany. Dostępne wartości to:
'exec': kod źródłowy jest skryptem, który ma być wykonany
'eval': kod źródłowy jest wyrażeniem, które ma być obliczone
'single': kod źródłowy jest instrukcją pojedynczą, która ma być wykonana""")
    return

if __name__ == "__main__":
    app.run()