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
    mo.md(r"""# Wykład 4: Meta-programowanie""")
    return

@app.cell
def _(mo):
    mo.md(r"""### LOGIKA: Dekoratory i Lambdy
`lambda x: x*2` to funkcja anonimowa. `@dekorator` to funkcja wyższego rzędu.""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `import time`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`time`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 2**: `var_x=0`
- Nazwa **`var_x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 3**: `source='var_x+=1'`
- Nazwa **`source`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'var_x+=1'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 4**: `# 'interial veriable source' - sygnał korzystania ze zmiennych zewnętrznych`
- **Komentarz `[ # 'interial veriable source' - sygnał korzystania ze zmiennych zewnętrznych ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 5**: `csource=compile(source,'interial veriable source','exec')`
- Nazwa **`csource`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`compile`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`source`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'interial veriable source'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'exec'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 7**: `start=time.time()`
- Nazwa **`start`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`time`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`time`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 8**: `for i in range(100000): result=exec(source)`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`i`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`range`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`100000`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Nazwa **`result`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`exec`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`source`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 9**: `end=time.time()`
- Nazwa **`end`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`time`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`time`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 10**: `print(var_x)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`var_x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 11**: `startc=time.time()`
- Nazwa **`startc`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`time`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`time`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 12**: `for i in range(100000): result=exec(csource)`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`i`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`range`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`100000`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Nazwa **`result`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`exec`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`csource`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 13**: `endc =time.time()`
- Nazwa **`endc`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`time`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`time`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 14**: `print(var_x)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`var_x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 15**: `print((end-start)/(endc-startc))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`end`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`-`**: Operator odejmowania.
- Nazwa **`start`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`/`**: Operator dzielenia.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`endc`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`-`**: Operator odejmowania.
- Nazwa **`startc`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    import time
    var_x=0
    source='var_x+=1'
    # 'interial veriable source' - sygnał korzystania ze zmiennych zewnętrznych
    csource=compile(source,'interial veriable source','exec')
    
    start=time.time()
    for i in range(100000): result=exec(source)
    end=time.time()
    print(var_x)
    startc=time.time()
    for i in range(100000): result=exec(csource)
    endc =time.time()
    print(var_x)
    print((end-start)/(endc-startc))
    return

@app.cell
def _(mo):
    mo.md(r"""## Pytania:

* Czym się różni eval od exec?
* Jakie są zalety compile?""")
    return

@app.cell
def _(mo):
    mo.md(r"""# Zakres zmiennych

Zmienne w języku Python są widoczne poza blokiem w którym zostały zdefiniowane. Nie są widoczne poza funkcją w której zostały zdefiniowane, ale to zostanie omówione po wprowadzeniu funkcji. Pozwala to na pisanie bardziej zwiezłego kodu, trzeba jednak pamietać o ryzyku odwoływania się do niezainicjalizowanej zmiennej.""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `x=int(input())`
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`int`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`input`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 2**: `if x>0:`
- Słowo kluczowe **`if`**: Słowo kluczowe 'if' (jeśli). Rozpoczyna instrukcję warunkową. Komputer sprawdzi postawiony warunek - jeśli jest on prawdziwy, wykona kod pod spodem.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`>`**: Znak większości. Pyta: 'czy to po lewej jest większe?'.
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 3**: `pp1=1`
- Nazwa **`pp1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 4**: `print(pp1)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`pp1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    x=int(input())
    if x>0:
        pp1=1
    print(pp1)
    return

@app.cell
def _(mo):
    mo.md(r"""# Funkcje

Funkcje w Pythonie mogą przyjmować dowolną liczbę argumentów oraz zwracać wartość (pojedynczą, None - gdy nic nie zwracają lub krotkę - wtedy zwracają "kilka wartości").
""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `# przekazywanie argumentów przez pozycję`
- **Komentarz `[ # przekazywanie argumentów przez pozycję ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 3**: `def get_fibonacci(max_val):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`get_fibonacci`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`max_val`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 4**: `a, b = 0, 1`
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 5**: `out = [a]`
- Nazwa **`out`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 6**: `while b <= max_val:`
- Słowo kluczowe **`while`**: Słowo kluczowe 'while' (dopóki). Rozpoczyna pętlę warunkową. Komputer będzie powtarzał kod pod spodem TAK DŁUGO, dopóki sprawdzany warunek jest wciąż prawdziwy.
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`<=`**: Znak mniejszy lub równy.
- Nazwa **`max_val`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 7**: `out.append(b)`
- Nazwa **`out`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`append`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 8**: `a, b = b, a + b`
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 9**: `return out`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Nazwa **`out`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 11**: `fib = get_fibonacci(10)`
- Nazwa **`fib`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`get_fibonacci`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`10`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 12**: `print(fib)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`fib`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    # przekazywanie argumentów przez pozycję
    
    def get_fibonacci(max_val):
      a, b = 0, 1
      out = [a]
      while b <= max_val:
        out.append(b)
        a, b = b, a + b
      return out
    
    fib = get_fibonacci(10)
    print(fib)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `# przekazywanie argumentów przez podanie nazwy`
- **Komentarz `[ # przekazywanie argumentów przez podanie nazwy ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 3**: `def get_fibonacci(max_val):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`get_fibonacci`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`max_val`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 4**: `a, b = 0, 1`
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 5**: `out = [a]`
- Nazwa **`out`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 6**: `while b <= max_val:`
- Słowo kluczowe **`while`**: Słowo kluczowe 'while' (dopóki). Rozpoczyna pętlę warunkową. Komputer będzie powtarzał kod pod spodem TAK DŁUGO, dopóki sprawdzany warunek jest wciąż prawdziwy.
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`<=`**: Znak mniejszy lub równy.
- Nazwa **`max_val`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 7**: `out.append(b)`
- Nazwa **`out`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`append`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 8**: `a, b = b, a + b`
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 9**: `return out`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Nazwa **`out`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 11**: `fib = get_fibonacci(max_val=40)`
- Nazwa **`fib`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`get_fibonacci`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`max_val`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`40`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 12**: `print(fib)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`fib`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    # przekazywanie argumentów przez podanie nazwy
    
    def get_fibonacci(max_val):
      a, b = 0, 1
      out = [a]
      while b <= max_val:
        out.append(b)
        a, b = b, a + b
      return out
    
    fib = get_fibonacci(max_val=40)
    print(fib)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `def print_fibonacci(max_val):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`print_fibonacci`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`max_val`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 2**: `\"\"\"`
- Tekst (String) **`\"\"\"
  brak return \"\"\"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 3**: `brak return \"\"\"`

#### 👉 **Linia 4**: `a, b = 0, 1`
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 5**: `print(a, end=' ')`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`end`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`' '`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 6**: `while b <= max_val-a:`
- Słowo kluczowe **`while`**: Słowo kluczowe 'while' (dopóki). Rozpoczyna pętlę warunkową. Komputer będzie powtarzał kod pod spodem TAK DŁUGO, dopóki sprawdzany warunek jest wciąż prawdziwy.
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`<=`**: Znak mniejszy lub równy.
- Nazwa **`max_val`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`-`**: Operator odejmowania.
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 7**: `a, b = b, a + b`
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 8**: `print(b, end=' ')`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`end`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`' '`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 9**: `print('', end='\n')`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`''`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`end`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'\n'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 11**: `#Tu nie ma wartości zwracanej`
- **Komentarz `[ #Tu nie ma wartości zwracanej ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 12**: `print_fibonacci(40)`
- Nazwa **`print_fibonacci`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`40`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 13**: `#A ścisle biorąc to jest None:`
- **Komentarz `[ #A ścisle biorąc to jest None: ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 14**: `ret = print_fibonacci(10)`
- Nazwa **`ret`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`print_fibonacci`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`10`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 15**: `print('Zwrócono:', ret)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'Zwrócono:'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`ret`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    def print_fibonacci(max_val):
      """
      brak return """
      a, b = 0, 1
      print(a, end=' ')
      while b <= max_val-a:
        a, b = b, a + b
        print(b, end=' ')
      print('', end='\n')
    
    #Tu nie ma wartości zwracanej
    print_fibonacci(40)
    #A ścisle biorąc to jest None:
    ret = print_fibonacci(10)
    print('Zwrócono:', ret)
    return

@app.cell
def _(mo):
    mo.md(r"""Wartości domyślne parametrów podaje się bezposrednio w ich definicji. Argumenty z wartościami domyślnymi muszą występować na końcu (po wszytstkich argumentach bez wartości domyślnych).""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `# Wartości domyślne muszę być na końcu`
- **Komentarz `[ # Wartości domyślne muszę być na końcu ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.
""")
    return
@app.cell
def _():
    # Wartości domyślne muszę być na końcu
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `def print_fibonacci(max_val, start=0):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`print_fibonacci`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`max_val`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`start`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 2**: `\"\"\"określamy początek ciągu\"\"\"`
- Tekst (String) **`\"\"\"określamy początek ciągu\"\"\"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 3**: `a, b = start, start + 1`
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`start`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`start`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 4**: `print(a, end=' ')`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`end`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`' '`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 5**: `while b <= max_val:`
- Słowo kluczowe **`while`**: Słowo kluczowe 'while' (dopóki). Rozpoczyna pętlę warunkową. Komputer będzie powtarzał kod pod spodem TAK DŁUGO, dopóki sprawdzany warunek jest wciąż prawdziwy.
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`<=`**: Znak mniejszy lub równy.
- Nazwa **`max_val`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 6**: `print(b, end=' ')`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`end`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`' '`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 7**: `a, b = b, a + b`
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 8**: `print('', end='\n')`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`''`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`end`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'\n'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 10**: `print_fibonacci(40)`
- Nazwa **`print_fibonacci`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`40`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 11**: `print_fibonacci(40, 3)`
- Nazwa **`print_fibonacci`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`40`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 12**: `print_fibonacci(60, start=5)`
- Nazwa **`print_fibonacci`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`60`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`start`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`5`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    def print_fibonacci(max_val, start=0):
      """określamy początek ciągu"""
      a, b = start, start + 1
      print(a, end=' ')
      while b <= max_val:
        print(b, end=' ')
        a, b = b, a + b
      print('', end='\n')
    
    print_fibonacci(40)
    print_fibonacci(40, 3)
    print_fibonacci(60, start=5)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `def print_fibonaccia(start=0,val_max):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`print_fibonaccia`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`start`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`val_max`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 2**: `\"\"\" !!!!!!  Blad wartość domyślna jest pierwsza\"\"\"`
- Tekst (String) **`\"\"\" !!!!!!  Blad wartość domyślna jest pierwsza\"\"\"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 3**: `a, b = start, start + 1`
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`start`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`start`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 4**: `print(a, end=' ')`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`end`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`' '`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 5**: `while b <= val_max:`
- Słowo kluczowe **`while`**: Słowo kluczowe 'while' (dopóki). Rozpoczyna pętlę warunkową. Komputer będzie powtarzał kod pod spodem TAK DŁUGO, dopóki sprawdzany warunek jest wciąż prawdziwy.
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`<=`**: Znak mniejszy lub równy.
- Nazwa **`val_max`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 6**: `print(b, end=' ')`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`end`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`' '`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 7**: `a, b = b, a + b`
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 8**: `print('', end='\n')`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`''`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`end`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'\n'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 10**: `print_fibonacci(40)`
- Nazwa **`print_fibonacci`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`40`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 11**: `print_fibonacci(40, 3)`
- Nazwa **`print_fibonacci`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`40`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 12**: `print_fibonacci(60, start=5)`
- Nazwa **`print_fibonacci`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`60`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`start`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`5`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    # def print_fibonaccia(start=0,val_max): # BŁĄD SYNTAKTYCZNY: argumenty domyślne muszą być na końcu!
    #   """ !!!!!!  Blad wartość domyślna jest pierwsza"""
    #   a, b = start, start + 1
    #   print(a, end=' ')
    #   while b <= val_max:
    #     print(b, end=' ')
    #     a, b = b, a + b
    #   print('', end='\n')
    pass
    
    print_fibonacci(40)
    print_fibonacci(40, 3)
    print_fibonacci(60, start=5)
    return

@app.cell
def _():
    pass
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `print_fibonacci(start=3, 40)   #błędna kolejność`
- Nazwa **`print_fibonacci`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`start`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`40`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- **Komentarz `[ #błędna kolejność ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.
""")
    return
@app.cell
def _():
    # print_fibonacci(start=3, 40)   # BŁĄD SYNTAKTYCZNY: argument pozycyjny po słowie kluczowym!
    pass
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `print_fibonacci(start=3, max_val=40)`
- Nazwa **`print_fibonacci`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`start`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`max_val`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`40`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    print_fibonacci(start=3, max_val=40)
    return

@app.cell
def _():
    pass
    return

@app.cell
def _(mo):
    mo.md(r"""Funkcje mogą być wywoływane z listą argumentów nieznanej długości (symbol gwiazadki) lub ze słownikiem argumentów, w drugim przypadku wartości argumentów zwykle są poprzedzone ich nazwą (symbol podwójnej gwiazdki). Jest to stosowane raczej przy bardziej złożonych funkcjach, mających bardzo wiele opcji.""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `def function_with_args(*args):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`function_with_args`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`*`**: Operator mnożenia (gwiazdka).
- Nazwa **`args`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 2**: `for arg in args:`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`arg`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`args`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 3**: `print(arg)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`arg`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 5**: `function_with_args(4, 'a', {0: False, 1: True})`
- Nazwa **`function_with_args`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`4`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'a'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Znak **`{`**: Lewy nawias klamrowy. Rozpoczyna słownik (zbiór par 'klucz: wartość') lub zbiór unikalnych elementów (set).
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Słowo kluczowe **`False`**: Wartość logiczna 'False' (Fałsz). Oznacza stan wyłączenia, niezgodność (w pamięci komputera to zero: 0).
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Słowo kluczowe **`True`**: Wartość logiczna 'True' (Prawda). Oznacza stan włączenia, potwierdzenie, że coś jest zgodne z prawdą (w pamięci komputera to jedynka: 1).
- Znak **`}`**: Prawy nawias klamrowy. Kończy słownik lub zbiór.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    def function_with_args(*args):
      for arg in args:
        print(arg)
    
    function_with_args(4, 'a', {0: False, 1: True})
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `function_with_args(2)`
- Nazwa **`function_with_args`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    function_with_args(2)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `def function_with_keyword_args(**kwargs):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`function_with_keyword_args`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`**`**: Operator potęgowania (liczba do potęgi).
- Nazwa **`kwargs`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 2**: `for name, value in kwargs.items():`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`value`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`kwargs`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`items`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 3**: `print(name, value)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`value`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 5**: `function_with_keyword_args(a=8, repeat=0, f=True)`
- Nazwa **`function_with_keyword_args`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`8`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`repeat`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`f`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Słowo kluczowe **`True`**: Wartość logiczna 'True' (Prawda). Oznacza stan włączenia, potwierdzenie, że coś jest zgodne z prawdą (w pamięci komputera to jedynka: 1).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    def function_with_keyword_args(**kwargs):
      for name, value in kwargs.items():
        print(name, value)
    
    function_with_keyword_args(a=8, repeat=0, f=True)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `def both_args_and_kwargs(*args, **kwargs):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`both_args_and_kwargs`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`*`**: Operator mnożenia (gwiazdka).
- Nazwa **`args`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Znak **`**`**: Operator potęgowania (liczba do potęgi).
- Nazwa **`kwargs`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 2**: `print('args:')`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'args:'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 3**: `for item in args:`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`item`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`args`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 4**: `print(item)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`item`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 5**: `print('keyword args:')`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'keyword args:'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 6**: `for key, value in kwargs.items():`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`key`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`value`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`kwargs`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`items`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 7**: `print("key=",key, "val=",value)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"key="`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`key`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`"val="`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`value`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 9**: `both_args_and_kwargs(3, ['abc', 'xyz'],x=6, a=4, c='text')`
- Nazwa **`both_args_and_kwargs`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Tekst (String) **`'abc'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'xyz'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`6`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`4`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`c`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'text'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    def both_args_and_kwargs(*args, **kwargs):
      print('args:')
      for item in args:
        print(item)
      print('keyword args:')
      for key, value in kwargs.items():
        print("key=",key, "val=",value)
    
    both_args_and_kwargs(3, ['abc', 'xyz'],x=6, a=4, c='text')
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `# tu będzie błąd, bo mamy ten sam typ, nie wiadomo kiedy zaczyna się jeden argument a kiedy drugi`
- **Komentarz `[ # tu będzie błąd, bo mamy ten sam typ, nie wiadomo kiedy zaczyna się jeden argument a kiedy drugi ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 3**: `def bad_function(*args, *args2):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`bad_function`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`*`**: Operator mnożenia (gwiazdka).
- Nazwa **`args`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Znak **`*`**: Operator mnożenia (gwiazdka).
- Nazwa **`args2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 4**: `print(args, args2)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`args`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`args2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 6**: `bad_function(1, 2, 3, 4, 5)`
- Nazwa **`bad_function`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`4`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`5`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    # tu będzie błąd, bo mamy ten sam typ, nie wiadomo kiedy zaczyna się jeden argument a kiedy drugi
    
    # def bad_function(*args, *args2): # BŁĄD: Można mieć tylko jeden argument z gwiazdką!
    #   print(args, args2)
    pass
    
    bad_function(1, 2, 3, 4, 5)
    return

@app.cell
def _(mo):
    mo.md(r"""# Zadanie: napisać funkcję, która zwraca sumę jej argumentów, liczba argumentów może być dowolna.""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `def sum(*args):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`sum`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`*`**: Operator mnożenia (gwiazdka).
- Nazwa **`args`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 2**: `k=0`
- Nazwa **`k`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 3**: `for i in args:`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`i`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`args`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 4**: `k=k+i`
- Nazwa **`k`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`k`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Nazwa **`i`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 5**: `return k`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Nazwa **`k`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 6**: `print(sum(1,2,3))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`sum`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 7**: `a=[1,2,3]`
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 8**: `print(sum(*a))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`sum`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`*`**: Operator mnożenia (gwiazdka).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    def sum(*args):
      k=0
      for i in args:
        k=k+i
      return k
    print(sum(1,2,3))
    a=[1,2,3]
    print(sum(*a))
    return

@app.cell
def _(mo):
    mo.md(r"""Zadanie: napisać funkcję, która wypisuje sumę cen artykułów zawartych w liście zakupów. Cennik artykułów jest argumentem funkcji.""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `# args - lista  produktów, kargs - słownik zawierający cenę produktów`
- **Komentarz `[ # args - lista  produktów, kargs - słownik zawierający cenę produktów ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `def BuyMe(*args,**kwargs):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`BuyMe`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`*`**: Operator mnożenia (gwiazdka).
- Nazwa **`args`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Znak **`**`**: Operator potęgowania (liczba do potęgi).
- Nazwa **`kwargs`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 3**: `print('args=',args)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'args='`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`args`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 4**: `print('args=',kwargs)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'args='`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`kwargs`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 5**: `k=0.0`
- Nazwa **`k`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`0.0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 6**: `for a in args:`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`args`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 7**: `if a in kwargs:  # Sprawdzenie, czy klucz istnieje w kwargs`
- Słowo kluczowe **`if`**: Słowo kluczowe 'if' (jeśli). Rozpoczyna instrukcję warunkową. Komputer sprawdzi postawiony warunek - jeśli jest on prawdziwy, wykona kod pod spodem.
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`kwargs`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- **Komentarz `[ # Sprawdzenie, czy klucz istnieje w kwargs ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 8**: `k += float(kwargs[a])  # Dodanie wartości do sumy`
- Nazwa **`k`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`+=`**: Znak interpunkcyjny lub operator: '+='. Służy do organizacji struktury kodu.
- Nazwa **`float`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`kwargs`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- **Komentarz `[ # Dodanie wartości do sumy ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 10**: `print(k)  # Wypisanie sumy`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`k`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- **Komentarz `[ # Wypisanie sumy ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 11**: `lista=['ser','mleko','chleb']`
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Tekst (String) **`'ser'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'mleko'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'chleb'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 12**: `ceny={'ser':10.0,'mleko':4.0,'chleb':8.0}`
- Nazwa **`ceny`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`{`**: Lewy nawias klamrowy. Rozpoczyna słownik (zbiór par 'klucz: wartość') lub zbiór unikalnych elementów (set).
- Tekst (String) **`'ser'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Liczba **`10.0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'mleko'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Liczba **`4.0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'chleb'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Liczba **`8.0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`}`**: Prawy nawias klamrowy. Kończy słownik lub zbiór.

#### 👉 **Linia 13**: `BuyMe(*lista, **ceny)`
- Nazwa **`BuyMe`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`*`**: Operator mnożenia (gwiazdka).
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Znak **`**`**: Operator potęgowania (liczba do potęgi).
- Nazwa **`ceny`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    # args - lista  produktów, kargs - słownik zawierający cenę produktów
    def BuyMe(*args,**kwargs):
      print('args=',args)
      print('args=',kwargs)
      k=0.0
      for a in args:
            if a in kwargs:  # Sprawdzenie, czy klucz istnieje w kwargs
                k += float(kwargs[a])  # Dodanie wartości do sumy
    
      print(k)  # Wypisanie sumy
    lista=['ser','mleko','chleb']
    ceny={'ser':10.0,'mleko':4.0,'chleb':8.0}
    BuyMe(*lista, **ceny)
    return

@app.cell
def _(mo):
    mo.md(r"""## Pytania
Mam funkcję:

def readdata(nazwa, format):
.....
Jaki będzie wynik wywołania:
readdata('plik')?
Dodatkowe pytanie.""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `def readdata(name, format='pdf'):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`readdata`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`format`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'pdf'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 2**: `print(name,' ', format)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`' '`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`format`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 3**: `readdata('name')`
- Nazwa **`readdata`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'name'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    def readdata(name, format='pdf'):
      print(name,' ', format)
    readdata('name')
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `def fun_a(*args):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`fun_a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`*`**: Operator mnożenia (gwiazdka).
- Nazwa **`args`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 2**: `for i in args: print(i)`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`i`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`args`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`i`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 4**: `lista=[1,2,3]`
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 6**: `#jaka jest różnica między:`
- **Komentarz `[ #jaka jest różnica między: ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 7**: `fun_a(lista)`
- Nazwa **`fun_a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 8**: `#a`
- **Komentarz `[ #a ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 9**: `fun_a(*lista)`
- Nazwa **`fun_a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`*`**: Operator mnożenia (gwiazdka).
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    def fun_a(*args):
      for i in args: print(i)
    
    lista=[1,2,3]
    
    #jaka jest różnica między:
    fun_a(lista)
    #a
    fun_a(*lista)
    return

@app.cell
def _(mo):
    mo.md(r"""## Funkcja jako obiekt""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `def BuyMe(*args,**kargs):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`BuyMe`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`*`**: Operator mnożenia (gwiazdka).
- Nazwa **`args`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Znak **`**`**: Operator potęgowania (liczba do potęgi).
- Nazwa **`kargs`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 2**: `print('args=',args)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'args='`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`args`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 3**: `print('args=',kargs)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'args='`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`kargs`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 5**: `Bm=BuyMe`
- Nazwa **`Bm`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`BuyMe`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 6**: `print(type(Bm))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`type`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`Bm`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    def BuyMe(*args,**kargs):
      print('args=',args)
      print('args=',kargs)
    
    Bm=BuyMe
    print(type(Bm))
    return

@app.cell
def _(mo):
    mo.md(r"""Dkaczego nie widzi kargs, jak to zmienić?""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `def BuyMe(*args,**kargs):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`BuyMe`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`*`**: Operator mnożenia (gwiazdka).
- Nazwa **`args`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Znak **`**`**: Operator potęgowania (liczba do potęgi).
- Nazwa **`kargs`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 2**: `print('args=',args)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'args='`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`args`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 3**: `print('kargs=',kargs)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'kargs='`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`kargs`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 5**: `Bm=BuyMe`
- Nazwa **`Bm`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`BuyMe`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 7**: `Bm('ser',{'ser':10})`
- Nazwa **`Bm`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'ser'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Znak **`{`**: Lewy nawias klamrowy. Rozpoczyna słownik (zbiór par 'klucz: wartość') lub zbiór unikalnych elementów (set).
- Tekst (String) **`'ser'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Liczba **`10`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`}`**: Prawy nawias klamrowy. Kończy słownik lub zbiór.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    def BuyMe(*args,**kargs):
      print('args=',args)
      print('kargs=',kargs)
    
    Bm=BuyMe
    
    Bm('ser',{'ser':10})
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `def Kup(*args):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`Kup`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`*`**: Operator mnożenia (gwiazdka).
- Nazwa **`args`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 2**: `print('kupuje', args)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'kupuje'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`args`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 3**: `def Idzpo(*args):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`Idzpo`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`*`**: Operator mnożenia (gwiazdka).
- Nazwa **`args`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 4**: `print('ide do sklepu po', args)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'ide do sklepu po'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`args`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 6**: `lista=['chleb','ser']`
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Tekst (String) **`'chleb'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'ser'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 7**: `dzialanie = [Idzpo,Kup]`
- Nazwa **`dzialanie`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Nazwa **`Idzpo`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`Kup`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 8**: `for  d in dzialanie:`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`d`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`dzialanie`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 9**: `d(*lista)`
- Nazwa **`d`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`*`**: Operator mnożenia (gwiazdka).
- Nazwa **`lista`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    def Kup(*args):
        print('kupuje', args)
    def Idzpo(*args):
        print('ide do sklepu po', args)
    
    lista=['chleb','ser']
    dzialanie = [Idzpo,Kup]
    for  d in dzialanie:
        d(*lista)
    
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `def Bake(a):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`Bake`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 2**: `print("piekę",a)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"piekę"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 3**: `def Mix(a):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`Mix`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 4**: `print("mieszam",a)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"mieszam"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 5**: `def Add(a):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`Add`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 6**: `print("dodaję",a)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"dodaję"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 7**: `# lista funkcja i argument`
- **Komentarz `[ # lista funkcja i argument ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 8**: `cookbook=[(Add,'mleko'),(Add,'cukier'),(Mix,'skladniki'),(Bake,'ciasto')]`
- Nazwa **`cookbook`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`Add`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'mleko'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`Add`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'cukier'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`Mix`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'skladniki'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`Bake`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'ciasto'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 9**: `for akcja,obiekt in cookbook:`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`akcja`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`obiekt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`cookbook`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 10**: `akcja(obiekt)`
- Nazwa **`akcja`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`obiekt`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    def Bake(a):
        print("piekę",a)
    def Mix(a):
        print("mieszam",a)
    def Add(a):
        print("dodaję",a)
     # lista funkcja i argument
    cookbook=[(Add,'mleko'),(Add,'cukier'),(Mix,'skladniki'),(Bake,'ciasto')]
    for akcja,obiekt in cookbook:
            akcja(obiekt)
    return

@app.cell
def _(mo):
    mo.md(r"""## Tworzenie funkcji na podstawie funkcji istniejącej""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `def Nf(kind='+'):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`Nf`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`kind`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'+'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 2**: `def fw(*args,kind=kind):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`fw`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`*`**: Operator mnożenia (gwiazdka).
- Nazwa **`args`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`kind`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`kind`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 3**: `w=0 if kind=='+' else 1`
- Nazwa **`w`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Słowo kluczowe **`if`**: Słowo kluczowe 'if' (jeśli). Rozpoczyna instrukcję warunkową. Komputer sprawdzi postawiony warunek - jeśli jest on prawdziwy, wykona kod pod spodem.
- Nazwa **`kind`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`==`**: Podwójny znak równości to 'operator porównania'. Komputer sprawdza, czy to co po lewej jest DOKŁADNIE TAKIE SAMO jak to po prawej. Zwraca odpowiedź Prawda (True) lub Fałsz (False).
- Tekst (String) **`'+'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Słowo kluczowe **`else`**: Słowo kluczowe 'else' (w przeciwnym razie). Używane na samym końcu. Oznacza: 'Jeśli ŻADEN z wcześniejszych warunków nie był prawdziwy, wykonaj ostatecznie ten kod'.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 4**: `if kind=='+':`
- Słowo kluczowe **`if`**: Słowo kluczowe 'if' (jeśli). Rozpoczyna instrukcję warunkową. Komputer sprawdzi postawiony warunek - jeśli jest on prawdziwy, wykona kod pod spodem.
- Nazwa **`kind`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`==`**: Podwójny znak równości to 'operator porównania'. Komputer sprawdza, czy to co po lewej jest DOKŁADNIE TAKIE SAMO jak to po prawej. Zwraca odpowiedź Prawda (True) lub Fałsz (False).
- Tekst (String) **`'+'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 5**: `for a in args:`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`args`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 6**: `w=w+a`
- Nazwa **`w`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`w`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 7**: `return w`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Nazwa **`w`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 8**: `else:`
- Słowo kluczowe **`else`**: Słowo kluczowe 'else' (w przeciwnym razie). Używane na samym końcu. Oznacza: 'Jeśli ŻADEN z wcześniejszych warunków nie był prawdziwy, wykonaj ostatecznie ten kod'.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 9**: `for a in args:`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`args`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 10**: `w=w*a`
- Nazwa **`w`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`w`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`*`**: Operator mnożenia (gwiazdka).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 11**: `return w`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Nazwa **`w`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 12**: `return fw`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Nazwa **`fw`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 13**: `sum=Nf('+')`
- Nazwa **`sum`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`Nf`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'+'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 14**: `mul=Nf('*')`
- Nazwa **`mul`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`Nf`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'*'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 15**: `print(mul(8,2,3))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`mul`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`8`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 16**: `print(sum(8,2,3))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`sum`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`8`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    def Nf(kind='+'):
        def fw(*args,kind=kind):
         w=0 if kind=='+' else 1
         if kind=='+':
          for a in args:
            w=w+a
          return w
         else:
          for a in args:
            w=w*a
          return w
        return fw
    sum=Nf('+')
    mul=Nf('*')
    print(mul(8,2,3))
    print(sum(8,2,3))
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `## przekazywanie argumentów do exec`
- **Komentarz `[ ## przekazywanie argumentów do exec ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `def Nf(kind='+'):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`Nf`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`kind`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'+'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 3**: `source='''`
- Nazwa **`source`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'''
def fw(*args):
     w=0
     for a in args:
        w=w{}a
return w
     '''`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 9**: `'''.format(kind)`
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`format`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`kind`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 10**: `return f`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Nazwa **`f`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
""")
    return
@app.cell
def _():
    ## przekazywanie argumentów do exec
    def Nf(kind='+'):
        source='''
    def fw(*args):
         w=0
         for a in args:
            w=w{}a
    return w
         '''.format(kind)
        return f
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `def Nf(kind='+'):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`Nf`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`kind`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'+'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 2**: `source = '''`
- Nazwa **`source`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`'''
def fw(*args, kind='{}'):
     w = 0 if kind == '+' else 1
     for a in args:
        w = w {} a
     return w
     '''`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 8**: `'''.format(kind, kind)`
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`format`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`kind`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`kind`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 9**: `exec(source, globals())`
- Nazwa **`exec`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`source`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`globals`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 10**: `return fw`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Nazwa **`fw`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 12**: `f_add = Nf('+')`
- Nazwa **`f_add`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`Nf`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'+'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 13**: `f_m = Nf('*')`
- Nazwa **`f_m`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`Nf`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'*'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 14**: `print(f_add(0, 2, 3))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`f_add`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    def Nf(kind='+'):
        source = '''
    def fw(*args, kind='{}'):
         w = 0 if kind == '+' else 1
         for a in args:
            w = w {} a
         return w
         '''.format(kind, kind)
        exec(source, globals())
        return fw
    
    f_add = Nf('+')
    f_m = Nf('*')
    print(f_add(0, 2, 3))
    return

@app.cell
def _(mo):
    mo.md(r"""## Pytania

Po co tworzymy funkcje dedykowane, jakie są zalety takiego rozwiązania?""")
    return

@app.cell
def _(mo):
    mo.md(r"""## Zmienne globalne

W języku Python bloki nie ograniczaja widoczności zmiennych ani możliwości ich zapisu:""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `a = 3`
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 2**: `for _ in range(2):`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`_`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`range`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 3**: `print(a)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 4**: `a = 4`
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`4`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 5**: `print(a)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    a = 3
    for _ in range(2):
      print(a)
      a = 4
    print(a)
    return

@app.cell
def _(mo):
    mo.md(r"""Inaczej jest w wypadku funkcji, w których możliwy jest odczyt, ale nie modyfikacja zmiennych:""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 2**: `b = 3`
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 4**: `def f(x):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`f`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 5**: `a1=5`
- Nazwa **`a1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`5`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 6**: `b=10`
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`10`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 7**: `return a1 * x + b`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Nazwa **`a1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`*`**: Operator mnożenia (gwiazdka).
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 10**: `print(f(2))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`f`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 11**: `print(b)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    
    b = 3
    
    def f(x):
      a1=5
      b=10
      return a1 * x + b
    
    
    print(f(2))
    print(b)
    return

@app.cell
def _(mo):
    mo.md(r"""W wypadku modyfikacji zmiennych spoza funkcji w jej wnętrzu zmianie ulegają ich lokalne kopie:""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `x = "global"`
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`"global"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 2**: `def foo():`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`foo`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 3**: `x=" "`
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`" "`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 4**: `x = x+"sdsdsd"`
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Tekst (String) **`"sdsdsd"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.

#### 👉 **Linia 5**: `print(x)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 7**: `foo()`
- Nazwa **`foo`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 8**: `print(x)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    x = "global"
    def foo():
        x=" "
        x = x+"sdsdsd"
        print(x)
    
    foo()
    print(x)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `a = 2`
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 2**: `b = 3`
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 4**: `def f(x):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`f`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 5**: `a = 1`
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 6**: `b = 0`
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 7**: `return a * x + b`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`*`**: Operator mnożenia (gwiazdka).
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 9**: `print(f(2))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`f`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 10**: `print('a=',a, 'b=',b)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'a='`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`'b='`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    a = 2
    b = 3
    
    def f(x):
      a = 1
      b = 0
      return a * x + b
    
    print(f(2))
    print('a=',a, 'b=',b)
    return

@app.cell
def _(mo):
    mo.md(r"""Aby zmienić wartość zmiennej globalnej, należy użyć słowa kluczowego global.
Nie zaleca się jednak takiego sposobu programowania.
 Podobne znaczenie ma słowo kluczowe nonlocal, ale dotyczy to funkcji wewnętrznych.""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `a = 4`
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`4`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 2**: `b = 3`
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 4**: `def f(x):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`f`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 5**: `global a, b`
- Słowo kluczowe **`global`**: Słowo kluczowe języka Python: 'global'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 6**: `a = 1`
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 7**: `b = 0`
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 8**: `return a * x + b`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`*`**: Operator mnożenia (gwiazdka).
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 10**: `print(f(2))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`f`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 11**: `print(a, b)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    a = 4
    b = 3
    
    def f(x):
      global a, b
      a = 1
      b = 0
      return a * x + b
    
    print(f(2))
    print(a, b)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `def f1(x):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`f1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 2**: `#  global a`
- **Komentarz `[ #  global a ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 3**: `a=2`
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 4**: `def f(x):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`f`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 5**: `nonlocal a`
- Słowo kluczowe **`nonlocal`**: Słowo kluczowe języka Python: 'nonlocal'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 6**: `a = 1`
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 7**: `return a * x`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`*`**: Operator mnożenia (gwiazdka).
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 8**: `y=f(x)`
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`f`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 9**: `print("wartość a  w f1",a,"wynik f1",y )`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"wartość a  w f1"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Tekst (String) **`"wynik f1"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 10**: `return(y)`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 11**: `a=10`
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`10`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 12**: `f1(2)`
- Nazwa **`f1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 13**: `print("wartość a na końcu", a)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"wartość a na końcu"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    def f1(x):
    #  global a
      a=2
      def f(x):
        nonlocal a
        a = 1
        return a * x
      y=f(x)
      print("wartość a  w f1",a,"wynik f1",y )
      return(y)
    a=10
    f1(2)
    print("wartość a na końcu", a)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `def f1(x):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`f1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 2**: `a=2`
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 3**: `b=3`
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 4**: `def f(x):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`f`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 5**: `global a,b`
- Słowo kluczowe **`global`**: Słowo kluczowe języka Python: 'global'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 6**: `a = 1`
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 7**: `b = 0`
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 8**: `return a * x + b`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`*`**: Operator mnożenia (gwiazdka).
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 9**: `y=f(2)`
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`f`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 10**: `print(a,b)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 11**: `return(y)`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 12**: `a=1`
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 13**: `b=2`
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 14**: `print(f1(2))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`f1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 15**: `print(a, b)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    def f1(x):
      a=2
      b=3
      def f(x):
        global a,b
        a = 1
        b = 0
        return a * x + b
      y=f(2)
      print(a,b)
      return(y)
    a=1
    b=2
    print(f1(2))
    print(a, b)
    return

@app.cell
def _(mo):
    mo.md(r"""## Import funkcji z innych plików

Popularność Pythona wynika w znacznej mierze z dużej liczby bibliotek ułatwiajacych wykonywanie różnorakich zadań oraz łatwości ich wykorzystania. Aby zaimportować biblioteke do programu korzystamy z polecenia import. Należy pamietać, ze każdy moduł zostanie zaimportowany tylko raz podczas wywołania programu, nawet jeśli wystąpi kilka wywołań. Biblioteki zwyczajowo importujemy na początku pliku .py""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `import os  # import modułu os`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`os`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- **Komentarz `[ # import modułu os ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `import numpy as np  # import modułu numpy i nadanie mu lokalnie nazwy np`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`numpy`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`as`**: Słowo kluczowe języka Python: 'as'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`np`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- **Komentarz `[ # import modułu numpy i nadanie mu lokalnie nazwy np ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.
""")
    return
@app.cell
def _():
    import os  # import modułu os
    import numpy as np  # import modułu numpy i nadanie mu lokalnie nazwy np
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `import os`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`os`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 2**: `import numpy as np`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`numpy`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`as`**: Słowo kluczowe języka Python: 'as'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`np`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 3**: `files = os.listdir('.')`
- Nazwa **`files`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`os`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`listdir`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'.'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 4**: `print(files)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`files`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    import os
    import numpy as np
    files = os.listdir('.')
    print(files)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `# Wywołanie funkcji array z modułu numpy, tworzącej tablicę`
- **Komentarz `[ # Wywołanie funkcji array z modułu numpy, tworzącej tablicę ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `import numpy as np`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`numpy`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`as`**: Słowo kluczowe języka Python: 'as'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`np`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 3**: `x = np.array([1, 2, 3])`
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
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

#### 👉 **Linia 4**: `print(x)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    # Wywołanie funkcji array z modułu numpy, tworzącej tablicę
    import numpy as np
    x = np.array([1, 2, 3])
    print(x)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `# Nie możemy odwoływać sie do biblioteki pod nazwą globalną,`
- **Komentarz `[ # Nie możemy odwoływać sie do biblioteki pod nazwą globalną, ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `# jeśli ustawilismy lokalną`
- **Komentarz `[ # jeśli ustawilismy lokalną ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 3**: `import numpy as np`
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`numpy`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`as`**: Słowo kluczowe języka Python: 'as'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`np`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 4**: `x = numpy.array([1, 2, 3])  #błąd bo np`
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`numpy`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
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
- **Komentarz `[ #błąd bo np ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.
""")
    return
@app.cell
def _():
    # Nie możemy odwoływać sie do biblioteki pod nazwą globalną,
    # jeśli ustawilismy lokalną
    import numpy as np
    x = numpy.array([1, 2, 3])  #błąd bo np
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `from time import time  # Import tylko wybranych składowych modułu`
- Słowo kluczowe **`from`**: Słowo kluczowe 'from' (z). Używane przy importowaniu, oznacza 'Z tej konkretnej, dużej biblioteki załaduj tylko ten jeden określony fragment'.
- Nazwa **`time`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`time`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- **Komentarz `[ # Import tylko wybranych składowych modułu ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `print(time())`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`time`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 3**: `# Gdyby wykonać zwykłe:`
- **Komentarz `[ # Gdyby wykonać zwykłe: ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 4**: `# import time`
- **Komentarz `[ # import time ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 5**: `# to trzeba by potem wywołać polecenie:`
- **Komentarz `[ # to trzeba by potem wywołać polecenie: ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 6**: `# print(time.time())`
- **Komentarz `[ # print(time.time()) ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 7**: `# Uwaga: poprawny ponowny import biblioteki time wymaga resetu notebooka`
- **Komentarz `[ # Uwaga: poprawny ponowny import biblioteki time wymaga resetu notebooka ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.
""")
    return
@app.cell
def _():
    from time import time  # Import tylko wybranych składowych modułu
    print(time())
    # Gdyby wykonać zwykłe:
    # import time
    # to trzeba by potem wywołać polecenie:
    # print(time.time())
    # Uwaga: poprawny ponowny import biblioteki time wymaga resetu notebooka
    return

@app.cell
def _(mo):
    mo.md(r"""Funkcje w poprawnie przygotowanych modułach zawieraja dokumentację w formie docstringa. Warto równiez o tym pamietać przy tworzeniu własnych modułów (co jest poza zakresem tego wykładu).""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `help(np.array)`
- Nazwa **`help`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`np`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
- Nazwa **`array`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    help(np.array)
    return

@app.cell
def _(mo):
    mo.md(r"""# Lambda

Lambda jest sposobem definiowania funkcji anonimowej pozwalającym często na bardziej zwięzły zapis kodu.""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `# Zwykłą funkcja`
- **Komentarz `[ # Zwykłą funkcja ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `def f1(x):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`f1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 3**: `return 2*x + 1`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`*`**: Operator mnożenia (gwiazdka).
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 5**: `# Lambda`
- **Komentarz `[ # Lambda ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 6**: `f2 = lambda x: 2*x + 1`
- Nazwa **`f2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Słowo kluczowe **`lambda`**: Słowo kluczowe języka Python: 'lambda'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`*`**: Operator mnożenia (gwiazdka).
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 8**: `# Identyczna składnia i wynik`
- **Komentarz `[ # Identyczna składnia i wynik ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 9**: `print(f1(3))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`f1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 10**: `print(f2(3))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`f2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 11**: `# Przypisanie lambdy do nazwanej zmiennej nie daje nowych możliwosci`
- **Komentarz `[ # Przypisanie lambdy do nazwanej zmiennej nie daje nowych możliwosci ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 12**: `# i obniza czytelność`
- **Komentarz `[ # i obniza czytelność ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.
""")
    return
@app.cell
def _():
    # Zwykłą funkcja
    def f1(x):
      return 2*x + 1
    
    # Lambda
    f2 = lambda x: 2*x + 1
    
    # Identyczna składnia i wynik
    print(f1(3))
    print(f2(3))
    # Przypisanie lambdy do nazwanej zmiennej nie daje nowych możliwosci
    # i obniza czytelność
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `lista_zwierze_waga = [('pies', 10.), ('kot', 5.), ('koń', 200.), ('wróbel', 0.1)]`
- Nazwa **`lista_zwierze_waga`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'pies'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`10.`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'kot'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`5.`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'koń'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`200.`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'wróbel'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`0.1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 3**: `# Sortowanie z wykorzystaniem funkcji`
- **Komentarz `[ # Sortowanie z wykorzystaniem funkcji ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 4**: `def odczyt_wagi(zwierze_waga):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`odczyt_wagi`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`zwierze_waga`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 5**: `return zwierze_waga[1]`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Nazwa **`zwierze_waga`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 7**: `posortowana_1 = sorted(lista_zwierze_waga, key=odczyt_wagi)`
- Nazwa **`posortowana_1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`sorted`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`lista_zwierze_waga`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`key`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`odczyt_wagi`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 9**: `# Sortowanie z lambdą - jedna linijka`
- **Komentarz `[ # Sortowanie z lambdą - jedna linijka ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 10**: `posortowana_2 = sorted(lista_zwierze_waga, key=lambda x: x[1])`
- Nazwa **`posortowana_2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`sorted`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`lista_zwierze_waga`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`key`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Słowo kluczowe **`lambda`**: Słowo kluczowe języka Python: 'lambda'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 12**: `for item in posortowana_1:`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`item`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`posortowana_1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 13**: `print(item)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`item`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 14**: `print('-----------')`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'-----------'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 15**: `for item in posortowana_2:`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`item`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`posortowana_2`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 16**: `print(item)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`item`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    lista_zwierze_waga = [('pies', 10.), ('kot', 5.), ('koń', 200.), ('wróbel', 0.1)]
    
    # Sortowanie z wykorzystaniem funkcji
    def odczyt_wagi(zwierze_waga):
      return zwierze_waga[1]
    
    posortowana_1 = sorted(lista_zwierze_waga, key=odczyt_wagi)
    
    # Sortowanie z lambdą - jedna linijka
    posortowana_2 = sorted(lista_zwierze_waga, key=lambda x: x[1])
    
    for item in posortowana_1:
      print(item)
    print('-----------')
    for item in posortowana_2:
      print(item)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `# Lambda moze mieć wiele arguemntów, np. dwa:`
- **Komentarz `[ # Lambda moze mieć wiele arguemntów, np. dwa: ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `f = lambda x, y: x * y`
- Nazwa **`f`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Słowo kluczowe **`lambda`**: Słowo kluczowe języka Python: 'lambda'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`*`**: Operator mnożenia (gwiazdka).
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 4**: `print(f(2, 3))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`f`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    # Lambda moze mieć wiele arguemntów, np. dwa:
    f = lambda x, y: x * y
    
    print(f(2, 3))
    return

@app.cell
def _(mo):
    mo.md(r"""# Funkcje wbudowane""")
    return

@app.cell
def _(mo):
    mo.md(r"""filter - zwraca iterator elementów kolekcji (a nie listę), które spełniaja określone kryterium""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `weights = [10, 40, 320, 450, 70, 115, 3]`
- Nazwa **`weights`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Liczba **`10`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`40`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`320`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`450`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`70`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`115`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 2**: `filter_heavy = filter(lambda x: x > 100, weights)`
- Nazwa **`filter_heavy`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`filter`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Słowo kluczowe **`lambda`**: Słowo kluczowe języka Python: 'lambda'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`>`**: Znak większości. Pyta: 'czy to po lewej jest większe?'.
- Liczba **`100`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`weights`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 3**: `print(filter_heavy)  #referencja do listy`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`filter_heavy`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- **Komentarz `[ #referencja do listy ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.
""")
    return
@app.cell
def _():
    weights = [10, 40, 320, 450, 70, 115, 3]
    filter_heavy = filter(lambda x: x > 100, weights)
    print(filter_heavy)  #referencja do listy
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `# Uzyskanie listy na podstawie iteratora`
- **Komentarz `[ # Uzyskanie listy na podstawie iteratora ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `weights = [10, 40, 320, 450, 70, 115, 3]`
- Nazwa **`weights`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Liczba **`10`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`40`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`320`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`450`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`70`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`115`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 3**: `filter_heavy = filter(lambda x: x > 100, weights)`
- Nazwa **`filter_heavy`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`filter`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Słowo kluczowe **`lambda`**: Słowo kluczowe języka Python: 'lambda'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`>`**: Znak większości. Pyta: 'czy to po lewej jest większe?'.
- Liczba **`100`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`weights`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 4**: `print(list(filter_heavy))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`list`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`filter_heavy`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    # Uzyskanie listy na podstawie iteratora
    weights = [10, 40, 320, 450, 70, 115, 3]
    filter_heavy = filter(lambda x: x > 100, weights)
    print(list(filter_heavy))
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `# Ponowne wywołanie - iterator dotarł do końca, jest pusty`
- **Komentarz `[ # Ponowne wywołanie - iterator dotarł do końca, jest pusty ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `weights = [10, 40, 320, 450, 70, 115, 3]`
- Nazwa **`weights`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Liczba **`10`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`40`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`320`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`450`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`70`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`115`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 3**: `filter_heavy = filter(lambda x: x < 100, weights)`
- Nazwa **`filter_heavy`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`filter`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Słowo kluczowe **`lambda`**: Słowo kluczowe języka Python: 'lambda'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`<`**: Znak mniejszości. Pyta: 'czy to po lewej jest mniejsze niż to po prawej?'.
- Liczba **`100`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`weights`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 4**: `print(list(filter_heavy))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`list`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`filter_heavy`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 5**: `print(list(filter_heavy))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`list`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`filter_heavy`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    # Ponowne wywołanie - iterator dotarł do końca, jest pusty
    weights = [10, 40, 320, 450, 70, 115, 3]
    filter_heavy = filter(lambda x: x < 100, weights)
    print(list(filter_heavy))
    print(list(filter_heavy))
    return

@app.cell
def _(mo):
    mo.md(r"""map - umożliwia zastosowanie danej operacji na każdym elemencie kolekcji i uzyskanie nowej kolekcji.

Szczególnie przydatne przy przetwarzaniu równoległym, gdy dla każdego z elementów należy wykonać skomplikowane obliczenia (przetwarzanie równoległe będzie omawiane później, poniższy przykład jest szeregowy)""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `def square(n):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`square`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`n`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 2**: `return n*n`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Nazwa **`n`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`*`**: Operator mnożenia (gwiazdka).
- Nazwa **`n`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 3**: `my_list = [2,3,4,5,6,7,8,9]`
- Nazwa **`my_list`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`4`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`5`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`6`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`7`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`8`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`9`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.

#### 👉 **Linia 4**: `updated_list = map(square, my_list)`
- Nazwa **`updated_list`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`map`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`square`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`my_list`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 5**: `#updated_list = map(lambda x: x*x, my_list)`
- **Komentarz `[ #updated_list = map(lambda x: x*x, my_list) ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 6**: `print('wskaznik',updated_list)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'wskaznik'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`updated_list`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 7**: `print(list(updated_list))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`list`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`updated_list`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    def square(n):
        return n*n
    my_list = [2,3,4,5,6,7,8,9]
    updated_list = map(square, my_list)
    #updated_list = map(lambda x: x*x, my_list)
    print('wskaznik',updated_list)
    print(list(updated_list))
    return

@app.cell
def _(mo):
    mo.md(r"""reduce - na podstawie kolekcji tworzy pojedynczą wartość, np. sumę:""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `from functools import reduce`
- Słowo kluczowe **`from`**: Słowo kluczowe 'from' (z). Używane przy importowaniu, oznacza 'Z tej konkretnej, dużej biblioteki załaduj tylko ten jeden określony fragment'.
- Nazwa **`functools`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`reduce`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 2**: `numbers = [ 1 , 2 , 3 , 4 , 5 ]`
- Nazwa **`numbers`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
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

#### 👉 **Linia 3**: `def il(a,b):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`il`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 4**: `return a*b`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`*`**: Operator mnożenia (gwiazdka).
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 5**: `result = reduce(il,numbers)`
- Nazwa **`result`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`reduce`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`il`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`numbers`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
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
    from functools import reduce
    numbers = [ 1 , 2 , 3 , 4 , 5 ]
    def il(a,b):
       return a*b
    result = reduce(il,numbers)
    print(result)
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `from functools import reduce`
- Słowo kluczowe **`from`**: Słowo kluczowe 'from' (z). Używane przy importowaniu, oznacza 'Z tej konkretnej, dużej biblioteki załaduj tylko ten jeden określony fragment'.
- Nazwa **`functools`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`reduce`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 2**: `numbers = [ 1 , 2 , 3 , 4 , 5 ]`
- Nazwa **`numbers`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
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

#### 👉 **Linia 3**: `sum_of_numbers = reduce(lambda x, y: x + y, numbers)`
- Nazwa **`sum_of_numbers`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`reduce`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Słowo kluczowe **`lambda`**: Słowo kluczowe języka Python: 'lambda'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`numbers`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 4**: `print(sum_of_numbers)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`sum_of_numbers`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 5**: `print(sum(numbers))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`sum`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`numbers`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    from functools import reduce
    numbers = [ 1 , 2 , 3 , 4 , 5 ]
    sum_of_numbers = reduce(lambda x, y: x + y, numbers)
    print(sum_of_numbers)
    print(sum(numbers))
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `from functools import reduce`
- Słowo kluczowe **`from`**: Słowo kluczowe 'from' (z). Używane przy importowaniu, oznacza 'Z tej konkretnej, dużej biblioteki załaduj tylko ten jeden określony fragment'.
- Nazwa **`functools`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`reduce`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 2**: `numbers = [ 1 , 2 , 3 , 4 , 5 ]`
- Nazwa **`numbers`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
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

#### 👉 **Linia 3**: `sum_of_numbers = reduce(lambda x, y: x + y, numbers,10)`
- Nazwa **`sum_of_numbers`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`reduce`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Słowo kluczowe **`lambda`**: Słowo kluczowe języka Python: 'lambda'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`numbers`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`10`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 4**: `#10 inicjalizacja`
- **Komentarz `[ #10 inicjalizacja ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 5**: `print(sum_of_numbers)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`sum_of_numbers`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 6**: `print(sum(numbers))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`sum`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`numbers`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    from functools import reduce
    numbers = [ 1 , 2 , 3 , 4 , 5 ]
    sum_of_numbers = reduce(lambda x, y: x + y, numbers,10)
    #10 inicjalizacja
    print(sum_of_numbers)
    print(sum(numbers))
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `from functools import reduce`
- Słowo kluczowe **`from`**: Słowo kluczowe 'from' (z). Używane przy importowaniu, oznacza 'Z tej konkretnej, dużej biblioteki załaduj tylko ten jeden określony fragment'.
- Nazwa **`functools`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`reduce`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 2**: `numbers = [ 1 , 2 , 3 , 4 , 5 ]`
- Nazwa **`numbers`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
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

#### 👉 **Linia 3**: `sum_of_numbers = reduce(lambda x, y: x+y if y%2==0 else x, numbers,0)`
- Nazwa **`sum_of_numbers`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`reduce`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Słowo kluczowe **`lambda`**: Słowo kluczowe języka Python: 'lambda'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`if`**: Słowo kluczowe 'if' (jeśli). Rozpoczyna instrukcję warunkową. Komputer sprawdzi postawiony warunek - jeśli jest on prawdziwy, wykona kod pod spodem.
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`%`**: Operator modulo (zwraca samą resztę z dzielenia dwóch liczb).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`==`**: Podwójny znak równości to 'operator porównania'. Komputer sprawdza, czy to co po lewej jest DOKŁADNIE TAKIE SAMO jak to po prawej. Zwraca odpowiedź Prawda (True) lub Fałsz (False).
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Słowo kluczowe **`else`**: Słowo kluczowe 'else' (w przeciwnym razie). Używane na samym końcu. Oznacza: 'Jeśli ŻADEN z wcześniejszych warunków nie był prawdziwy, wykonaj ostatecznie ten kod'.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`numbers`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 4**: `print(sum_of_numbers)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`sum_of_numbers`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    from functools import reduce
    numbers = [ 1 , 2 , 3 , 4 , 5 ]
    sum_of_numbers = reduce(lambda x, y: x+y if y%2==0 else x, numbers,0)
    print(sum_of_numbers)
    return

@app.cell
def _(mo):
    mo.md(r"""## Pytania


Co to jest wyrażenie lambda?
Napisać wyrażenie lambda które sumuje dwie liczby

""")
    return

@app.cell
def _():
    pass
    return

@app.cell
def _(mo):
    mo.md(r"""# Dekoratory, generatory, funkcje częściowe

Funkcje cząstkowe - przydatne, gdy nie chcemy wielokrotnie podawać tych samych wartości niektórych argumentów.""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `from functools import partial`
- Słowo kluczowe **`from`**: Słowo kluczowe 'from' (z). Używane przy importowaniu, oznacza 'Z tej konkretnej, dużej biblioteki załaduj tylko ten jeden określony fragment'.
- Nazwa **`functools`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
- Nazwa **`partial`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 3**: `def power(x, y):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`power`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 4**: `return x**y`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`**`**: Operator potęgowania (liczba do potęgi).
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 6**: `square = partial(power, y=2)`
- Nazwa **`square`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`partial`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`power`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 7**: `print(square(4))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`square`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`4`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    from functools import partial
    
    def power(x, y):
      return x**y
    
    square = partial(power, y=2)
    print(square(4))
    return

@app.cell
def _(mo):
    mo.md(r"""Generatory - funkcje umożliwiajace tworzenie iteratorów. Od zwykłych funkcji różnią się tym, że:
*   zwracają kolejną wartosć za pomocą słowa kluczowego yield
*   zapamiętują swój stan z momentu ostatniego wywołania
*   zwracaja kolejną wartość po zastosowaniu do nich polecenia next()""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `def generuj_parzyste(stop):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`generuj_parzyste`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`stop`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 2**: `x = 0`
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 3**: `while x < stop:`
- Słowo kluczowe **`while`**: Słowo kluczowe 'while' (dopóki). Rozpoczyna pętlę warunkową. Komputer będzie powtarzał kod pod spodem TAK DŁUGO, dopóki sprawdzany warunek jest wciąż prawdziwy.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`<`**: Znak mniejszości. Pyta: 'czy to po lewej jest mniejsze niż to po prawej?'.
- Nazwa **`stop`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 4**: `yield x`
- Słowo kluczowe **`yield`**: Słowo kluczowe języka Python: 'yield'. Jest to wbudowane polecenie o specjalnym znaczeniu.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 5**: `x += 2`
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`+=`**: Znak interpunkcyjny lub operator: '+='. Służy do organizacji struktury kodu.
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 7**: `generator = generuj_parzyste(6)`
- Nazwa **`generator`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`generuj_parzyste`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`6`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 8**: `print(next(generator))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`next`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`generator`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 9**: `print(next(generator))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`next`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`generator`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 10**: `print(next(generator))`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`next`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`generator`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 11**: `if generator==None:`
- Słowo kluczowe **`if`**: Słowo kluczowe 'if' (jeśli). Rozpoczyna instrukcję warunkową. Komputer sprawdzi postawiony warunek - jeśli jest on prawdziwy, wykona kod pod spodem.
- Nazwa **`generator`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`==`**: Podwójny znak równości to 'operator porównania'. Komputer sprawdza, czy to co po lewej jest DOKŁADNIE TAKIE SAMO jak to po prawej. Zwraca odpowiedź Prawda (True) lub Fałsz (False).
- Słowo kluczowe **`None`**: Słowo 'None' oznacza 'Nic'. Specjalna wartość mówiąca, że zmienna jest pusta, nie ma w niej zupełnie żadnej wartości, nawet zera.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 12**: `print('null')`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'null'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    def generuj_parzyste(stop):
      x = 0
      while x < stop:
        yield x
        x += 2
    
    generator = generuj_parzyste(6)
    print(next(generator))
    print(next(generator))
    print(next(generator))
    if generator==None:
      print('null')
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `# Użycie generatora z pętlą for`
- **Komentarz `[ # Użycie generatora z pętlą for ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

#### 👉 **Linia 2**: `generator = generuj_parzyste(12)`
- Nazwa **`generator`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`generuj_parzyste`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`12`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 3**: `for x in generator:`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`generator`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 4**: `print(x)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    # Użycie generatora z pętlą for
    generator = generuj_parzyste(12)
    for x in generator:
      print(x)
    return

@app.cell
def _(mo):
    mo.md(r"""W Pythonie funkcja jest obiektem""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `def func():`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`func`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 2**: `print('tekst')`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'tekst'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 3**: `f1=func`
- Nazwa **`f1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`func`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 4**: `f1()`
- Nazwa **`f1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    def func():
        print('tekst')
    f1=func
    f1()
    return

@app.cell
def _(mo):
    mo.md(r"""Jeśli f to funkcja, to jaka jest różnica między:
f2=f, a f2=f()?""")
    return

@app.cell
def _(mo):
    mo.md(r"""Dekorator - funkcja lub obiekt, który można wywołać przekazując mu jako argument dekorowaną funkcję lub klasę, w wyniku czego uzyska sie funkcję lub klasę o rozszerzonej funkcjonalności (udekorowaną)""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `def hello(func):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`hello`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`func`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 2**: `def inner():`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`inner`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 3**: `print("Witaj ")`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Witaj "`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 4**: `func()`
- Nazwa **`func`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 5**: `return inner`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Nazwa **`inner`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 7**: `def name():`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 8**: `print("Alu")`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Alu"`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 11**: `obj = hello(name)`
- Nazwa **`obj`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`hello`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 12**: `obj()`
- Nazwa **`obj`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    def hello(func):
        def inner():
            print("Witaj ")
            func()
        return inner
    
    def name():
        print("Alu")
    
    
    obj = hello(name)
    obj()
    return

@app.cell
def _(mo):
    mo.md(r"""W tym przypadku hello jest dekoratorem""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `def hello(func):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`hello`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`func`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 2**: `def inner():`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`inner`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 3**: `print("Witaj ",end="")`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`"Witaj "`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`end`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Tekst (String) **`""`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 4**: `func()`
- Nazwa **`func`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 5**: `return inner`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Nazwa **`inner`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 7**: `@hello`
- Znak **`@`**: Znak interpunkcyjny lub operator: '@'. Służy do organizacji struktury kodu.
- Nazwa **`hello`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 8**: `def name():`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 9**: `print('Ala')`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'Ala'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 11**: `name()`
- Nazwa **`name`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    def hello(func):
        def inner():
            print("Witaj ",end="")
            func()
        return inner
    
    @hello
    def name():
        print('Ala')
    
    name()
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `def log_input(funkcja):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`log_input`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`funkcja`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 2**: `def log(*args):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`log`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Znak **`*`**: Operator mnożenia (gwiazdka).
- Nazwa **`args`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 3**: `print('Input is', args)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'Input is'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`args`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 4**: `return log`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Nazwa **`log`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 6**: `@log_input`
- Znak **`@`**: Znak interpunkcyjny lub operator: '@'. Służy do organizacji struktury kodu.
- Nazwa **`log_input`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 7**: `def y(x):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 8**: `return 2*x + 1`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`*`**: Operator mnożenia (gwiazdka).
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

#### 👉 **Linia 10**: `@log_input`
- Znak **`@`**: Znak interpunkcyjny lub operator: '@'. Służy do organizacji struktury kodu.
- Nazwa **`log_input`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 11**: `def another_func(a, b, c):`
- Słowo kluczowe **`def`**: Słowo kluczowe 'def' (skrót od define) oznacza 'definiuj'. Informuje komputer: 'Teraz będę tworzyć nową, własną funkcję (czyli zestaw instrukcji, który dostanie swoją nazwę i będzie można go używać wielokrotnie).'
- Nazwa **`another_func`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`c`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 12**: `return a + 2*b + 3*c`
- Słowo kluczowe **`return`**: Słowo kluczowe 'return' (zwróć). Każe funkcji natychmiast się zakończyć i 'wypluć' wynik na zewnątrz, do miejsca, z którego funkcja została wezwana.
- Nazwa **`a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`*`**: Operator mnożenia (gwiazdka).
- Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`*`**: Operator mnożenia (gwiazdka).
- Nazwa **`c`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

#### 👉 **Linia 14**: `y(3)`
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 15**: `another_func(4, 2, 1)`
- Nazwa **`another_func`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`4`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    def log_input(funkcja):
      def log(*args):
        print('Input is', args)
      return log
    
    @log_input
    def y(x):
      return 2*x + 1
    
    @log_input
    def another_func(a, b, c):
      return a + 2*b + 3*c
    
    y(3)
    another_func(4, 2, 1)
    return

@app.cell
def _():
    pass
    return

@app.cell
def _(mo):
    mo.md(r"""## Praca  domowa



1. Utwórz  następujące funkcje:

def double(x):
    return 2 *x

def square(x):
    return x**2

def negative(x):
    return -x


2. Zdefiniuj listę transform składającą sie z funkcji:

double

square

negative

square
zainicjalizuj zmienną np. value
Napisz pętlę, która:
przejdzie przez wszystkie pozycje listy transform
za każdym razem wywoła odpowiednią funkcję, przekazując do niej aktualną wartość argumentu value i wyświetli aktualną wartość value""")
    return

@app.cell
def _(mo):
    mo.md(r"""Proszę napisać kod w sposób "pythonowy", wykorzystując wyrażenie lambda""")
    return

@app.cell
def _(mo):
    mo.md(r"""### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

#### 👉 **Linia 1**: `osoba={}`
- Nazwa **`osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Znak **`{`**: Lewy nawias klamrowy. Rozpoczyna słownik (zbiór par 'klucz: wartość') lub zbiór unikalnych elementów (set).
- Znak **`}`**: Prawy nawias klamrowy. Kończy słownik lub zbiór.

#### 👉 **Linia 2**: `x=int(input('Proszę podać liczbę osób: '))`
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`int`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`input`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'Proszę podać liczbę osób: '`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 3**: `for i in range(0,x):`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`i`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`range`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Liczba **`0`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
- Znak **`,`**: Przecinek. Służy do oddzielania od siebie wielu elementów (np. elementów na liście lub argumentów przekazywanych do funkcji).
- Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 4**: `nazwisko=input('Proszę podać nazwisko: ')`
- Nazwa **`nazwisko`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`input`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'Proszę podać nazwisko: '`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 5**: `osoba[nazwisko]=int(input('Proszę podać wiek: '))`
- Nazwa **`osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Nazwa **`nazwisko`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`int`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`input`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'Proszę podać wiek: '`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 6**: `y=int(input('Wypisanie nazwisk powyżej wieku: '))`
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
- Nazwa **`int`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`input`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Tekst (String) **`'Wypisanie nazwisk powyżej wieku: '`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 7**: `for key in osoba:`
- Słowo kluczowe **`for`**: Słowo kluczowe 'for' (dla). Rozpoczyna pętlę iteracyjną. Komputer będzie przechodził przez każdy jeden element z podanej kolekcji, krok po kroku, i wykonywał dla niego ten sam blok kodu.
- Nazwa **`key`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Słowo kluczowe **`in`**: Słowo kluczowe 'in' (w). Służy do sprawdzania czy dany element znajduje się Wewnątrz innej kolekcji (np. czy litera jest w słowie, albo liczba w liście).
- Nazwa **`osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 8**: `if osoba[key] > y:`
- Słowo kluczowe **`if`**: Słowo kluczowe 'if' (jeśli). Rozpoczyna instrukcję warunkową. Komputer sprawdzi postawiony warunek - jeśli jest on prawdziwy, wykona kod pod spodem.
- Nazwa **`osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`[`**: Lewy nawias kwadratowy. Oznacza początek listy (kolekcji wielu elementów ułożonych w rzędzie) lub służy do wybierania konkretnego, pojedynczego elementu z istniejącej kolekcji.
- Nazwa **`key`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`]`**: Prawy nawias kwadratowy. Kończy definicję listy lub operację wybierania elementu.
- Znak **`>`**: Znak większości. Pyta: 'czy to po lewej jest większe?'.
- Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

#### 👉 **Linia 9**: `print(key)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`key`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

#### 👉 **Linia 10**: `print(osoba)`
- Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
- Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
- Nazwa **`osoba`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
- Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
""")
    return
@app.cell
def _():
    osoba={}
    x=int(input('Proszę podać liczbę osób: '))
    for i in range(0,x):
        nazwisko=input('Proszę podać nazwisko: ')
        osoba[nazwisko]=int(input('Proszę podać wiek: '))
    y=int(input('Wypisanie nazwisk powyżej wieku: '))
    for key in osoba:
        if osoba[key] > y:
            print(key)
    print(osoba)
    return

if __name__ == "__main__":
    app.run()