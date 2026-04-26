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
    # Wykład 6: Analiza Danych
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Wykład 6
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## PLAN
    Na wykładzie zostaną przedstawione:

    * instrukcje wejścia-wyjścia

    oraz następujące biblioteki

    * **Pandas** - biblioteka umożliwiająca operowaniem danymi tabelarycznymi np. *.xls,*.xlsx, *.csv

    * **NumPy** - biblioteka do obliczeń numerycznych, dane są zapisywane w formie tablic

    Na końcu praktyczne zastosowanie - system rekomendacyjny
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Instrukcje wejścia-wyjścia
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Instrukcje we/wy w Pythonie są używane do komunikacji programu z użytkownikiem, umożliwiając wprowadzanie danych przez użytkownika (wejście) oraz wyświetlanie wyników lub informacji (wyjście).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Input - umożliwia wprowadzenie danych z klawiatury.  Trzeba pamiętać o rzutowaniu danych, input zwraca string.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Aby wyświetlić dane użytkownikowi, używamy funkcji print(). Funkcja ta przyjmuje jeden lub więcej argumentów i wypisuje je na standardowe wyjście (zwykle ekran).
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
    # Wyświetlenie wartości zmiennej
    _imie = "Jan"
    _wiek = 25
    print(f"Imię: {_imie}, Wiek: {_wiek}")
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
    # domyślnie end to nowa linia, aby to zmienć deiniujem end=
    print("Witaj", end=" ")
    print("w Pythonie!")
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
    from google.colab import files
    _uploaded = files.upload()

    # Załaduj obraz za pomocą OpenCV (po przesłaniu)
    _image_path = list(_uploaded.keys())[0]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Python oferuje wiele metod do pracy z danymi wejściowymi i wyjściowymi. Oprócz podstawowych funkcji input() i print(), mamy:

    * Pliki: Do odczytu i zapisu plików tekstowych, CSV, JSON, czy binarnych.
    * Strumienie: Do pracy z danymi wejściowymi/wyjściowymi na poziomie systemu (np. sys.stdin, sys.stdout).
    * Bazy danych: Do zapisu i odczytu danych z baz danych takich jak SQLite, MySQL czy PostgreSQL.
    Na wykładzie omówione będzie we/wy dla plików.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Wejście/Wyjście - pliki
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
    from google.colab import drive
    ## montowanie dysku w google collab, klasycznie nie stosowane
    drive.mount('/content/drive')
    _file = '/content/drive/MyDrive/pliki/elves.txt'
    # Otwarcie pliku do odczytu
    # plik zawiera _dane w języku elfów
    with open(_file, 'r') as plik:
        # Odczytanie danych z pliku i przypisanie ich do zmiennej
        _dane = plik.read()

    # Wyświetlenie wczytanych danych
    print(_dane)
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
    # Listowanie zawartości

    import os

    #_katalog = '.'  # Aktualny _katalog
    _katalog = '/content/drive/MyDrive/pliki/'
    _zawartosc = os.listdir(_katalog)

    print(_zawartosc)
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
    _file = '/content/drive/MyDrive/pliki/plik.txt'
    # Otwarcie pliku do odczytu
    # plik zawiera dane w języku elfów
    with open(_file, 'w') as plik:
        # Odczytanie danych z pliku i przypisanie ich do zmiennej
        plik.write("tekst  12.8")
    plik.close()
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
    _file = '/content/drive/MyDrive/pliki/plik.txt'
    # Otwarcie pliku do odczytu
    # plik zawiera dane w języku elfów
    with open(_file, 'r') as plik:
        # Odczytanie danych z pliku i przypisanie ich do zmiennej
        _line=plik.read()
        print(_line)
    tekst, ints = _line.split()
    print(tekst,"  ",ints)
    print(type(ints))
    _intf=float(ints)
    print(type(_intf))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    operator sep - określamy separator napisów
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
    print('09', '01', '2024', sep='-')
    print('09', '02', '2024', sep='.')
    print('09', '03', '2024', sep=' ')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Wyjście formatowane, analogicznie jak w C
    * %d –integer
    * %f – float
    * %s – string
    * %x –heksagonalny
    * %o – ósemkowy
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
    _x=21
    print("_x=%o _x=%_x" %(_x,_x))
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
    _amount = 12.345
    _x = 42
    print("liczba {:5.2f} {:2}".format(_amount, _x))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    użycie string
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
    _amount=10.2
    print(f"liczba {_amount}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Pickle jest biblioteką w Pythonie służącą do serializacji i deserializacji obiektów Pythona. Pozwala to na zapisywanie obiektów Pythona do plików i późniejsze ich odczytywanie, zachowując ich stan.

    Oto prosty przykład zastosowania pickle, gdzie zapisujemy listę obiektów Pythona do pliku za pomocą pickle.dump() i później odczytujemy tę listę z pliku za pomocą pickle.load()
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
    import pickle

    # Lista obiektów Pythona
    _data = [1, 2, 3, "apple", "banana", {"name": "John", "age": 30}]

    # Zapisanie listy do pliku "_data.pickle"
    with open("/content/drive/MyDrive/pliki/_data.pickle", "wb") as f:
        pickle.dump(_data, f)

    # Odczytanie listy z pliku "_data.pickle"
    with open("/content/drive/MyDrive/pliki/_data.pickle", "rb") as f:
        _loaded_data = pickle.load(f)

    # Wyświetlenie odczytanej listy
    print(_loaded_data)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    W wielu praktycznych zastosowaniach wygodniej jest zapisywać i odczytywać dane z plików excela
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Biblioteka Pandas - zastosowanie
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    * Wczytywanie różnych formatów danych (CSV, Excel, SQL, pliki płaskie itd.)
    * Filtrowanie, sortowanie i inne operacje z danymi
    * Czyszczenie danych (usuwanie wartości NaN – Not a Number),
    * Uśrednianie, zastępowanie wartości itp.)
    * Szybkie i efektywne obliczanie statystyk
    * Wizualizacja danych za pomocą wykresów
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Obiekt **Series** i **DataFrame** to dwa podstawowe obiekty w bibliotece Pandas. **Series** to jednowymiarowa tablica etykietowanych danych, podobna do kolumny w tabeli, natomiast **DataFrame** to dwuwymiarowa tablica etykietowanych danych, podobna do tabeli z danymi.

    Różnica między nimi polega na tym, że Series zawiera tylko jedną kolumnę, podczas gdy DataFrame może zawierać wiele kolumn.

    Aby przekształcić Series na DataFrame, można użyć metody to_frame(), która tworzy nowy DataFrame z jedną kolumną zawierającą wartości z oryginalnej Series.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Podstawowe struktury danych:

    * Series
    * DataFrame
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
    # import biblioteki

    import pandas

    # lub

    import pandas as pd

    # Tworzenie serii
    _s = pd.Series([10, 20, 30, 40, 50], name='numbers')
    #print(_s[1])
    print(_s)
    return (pd,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    """)
    return


@app.cell
def _():
    import pandas as pd
    _vals_sr = pd.Series(["Val_1", "Val_2", "Val_3", "Val_4", "Val_5"], index=["A", "B", "C", "D", "E"])
    #print(_vals_sr)
    print(_vals_sr["A"])
    return (pd,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Zadanie:  Mam słownik, jak zapisać dane w postaci Series?
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
def _(pd):
    dict = {'a':10, 'b':20, 'c':30, 'd':40, 'e':50}
    _s = pd.Series(dict)
    print(_s)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Mamy obiekt klasy Auto, jak zapisać go w postaci słownika i pd.Series?
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
def _(pd):
    class Auto:
        def __init__(self, marka, model, rok):
            self.marka = marka
            self.model = model
            self.rok = rok

    _auto = Auto("Toyota", "Corolla", 2020)
    dict=vars(_auto)
    print(dict)
    _s = pd.Series(dict)
    print(_s)
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
    import pandas as pd

    # Tworzenie serii
    _s = pd.Series([1, 2, 3, 4, 5], name='numbers')
    print(_s)
    # Konwertowanie serii na ramkę danych
    _df = _s.to_frame()

    print(_df)
    print(_df['numbers'])
    return (pd,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Metody klasy DataFrame:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Pełna dokumentacja: https://pandas.pydata.org

    Odczyt zapis danych:

    * df.to_csv('plik.csv')	 - Zapis do pliku CSV
    * pd.read_csv('plik.csv')	- Odczyt z pliku CSV
    * df.to_excel('plik.xlsx')	- Zapis do Excela
    * pd.read_excel('plik.xlsx')	- Odczyt z pliku Excel
    * df.to_json('plik.json')	- Zapis do formatu JSON
    * pd.read_json('plik.json')	- Odczyt JSON
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
    # czytanie danych przy użyciu Pandas
    from google.colab import drive
    drive.mount('/content/drive')       #montowanie dysku
    _file = '/content/drive/MyDrive/pliki/anal.xlsx'
    import pandas as pd

    _df = pd.read_excel(_file)   # otwarcie i czytanie całęgo pliku

    _kolumna = _df.iloc[2:8, [1,2]]  # pobieranie zawartości kolumny drugiej i trzeciej w zakresie od 2 do 8
    print(_kolumna)
    # drukowanie bez nagłówków i numerów
    print(_df.iloc[2:8, [1, 2]].to_string(index=False, header=False))
    #zapisanie kolumny drugiej od 2 do 8 do tablicy
    _tablica = _df.iloc[2:8,1].values
    print(_tablica)
    print(type(_tablica))     #to nie jest DataFrame
    return (pd,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Dane przechowywane w tabeli DataFrame, jeśli chcemy wyświelić określoną liczbę wierszy to piszemy  head() z parametrem
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
def _(df):
    df.head(8)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Analiza**: Implementacja logiki algorytmu z wykorzystaniem standardowej składni i wbudowanych mechanizmów Pythona.
    """)
    return


