import marimo

__generated_with = "0.23.3"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

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

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Wykład 1: Wstęp i Fundamenty
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### TEORIA: Filozofia i Składnia
    Python używa wcięć (indentacji) zamiast klamerek `{}`. Każdy znak ma znaczenie:
    - `:` na końcu linii oznacza początek bloku kodu.
    - `#` oznacza komentarz ignorowany przez interpreter.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Wykład 1

    ## Plan


    *   Wstęp
    *   Narzędzia programistyczne
    *   Typy zmiennych
    *   Kolekcje
    *   Instrukcje
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Wstęp
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Trochę historii

    *   Nazwa języka pochodzi od serialu BBC Latający Cyrk Monty Pythona.
    *   Twórcą Pythona jest holender Guido van Rossum.
    *   Python (jego interpreter) zaczął powstawać od 1989.
    *   Od wersji 2.1 (2001) język jest rozwijany jako projekt Open Source przez niedochodową organizację Python Software Foundation (PSF).
    *   Od 2008 istnieją dwie gałęzie: Python 2 i Python 3.
    *   Wersja 2 nie będzie rozwijana
    *   Kod napisany w Pythonie 2 może być prawie mechanicznie przetaumaczony na Pythona 3. Istnieje narzędzie 2to3 stworzone do tego celu. Inne narzędzie to 3to2, które wykonuje konwersję w drugą stronę.

    Daty wydania:
       Python 3

    *   3.11.2  8 lutego 2023
    *   3.9 -- 2021-02-19
    *   3.8 -- 2020-02-01
    *   3.7 -- 2018-06-27
    *   3.6 -- 2016-12-23
    *   3.5 -- 2015-09-13
    *   3.4 -- 2014-03-17
    *   3.3 -- 2012-09-29
    *   3.2 -- 2011-02-20
    *   3.1 -- 2009-06-26
    *   3.0 -- 2008-12-03


       Python 2


    *   2.7 -- 2010-07-03
    *   2.6 -- 2008-10-02
    *   2.5 -- 2006-09-19
    *   2.4 -- 2004-11-30
    *   2.3 -- 2003-07-29
    *   2.2 -- 2001-12-21
    *   2.1 -- 2001-04-15
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
 
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    "Python – język programowania wysokiego poziomu ogólnego przeznaczenia, o rozbudowanym pakiecie bibliotek standardowych, którego ideą przewodnią jest czytelność i klarowność kodu źródłowego.
    Jego składnia cechuje się przejrzystością i zwięzłością."   - Wikipedia (to zależy)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Trochę filozofii

    *   Python nie wymusza jednego stylu programowania, możliwe jest programowanie obiektowe, strukturalne, funkcyjne.
    *   Typy sprawdzane są dynamicznie, do zarządzania pamięcią stosuje się garbage collection.
    *   Projektanci Pythona odrzucili złożoną skaadnię Perla na rzecz bardziej oszczędnej.
    *   Niezależny od systemu operacyjnego.
    *   Łatwe łączenie z C++ lub Javą
    *   Python jest klasyfikowany jako język skryptowy.
    *   Wykorzystuje się go do tworzenia dużych projektów.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Narzędzia




    *   PyCharm
    *   VS Code
    *  Sublime Text
    *  Jupyter
    *  VIM
    *  IDLE
    *  Notepad++
    *  **Spyder**
    *  Thonny
    *  **google colab**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Funkcja help

    Bardzo przydatną funkcją jest funkcja help.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

    Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

    #### 👉 **Linia 1**: `help(max)`
    - Nazwa **`help`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
    - Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
    - Nazwa **`max`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
    - Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
    """)
    return


@app.cell
def _():
    help(max)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Python jako kalkulator
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

    Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

    #### 👉 **Linia 1**: `width = 10`
    - Nazwa **`width`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
    - Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
    - Liczba **`10`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

    #### 👉 **Linia 2**: `height = 15`
    - Nazwa **`height`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
    - Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
    - Liczba **`15`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

    #### 👉 **Linia 3**: `width * height`
    - Nazwa **`width`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
    - Znak **`*`**: Operator mnożenia (gwiazdka).
    - Nazwa **`height`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
    """)
    return


