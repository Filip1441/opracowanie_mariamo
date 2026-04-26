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
    # Wykład 4: Meta-programowanie
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### LOGIKA: Dekoratory i Lambdy
    `lambda x: x*2` to funkcja anonimowa. `@dekorator` to funkcja wyższego rzędu.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Generator range**: Wykorzystanie leniwego generatora `range()` do generowania sekwencji liczb bez alokowania pełnej listy w pamięci.
    - **Dynamiczne Wykonywanie**: Funkcja `exec()` pozwala na uruchamianie całych bloków kodu zapisanego w stringu. W przeciwieństwie do `eval`, nie zwraca wartości.
    - **Iteracja**: Zastosowanie pętli `for` do przetwarzania elementów sekwencji.
    """)
    return


@app.cell
def _():
    import time
    _var_x=0
    _source='_var_x+=1'
    # 'interial veriable _source' - sygnał korzystania ze zmiennych zewnętrznych
    _csource=compile(_source,'interial veriable _source','exec')

    _start=time.time()
    for i in range(100000): result=exec(_source)
    _end=time.time()
    print(_var_x)
    _startc=time.time()
    for i in range(100000): result=exec(_csource)
    _endc =time.time()
    print(_var_x)
    print((_end-_start)/(_endc-_startc))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Pytania:

    * Czym się różni eval od exec?
    * Jakie są zalety compile?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Zakres zmiennych

    Zmienne w języku Python są widoczne poza blokiem w którym zostały zdefiniowane. Nie są widoczne poza funkcją w której zostały zdefiniowane, ale to zostanie omówione po wprowadzeniu funkcji. Pozwala to na pisanie bardziej zwiezłego kodu, trzeba jednak pamietać o ryzyku odwoływania się do niezainicjalizowanej zmiennej.
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
    _x=int(input())
    if _x>0:
        _pp1=1
    print(_pp1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Funkcje

    Funkcje w Pythonie mogą przyjmować dowolną liczbę argumentów oraz zwracać wartość (pojedynczą, None - gdy nic nie zwracają lub krotkę - wtedy zwracają "kilka wartości").
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
    # przekazywanie argumentów przez pozycję

    def get_fibonacci(max_val):
      a, b = 0, 1
      _out = [a]
      while b <= max_val:
        _out.append(b)
        a, b = b, a + b
      return _out

    _fib = get_fibonacci(10)
    print(_fib)
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
    # przekazywanie argumentów przez podanie nazwy

    def get_fibonacci(max_val):
      a, b = 0, 1
      _out = [a]
      while b <= max_val:
        _out.append(b)
        a, b = b, a + b
      return _out

    _fib = get_fibonacci(max_val=40)
    print(_fib)
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
    _ret = print_fibonacci(10)
    print('Zwrócono:', _ret)
    return (print_fibonacci,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Wartości domyślne parametrów podaje się bezposrednio w ich definicji. Argumenty z wartościami domyślnymi muszą występować na końcu (po wszytstkich argumentach bez wartości domyślnych).
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
    # Wartości domyślne muszę być na końcu
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
    return (print_fibonacci,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Analiza**: Implementacja logiki algorytmu z wykorzystaniem standardowej składni i wbudowanych mechanizmów Pythona.
    """)
    return


@app.cell
def _(print_fibonacci):
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Analiza**: Implementacja logiki algorytmu z wykorzystaniem standardowej składni i wbudowanych mechanizmów Pythona.
    """)
    return


@app.cell
def _():
    # print_fibonacci(start=3, 40)   # BŁĄD SYNTAKTYCZNY: argument pozycyjny po słowie kluczowym!
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
def _(print_fibonacci):
    print_fibonacci(start=3, max_val=40)
    return


@app.cell
def _():
    pass
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Funkcje mogą być wywoływane z listą argumentów nieznanej długości (symbol gwiazadki) lub ze słownikiem argumentów, w drugim przypadku wartości argumentów zwykle są poprzedzone ich nazwą (symbol podwójnej gwiazdki). Jest to stosowane raczej przy bardziej złożonych funkcjach, mających bardzo wiele opcji.
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
    def function_with_args(*args):
      for arg in args:
        print(arg)

    function_with_args(4, 'a', {0: False, 1: True})
    return (function_with_args,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Analiza**: Implementacja logiki algorytmu z wykorzystaniem standardowej składni i wbudowanych mechanizmów Pythona.
    """)
    return