@app.cell
def _(df):
    df.tail(2)                     #elementy na końcu
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    NaN - oznacza brak danych z taką sytuacją musimy sobie radzić, w Pandas są odpowiednie narzędzia które zostaną przedstawione !!!!!!!
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
def _(df):
    df.shape          # określenie wymiaru DataFrame
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Jak wyświetlić oddzielnie wiersze i kolumny?
    """)
    return


@app.cell
def _():
    pass
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Analiza**: Implementacja logiki algorytmu z wykorzystaniem standardowej składni i wbudowanych mechanizmów Pythona.
    """)
    return


@app.cell
def _(df):
    df.size                                #iloczyn liczby wierszy i kolumn
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Analiza**: Implementacja logiki algorytmu z wykorzystaniem standardowej składni i wbudowanych mechanizmów Pythona.
    """)
    return


@app.cell
def _(df):
    len(df)                                  #liczba wierszy
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Iteracja**: Zastosowanie pętli `for` do przetwarzania elementów sekwencji.
    """)
    return


@app.cell
def _(df):
    _a=df.columns
    for k in _a: print(k)                                  # Nazwy kolumn
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Pobranie kolumny (w wersji enumerate)
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
def _(df):
    df['Mff']
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Pobranie zakresu lub konkretnej wartości
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
def _(df):
    df['Mff'][3:5]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    """)
    return


@app.cell
def _(df):
    df[['Mff', 'Fis1']]                                                               #możemy wybierać kilka kolumn
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
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    """)
    return