@app.cell
def _():
    _width = 10
    _height = 15
    _width * _height
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

    Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

    #### 👉 **Linia 1**: `17 / 2  # dzielenie`
    - Liczba **`17`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
    - Znak **`/`**: Operator dzielenia.
    - Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
    - **Komentarz `[ # dzielenie ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.
    """)
    return


@app.cell
def _():
    17 / 2  # dzielenie
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

    Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

    #### 👉 **Linia 1**: `8 // 3  # dzielenie całkowite`
    - Liczba **`8`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
    - Znak **`//`**: Operator dzielenia całkowitego (dzieli i odrzuca resztę, zostawiając samą całość).
    - Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
    - **Komentarz `[ # dzielenie całkowite ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.
    """)
    return


@app.cell
def _():
    8 // 3  # dzielenie całkowite
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

    Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

    #### 👉 **Linia 1**: `5 ** 3  # potęgowanie`
    - Liczba **`5`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
    - Znak **`**`**: Operator potęgowania (liczba do potęgi).
    - Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
    - **Komentarz `[ # potęgowanie ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.
    """)
    return


@app.cell
def _():
    5 ** 3  # potęgowanie
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Struktura programu

    *   Nie musimy wywoływać main (chociaż jest przydatne)
    *   Brak jawnej deklaracji zmiennych
    *   Nie ma skrótów typu i++
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

    Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

    #### 👉 **Linia 1**: `# Komentarz można zacząć w dowolnym miejscu`
    - **Komentarz `[ # Komentarz można zacząć w dowolnym miejscu ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

    #### 👉 **Linia 2**: `pierwszy_czynnik_0_dlugiej_nazwie = 3  # i trwa on do końca linii`
    - Nazwa **`pierwszy_czynnik_0_dlugiej_nazwie`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
    - Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
    - Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
    - **Komentarz `[ # i trwa on do końca linii ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

    #### 👉 **Linia 3**: `drugi_czynnik_o_jeszcze_dluzszej_nazwie = 2`
    - Nazwa **`drugi_czynnik_o_jeszcze_dluzszej_nazwie`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
    - Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
    - Liczba **`2`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

    #### 👉 **Linia 4**: `# Linie można dzielić`
    - **Komentarz `[ # Linie można dzielić ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

    #### 👉 **Linia 5**: `iloczyn_o_bardzo_dlugiej_nazwie = pierwszy_czynnik_0_dlugiej_nazwie * \`
    - Nazwa **`iloczyn_o_bardzo_dlugiej_nazwie`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
    - Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
    - Nazwa **`pierwszy_czynnik_0_dlugiej_nazwie`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
    - Znak **`*`**: Operator mnożenia (gwiazdka).

    #### 👉 **Linia 6**: `drugi_czynnik_o_jeszcze_dluzszej_nazwie`
    - Nazwa **`drugi_czynnik_o_jeszcze_dluzszej_nazwie`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
    """)
    return


@app.cell
def _():
    # Komentarz można zacząć w dowolnym miejscu
    _pierwszy_czynnik_0_dlugiej_nazwie = 3  # i trwa on do końca linii
    _drugi_czynnik_o_jeszcze_dluzszej_nazwie = 2
    # Linie można dzielić
    _iloczyn_o_bardzo_dlugiej_nazwie = _pierwszy_czynnik_0_dlugiej_nazwie * \
    _drugi_czynnik_o_jeszcze_dluzszej_nazwie
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Identyfikatory

    *   Identyfikatory zaczynają się od litery lub znaku podkreślenia i skłądaja się z ciągu liter, cyfr lub znaków podkreślenia.
    *   Wielkie i małe litery są rozróżniane.
    *   Dla zwiększenia czytelności stosuje się pewne konwencje nazewnictwa, jednak nie są one wymuszane przez interpreter.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

    Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

    #### 👉 **Linia 1**: `#kod poprawny`
    - **Komentarz `[ #kod poprawny ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

    #### 👉 **Linia 2**: `x_1 = 1`
    - Nazwa **`x_1`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
    - Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
    - Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

    #### 👉 **Linia 3**: `_a = 7`
    - Nazwa **`_a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
    - Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
    - Liczba **`7`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

    #### 👉 **Linia 4**: `STALA = 4`
    - Nazwa **`STALA`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
    - Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
    - Liczba **`4`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
    """)
    return


@app.cell
def _():
    #kod poprawny
    _x_1 = 1
    _a = 7
    _STALA = 4
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

    Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

    #### 👉 **Linia 1**: `#kod z błędem`
    - **Komentarz `[ #kod z błędem ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

    #### 👉 **Linia 2**: `1_a = 5`
    - Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
    - Nazwa **`_a`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
    - Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
    - Liczba **`5`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
    """)
    return


