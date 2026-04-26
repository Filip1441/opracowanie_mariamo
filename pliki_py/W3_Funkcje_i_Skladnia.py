import marimo

__generated_with = "0.23.3"
app = marimo.App(theme="dark")


@app.cell
def _():
    import marimo as mo
    return (mo,)



@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Generator range**: Wykorzystanie leniwego generatora `range()` do generowania sekwencji liczb bez alokowania pełnej listy w pamięci.
    - **Iteracja**: Zastosowanie pętli `for` do przetwarzania elementów sekwencji.
    - **Kontrola Przepływu**: Implementacja logiki warunkowej sterującej wykonaniem bloku kodu.
    """)
    return


@app.cell
def _():
    for i in range(3):
      _k=int(input('podaj _k'))
      if _k<0: break
    else: print('koniec')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Przykłady
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Generator range**: Wykorzystanie leniwego generatora `range()` do generowania sekwencji liczb bez alokowania pełnej listy w pamięci.
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    - **Iteracja**: Zastosowanie pętli `for` do przetwarzania elementów sekwencji.
    """)
    return


@app.cell
def _():
    #tworzymy listę składającą się z liczb od 0 do 9   kod w stylu C, ale nie pythona
    _kw=[]
    for i in range(10):
        _kw.append(i)
    print(_kw)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Generator range**: Wykorzystanie leniwego generatora `range()` do generowania sekwencji liczb bez alokowania pełnej listy w pamięci.
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    - **Iteracja**: Zastosowanie pętli `for` do przetwarzania elementów sekwencji.
    """)
    return


@app.cell
def _():
    #zapis bardziej pythonowy
    print(list([x for x in range(10)]))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Generator range**: Wykorzystanie leniwego generatora `range()` do generowania sekwencji liczb bez alokowania pełnej listy w pamięci.
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    """)
    return


@app.cell
def _():
    #zapis bardziej pythonowy
    print(list(range(10)))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Kontrola Przepływu**: Implementacja logiki warunkowej sterującej wykonaniem bloku kodu.
    """)
    return


@app.cell
def _():
    _a=True
    if _a==True:
        _b=1
    else:
        _b=2
    print(_b)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Kontrola Przepływu**: Implementacja logiki warunkowej sterującej wykonaniem bloku kodu.
    """)
    return


@app.cell
def _():
    #zapis bardziej pythonowy
    _a=True
    print(b := 1 if _a else 2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Generator range**: Wykorzystanie leniwego generatora `range()` do generowania sekwencji liczb bez alokowania pełnej listy w pamięci.
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    - **Iteracja**: Zastosowanie pętli `for` do przetwarzania elementów sekwencji.
    - **Kontrola Przepływu**: Implementacja logiki warunkowej sterującej wykonaniem bloku kodu.
    """)
    return


@app.cell
def _():
    # zapis w stylu C
    _lista=[1,2,3,4,5]
    _n=3
    for i in range(len(_lista)):
        if i > _n: print(_lista[i])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    - **Iteracja**: Zastosowanie pętli `for` do przetwarzania elementów sekwencji.
    - **Kontrola Przepływu**: Implementacja logiki warunkowej sterującej wykonaniem bloku kodu.
    """)
    return


@app.cell
def _():
    _lista=[1,2,3,4,5]
    _n=3
    for x in _lista: print(x if x>_n else "")
    return


@app.cell
def _():
    pass
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Napisać kod w którym  wprowadzam z klawiatury nazwę funkcji,która jest następnie wykonywana
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Metoda eval - umieszczenie fragmentu kodu z zewnątrz
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Dynamiczna Ewaluacja**: Funkcja `eval()` interpretuje ciąg znaków jako wyrażenie Pythona i zwraca jego wynik. Wymaga ostrożności ze względów bezpieczeństwa (code injection).
    """)
    return


@app.cell
def _():
    _source='print("test eval xxxx")'
    _result=eval(_source)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Dynamiczna Ewaluacja**: Funkcja `eval()` interpretuje ciąg znaków jako wyrażenie Pythona i zwraca jego wynik. Wymaga ostrożności ze względów bezpieczeństwa (code injection).
    """)
    return