@app.cell
def _(df):
    df[['Mff', 'Fis1']][2:5]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Możemy też wczytywać dane z plików csv i tworzyć tabelę, określamy nazwy kolumn, separator użyty w pliku, liczbę kolumn oraz rodzaj kodowania.
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
    import pandas as pd
    import matplotlib.pyplot as plt

    # Tworzenie przykładowego DataFrame
    _data = {
        'Rok': [  2020,   2021,   2022],
        'Sprzedaż': [150, 1200, 250]
    }
    _df = pd.DataFrame(_data)
    print(_df)
    # tu dodajemy kolejne dane
    _data2= {'Rok': 2023,'Sprzedaż':2000}
    _df = pd.concat([_df,pd.DataFrame([_data2])], ignore_index=True)
    print(_df)
    return (pd,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Budujemy "pusty" DataFrame
    """)
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
    import pandas as pd
    import numpy as np

    # Tworzymy pusty DataFrame z 3 kolumnami i 5 wierszami
    _df = pd.DataFrame(np.nan, index=range(5), columns=['A', 'B', 'C'])

    print(_df)
    return np, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Dodane wiersza
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
def _(df):
    df.loc[len(df)] = [7, 8, 9]
    print(df)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    """)
    return


@app.cell
def _(df):
    # Wstawienie wiersza
    df.loc[1] = [7, 8, 9]
    print(df)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    """)
    return


@app.cell
def _(df):
    # Usuwanie wiersza

    _df1 = df.drop([1, 3])

    print("\nPo usunięciu wierszy o indeksach 1 i 3")
    print(_df1)
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
    # Usuwanie wierszy, w których wartość w kolumnie 'A' jest nan
    print(_df)
    _df = _df[_df['A'].isna()]

    print("\nPo usunięciu wierszy, w których wartość w kolumnie 'A' jest większa niż 2:")
    print(_df)
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
def _(pd):
    # czytamy informację zawierającą oceny filmów przez poszczególnych użytkowników
    _filmr = '/content/drive/MyDrive/pliki/u.data'
    _cols = ['user_id', 'movie_id', 'rating']
    _rt = pd.read_csv(_filmr, sep='\t', names=_cols, usecols=range(3), encoding="ISO-8859-1")
    _rt.head(5)
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
def _(pd):
    _namef = '/content/drive/MyDrive/pliki/u.item'
    _m_cols = ['movie_id', 'title']
    _movies = pd.read_csv(_namef, sep='|', names=_m_cols, usecols=range(2), encoding="ISO-8859-1")
    _movies.head(5)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Zadanie: mając dane o oglądanych filmach i ocenie tych filmów. Należy zbudować system, który znając wysoko oceniany przez na film rekomenduje kolejny. Poniżej przedstawione zostaną kolejne kroki algorytmu.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Naszym zadaniem będzie rekomendowanie filmów, na podstawie poprzednio oglądanego wysoko przez nas ocenianego filmu. Interesują więc nas nazwy filmów, a nie ich ID. Ze względów praktycznych warto operować jedną tablicą nie dwoma.
    Wykorzystujemy inteligentne łączenie tabel (wspólne movies_id)
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
def _(movies, pd):
    _rt = pd.merge(movies, _rt)
    _rt.head(8)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Teraz chcemy, aby nazwy kolumn były tytułami filmów, w tym celu stosujemy metodę pivot_table
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
def _(rt):
    _movieRatings = rt.pivot_table(index=['user_id'],columns=['title'],values='rating')
    _a=_movieRatings.columns
    for k in _a: print(k)                                  # Nazwy kolumn
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Analiza**: Implementacja logiki algorytmu z wykorzystaniem standardowej składni i wbudowanych mechanizmów Pythona.
    """)
    return


