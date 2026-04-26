import marimo

__generated_with = "0.23.3"
app = marimo.App(theme="dark")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Analiza**: Implementacja logiki algorytmu z wykorzystaniem standardowej składni i wbudowanych mechanizmów Pythona.
    """)
    return
@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Wykład 2: Kolekcje i Logika
    """)
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
    _a="100"
    _b="200"
    print(_a+_b)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Operacje w klasie str



    *   len -  określenie długości
    *   pobieranie konkretnego znaku, jest takie jak pobieranie elementu tablicy
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    """)
    return
@app.cell
def _():
    _a="abcd"
    print("długość ",len(_a))
    print("drugi znak ",_a[3])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    """)
    return
@app.cell
def _():
    # pobieranie fragmentu

    _a="abcd"
    _b=_a[1:3]
    print(_b)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    """)
    return
@app.cell
def _():
    _a="abcdefgh"
    _b=_a[0:-2]
    print(_b)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Rzutowanie typów sczególnie ze string na liczby jest łatwiejsze niż np. w Javie.
    """)
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
    _a="100"
    _b="200"
    print(_a+_b)
    print(int(_a)+int(_b))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Sprawdzenie typu
    """)
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
    _a="100"
    _b=100j
    print(type(_a))
    print(_a)
    print(type(_b))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Typowanie**: Wykorzystanie `isinstance()` do dynamicznej weryfikacji przynależności obiektu do klasy lub typu. Jest to bezpieczniejsza alternatywa dla `type() == ...` ze względu na obsługę dziedziczenia.
    - **Kontrola Przepływu**: Implementacja logiki warunkowej sterującej wykonaniem bloku kodu.
    """)
    return
@app.cell
def _():
    _a=100j
    if isinstance(_a,int): print("int")
    else: print("not int")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Kolekcje

    ## Listy

    Przypominają tablice z innych języków lub wektory z C++. Mogą skłądać się z elementów różnego typu.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    """)
    return
@app.cell
def _():
    _lista = [7, 2, 5, 4]
    print(_lista)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Dodanie elementu do listy
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    """)
    return
@app.cell
def _():
    _lista_1 = [1, 'a', 2, 'b']
    _lista_1.append(3)
    print(_lista_1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Połączenie list
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    """)
    return
@app.cell
def _():
    _lista_1 = [1, 'a', 2, 'b']
    _lista = [3, 'x', 2, 'b']
    _lista_1.extend(_lista)
    print(_lista_1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    """)
    return
@app.cell
def _():
    _lista_1 = [1, 'a', 2, 'b']
    _lista = [3, 'x', 2, 'b']
    _lista_1 += _lista
    print(_lista_1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Sortowanie
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    """)
    return
@app.cell
def _():
    _lista = ['x', 'u', 'b']
    _lista.sort()
    print(_lista)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Zmiana kolejności
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    """)
    return
@app.cell
def _():
    _lista = ['z', 'x', 'u', 'b']
    _lista.reverse()
    print(_lista)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    """)
    return
@app.cell
def _():
    _lista = ['z', 'x', 'u', 'b']
    _lista.pop(2)
    print(_lista)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Przypisanie wartości

    Jeśli a i b są listami, to instrukcja a = b powoduje przypisanie referencji, zmiany listy a będą powodowały zmiany listy b i odwrotnie. Jeśli chcemy kopiować listy, to uzywamy a = b[:]
    _Instrukcja == porównuje zawartość, instrukcja is sprawdza referencję.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    """)
    return
@app.cell
def _():
    _a = [1, 2, 3, 4, 5]
    _b = _a  #  przypisanie referencji
    print(_a == _b)  # porównanie wartości
    print(_a is _b)  # porównanie referencji
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    """)
    return
@app.cell
def _(a):
    _b = a[:]  #kopiowanie tablic, powstanie nowa tablica
    print(a == _b)
    print(a is _b)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    """)
    return
@app.cell
def _(a):
    print(a[0:3])
    print(a[0:-2])
    print(a[-3:-1])
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
    print(list(range(1,5,2)))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Krotki (ang. tuple)

    Przypominają listy, ale są niezmienne (nie mozna zmieniać ich elementów, nie są jednak odpwiednikiem stałych z C, bo jako całość mogą ulec zmianie).
    """)
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
    _ip_address = ('10.20.30.40', 8080)
    print(_ip_address)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    """)
    return