@app.cell
def _():
    #kod z błędem
    # 1_a = 5
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Budowa programu

    Program języka Python w najprostszym przypadku zapisany może być w zwykłym pliku tekstowym o rozszerzeniu .py
    Tutaj wykorzystujemy notebook Google colabolatory, wygodniejszy do nauki.
    Najprostszy program moze składać się z jednej instrukcji:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

    Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

    #### 👉 **Linia 1**: `print('Hello')`
    - Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
    - Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
    - Tekst (String) **`'Hello'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
    - Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
    """)
    return


@app.cell
def _():
    print('Hello')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Kod języka Python zorganizowany jest w bloki o równym wcięciu (odpwoiadajace nawiasom klamrowym w C)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

    Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

    #### 👉 **Linia 1**: `#kod poprawny`
    - **Komentarz `[ #kod poprawny ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

    #### 👉 **Linia 2**: `temperature = 22`
    - Nazwa **`temperature`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
    - Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
    - Liczba **`22`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

    #### 👉 **Linia 3**: `print('Hello')`
    - Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
    - Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
    - Tekst (String) **`'Hello'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
    - Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

    #### 👉 **Linia 4**: `if temperature >= 18:`
    - Słowo kluczowe **`if`**: Słowo kluczowe 'if' (jeśli). Rozpoczyna instrukcję warunkową. Komputer sprawdzi postawiony warunek - jeśli jest on prawdziwy, wykona kod pod spodem.
    - Nazwa **`temperature`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
    - Znak **`>=`**: Znak większy lub równy.
    - Liczba **`18`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
    - Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

    #### 👉 **Linia 5**: `print('Nice weather')`
    - Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
    - Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
    - Tekst (String) **`'Nice weather'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
    - Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

    #### 👉 **Linia 6**: `x = 3`
    - Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
    - Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
    - Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

    #### 👉 **Linia 7**: `b = 7`
    - Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
    - Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
    - Liczba **`7`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

    #### 👉 **Linia 8**: `print('How are you?')`
    - Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
    - Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
    - Tekst (String) **`'How are you?'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
    - Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
    """)
    return


@app.cell
def _():
    #kod poprawny
    _temperature = 22
    print('Hello')
    if _temperature >= 18:
      print('Nice weather')
      _x = 3
    _b = 7
    print('How are you?')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Głębokość wcięcia moze być dowolna, zwykle są to 2 lub 4 spacje.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

    Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

    #### 👉 **Linia 1**: `#kod zawiera błąd`
    - **Komentarz `[ #kod zawiera błąd ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

    #### 👉 **Linia 2**: `temperature = 22`
    - Nazwa **`temperature`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
    - Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
    - Liczba **`22`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

    #### 👉 **Linia 3**: `print('Hello')`
    - Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
    - Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
    - Tekst (String) **`'Hello'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
    - Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

    #### 👉 **Linia 4**: `if temperature >= 18:`
    - Słowo kluczowe **`if`**: Słowo kluczowe 'if' (jeśli). Rozpoczyna instrukcję warunkową. Komputer sprawdzi postawiony warunek - jeśli jest on prawdziwy, wykona kod pod spodem.
    - Nazwa **`temperature`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
    - Znak **`>=`**: Znak większy lub równy.
    - Liczba **`18`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
    - Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

    #### 👉 **Linia 5**: `print('Nice weather')`
    - Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
    - Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
    - Tekst (String) **`'Nice weather'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
    - Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

    #### 👉 **Linia 6**: `x = 3`
    - Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
    - Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
    - Liczba **`3`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

    #### 👉 **Linia 7**: `b = 7                      #błędna linia`
    - Nazwa **`b`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
    - Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
    - Liczba **`7`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
    - **Komentarz `[ #błędna linia ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

    #### 👉 **Linia 8**: `print('How are you?')`
    - Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
    - Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
    - Tekst (String) **`'How are you?'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
    - Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
    """)
    return