@app.cell
def _(movieRatings):
    movieRatings.head(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Załóżmy, że podobał się nam film: Young Frankenstein (1974), jaki film będzie nam rekomendowany? Poszukujemy więc filmów, które były wysoko oceniane łącznie z filmem Young Frankenstein (1974). Jakie mamy narzędzia?
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
def _(movieRatings):
    # Pobieramy kolumnę ocen dla Y.F.
    _YF = movieRatings['Young Frankenstein (1974)']
    _YF.head(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Poszukujemy kolumny najsilniej skorelowanej (tz, takiej która ma podobne oceny). Problem brak danych w pewnych miejscach. funkcja **dropna** usuwa takie dane. Korelację między kolumnami obliczmay funkcją **corrwith**
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
def _(YF, movieRatings):
    _sm = movieRatings.corrwith(YF)
    _sm = _sm.dropna()


    print(type(_sm))
    print(_sm)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    """)
    return


@app.cell
def _(pd):
    _s = pd.Series([10, 2, 3], index=['a', 'b', 'c'], name='my_series')
    _s.sort_values(ascending=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Analiza**: Implementacja logiki algorytmu z wykorzystaniem standardowej składni i wbudowanych mechanizmów Pythona.
    """)
    return


@app.cell
def _(pd, s):
    _df = pd.DataFrame(s)
    print(_df.columns)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Teraz warto dane posortować i wybrać wartości największe
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
def _(sm):
    sm.sort_values(ascending=False,ignore_index=False)   #od największej do najmniejszej wartości

    #print(sm)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    I tą część możemy rozwijać dalej, biorąc pod uwagę różne kryteria podobieństwa i wyboru.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Biblioteka numpy
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Zamiana numpy.array na DataFrame i odwrotnie
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
    import numpy as np
    import pandas as pd

    _ndarray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    _df = pd.DataFrame(_ndarray, columns=['col1', 'col2', 'col3'], index=['row1', 'row2', 'row3'])
    _df.head(3)
    return np, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Analiza**: Implementacja logiki algorytmu z wykorzystaniem standardowej składni i wbudowanych mechanizmów Pythona.
    """)
    return


@app.cell
def _(df):
    _nparray=df.values
    print(_nparray)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    """)
    return