@app.cell
def _(function_with_args):
    function_with_args(2)
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
    def function_with_keyword_args(**kwargs):
      for name, value in kwargs.items():
        print(name, value)

    function_with_keyword_args(a=8, repeat=0, f=True)
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
    def both_args_and_kwargs(*args, **kwargs):
      print('args:')
      for item in args:
        print(item)
      print('keyword args:')
      for key, value in kwargs.items():
        print("key=",key, "val=",value)

    both_args_and_kwargs(3, ['abc', 'xyz'],x=6, a=4, c='text')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Analiza**: Implementacja logiki algorytmu z wykorzystaniem standardowej składni i wbudowanych mechanizmów Pythona.
    """)
    return


@app.cell
def _(bad_function):
    # tu będzie błąd, bo mamy ten sam typ, nie wiadomo kiedy zaczyna się jeden argument a kiedy drugi

    # def bad_function(*args, *args2): # BŁĄD: Można mieć tylko jeden argument z gwiazdką!
    #   print(args, args2)
    pass

    bad_function(1, 2, 3, 4, 5)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Zadanie: napisać funkcję, która zwraca sumę jej argumentów, liczba argumentów może być dowolna.
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
    def sum(*args):
      _k=0
      for i in args:
        _k=_k+i
      return _k
    print(sum(1,2,3))
    _a=[1,2,3]
    print(sum(*_a))
    return (sum,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Zadanie: napisać funkcję, która wypisuje sumę cen artykułów zawartych w liście zakupów. Cennik artykułów jest argumentem funkcji.
    """)
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
    # args - _lista  produktów, kargs - słownik zawierający cenę produktów
    def BuyMe(*args,**kwargs):
      print('args=',args)
      print('args=',kwargs)
      _k=0.0
      for a in args:
            if a in kwargs:  # Sprawdzenie, czy klucz istnieje w kwargs
                _k += float(kwargs[a])  # Dodanie wartości do sumy

      print(_k)  # Wypisanie sumy
    _lista=['ser','mleko','chleb']
    _ceny={'ser':10.0,'mleko':4.0,'chleb':8.0}
    BuyMe(*_lista, **_ceny)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Pytania
    Mam funkcję:

    def readdata(nazwa, format):
    .....
    Jaki będzie wynik wywołania:
    readdata('plik')?
    Dodatkowe pytanie.
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
    def readdata(name, format='pdf'):
      print(name,' ', format)
    readdata('name')
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
    def fun_a(*args):
      for i in args: print(i)

    _lista=[1,2,3]

    #jaka jest różnica między:
    fun_a(_lista)
    #a
    fun_a(*_lista)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Funkcja jako obiekt
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
    def BuyMe(*args,**kargs):
      print('args=',args)
      print('args=',kargs)

    _Bm=BuyMe
    print(type(_Bm))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Dkaczego nie widzi kargs, jak to zmienić?
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
    def BuyMe(*args,**kargs):
      print('args=',args)
      print('kargs=',kargs)

    _Bm=BuyMe

    _Bm('ser',{'ser':10})
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
    def Kup(*args):
        print('kupuje', args)
    def Idzpo(*args):
        print('ide do sklepu po', args)

    _lista=['chleb','ser']
    _dzialanie = [Idzpo,Kup]
    for  d in _dzialanie:
        d(*_lista)

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
    def Bake(a):
        print("piekę",a)
    def Mix(a):
        print("mieszam",a)
    def Add(a):
        print("dodaję",a)
     # lista funkcja i argument
    _cookbook=[(Add,'mleko'),(Add,'cukier'),(Mix,'skladniki'),(Bake,'ciasto')]
    for akcja,obiekt in _cookbook:
            akcja(obiekt)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Tworzenie funkcji na podstawie funkcji istniejącej
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Iteracja**: Zastosowanie pętli `for` do przetwarzania elementów sekwencji.
    - **Kontrola Przepływu**: Implementacja logiki warunkowej sterującej wykonaniem bloku kodu.
    """)
    return


@app.cell
def _():
    def Nf(kind='+'):
        def fw(*args,kind=kind):
         _w=0 if kind=='+' else 1
         if kind=='+':
          for a in args:
            _w=_w+a
          return _w
         else:
          for a in args:
            _w=_w*a
          return _w
        return fw
    _sum=Nf('+')
    _mul=Nf('*')
    print(_mul(8,2,3))
    print(_sum(8,2,3))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Iteracja**: Zastosowanie pętli `for` do przetwarzania elementów sekwencji.
    """)
    return