@app.cell
def _():
    _ip_address = ('10.20.30.40', 8080)
    print(_ip_address[0])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    """)
    return
@app.cell
def _():
    #próba zmiany, błąd
    _ip_address = ('10.20.30.40', 8080)
    _ip_address[0] = '10.20.30.250'
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
    # a to jest poprawne
    _ip_address1 = ('10.20.30.40', 8080)
    _ip_address1 = ('10.20.30.50', 8082)
    print(_ip_address1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Zbiory

    Zawieraja elementy unikalne i nie są uporządkowane.
    """)
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
    _duze_miasta = {'Warszawa', 'Kraków', 'Gdańsk'}
    _miasta_mazowsza = {'Radom', 'Płock', 'Warszawa'}
    _stolice_europy = {'Paryż', 'Berlin', 'Warszawa'}
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Iloczyn zbiorów
    """)
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
    _duze_miasta = {'Warszawa', 'Kraków', 'Gdańsk'}
    _miasta_mazowsza = {'Radom', 'Płock', 'Warszawa'}
    _stolice_europy = {'Paryż', 'Berlin', 'Warszawa'}
    _duze_miasta_mazowsza = _duze_miasta.intersection(_miasta_mazowsza)
    print(_duze_miasta_mazowsza)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Różnica zbiorów
    """)
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
    _duze_miasta = {'Warszawa', 'Kraków', 'Gdańsk'}
    _miasta_mazowsza = {'Radom', 'Płock', 'Warszawa'}
    _stolice_europy = {'Paryż', 'Berlin', 'Warszawa'}
    _male_miasta_mazowsza = _miasta_mazowsza.difference(_duze_miasta)
    print(_male_miasta_mazowsza)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Sprawdzenie podzbiorów i rozłączności
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Analiza**: Implementacja logiki algorytmu z wykorzystaniem standardowej składni i wbudowanych mechanizmów Pythona.
    """)
    return
@app.cell
def _(duze_miasta_mazowsza):
    _duze_miasta = {'Warszawa', 'Kraków', 'Gdańsk'}
    _miasta_mazowsza = {'Radom', 'Płock', 'Warszawa'}
    _stolice_europy = {'Paryż', 'Berlin', 'Warszawa'}
    _male_miasta_mazowsza = _miasta_mazowsza.difference(_duze_miasta)
    print(duze_miasta_mazowsza.issubset(_stolice_europy))
    print(_male_miasta_mazowsza.isdisjoint(_stolice_europy))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Sprawdzanie przynależności elementu do zbioru (uwaga - ta sama składnia działa też dla innych kolekcji)
    """)
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
    _stolice_europy = {'Paryż', 'Berlin', 'Warszawa'}
    print('Berlin' in _stolice_europy)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Sprawdzenia nieobecności elementu w zbiorze najlepiej dokonać przez operator not in:
    """)
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
    _stolice_europy = {'Paryż', 'Berlin', 'Warszawa'}
    print('Radom' not in _stolice_europy)  # Zalecane
    print(not 'Radom' in _stolice_europy)  # Niezalecane, ale też działa
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Rozmiar zbioru (ponownie - ta sama składnia dla innych kolekcji)
    """)
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
    _miasta_mazowsza = {'Radom', 'Płock', 'Warszawa'}
    print(len(_miasta_mazowsza))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Słowniki

    Słownik to zbiór par klucz-wartość.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Zmiana zmiennych powoduje zarezerwowanie nowego miejsca w pamięci**
    """)
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
    _a="dane"
    print(type(_a),"  ",id(_a))
    _a+="  test"
    print(type(_a),"  ",id(_a))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Quiz
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    """)
    return