@app.cell
def _():
    #wprowadzanie parametrów
    _var_x=55
    _source='print("test eval",_var_x)'
    print(_source)
    _result=eval(_source)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Dynamiczna Ewaluacja**: Funkcja `eval()` interpretuje ciąg znaków jako wyrażenie Pythona i zwraca jego wynik. Wymaga ostrożności ze względów bezpieczeństwa (code injection).
    """)
    return


@app.cell
def _():
    import math
    _x=2
    _source='math.sqrt(_x)'
    _result=eval(_source)
    print(_result)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Dynamiczna Ewaluacja**: Funkcja `eval()` interpretuje ciąg znaków jako wyrażenie Pythona i zwraca jego wynik. Wymaga ostrożności ze względów bezpieczeństwa (code injection).
    """)
    return


@app.cell
def _():
    #wprowadzanie parametrów
    _x=20
    _y=1000
    _source='_x/_y'
    _result=eval(_source)
    print(_result)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Dynamiczna Ewaluacja**: Funkcja `eval()` interpretuje ciąg znaków jako wyrażenie Pythona i zwraca jego wynik. Wymaga ostrożności ze względów bezpieczeństwa (code injection).
    """)
    return


@app.cell
def _():
    # wprowadzenie instrukcji z klawiatury
    _x=20
    _y=30
    _source=input("wprowadź instrukcję: ")
    _result=eval(_source)
    print(_result)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Funkcja exec wykonuje blok kodu, ale nie zwraca żadnej wartości
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Dynamiczne Wykonywanie**: Funkcja `exec()` pozwala na uruchamianie całych bloków kodu zapisanego w stringu. W przeciwieństwie do `eval`, nie zwraca wartości.
    """)
    return


@app.cell
def _():
    _var_x=20
    _source='_var_x=30'          #próba zmiany wartości
    _result=exec(_source)        #nic nie zwraca
    print(_result)
    print(_var_x)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Dynamiczne Wykonywanie**: Funkcja `exec()` pozwala na uruchamianie całych bloków kodu zapisanego w stringu. W przeciwieństwie do `eval`, nie zwraca wartości.
    """)
    return


@app.cell
def _():
    _var_x=20
    _source=input("podaj kod")          #próba zmiany wartości
    _result=exec(_source)                #nic nie zwraca
    print(_var_x)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Dynamiczne Wykonywanie**: Funkcja `exec()` pozwala na uruchamianie całych bloków kodu zapisanego w stringu. W przeciwieństwie do `eval`, nie zwraca wartości.
    """)
    return


@app.cell
def _():
    _var_x=20
    _source='''
    print("poprzednia wartość ",_var_x)
    _var_x=10

    '''
    _csource=compile(_source,'','exec')
    _result=exec(_csource)
    print("nowa wartość ",_var_x)
    print(_result)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    compile - tworzy kod wykonywalny (bytowy) z fragmentu kodu, ma to istotne znaczenie, jeśli dany fragment wykonujemy wiele razy.

    Funkcja compile() w Pythonie służy do kompilowania kodu źródłowego Pythona do kodu bajtowego, który jest gotowy do wykonania przez interpreter. Funkcja ta przyjmuje trzy argumenty:


    *   source - kod źródłowy Pythona, który ma być skompilowany. Może to być napis, plik lub obiekt typu code.
    *  filename - opcjonalny argument, który określa nazwę pliku, z którego został wczytany kod źródłowy. Jeśli argument ten nie jest przekazany, funkcja przyjmuje nazwę "<string>".
    * mode - tryb kompilacji, określający typ kodu źródłowego, który jest
    kompilowany. Dostępne wartości to:
    'exec': kod źródłowy jest skryptem, który ma być wykonany
    'eval': kod źródłowy jest wyrażeniem, które ma być obliczone
    'single': kod źródłowy jest instrukcją pojedynczą, która ma być wykonana
    """)
    return


if __name__ == "__main__":
    app.run()
