import marimo

__generated_with = "0.23.3"
app = marimo.App(theme="dark")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Import**: Załadowanie modułu `marimo` pod aliasem `mo`. Standardowa praktyka w Pythonie służąca skracaniu odwołań do biblioteki.
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
    ### 💻 ANALIZA TECHNICZNA
    - **Instrospekcja**: Wywołanie wbudowanej funkcji `help()` z argumentem `max`. Funkcja ta wyciąga docstring (dokumentację) podanego obiektu, prezentując sygnaturę i opis działania.
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
    ### 💻 ANALIZA TECHNICZNA
    - **Zmienne i Operatory**: Inicjalizacja zmiennych liczbowych i wykonanie operacji mnożenia. Python automatycznie rozpoznaje typ `int`. Wynik operacji w notebooku jest automatycznie wypisywany (REPL).
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
    ### 💻 ANALIZA TECHNICZNA
    - **Dzielenie**: Operator `/` w Pythonie 3 zawsze zwraca typ zmiennoprzecinkowy (`float`), nawet jeśli wynik jest liczbą całkowitą.
    """)
    return


@app.cell
def _():
    17 / 2  # dzielenie
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Dzielenie całkowite**: Operator `//` wykonuje dzielenie z ucięciem części ułamkowej (floor division), zwracając wyłącznie część całkowitą.
    """)
    return


@app.cell
def _():
    8 // 3  # dzielenie całkowite
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Analiza**: Implementacja logiki algorytmu z wykorzystaniem standardowej składni i wbudowanych mechanizmów Pythona.
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
    ### 💻 ANALIZA TECHNICZNA
    - **Formatowanie i Komentarze**: Wykorzystanie operatora kontynuacji linii `\` (backslash) do łamania długich instrukcji. Wskazanie na dowolność umieszczania komentarzy inline za pomocą znaku `#`.
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
    print(_iloczyn_o_bardzo_dlugiej_nazwie)
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
    ### 💻 ANALIZA TECHNICZNA
    - **Nazewnictwo (Identyfikatory)**: Przykłady poprawnych nazw zmiennych. Python dopuszcza litery, cyfry (nie na początku) oraz podkreślenia. Wielkość liter ma znaczenie (`STALA` != `stala`).
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
    ### 💻 ANALIZA TECHNICZNA
    - **Błąd Składniowy**: Próba rozpoczęcia identyfikatora od cyfry `1_a`. Python zgłosi `SyntaxError`, ponieważ parser oczekuje w tym miejscu literału liczbowego, a nie nazwy zmiennej.
    """)
    return


app._unparsable_cell(
    r"""
    #kod z błędem
    1_a=5
    """,
    name="_"
)


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
    ### 💻 ANALIZA TECHNICZNA
    - **Output**: Funkcja `print()` służy do wysyłania danych do standardowego wyjścia (stdout). Przyjmuje obiekty, konwertuje je na tekst i dodaje znak nowej linii.
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
    ### 💻 ANALIZA TECHNICZNA
    - **Instrukcja warunkowa**: Słowo kluczowe `if` ewaluuje wyrażenie logiczne `_temperature >= 18`. Zakończenie linii dwukropkiem `:` definiuje początek bloku kodu, który musi posiadać wcięcie (indentację). Blok ten zostanie wykonany tylko jeśli wynik porównania to `True`.
    """)
    return


@app.cell
def _():
    #kod poprawny
    _temperature = 90
    print('Hello')
    if _temperature >= 18:
      print('Nice weather')
      _x = 3
    _b = 7
    print('How are you?')
    print(_x)
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
    ### 💻 ANALIZA TECHNICZNA
    - **Indentyfikacja błędów wcięć**: W Pythonie `IndentationError` występuje, gdy instrukcje wewnątrz bloku (np. po `if`) nie mają spójnego poziomu wcięć. Kod po lewej stronie musi być wyrównany pionowo w ramach tego samego bloku.
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
    ### 💻 ANALIZA TECHNICZNA
    - **Truthiness**: W Pythonie wartości liczbowe różne od zera są ewaluowane jako `True` w kontekście logicznym. Zmienna `_x = 1.1` spełnia warunek `if _x:`.
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
    ### 💻 ANALIZA TECHNICZNA
    - **Typ Bool**: Zastosowanie literałów logicznych `True` i `False`. Służą one do bezpośredniego sterowania przepływem programu w instrukcjach warunkowych.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Liczby Zespolone**: Python natywnie wspiera typ `complex`. Część urojoną definiuje się za pomocą sufiksu `j`. Operacje arytmetyczne na tych liczbach są wbudowane w interpreter.
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
    ### 💻 ANALIZA TECHNICZNA
    - **Biblioteki Standardowe**: Import modułu `math` umożliwia dostęp do zaawansowanych funkcji matematycznych i stałych (np. `math.pi`).
    - **Namespace**: Odwołania `math.sin()` wykorzystują operator kropki do nawigacji w przestrzeni nazw modułu.
    """)
    return


@app.cell
def _():
    import math
    import numpy as np
    _x=math.pi
    print(_x)
    print(np.sin(np.pi))
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
    ### 💻 ANALIZA TECHNICZNA
    - **Operatory Logiczne**: Zastosowanie słowa kluczowego `and`. Warunek jest spełniony tylko wtedy, gdy oba operandy (`_x` oraz `_y`) są oceniane jako `True`. W Pythonie zachodzi tzw. "short-circuit evaluation" (jeśli pierwszy element `and` jest fałszywy, drugi nie jest sprawdzany).
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
