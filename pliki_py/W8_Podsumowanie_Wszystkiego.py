import marimo

__generated_with = "0.23.3"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 🏆 MASTER CHEAT SHEET - PODSUMOWANIE SEMESTRU
    *Kompletne zestawienie wszystkich konstrukcji i bibliotek omówionych na wykładach.*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 1️⃣ Podstawy i Typy Danych
    - **int, float, complex, bool**: Podstawowe typy numeryczne i logiczne.
    - **type() / isinstance()**: Sprawdzanie typów.
    - **f-strings**: Nowoczesne formatowanie tekstu.
    """)
    return


@app.cell
def _():
    # Liczby i bool
    _x = 10          # int
    _y = 3.14        # float
    _z = 1 + 2j      # complex
    _is_valid = True # bool

    # Sprawdzanie typów
    print(f"Typ _x: {type(_x)}")
    print(f"Czy _y jest floatem? {isinstance(_y, float)}")

    # Formatowanie f-string
    print(f"Suma _x + _y to: {_x + _y:.2f}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 2️⃣ Kolekcje (Struktury Danych)
    - **Listy `[]`**: Uporządkowane, modyfikowalne.
    - **Słowniki `{}`**: Pary klucz-wartość.
    - **Krotki `()`**: Niezmienne listy.
    - **Zbiory `{}`**: Unikalne elementy, brak kolejności.
    """)
    return


@app.cell
def _():
    # Lista i operacje
    _lista = [1, 2, 3]
    _lista.append(4)
    print(f"Lista: {_lista}, Slicing [1:3]: {_lista[1:3]}")

    # Słownik
    _slownik = {"marka": "Toyota", "rok": 2020}
    _slownik["model"] = "Corolla"
    print(f"Słownik: {_slownik}, Klucze: {list(_slownik.keys())}")

    # List Comprehension (Skrócony zapis tworzenia list)
    _kwadraty = [x**2 for x in range(5)]
    print(f"Kwadraty: {_kwadraty}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 3️⃣ Kontrola Przepływu (Logika)
    - **if / elif / else**: Warunki.
    - **for / while**: Pętle.
    - **break / continue / else w pętli**: Sterowanie pętlą.
    """)
    return


@app.cell
def _():
    # Warunek
    _a = 5
    if _a > 0:
        print("Dodatnia")
    elif _a == 0:
        print("Zero")
    else:
        print("Ujemna")

    # Pętla for z range i else
    for i in range(3):
        print(f"Iteracja {i}")
    else:
        print("Pętla zakończona bez przerwania (break)")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 4️⃣ Funkcje: Detale Składniowe
    - **Pola domyślne**: Pozwalają wywołać funkcję bez podawania wszystkich argumentów.
    - **\*args**: Przekazywanie dowolnej liczby argumentów pozycyjnych (trafiają do krotki).
    - **\*\*kwargs**: Przekazywanie dowolnej liczby argumentów nazwanych (trafiają do słownika).
    """)
    return


@app.cell
def _():
    # 1. Pola domyślne
    def _powitanie(imie, komunikat="Witaj"):
        return f"{komunikat}, {imie}!"

    print(_powitanie("Jan")) # Użyje "Witaj"
    print(_powitanie("Anna", "Cześć")) # Nadpisze "Cześć"

    # 2. *args (dowolna liczba elementów -> tuple)
    def _suma_liczb(*args):
        print(f"args to: {type(args)} o rozmiarze {len(args)}")
        return sum(args)

    print(f"Suma (1,2,3): {_suma_liczb(1, 2, 3)}")

    # 3. **kwargs (dowolna liczba nazwanych -> dict)
    def _wizytowka(**kwargs):
        print(f"kwargs to: {type(kwargs)} o rozmiarze {len(kwargs)}")
        for klucz, wartosc in kwargs.items():
            print(f"- {klucz}: {wartosc}")

    _wizytowka(imie="Marek", rola="Admin", poziom=5)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 5️⃣ Zasięg Zmiennych (Scope)
    - **Globalne**: Dostępne w całym module.
    - **Lokalne**: Żyją tylko wewnątrz funkcji.
    - **Słowo kluczowe `global`**: Pozwala na modyfikację zmiennej globalnej wewnątrz funkcji (używać ostrożnie!).
    """)
    return


@app.cell
def _():
    _zmienna_globalna = "Jestem z góry"

    def _test_zasiegu():
        _zmienna_lokalna = "Jestem z funkcji"
        print(f"Wewnątrz: {_zmienna_globalna}") # Odczyt globalnej jest OK
        print(f"Wewnątrz: {_zmienna_lokalna}")

    _test_zasiegu()
    # print(_zmienna_lokalna) # BLAD! Ta zmienna tutaj nie istnieje.

    def _modyfikuj_globalna():
        global _zmienna_globalna
        _zmienna_globalna = "Zmieniono mnie!"

    _modyfikuj_globalna()
    print(f"Po zmianie: {_zmienna_globalna}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 6️⃣ Referencje i Obiekty (Mechanika Pamięci)
    - **Wszystko jest obiektem**: Zmienne to tylko etykiety (nazwy) wskazujące na miejsce w pamięci.
    - **id()**: Zwraca unikalny adres obiektu w pamięci.
    - **Kopiowanie vs Referencja**: Przypisanie `a = b` nie tworzy kopii danych, tylko nową etykietę do tego samego obiektu.
    """)
    return