@app.cell
def _(f):
    ## przekazywanie argumentów do exec
    def Nf(kind='+'):
        _source='''
    def fw(*args):
         _w=0
         for a in args:
            _w=_w{}a
    return _w
         '''.format(kind)
        return f

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Dynamiczne Wykonywanie**: Funkcja `exec()` pozwala na uruchamianie całych bloków kodu zapisanego w stringu. W przeciwieństwie do `eval`, nie zwraca wartości.
    - **Iteracja**: Zastosowanie pętli `for` do przetwarzania elementów sekwencji.
    - **Kontrola Przepływu**: Implementacja logiki warunkowej sterującej wykonaniem bloku kodu.
    """)
    return


@app.cell
def _(fw):
    def Nf(kind='+'):
        _source = '''
    def fw(*args, kind='{}'):
         _w = 0 if kind == '+' else 1
         for a in args:
            _w = _w {} a
         return _w
         '''.format(kind, kind)
        exec(_source, globals())
        return fw

    _f_add = Nf('+')
    _f_m = Nf('*')
    print(_f_add(0, 2, 3))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Pytania

    Po co tworzymy funkcje dedykowane, jakie są zalety takiego rozwiązania?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Zmienne globalne

    W języku Python bloki nie ograniczaja widoczności zmiennych ani możliwości ich zapisu:
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
    _a = 3
    for _ in range(2):
      print(_a)
      _a = 4
    print(_a)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Inaczej jest w wypadku funkcji, w których możliwy jest odczyt, ale nie modyfikacja zmiennych:
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

    _b = 3

    def f(x):
      _a1=5
      _b=10
      return _a1 * x + _b


    print(f(2))
    print(_b)
    return (f,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    W wypadku modyfikacji zmiennych spoza funkcji w jej wnętrzu zmianie ulegają ich lokalne kopie:
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
    _x = "global"
    def foo():
        _x=" "
        _x = _x+"sdsdsd"
        print(_x)

    foo()
    print(_x)
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
    _a = 2
    _b = 3

    def f(x):
      _a = 1
      _b = 0
      return _a * x + _b

    print(f(2))
    print('_a=',_a, '_b=',_b)
    return (f,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Aby zmienić wartość zmiennej globalnej, należy użyć słowa kluczowego global.
    Nie zaleca się jednak takiego sposobu programowania.
     Podobne znaczenie ma słowo kluczowe nonlocal, ale dotyczy to funkcji wewnętrznych.
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
    _a = 4
    _b = 3

    def f(x):
      global _a, _b
      _a = 1
      _b = 0
      return _a * x + _b

    print(f(2))
    print(_a, _b)
    return (f,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Analiza**: Implementacja logiki algorytmu z wykorzystaniem standardowej składni i wbudowanych mechanizmów Pythona.
    """)
    return