@app.cell
def _():
    # Jaki będzie wynik działania kodu:
    _aTuple = (1, 'Jhon', 1+3j)
    print(type(_aTuple[2:3]))
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
    # Jaki będzie wynik działania kodu:
    print(bool(0.0), bool(3.14159), bool(-3), bool(1.0+1j))
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
    print(type(10))
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
    print(type({}) is set)
    print(type({}))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    """)
    return
@app.cell
def _():
    _aTuple = (1, 'Jhon', 1+3j)
    print(type(_aTuple[2:3]))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Instrukcje

    Instrukcje języka Python są elastyczne. Można wyróznić instrukcje związane ze składnią języka (np. if, for while), wykorzystanie operatorów (np. =, ==, +, **) i metod/funkcji. W jednej linii można łaczyc instrukcje róznego rodzaju, co przy dobrym wykorzystaniu sprzyja czytelności kodu.

    ## Podstawienie

    Może dotyczyc jednego argumentu lub kilku, dzięki czemu np. operacja zamiany zmiennych jest łatwiejsza niż w C.
    """)
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
    _a = 3
    b, c = 5, 7
    print(_a, b, c)
    b, c = c, b
    print(_a, b, c)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Instrukcja if
    """)
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
    _x = int(input('Please enter an integer'))
    if _x < 0:
      print('Negative')
    else:
      print('Positive or zero')
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
    _x = int(input('Please enter an integer'))
    if _x < 0:
      print('Negative')
    elif _x == 0:
      print('Zero')
    else:
      print('Positive')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    W Pythonie istnieje również odpowiednik operatora trójarguemntowego C o bardziej czytelnym zapisie:
    """)
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
    _x = int(input('Please enter an integer'))
    print( 'Negative' if _x < 0 else 'Positive or zero' )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Warunki logiczne łączymy operatorami and i or. Negacje wykonuje operator not.
    """)
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
    _wiek = 27
    if _wiek < 30 or _wiek % 10 == 0:
      print('Możesz zorganizować huczne urodziny')
    else:
      print('Wystarczy ciasto dla najbliższych, masz kredyt hipoteczny')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Instrukcja for

    Pozwala na iterację po dowolnym obiekcie iterowalnym (np. liście, krotce, słowniku, ale i Stringu)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    - **Iteracja**: Zastosowanie pętli `for` do przetwarzania elementów sekwencji.
    """)
    return
@app.cell
def _():
    for i in [0, 4, 7, 12]:
      print(i)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Iteracja**: Zastosowanie pętli `for` do przetwarzania elementów sekwencji.
    """)
    return
@app.cell
def _():
    for letter in 'Radom':
      print(letter)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Instrukcja for jest często łaczona z range(), tworzącą w Python iterowalny obiekt (nie mylić z iteratorem).
    range ma w ogólności postać: range(start, stop, krok)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Generator range**: Wykorzystanie leniwego generatora `range()` do generowania sekwencji liczb bez alokowania pełnej listy w pamięci.
    - **Iteracja**: Zastosowanie pętli `for` do przetwarzania elementów sekwencji.
    """)
    return
@app.cell
def _():
    _lista = range(1,10,3)
    print(_lista)
    for i in _lista:
      print(i)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Generator range**: Wykorzystanie leniwego generatora `range()` do generowania sekwencji liczb bez alokowania pełnej listy w pamięci.
    - **Iteracja**: Zastosowanie pętli `for` do przetwarzania elementów sekwencji.
    """)
    return
@app.cell
def _():
    for i in range(4, 10, 2):
      print(i)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Jeśli oprócz wartosci elementu listy chcemy znać jego pozycję na tej lisćie, wykorzystujemy enumerate().
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    - **Iteracja**: Zastosowanie pętli `for` do przetwarzania elementów sekwencji.
    """)
    return
@app.cell
def _():
    _najwieksze_kraje = ['Rosja', 'Kanada', 'USA']
    for idx, item in enumerate(_najwieksze_kraje):
      print(idx, item)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Do sterowania przebiegiem pętli można wykorzystywać instrukcje break i continue.
    """)
    return


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
    for num in range(2, 10):
      print(num)
      if num % 2 == 0:
        print('Found an even number -', num)
        break
    return


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
    for num in range(2, 10):
      if num % 2 == 0:
        print('Found an even number -', num)
        continue
      _x = 10 / (num % 2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Z instrukcją for możemy wiązać instrukcję else, chociaż nie działa ona zgodnie z intuicją, bo instrukcje po else wykonywane są zawsze bez wzgledu na działanie for
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Iteracja**: Zastosowanie pętli `for` do przetwarzania elementów sekwencji.
    """)
    return