@app.cell
def _():
    # Demonstracja referencji na liście (typ mutowalny)
    _lista_a = [1, 2, 3]
    _lista_b = _lista_a # To jest referencja, nie kopia!

    _lista_b.append(99)

    print(f"Lista A: {_lista_a} (id: {id(_lista_a)})")
    print(f"Lista B: {_lista_b} (id: {id(_lista_b)})")
    print(f"Czy to ten sam obiekt? {_lista_a is _lista_b}")

    # Tworzenie prawdziwej kopii
    _lista_c = _lista_a.copy()
    print(f"Czy C to ten sam obiekt co A? {_lista_a is _lista_c}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 5️⃣ Programowanie Obiektowe (OOP)
    - **Klasy**: Szablony obiektów.
    - **__init__**: Konstruktor.
    - **self**: Odwołanie do instancji.
    - **Dziedziczenie**: Przejmowanie cech innej klasy.
    """)
    return


@app.cell
def _():
    class Pojazd:
        def __init__(self, nazwa):
            self.nazwa = nazwa
        def trabienie(self):
            return "Beep!"

    class Auto(Pojazd): # Dziedziczenie
        def trabienie(self):
            return f"{self.nazwa} trąbi: VRUUM!"

    _moje_auto = Auto("Audi")
    print(_moje_auto.trabienie())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 6️⃣ Biblioteki: Pandas i NumPy
    - **NumPy**: Szybkie operacje na tablicach.
    - **Pandas**: Dane tabelaryczne (DataFrame).
    - **Analiza**: Filtrowanie, statystyki, wczytywanie plików.
    """)
    return


@app.cell
def _():
    import numpy as np
    import pandas as pd

    # NumPy
    _tablica = np.array([1, 2, 3])
    print(f"Średnia NumPy: {np.mean(_tablica)}")

    # Pandas DataFrame
    _data = {'Produkt': ['A', 'B'], 'Cena': [10, 20]}
    _df = pd.DataFrame(_data)
    print("Pandas DataFrame:")
    print(_df.head())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 7️⃣ Obraz i Wielowątkowość (OpenCV & Threads)
    - **OpenCV (cv2)**: Przetwarzanie obrazu (filtry, kolory).
    - **threading**: Wykonywanie zadań w tle.
    """)
    return


@app.cell
def _():
    import cv2
    import threading
    import time

    # Symulacja wątku
    def zadanie_w_tle():
        print("Wątek pracuje...")
        time.sleep(1)
        print("Wątek skończył.")

    _watek = threading.Thread(target=zadanie_w_tle)
    _watek.start()

    # OpenCV (przykład teoretyczny - wymaga pliku)
    # img = cv2.imread('foto.jpg')
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print("OpenCV i Wątki zainicjalizowane.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 8️⃣ Narzędzia Systemowe i Dynamiczne
    - **eval / exec**: Wykonywanie stringów jako kodu.
    - **os**: Operacje na plikach i systemie.
    - **pickle**: Serializacja (zapisywanie obiektów do pliku).
    """)
    return


@app.cell
def _():
    import os
    import pickle

    # Eval
    _kod = "5 * 10"
    print(f"Eval result: {eval(_kod)}")

    # Pickle
    _dane = {"id": 1, "status": "ok"}
    _binary = pickle.dumps(_dane)
    print(f"Zserializowane: {_binary}")
    _odczyt = pickle.loads(_binary)
    print(f"Odszyfrowane: {_odczyt}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🏁 PODSUMOWANIE
    Powyższy arkusz zawiera esencję całego kursu. Korzystaj z niego jako szybkiej ściągi podczas rozwiązywania zadań i powtórek!
    """)
    return


if __name__ == "__main__":
    app.run()