@app.cell
def _(df):
    _pom=df['col1']
    _pom.head(3)      #to nie jest wektor
    print(_pom.values)  #to jest wektor
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Dodanie kolumny
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
    import pandas as pd

    # Istniejąca tabela
    _df = pd.DataFrame({'Name': ['John', 'Alice'], 'Age': [25, 30], 'Gender': ['Male', 'Female']})

    # Nowa kolumna do dodania
    _new_col = pd.Series(['Engineer', 'Doctor'], name='Profession')

    # Łączenie tabel wzdłuż osi 1 (kolumn)
    _df = pd.concat([_df, _new_col], axis=1)   #kierunek dodawania

    print(_df)
    return (pd,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Tworzenie nowej kolumny na podstawie wartości  innych kolumn
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
    import pandas as pd

    # Tworzenie ramki danych
    _df = pd.DataFrame({'col1': [1, 2, 3, 4, 5], 'col2': [10, 20, 30, 40, 50]})

    # Dodawanie wartości z kolumn "col1" i "col2" i przypisanie wyniku do nowej kolumny "sum"
    _df['sum'] = _df['col1'] + _df['col2']

    print(_df)
    return (pd,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Wstawianie wiersza tablicy numpy do DataFrame
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
    import pandas as pd
    import numpy as np

    # Tworzenie ramki danych
    _df = pd.DataFrame({'col1': [1, 2, 3, 4, 5], 'col2': [10, 20, 30, 40, 50]})

    # Tworzenie wektora numpy
    _arr = np.array([6, 7, 8, 9, 10])

    # Przypisywanie wektora numpy do kolumny "col1"
    _df['col1'] = _arr

    print(_df)
    return np, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    zapis do pliku xlsx lub csv
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
    import pandas as pd

    # Tworzenie ramki danych
    _df = pd.DataFrame({'col1': [1, 2, 3, 4, 5], 'col2': [10, 20, 30, 40, 50]})

    # Zapisywanie ramki danych do pliku CSV
    _df.to_csv('nazwa_pliku.csv', index=False)     #to_excel  dla plików excela
    return (pd,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Sortowanie Tabeli na podstawie zawartości kolumny
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
    import pandas as pd

    # Tworzenie ramki danych
    _df = pd.DataFrame({'col1': [3, 1, 4, 2, 5], 'col2': [10, 20, 30, 40, 50]})

    # Sortowanie według wartości w kolumnie "col1"
    _df_sorted = _df.sort_values(by='col1', ascending=True)

    print(_df_sorted)
    return (pd,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    """)
    return


@app.cell
def _(df_sorted):
    _new_index = [0, 1, 2, 3, 4]
    _dfr = df_sorted.reindex(_new_index)
    print(_dfr)
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
    _new_in = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E'}

    _df = _df.rename(index=_new_in)
    print(_df)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Obliczanie funkcji dla danej kolumny
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
def _(df):
    _max_val = df['col1'].max()
    _median_val = df['col2'].median()

    print("max=", _max_val,"mediana=",_median_val)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Funkcji mamy bardzo dużo, np.
    describe(): wyświetla podsumowanie statystyczne dla każdej kolumny, w tym wartość średnią, odchylenie standardowe, wartości minimalne i maksymalne oraz kwantyle.
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
def _(df):
    _des = df['col1'].describe()
    print(_des)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    """)
    return


@app.cell
def _(df):
    _des = df['col1'].describe()
    print(_des['count'])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Biblioteka numpy
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Tworzenie tablic
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
    import numpy as np
    # Na podstawie listy liczb
    _arr = np.array([[1, 2, 3], [4, 5, 6]])
    print(_arr)
    return (np,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Analiza**: Implementacja logiki algorytmu z wykorzystaniem standardowej składni i wbudowanych mechanizmów Pythona.
    """)
    return


@app.cell
def _(np):
    _arr=np.zeros((5,4),dtype=float)
    print(_arr)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Analiza**: Implementacja logiki algorytmu z wykorzystaniem standardowej składni i wbudowanych mechanizmów Pythona.
    """)
    return


@app.cell
def _(np):
    _arr=np.ones((5,4),dtype=complex)
    print(_arr)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Analiza**: Implementacja logiki algorytmu z wykorzystaniem standardowej składni i wbudowanych mechanizmów Pythona.
    """)
    return


@app.cell
def _(np):
    _arr=np.empty((5,4),dtype=int)
    print(_arr)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Przykładowe typy danych
    numpy.int8 - Byte (-128 to 127)

    numpy.int16 - Integer (-32768 to 32767)

    numpy.int32 - Integer (-2147483648 to 2147483647

    numpy.int64 - Integer (-9223372036854775808 to 9223372036854775807)

    numpy.uint8 - Unsigned integer (0 to 255)

    numpy.uint16 - Unsigned integer (0 to 65535)

    numpy.uint32 - Unsigned integer (0 to 4294967295)

    numpy.uint64 - Unsigned integer (0 to 18446744073709551615)

    numpy.float64 / numpy.float_

    numpy.complex64

    numpy.complex128 / numpy.complex_
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Informacje o tablicy
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
    import numpy as np
    # Na podstawie listy liczb
    _arr = np.array([[1, 2, 3], [4, 5, 6]])
    # Liczba wymiarów tablicy
    print(_arr.ndim)
    # Rozmiar tablicy
    print(_arr.shape)
    return (np,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Analiza**: Implementacja logiki algorytmu z wykorzystaniem standardowej składni i wbudowanych mechanizmów Pythona.
    """)
    return


@app.cell
def _(np):
    # Kwadratowa macierz jednostkowa
    print(np.eye(3))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Generator range**: Wykorzystanie leniwego generatora `range()` do generowania sekwencji liczb bez alokowania pełnej listy w pamięci.
    """)
    return


@app.cell
def _(np):
    # 1-wymiarowa tablica podobna do range()
    print(np.arange(5))
    print(np.arange(3.0, 5.0, 0.5))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Analiza**: Implementacja logiki algorytmu z wykorzystaniem standardowej składni i wbudowanych mechanizmów Pythona.
    """)
    return


@app.cell
def _(np):
    # 1-wymiarowa tablica o _N wartościach od _A do _B
    _A = 4.0
    _B = 7.0
    _N = 13
    print(np.linspace(_A, _B, _N))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Generator range**: Wykorzystanie leniwego generatora `range()` do generowania sekwencji liczb bez alokowania pełnej listy w pamięci.
    """)
    return


@app.cell
def _(np):
    # Macierz diagonalna o wartościach na przekątnej podanych w tablicy 1D
    print(np.diag(np.arange(1, 5)))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Podstawowe operacje na tablicach
    Pakiet numpy pozwala na wygodne i efektywne wykonywanie wielu operacji matematycznych.
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
def _(np):
    _arr = np.array([[2, 8, 3], [5, 6, 2]])
    # Operacje powyzsze, jak i wiele innych, można wykonywać wzdłuz wybranych osi
    print(np.max(_arr))
    print(np.max(_arr, axis=0))
    print(np.max(_arr, axis=1))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    """)
    return