@app.cell
def _():
    def f1(x):
    #  global _a
      _a=2
      def f(x):
        nonlocal _a
        _a = 1
        return _a * x
      _y=f(x)
      print("wartość _a  w f1",_a,"wynik f1",_y )
      return(_y)
    _a=10
    f1(2)
    print("wartość _a na końcu", _a)
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
    def f1(x):
      _a=2
      _b=3
      def f(x):
        global _a,_b
        _a = 1
        _b = 0
        return _a * x + _b
      _y=f(2)
      print(_a,_b)
      return(_y)
    _a=1
    _b=2
    print(f1(2))
    print(_a, _b)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Import funkcji z innych plików

    Popularność Pythona wynika w znacznej mierze z dużej liczby bibliotek ułatwiajacych wykonywanie różnorakich zadań oraz łatwości ich wykorzystania. Aby zaimportować biblioteke do programu korzystamy z polecenia import. Należy pamietać, ze każdy moduł zostanie zaimportowany tylko raz podczas wywołania programu, nawet jeśli wystąpi kilka wywołań. Biblioteki zwyczajowo importujemy na początku pliku .py
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
    import os  # import modułu os
    import numpy as np  # import modułu numpy i nadanie mu lokalnie nazwy np

    return (np,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Analiza**: Implementacja logiki algorytmu z wykorzystaniem standardowej składni i wbudowanych mechanizmów Pythona.
    """)
    return


@app.cell
def _():
    import os
    import numpy as np
    _files = os.listdir('.')
    print(_files)
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
    # Wywołanie funkcji array z modułu numpy, tworzącej tablicę
    import numpy as np
    _x = np.array([1, 2, 3])
    print(_x)
    return (np,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    """)
    return


@app.cell
def _(numpy):
    # Nie możemy odwoływać sie do biblioteki pod nazwą globalną,
    # jeśli ustawilismy lokalną
    import numpy as np
    _x = numpy.array([1, 2, 3])  #błąd bo np
    return (np,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Analiza**: Implementacja logiki algorytmu z wykorzystaniem standardowej składni i wbudowanych mechanizmów Pythona.
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Funkcje w poprawnie przygotowanych modułach zawieraja dokumentację w formie docstringa. Warto równiez o tym pamietać przy tworzeniu własnych modułów (co jest poza zakresem tego wykładu).
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
def _(np):
    help(np.array)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Lambda

    Lambda jest sposobem definiowania funkcji anonimowej pozwalającym często na bardziej zwięzły zapis kodu.
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
    # Zwykłą funkcja
    def f1(x):
      return 2*x + 1

    # Lambda
    _f2 = lambda x: 2*x + 1

    # Identyczna składnia i wynik
    print(f1(3))
    print(_f2(3))
    # Przypisanie lambdy do nazwanej zmiennej nie daje nowych możliwosci
    # i obniza czytelność
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
    _lista_zwierze_waga = [('pies', 10.), ('kot', 5.), ('koń', 200.), ('wróbel', 0.1)]

    # Sortowanie z wykorzystaniem funkcji
    def odczyt_wagi(zwierze_waga):
      return zwierze_waga[1]

    _posortowana_1 = sorted(_lista_zwierze_waga, key=odczyt_wagi)

    # Sortowanie z lambdą - jedna linijka
    _posortowana_2 = sorted(_lista_zwierze_waga, key=lambda x: x[1])

    for item in _posortowana_1:
      print(item)
    print('-----------')
    for item in _posortowana_2:
      print(item)
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
    # Lambda moze mieć wiele arguemntów, np. dwa:
    _f = lambda x, y: x * y

    print(_f(2, 3))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Funkcje wbudowane
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    filter - zwraca iterator elementów kolekcji (a nie listę), które spełniaja określone kryterium
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
    _weights = [10, 40, 320, 450, 70, 115, 3]
    _filter_heavy = filter(lambda x: x > 100, _weights)
    print(_filter_heavy)  #referencja do listy
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
    # Uzyskanie listy na podstawie iteratora
    _weights = [10, 40, 320, 450, 70, 115, 3]
    _filter_heavy = filter(lambda x: x > 100, _weights)
    print(list(_filter_heavy))
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
    # Ponowne wywołanie - iterator dotarł do końca, jest pusty
    _weights = [10, 40, 320, 450, 70, 115, 3]
    _filter_heavy = filter(lambda x: x < 100, _weights)
    print(list(_filter_heavy))
    print(list(_filter_heavy))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    map - umożliwia zastosowanie danej operacji na każdym elemencie kolekcji i uzyskanie nowej kolekcji.

    Szczególnie przydatne przy przetwarzaniu równoległym, gdy dla każdego z elementów należy wykonać skomplikowane obliczenia (przetwarzanie równoległe będzie omawiane później, poniższy przykład jest szeregowy)
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
    def square(n):
        return n*n
    _my_list = [2,3,4,5,6,7,8,9]
    _updated_list = map(square, _my_list)
    #_updated_list = map(lambda x: x*x, _my_list)
    print('wskaznik',_updated_list)
    print(list(_updated_list))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    reduce - na podstawie kolekcji tworzy pojedynczą wartość, np. sumę:
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
    from functools import reduce
    _numbers = [ 1 , 2 , 3 , 4 , 5 ]
    def il(a,b):
       return a*b
    _result = reduce(il,_numbers)
    print(_result)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    """)
    return


@app.cell
def _(sum):
    from functools import reduce
    _numbers = [ 1 , 2 , 3 , 4 , 5 ]
    _sum_of_numbers = reduce(lambda x, y: x + y, _numbers)
    print(_sum_of_numbers)
    print(sum(_numbers))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    """)
    return