@app.cell
def _():
    #kod zawiera błąd
    _temperature = 22
    print('Hello')
    if _temperature >= 18:
        print('Nice weather')
        _x = 3
        _b = 7                      #błędna linia
    print('How are you?')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Wcięcia muszą byc równe.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Typy danych

    Typ danych nie jest w Pythonie pojęciem identycznym jak w C/C++, nie jest jawnie definiowany. Python skupia się raczej na właściwościach obiektów. Niemniej wyróznić można następujące typy podstawowe:
    *   float
    *   int
    *   complex (liczby zepsolone)
    *   bool
    *   String (zapisywane 'tak' lub "tak")
    *   listy
    *   krotki
    *   słowniki
    *   zbiory
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # bool
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

    Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

    #### 👉 **Linia 1**: `x=1.1`
    - Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
    - Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
    - Liczba **`1.1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

    #### 👉 **Linia 2**: `if x:`
    - Słowo kluczowe **`if`**: Słowo kluczowe 'if' (jeśli). Rozpoczyna instrukcję warunkową. Komputer sprawdzi postawiony warunek - jeśli jest on prawdziwy, wykona kod pod spodem.
    - Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
    - Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

    #### 👉 **Linia 3**: `print(x)`
    - Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
    - Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
    - Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
    - Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
    """)
    return


@app.cell
def _():
    _x=1.1
    if _x:
        print(_x)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

    Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

    #### 👉 **Linia 1**: `x=True`
    - Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
    - Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
    - Słowo kluczowe **`True`**: Wartość logiczna 'True' (Prawda). Oznacza stan włączenia, potwierdzenie, że coś jest zgodne z prawdą (w pamięci komputera to jedynka: 1).

    #### 👉 **Linia 2**: `y=False`
    - Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
    - Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
    - Słowo kluczowe **`False`**: Wartość logiczna 'False' (Fałsz). Oznacza stan wyłączenia, niezgodność (w pamięci komputera to zero: 0).

    #### 👉 **Linia 3**: `if x:`
    - Słowo kluczowe **`if`**: Słowo kluczowe 'if' (jeśli). Rozpoczyna instrukcję warunkową. Komputer sprawdzi postawiony warunek - jeśli jest on prawdziwy, wykona kod pod spodem.
    - Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
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
    _x=True
    _y=False
    if _x:
        print(_x)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## *Complex*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

    Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

    #### 👉 **Linia 1**: `x=3j`
    - Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
    - Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
    - Liczba **`3j`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

    #### 👉 **Linia 2**: `y=1+1j`
    - Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
    - Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
    - Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
    - Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
    - Liczba **`1j`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.

    #### 👉 **Linia 3**: `print(x+y)`
    - Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
    - Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
    - Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
    - Znak **`+`**: Operator dodawania. Służy do sumowania liczb lub łączenia tekstów ze sobą.
    - Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
    - Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
    """)
    return


@app.cell
def _():
    _x=3j
    _y=1+1j
    print(_x+_y)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Operacje matematyczne
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    acos(x) - arcus cosinus argumentu x

    asin(x) - arcus sinus argumentu x

    atan(x) - arcus tangens argumentu x

    atan2(y, x) -  wartość atan(y / x)

    cos(x) - cosinus argumentu x

    cosh(x) - cosinus hiperboliczny argumentu x.

    degrees(x) - przekształca kąt x z radianów na stopnie.

    exp(x) - zwraca wartość e**x.

    fabs(x) - wraca moduł (wartość bezwzględną) argumentu x.

    floor(x) - obcięcie do liczby całkowitej

    hypot(x, y) -  zwraca wartość sqrt(x*x + y*y)

    log(x[, podstawa_logarytmu])

    log10(x)

    radians(x)

    sin(x)

    sinh(x)

    sqrt(x)

    tan(x)

    tanh(x)

    ** użycie funkcji matematycznych wymaga importu pakietu math **
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

    Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

    #### 👉 **Linia 1**: `import math`
    - Słowo kluczowe **`import`**: Słowo kluczowe 'import'. Nakazuje komputerowi 'załaduj dodatkowe, zaawansowane narzędzia z zewnętrznej biblioteki, których nie ma w standardowym, podstawowym zestawie Pythona'.
    - Nazwa **`math`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

    #### 👉 **Linia 2**: `x=math.pi`
    - Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
    - Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
    - Nazwa **`math`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
    - Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
    - Nazwa **`pi`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.

    #### 👉 **Linia 3**: `print(x)`
    - Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
    - Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
    - Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
    - Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.

    #### 👉 **Linia 4**: `print(math.sin(x))`
    - Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
    - Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
    - Nazwa **`math`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
    - Znak **`.`**: Kropka. To jest tzw. 'operator dostępu'. Działa jak polecenie 'wejdź w ten obiekt przed kropką i użyj jego funkcji lub właściwości znajdującej się po kropce'.
    - Nazwa **`sin`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
    - Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
    - Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
    - Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
    - Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
    """)
    return


@app.cell
def _():
    import math
    _x=math.pi
    print(_x)
    print(math.sin(_x))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Operacje logiczne
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🧠 SZCZEGÓŁOWA ANALIZA KODU KROK PO KROKU (Dla całkowicie początkujących)

    Poniżej znajduje się absolutnie szczegółowe, łopatologiczne wyjaśnienie każdego znaku, słowa i polecenia z komórki z kodem poniżej:

    #### 👉 **Linia 1**: `x=1  #True`
    - Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
    - Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
    - Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
    - **Komentarz `[ #True ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

    #### 👉 **Linia 2**: `y=1  #True`
    - Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
    - Znak **`=`**: Znak równości to w programowaniu 'operator przypisania'. Działa jak wkładanie rzeczy do podpisanego pudełka: bierze wartość po prawej stronie i zapisuje ją pod nazwą po lewej stronie. To NIE JEST równanie matematyczne.
    - Liczba **`1`**: To jest wartość liczbowa. Komputer potrafi wykonywać na niej operacje matematyczne. Jeśli nie ma kropki, to liczba całkowita. Jeśli ma kropkę, to ułamek dziesiętny.
    - **Komentarz `[ #True ]`**: To jest notatka zostawiona przez programistę dla ludzi. Komputer całkowicie to ignoruje i nie wykonuje tego. Służy tylko do opisu.

    #### 👉 **Linia 3**: `if x and y:`
    - Słowo kluczowe **`if`**: Słowo kluczowe 'if' (jeśli). Rozpoczyna instrukcję warunkową. Komputer sprawdzi postawiony warunek - jeśli jest on prawdziwy, wykona kod pod spodem.
    - Nazwa **`x`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
    - Słowo kluczowe **`and`**: Słowo 'and' (i / oraz). Łączy dwa warunki. Całość jest prawdziwa TYLKO WTEDY, gdy oba połączone warunki naraz są prawdziwe.
    - Nazwa **`y`**: To jest nazwa (identyfikator). Może to być nazwa zmiennej (pojemnika na dane), funkcji (gotowego przepisu na wykonanie zadania) lub metody.
    - Znak **`:`**: Dwukropek. Jest to znak 'uwaga, teraz nastąpi zagnieżdżony blok kodu!'. Występuje zawsze po instrukcjach warunkowych (if), pętlach (for/while) czy definicjach (def). Wszystko poniżej tego znaku musi mieć wcięcie.

    #### 👉 **Linia 4**: `print('and')`
    - Słowo kluczowe **`print`**: Wbudowana funkcja 'print' (drukuj). Jej głównym zadaniem jest wyświetlenie tekstu lub wyliczonej wartości zmiennych na ekranie komputera, żeby człowiek mógł to zobaczyć i przeczytać.
    - Znak **`(`**: Lewy nawias okrągły. Rozpoczyna listę argumentów (parametrów i informacji) podawanych do funkcji, albo po prostu grupuje działania matematyczne (jak w matematyce).
    - Tekst (String) **`'and'`**: To jest ciąg znaków (tekst). Zawsze znajduje się w cudzysłowach lub apostrofach. Komputer traktuje to dosłownie jako napis, a nie jako polecenie do wykonania.
    - Znak **`)`**: Prawy nawias okrągły. Kończy argumenty funkcji lub grupowanie.
    """)
    return


@app.cell
def _():
    _x=1  #True
    _y=1  #True
    if _x and _y:
        print('and')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Typ **String**
    """)
    return


if __name__ == "__main__":
    app.run()