@app.cell
def _(np):
    _arr = np.array([[2, 8, 3], [5, 6, 2]])
    print('Średnia:', np.mean(_arr))
    print('Suma:', np.sum(_arr))
    print('Wariancja:', np.var(_arr))
    print('Odchylenie standardowe:', np.std(_arr))
    print('Tablica przekształcona do 1D:', _arr.flatten())
    print('Iloczyn elementów tablicy:', np.prod(_arr))
    print('Macierz transponowana:\n', np.transpose(_arr))
    print('Sortowanie macierzy:\n', np.sort(_arr, axis=1))
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
    import numpy as np
    # Operacje na macierzach - operatory
    _a = np.array([[1, 2], [4, 5]])
    print('_a =\n', _a)
    print('2a =\n', 2*_a)
    print('2a+1 = \n', 2 * _a + 1)
    _b = np.array([[3, 2], [1, 1]])
    print('_b =\n', _b)
    print('_a*_b =\n', _a*_b)  # Iloczyn elementów, ale nie macierzy
    print('_a/_b =\n', _a/_b)
    print('_a X _b', np.dot(_a,_b))     #Iloczyn macierzy
    return (np,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    """)
    return


@app.cell
def _():
    import numpy as np
    _a = np.array([[1, 2], [4, 5]])
    print('Wyznacznik macierzy:', np.linalg.det(_a))
    print('Wartości własne:', np.linalg.eigvals(_a))
    print('Wektory własne:', np.linalg.eig(_a))
    return (np,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    """)
    return