@app.cell
def _():
    for i in range (0,2):
      print(i)
    else:
      print("koniec")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    W języku Python istnieje instrukcja pusta pass, wykorzystywana głównie jako tymczasowa zaślepka lub przy tworzeniu funkcji wirtualnych - składnia Pythona nie pozwala powiem na tworzenie pustych bloków, analogicznych jak {} w C/C++
    """)
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
    _x=10
    if _x>100:
        pass
    else:
        print(_x)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Bardzo interesującą własnoscią języka Python jest inicjalizacja całych list w jednej instrukcji (podobna składnia również dla innych kolekcji)
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
    _kwadraty = [x**2 for x in range(10)]  # tworzenie listy kwadratów liczb od 1 do 9
    print(_kwadraty)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Analogiczne operacje można wykonać dla słowników.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Generator range**: Wykorzystanie leniwego generatora `range()` do generowania sekwencji liczb bez alokowania pełnej listy w pamięci.
    - **Iteracja**: Zastosowanie pętli `for` do przetwarzania elementów sekwencji.
    """)
    return
@app.cell
def _():
    _kwadraty_dict = {x: x**2 for x in range(10)}
    for liczba, kwadrat in _kwadraty_dict.items():
      print(liczba, kwadrat)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Do nowo tworzonej kolekcji można wybrać wszystkie (jak wyżej) lub tylko część spośród elementów:
    """)
    return


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
    _kwadraty_parzyste_dict = {x: x**2 for x in range(10) if x%2 == 0}
    for liczba, kwadrat in _kwadraty_parzyste_dict.items():
      print(liczba, kwadrat)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Możliwe jest również stosowanie pętli podwójnych:
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
    _tabliczka_mnozenia = [{'czynnik_1': x, 'czynnik_2': y, 'iloczyn': x * y}
                          for x in range(1, 5) for y in range(1, x+1)]
    for item in _tabliczka_mnozenia:
      print(item)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Podstawienie wielu wartości (ścisle - krotki) moze być wykorzystane w dowolnym miejscu, np:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    - **Iteracja**: Zastosowanie pętli `for` do przetwarzania elementów sekwencji.
    """)
    return
@app.cell
def _():
    _lista_krotek = [('a', 'b', 'c'), ('x', 'y', 'z'), ('1', '2', '3')]
    for item in _lista_krotek:
      print(item)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Iteracja**: Zastosowanie pętli `for` do przetwarzania elementów sekwencji.
    """)
    return
@app.cell
def _(lista_krotek):
    for i1, i2, i3 in lista_krotek:
      print(i1, i2, i3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Instrukcja while
    """)
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
    _i = 0
    while _i**2 < 30:
      _i = _i+1
      print(_i)
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
    _i = 2
    while 1 < _i**2 < 30:
      _i = _i+1
      print(_i)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Zakres zmiennych

    Zmienne w języku Python są widoczne poza blokiem w którym zostały zdefiniowane. Nie są widoczne poza funkcją w której zostały zdefiniowane, ale to zostanie omówione po wprowadzeniu funkcji. Pozwala to na pisanie bardziej zwięzłego kodu, trzeba jednak pamietać o ryzyku odwołania  do niezainicjalizowanej zmiennej.
    """)
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
    _x=1
    if _x>0:
        _y=1
    print(_y)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
 
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##Quiz
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
    ### 💻 ANALIZA TECHNICZNA
    - **Generator range**: Wykorzystanie leniwego generatora `range()` do generowania sekwencji liczb bez alokowania pełnej listy w pamięci.
    - **Iteracja**: Zastosowanie pętli `for` do przetwarzania elementów sekwencji.
    """)
    return
@app.cell
def _():
    # Jaki jest wynik uruchomienia programu

    for i in range(1,5,1):
      print(i)
    else: print("koniec")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Jak napisać instrukcję:

    if x%2==0: print(Parzyste)
    else print("nieparzyste")

    w sposób bardziej "pythonowy"
    """)
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
    _x=2
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Praca domowa (termin oddania 12.03.2023)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Napisać program, który wczytuje kilka par nazwisko, wiek (instrukcja input), tworzy słownik i wypisuje komórki słownika, dla których wiek przekracza zadaną wartość, proszę napisać jak najbardziej związły kod. (minimum linii)
    """)
    return


if __name__ == "__main__":
    app.run()