@app.cell
def _(sum):
    from functools import reduce
    _numbers = [ 1 , 2 , 3 , 4 , 5 ]
    _sum_of_numbers = reduce(lambda x, y: x + y, _numbers,10)
    #10 inicjalizacja
    print(_sum_of_numbers)
    print(sum(_numbers))
    return


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
    from functools import reduce
    _numbers = [ 1 , 2 , 3 , 4 , 5 ]
    _sum_of_numbers = reduce(lambda x, y: x+y if y%2==0 else x, _numbers,0)
    print(_sum_of_numbers)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Pytania


    Co to jest wyrażenie lambda?
    Napisać wyrażenie lambda które sumuje dwie liczby
    """)
    return


@app.cell
def _():
    pass
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Dekoratory, generatory, funkcje częściowe

    Funkcje cząstkowe - przydatne, gdy nie chcemy wielokrotnie podawać tych samych wartości niektórych argumentów.
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
    from functools import partial

    def power(x, y):
      return x**y

    _square = partial(power, y=2)
    print(_square(4))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Generatory - funkcje umożliwiajace tworzenie iteratorów. Od zwykłych funkcji różnią się tym, że:
    *   zwracają kolejną wartosć za pomocą słowa kluczowego yield
    *   zapamiętują swój stan z momentu ostatniego wywołania
    *   zwracaja kolejną wartość po zastosowaniu do nich polecenia next()
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
    def generuj_parzyste(stop):
      _x = 0
      while _x < stop:
        yield _x
        _x += 2

    _generator = generuj_parzyste(6)
    print(next(_generator))
    print(next(_generator))
    print(next(_generator))
    if _generator==None:
      print('null')
    return (generuj_parzyste,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Iteracja**: Zastosowanie pętli `for` do przetwarzania elementów sekwencji.
    """)
    return


@app.cell
def _(generuj_parzyste):
    # Użycie generatora z pętlą for
    _generator = generuj_parzyste(12)
    for x in _generator:
      print(x)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    W Pythonie funkcja jest obiektem
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
    def func():
        print('tekst')
    _f1=func
    _f1()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Jeśli f to funkcja, to jaka jest różnica między:
    _f2=f, a _f2=f()?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Dekorator - funkcja lub obiekt, który można wywołać przekazując mu jako argument dekorowaną funkcję lub klasę, w wyniku czego uzyska sie funkcję lub klasę o rozszerzonej funkcjonalności (udekorowaną)
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
    def hello(func):
        def inner():
            print("Witaj ")
            func()
        return inner

    def name():
        print("Alu")


    _obj = hello(name)
    _obj()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    W tym przypadku hello jest dekoratorem
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Analiza**: Implementacja logiki algorytmu z wykorzystaniem standardowej składni i wbudowanych mechanizmów Pythona.
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Praca  domowa



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
    za każdym razem wywoła odpowiednią funkcję, przekazując do niej aktualną wartość argumentu value i wyświetli aktualną wartość value
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Proszę napisać kod w sposób "pythonowy", wykorzystując wyrażenie lambda
    """)
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
    _osoba={}
    _x=int(input('Proszę podać liczbę osób: '))
    for i in range(0,_x):
        _nazwisko=input('Proszę podać _nazwisko: ')
        _osoba[_nazwisko]=int(input('Proszę podać wiek: '))
    _y=int(input('Wypisanie nazwisk powyżej wieku: '))
    for key in _osoba:
        if _osoba[key] > _y:
            print(key)
    print(_osoba)
    return


if __name__ == "__main__":
    app.run()