@app.cell
def _():
    import numpy as np
    _a = np.array([[1, 2], [3, 5]])
    _b = np.array([1, 2])
    _x = np.linalg.solve(_a, _b)
    print(_x)
    return (np,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Pakiet numpy umożliwia również:

    transormatę Fouriera (sygnałów i obrazów)

    operacje na wielomianach: takie jak obliczenie pierwiastków wielomianu na podstawie jego współczynników (i odwrotnie) czy tez aproksymacje wielomianem.

    operacje binarne

    statystyka

    operacje na tekstach

    szczegóły: https://numpy.org/doc
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
    import numpy as np
    _wspolczynniki = [1, 0, -4]
    _pierwiastki = np.roots(_wspolczynniki)
    print(_pierwiastki)
    print(np.poly(_pierwiastki))
    print(np.roots([1, 0, 4]))  # Wartosci zespolone
    return (np,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    - **Kontrola Przepływu**: Implementacja logiki warunkowej sterującej wykonaniem bloku kodu.
    """)
    return


@app.cell
def _():
    import numpy as np
    _xs = [1, 2, 3, 4, 5, 6]
    _ys = [1, 4.1, 8.9, 16, 25.2, 35.8]
    _w_2_stopnia = np.polyfit(_xs, _ys, 2)
    print(_w_2_stopnia)
    return (np,)


if __name__ == "__main__":
    app.run()
