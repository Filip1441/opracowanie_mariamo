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
    Podstawowe operacje na ciągach znaków:
    * str.upper() - zamienia wszystkie litery na wielkie.
    * str.lower() - zamienia wszystkie litery na małe.
    * str.capitalize() - zamienia pierwszą literę na wielką, resztę na małe.
    * str.title() - zamienia pierwsze litery wszystkich słów na wielkie.
    * str.swapcase() - zamienia wielkie litery na małe i odwrotnie.

    Sprawdzanie zawartości ciągu znaków:

    * str.startswith(prefix) - sprawdza, czy ciąg zaczyna się od prefix.
    * str.endswith(suffix) - sprawdza, czy ciąg kończy się na suffix.
    * str.isalpha() - sprawdza, czy ciąg zawiera tylko litery.
    * str.isdigit() - sprawdza, czy ciąg zawiera tylko cyfry.
    * str.isalnum() - sprawdza, czy ciąg zawiera tylko litery i cyfry.
    * str.isspace() - sprawdza, czy ciąg zawiera tylko białe znaki.
    * str.islower() - sprawdza, czy wszystkie litery są małe.
    * str.isupper() - sprawdza, czy wszystkie litery są wielkie.

    Operacje na białych znakach:

    * str.strip([chars]) -  usuwa białe znaki (lub podane znaki) z początku i końca ciągu.
    * str.lstrip([chars]) - usuwa białe znaki (lub podane znaki) z początku ciągu.
    * str.rstrip([chars]) - usuwa białe znaki (lub podane znaki) z końca ciągu.

    Zastępowanie i modyfikowanie tekstu:

    * str.replace(old, new[, count]) - zamienia wszystkie (lub określoną liczbę) wystąpienia old na new.
    * str.translate(table) - tłumaczy znaki zgodnie z podaną tabelą (stosowane z str.maketrans).
    * str.zfill(width) - dodaje zera na początku, aby osiągnąć określoną długość.

    Wyszukiwanie i dzielenie tekstu:

    * str.find(sub[, start[, end]]) – zwraca indeks pierwszego wystąpienia sub lub -1, jeśli nie znaleziono.
    * str.rfind(sub[, start[, end]]) – zwraca indeks ostatniego wystąpienia sub.
    * str.index(sub[, start[, end]]) – jak find(), ale rzuca wyjątek ValueError, jeśli sub nie występuje.
    * str.rindex(sub[, start[, end]]) – jak rfind(), ale rzuca wyjątek ValueError, jeśli sub nie występuje.
    * str.count(sub[, start[, end]]) – zwraca liczbę wystąpień sub w ciągu.
    * str.split([sep[, maxsplit]]) – dzieli ciąg według sep, zwracając listę części.
    * str.rsplit([sep[, maxsplit]]) – jak split(), ale dzielenie zaczyna się od końca.
    * str.splitlines([keepends]) – dzieli tekst na linie.
    * str.partition(sep) – dzieli ciąg na trzyczęściową krotkę: (przed, sep, po).
    * str.rpartition(sep) – podobne do partition(), ale szuka sep od końca.

    Formatowanie tekstu:

    * str.center(width[, fillchar]) – centruje ciąg w polu o szerokości width.
    * str.ljust(width[, fillchar]) – wyrównuje ciąg do lewej.
    * str.rjust(width[, fillchar]) – wyrównuje ciąg do prawej.
    * str.format(*args, **kwargs) – formatuje ciąg według podanych argumentów.
    * str.format_map(mapping) – jak format(), ale używa słownika.
    * str.join(iterable) – łączy elementy iterowalnej kolekcji w jeden ciąg, używając ciągu jako separatora.
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
    str = "Ala ma kota {}"
    print(str.upper())
    print(str.lower())
    _text1 = "Produkt: {produkt}, cena: {cena} zł"
    print(_text1)
    _text=_text1.format(produkt="Chleb", cena=4.5)
    print(_text)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Świat bez klas
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Chcemy zbudować zbiór danych o osobach.
    * Co powinniśmy zrobić?
    * Jakie struktury danych należu użyć?
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
    _osoba1={'name':'ALA','age':15}
    def getname(osoba):
      return osoba['name']
    def getage(osoba):
      return osoba['age']
    print(getname(_osoba1))
    print(getage(_osoba1))
    return (getname,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    - **Iteracja**: Zastosowanie pętli `for` do przetwarzania elementów sekwencji.
    """)
    return


@app.cell
def _(getname, osoba1):
    _osoba2={'name':'TOMEK','age':85}
    _lista=[osoba1,_osoba2]
    for os in _lista: print(getname(os))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Z tekstu nie wynika jednoznacznie, że dwa obiekty należą do tej samej klasy, lista obiektów nie jest związana w sposób widoczny z klasami, liczba elementów przechowywana w oddzielnej zmiennej
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Programowanie obiektowe
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    W klasycznych językach programowania klasa składa się


    * Opisu atrybutów klasy (argumentów, nazw pól)
    * Konstruktora
    * Metod

    Dodatkowe pojęcia:

    * argumenty prywatne
    * argumenty statyczne
    * metody statyczne
    * polimorfizm
    * dziedziczenie
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
    # klasa Osoba  - konstruktor

    class Osoba:
     def  __init__(self, name, age):
      self.name=name
      self.age=age

    _o1=Osoba("Ania",50)
    print(_o1.name,_o1.age)
    return (Osoba,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Nie definiujemy pól w nagłówku, są one definiowane w konstruktorze
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
    # klasa Osoba, dodajemy metody

    class Osoba:
     def  __init__(self, name, age):
      self.name=name
      self.age=age
     def  druk(self):
      print(self.name,self.age)

    _o1=Osoba("Ania",50)
    _o1.druk()
    return (Osoba,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Pola statyczne
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    pola statyczne są powiązane z klasą, a nie z obiektem, nie mamy słów kluczowych, decyduje miejsce deklaracji
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
    class Osoba:
     _liczba=0              #_liczba elementów            #miejsce deklaracji
     _lista=[]              #_lista elementów
     def  __init__(self, name, age):
      self.name=name
      self.age=age
      Osoba._liczba+=1
      Osoba._lista.append(self)
     def  druk(self):
      print(self.name,self.age,Osoba._liczba)

    _o1=Osoba("Ania",50)
    _o1.druk()
    _o2=Osoba("Agata",50)
    _o2.druk()
    _o1.druk()
    return (Osoba,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Pobieranie informacji o instancji lub klasie
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Typowanie**: Wykorzystanie `isinstance()` do dynamicznej weryfikacji przynależności obiektu do klasy lub typu. Jest to bezpieczniejsza alternatywa dla `type() == ...` ze względu na obsługę dziedziczenia.
    """)
    return


@app.cell
def _(Osoba, o1):
    print(isinstance(o1,Osoba))  #sprawdzenie czy o1 jest instancją klasy
    print(type(o1))  #sprawdzenie instancją jakiej klasy jest o1
    print(o1.__class__)  # __cos__  - specjalne metody lub pola
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
    # dokładniejsze informacje o obiekcie
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Analiza**: Implementacja logiki algorytmu z wykorzystaniem standardowej składni i wbudowanych mechanizmów Pythona.
    """)
    return


@app.cell
def _(o1):
    print(vars(o1))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Analiza**: Implementacja logiki algorytmu z wykorzystaniem standardowej składni i wbudowanych mechanizmów Pythona.
    """)
    return


@app.cell
def _(Osoba):
    print(vars(Osoba))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Analiza**: Implementacja logiki algorytmu z wykorzystaniem standardowej składni i wbudowanych mechanizmów Pythona.
    """)
    return


@app.cell
def _(Osoba):
    dir(vars(Osoba))
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
    class Osoba:
     def  __init__(self, name, age, sex):
      self.name=name
      self.age=age
      self.__sex=sex
    _o1=Osoba("Ania",50,"women")
    print(_o1.name,_o1.age,_o1.__sex)    #próba dostępu do pola prywatnego, błąd
    return (Osoba,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Pola prywatne - brak dostępu poza klasą
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
    class Osoba:
     _l=1
     def  __init__(self, name, age,sex,_l):
      self.name=name
      self.age=age
      self.__l=_l
    _o1=Osoba("Ania",50,"women",2)
    _o1.__l=8        #powstaje nowe pole
    print(vars(_o1))
    return (Osoba,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Analiza**: Implementacja logiki algorytmu z wykorzystaniem standardowej składni i wbudowanych mechanizmów Pythona.
    """)
    return


@app.cell
def _():
    class Osoba:
     def  __init__(self, name, age, sex):
      self.name=name
      self.age=age
      self.__sex=sex
    _o1=Osoba("Ania",50,"women")
    _o1.__sex="mmm"                             #powstaje nowe pole
    print(_o1.name,_o1.age,_o1.__sex)
    print(vars(_o1))
    return (Osoba,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Analiza**: Implementacja logiki algorytmu z wykorzystaniem standardowej składni i wbudowanych mechanizmów Pythona.
    """)
    return


@app.cell
def _():
    #dodawanie pól poza klasą


    class Osoba:
     def  __init__(self, name, age):
      self.name=name
      self.age=age
    _o1=Osoba("Ania",50)
    print(vars(_o1))
    _o1.sex="Women"                         #powstaje nowe pole
    print(_o1.name,_o1.age,_o1.sex)
    print(vars(_o1))
    return (Osoba,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Analiza**: Implementacja logiki algorytmu z wykorzystaniem standardowej składni i wbudowanych mechanizmów Pythona.
    """)
    return


@app.cell
def _():
    # usuwanie atrybutu

    class Osoba:
     def  __init__(self, name, age):
      self.name=name
      self.age=age
    _o1=Osoba("Ania",50)
    _o1.sex="Women"
    print(vars(_o1))
    del _o1.sex
    print(vars(_o1))
    return (Osoba,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Funkcja setattr       umożliwia zmianę wartości pól, kolejność jak w konstruktorze
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
    class Osoba1:
     def  __init__(self, name, age):
      self.name=name
      self.age=age
    _o2=Osoba1("Ania",50)
    # print(_o2.name,_o2.age,_o2.sex)
    setattr(_o2,"sex","woman")    #_o2 musi istnieć
    print(_o2.name,_o2.age,_o2.sex)
    print(vars(_o2))
    delattr(_o2,"sex")             #tu usuwamy atrybut
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Metody statyczne, to metody związane z klasą, a nie z pojedynczym obiektem
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
    #metody klasy

    class Osoba:
     def  __init__(self, name, age):
      self.name=name
      self.age=age
    #definiujemy metodę statyczną
     @classmethod             #metoda statyczna
     def nag(cls):
      print("klasa osoba")
    _o1=Osoba("Ania",50)
    _o1.sex="Women"
    Osoba.nag()
    print(_o1.name,_o1.age,_o1.sex)
    print(vars(_o1))
    return (Osoba,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Analiza**: Implementacja logiki algorytmu z wykorzystaniem standardowej składni i wbudowanych mechanizmów Pythona.
    """)
    return


@app.cell
def _():
    # metoda split, będzie potrzebna w kolejnym przykładzie
    _tekst="jan ma"
    print(*_tekst.split(' '))
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
    #metody klasy trochę bardziej skomplikowane, tworzenie obiektu bez konstruktora

    class Osoba:
     def  __init__(self, name, age):
      self.name=name
      self.age=age
    #definiujemy metodę statyczną
     @classmethod
     def newob(cls,tekst):
      print(tekst)   #tekst, wartości argumentów
      print(*tekst)  #ciąg znaków
      _o2=cls(*tekst.split(' '))
      return(_o2)
    _o1=Osoba("Ania",50)
    _o2=Osoba.newob("Jan 100")
    print('_o2', _o2.name,_o2.age)
    print('vars _o2', vars(_o2))
    return (Osoba,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Analiza**: Implementacja logiki algorytmu z wykorzystaniem standardowej składni i wbudowanych mechanizmów Pythona.
    """)
    return


@app.cell
def _():
    # Dekoratory - property, odwołujemy się do metody jak do pola klasy
    class Osoba:
     def  __init__(self, name, age, sex):
      self.name=name
      self.age=age
      self.sex=sex
     @property       #możemy się odwoływać do metody jak do pola klasy
     def prints(self):
       print(self.sex)
    _o1=Osoba("Ania",50,"women")
    print(_o1.name,_o1.age)
    _o1.prints              # to jest poprawne
    print(vars(_o1))
    print(vars(Osoba))
    return (Osoba,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Analiza**: Implementacja logiki algorytmu z wykorzystaniem standardowej składni i wbudowanych mechanizmów Pythona.
    """)
    return


@app.cell
def _():
    # Dekoratory ustawianie wartości
    class Osoba:
     def  __init__(self, name, age, sex):
      self.name=name
      self.age=age
      self.__sex=sex
     @property                           # umożliwia pobranie wartości pola prywatnego
     def sex(self):
       return self.__sex
     @sex.setter                         # umożliwia zmianę wartości pola prywatnego
     def sex(self,newval):
       self.__sex=newval
    _o1=Osoba("Ania",50,"women")
    print(_o1.name,_o1.age,_o1.sex)             # sex to funkcja, a nie pole klasy
    _o1.sex="man"
    print(vars(_o1))


    _o2=Osoba("Tom",50,"women")
    print(_o2.name,_o1.age)
    _o2.sex="man"
    print(vars(_o2))
    return (Osoba,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Metody prywatne, podobnie jak pola zaczynają się od __
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
    class Osoba:
     def  __init__(self, name, age, sex):
      self.name=name
      self.age=age
      self.__sex=sex
     def __getname(self):
      return self.name
     def printname(self):
       print(self.__getname())
    _o1=Osoba("Basia",100,"nn")
    _o1.printname()
    return (Osoba,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Klasy collable, obiekty tych klas możemy wyoływać jak funkcje
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
    # sprawdzamy
    print(callable(len))          # True (funkcja wbudowana)
    print(callable(42))           # False (liczba nie jest callable)
    print(callable(lambda x: x))
    _a1=lambda x:x
    print(callable(_a1))
    return


@app.cell
def _():
    pass
    return


@app.cell
def _():
    pass
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
    #klasyczne podejście
    class Osoba:
     def  __init__(self, name, lista):
      self.name=name
      self.lista=lista
    _o1=Osoba("Basia",[])
    _o1.lista.append("Basia")
    print(_o1.lista)
    return (Osoba,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    """)
    return


@app.cell
def _():
    #nowe podejście rozszerzania listy, kod jest bardziej czytelny, odzielamy inicjalizację od wykonania
    class Osoba:
     def  __init__(self, name, lista):
      self.name=name
      self.lista=lista
     def __call__(self, item):
       self.lista.append(item)
       print("dodaję",item)
    _o1=Osoba("Basia",[])
    _o2=_o1(" xxxx")
    _o1(" yyy")
    print(_o1.lista)
    print(callable(_o1),callable(_o2))
    return (Osoba,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Do konstruktora możemy przekazać funkcję, tak jak pole klasy
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
    class Osoba:
     _lista=[]
     def  __init__(self, func):
      self.func=func
    def test():
      print("test")
    _o1=Osoba(test)
    _o1.func()
    return (Osoba,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Operatory, operacje na obiektach
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
    class Osoba:
     def  __init__(self, name,lista):
      self.name=name
      self.lista=lista
     def __add__(self,other):           #zwracamy String
       return self.name+" "+other.name
    _o1=Osoba("Basia",[])
    _o2=Osoba("Adam",[])
    print(_o1+_o2)
    return (Osoba,)


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
    class MyClass:
        def __init__(self, value):
            self.value = value

        def __mul__(self, other):
            if isinstance(other, int):
                return MyClass(self.value * other) # zwracamy obieky klasy
            else:
                return 0
    _m1 = MyClass(5)
    _m2=_m1*3
    print(_m2.value)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Przykładowe nazwy:

    * __add__ - Przeciąża operator dodawania +.
    * __sub__ - Przeciąża operator odejmowania -.
    * __div__ - Przeciąża operator dzielenia / (w starszych wersjach Pythona, w Pythonie 3.x należy używać __truediv__).
    * __floordiv__ - Przeciąża operator dzielenia całkowitego //.
    * __mod__ - Przeciąża operator modulo %.
    * __pow__ - Przeciąża operator potęgowania **.
    * __lt__ - Przeciąża operator < (mniejsze niż).
    * __le__ - Przeciąża operator <= (mniejsze niż lub równe).
    * __eq__ - Przeciąża operator == (równe).
    * __ne__ - Przeciąża operator != (różne).
    * __gt__ - Przeciąża operator > (większe niż).
    * __ge__ - Przeciąża operator >= (większe niż lub równe).
    * __getitem__ - Przeciąża operator indeksowania [].
    * __setitem__ - Przeciąża operator przypisania wartości dla indeksu [].
    * __len__ - Przeciąża funkcję len().
    * __str__ - Przeciąża funkcję str().
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Dziedziczenie
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
    #metoda1

    class Osoba:
     def  __init__(self, name):
      self.name=name
    class Student(Osoba):
      def __init__(self,name,id):
       super().__init__(name)
       self.id=id
    _o1=Osoba("Basia")
    _o2=Student("Adam","sdsdsd")
    print(_o2.id)
    return (Osoba,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Analiza**: Implementacja logiki algorytmu z wykorzystaniem standardowej składni i wbudowanych mechanizmów Pythona.
    """)
    return


@app.cell
def _():
    #metoda2

    class Osoba:
     def  __init__(self, name):
      self.name=name
    class Student(Osoba):                           #  Student dziedziczy po klasie Osoba
      def __init__(self,name,id):
       Osoba.__init__(self,name)
       self.id=id
    _o1=Osoba("Basia")
    _o2=Student("Adam","sdsdsd")
    print(_o2.id)
    return (Osoba,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Polimorfizm  - różne zachowanie metody, zależnie od kontekstu
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
    class Kot:
        def dzwiek(self):
            return "Miau!"

    class Pies:
        def dzwiek(self):
            return "Hau!"

    # Funkcja wykorzystująca polimorfizm
    def wydaj_dzwiek(zwierze):
        print(zwierze.dzwiek())

    # Tworzenie obiektów
    _kot = Kot()
    _pies = Pies()

    # Wywołanie tej samej metody na różnych obiektach, a właściwie metody statycznej klasy
    wydaj_dzwiek(_kot)  # Miau!
    wydaj_dzwiek(_pies)  # Hau!
    _lista=[_kot,_pies]   #  Mamy elementy różnych klas
    for zwierze in _lista:
      wydaj_dzwiek(zwierze)
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
    class Osoba:
     def  __init__(self, name):
      self.name=name
     def druk(self):
       print(self.name)
    class Student(Osoba):
      def __init__(self,name,id):
       Osoba.__init__(self,name)
       self.id=id
      def druk(self):
       print(self.name,"  ",self.id)
      def druk(self,tekst):
       print(tekst,"  ",self.name,"  ",self.id)
    _o1=Osoba("Basia")
    _o1.druk()
    _o2=Student("Adam","indeks")
    _o2.druk("tekst")
    return (Osoba,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Dziedziczenie po wielu klasach
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
    class Color:
      def __init__(self,color):
        self.color=color
    class Punkt:
      def __init__(self,x,y):
        self.x=x
        self.y=y
    class Cpunkt(Color,Punkt):
      def __init__(self,x,y,color):
        Color.__init__(self,color)
        Punkt.__init__(self,x,y)
    _o1=Cpunkt(1,2,"red")
    print(vars(_o1))
    return Color, Punkt


@app.cell
def _():
    pass
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    W przypadku wielodziedziczenia mamy problem funkcja z jakiej klasy będzie wywoływana, jeśli nazwy i argumenty są takie same, tu decyduje kolejność klas podana w konstruktorze
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
    class Color:
      def __init__(self,color):
        self.color=color
      def printn(self,ttt):
        print("Color")
        print(ttt)
    class Punkt:
      def __init__(self,x,y):
        self.x=x
        self.y=y
      def printn(self,ttt):
        print("Punkt")
        print(ttt)
    class Cpunkt(Punkt,Color):
      def __init__(self,x,y,color):
        Color.__init__(self,color)
        Punkt.__init__(self,x,y)
    _o1=Cpunkt(1,1,"red")
    _o1.printn("test")
    return Color, Punkt


@app.cell
def _():
    pass
    return


@app.cell
def _():
    pass
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Jeśli funkcja występuje tylko w jednej klasie nadrzędnej to problemu nie mamy
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

    class Color:
      def __init__(self,color):
        self.color=color
      def mprint(self,ttt):
        print("Color")
        print(ttt)
    class Punkt:
      def __init__(self,x,y):
        self.x=x
        self.y=y
      def xmprint(self,ttt):
        print("Punkt")
        print(ttt)
    class Cpunkt(Punkt,Color):
      def __init__(self,x,y,color):
        Color.__init__(self,color)
        Punkt.__init__(self,x,y)
      def mprint(self,ttt):
        super().mprint(ttt)
    _o1=Cpunkt(1,1,"red")
    _o1.mprint("test")
    return Color, Punkt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Warto jest dokumentować kod, a w szczególności klasę którą się zbudowało. Dokumentowanie klasy polega na opisaniu, czym jest klasa, jakie ma atrybuty i metody, jakich typów są argumenty i zwracane wartości, jakie są założenia i wymagania co do poprawności danych wejściowych oraz ogólnie jak korzystać z klasy.

    Zwykle dokumentacja klas jest pisana w tzw. Docstrings, czyli w specjalnym komentarzu umieszczonym na początku definicji klasy, metody lub funkcji. Docstrings są specjalnymi ciągami znaków umieszczonymi w trzech cudzysłowach.
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
def _(Punkt):
    help(Punkt)
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
    class Color:
      """
        Przykład opisu klasy kolor
      """
      def __init__(self,color):
        """
        Do konstruktora przekazujemy kolor
        """
        self.color=color
      def mprint(self,ttt):
        print("Color")
        print(ttt)
    class Punkt:
      def __init__(self,x,y):
        self.x=x
        self.y=y
      def xmprint(self,ttt):
        print("Punkt")
        print(ttt)
    class Cpunkt(Punkt,Color):
      def __init__(self,x,y,color):
        Color.__init__(self,color)
        Punkt.__init__(self,x,y)
      def mprint(self,ttt):
        super().mprint(ttt)
    _o1=Cpunkt(1,1,"red")
    _o1.mprint("test")
    return Color, Punkt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Analiza**: Implementacja logiki algorytmu z wykorzystaniem standardowej składni i wbudowanych mechanizmów Pythona.
    """)
    return


@app.cell
def _(Color):
    help(Color)
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
    ## przykład wykorzystania na wykładzie
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Obsługa wyjątków (błędów)
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
    _x=0
    _z=1/_x
    print(_z)
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
    _x=0
    try:
      _z=1/_x
    except:
      print("dzielenie przez zero")
    else:
      print(_z)
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
    _x=1
    try:
      _z=1/_x
    except:
      print("dzielenie przez zero")
    else:
      print(_z)
    finally:
      print("koniec")
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
    _x=0
    try:
      _z=1/_x
    except Exception as e:
      print("dzielenie przez zero",e)
    else:
      print(_z)
    finally:
      print("koniec")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    W bloku try możemy wykryć różne rodzaje błędów, które mogą wystąpić podczas wykonywania kodu.



    1.    Błędy składniowe (SyntaxError) - wykrywane przez interpreter podczas analizowania składni kodu.
    Wyjątki związane z typami danych (TypeError, ValueError) - np. próba wykonania
    operacji nieobsługiwanej przez dany typ danych, przekroczenie zakresu itp.
    2.   Wyjątki związane z plikami (FileNotFoundError, PermissionError) - np. próba otwarcia nieistniejącego pliku, brak uprawnień do odczytu/zapisu pliku itp.
    3.   Wyjątki związane z innymi błędami wykonania (RuntimeError) - np. próba wykonania niepoprawnej operacji, przekroczenie stosu, itp.
    4.   Wyjątki związane z siecią (ConnectionError) - np. błędy połączenia, przekroczenie czasu oczekiwania itp.
    Istnieją też inne wyjątki, takie jak ZeroDivisionError, IndexError, KeyError, ImportError, AssertionError, oraz wiele innych.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    * Exception: Bazowa klasa dla wszystkich wyjątków.
    * AttributeError: Występuje, gdy atrybut obiektu nie istnieje.
    * IndexError: Występuje, gdy indeks listy lub innej sekwencji jest poza zakresem.
    * KeyError: Występuje, gdy klucz nie istnieje w słowniku.
    * ValueError: Występuje, gdy funkcja otrzymuje argument o niewłaściwej wartości.
    * TypeError: Występuje, gdy operacja lub funkcja jest stosowana do obiektu niewłaściwego typu.
    * NameError: Występuje, gdy zmienna lub nazwa funkcji nie jest zdefiniowana.
    * ZeroDivisionError: Występuje, gdy próbujesz podzielić przez zero.
    * FileNotFoundError: Występuje, gdy próba otwarcia pliku, który nie istnieje, kończy się niepowodzeniem.
    * ImportError: Występuje, gdy moduł nie może zostać zaimportowany.
    * IOError: Występuje, gdy operacja wejścia/wyjścia (np. otwarcie pliku) kończy się niepowodzeniem.
    * RuntimeError: Występuje, gdy błąd nie pasuje do żadnej innej kategorii wyjątków.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Własne wyjątki
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
    class Kwadrat:
     def  __init__(self,x,y):
        self.x=x
        self.y=y
     def pole(self):
       return self.x*self.y       #tu musi być self
    _k1=Kwadrat(2,2)
    print(_k1.pole())
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
    # Tu zgłaszamy własny wyjątek

    class Kwadrat:
     def  __init__(self,x,y):
        self.x=x
        self.y=y
     def pole(self):
       if self.x < 0 or self.y <0:
         raise Exception("Złe wymiary")
       else:
        return self.x*self.y       #tu musi być self
    _k1=Kwadrat(2,2)
    print(_k1.pole())
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
    # No to jescze musimy obsłużyć ten wyjątek

    class Kwadrat:
     def  __init__(self,x,y):
        self.x=x
        self.y=y
     def pole(self):
       if self.x < 0 or self.y <0:
          raise Exception("Złe wymiary")
       else:
        return self.x*self.y       #tu musi być self

    _k1=Kwadrat(2,2)
    try:
     _k=_k1.pole()
    except Exception as e:
      print(e)
    else:
      print(_k)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Bardziej elegancko będzie wyglądać kod w którym mamy własną klasę np. BadDimensionError . Klasa BadDimensionError powinna dziedziczyć po wbudowanej klasie wyjątków ValueError, ponieważ ten wyjątek jest przeznaczony do sygnalizowania błędów związanych z nieprawidłowymi wartościami argumentów.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Analiza**: Implementacja logiki algorytmu z wykorzystaniem standardowej składni i wbudowanych mechanizmów Pythona.
    """)
    return


@app.class_definition
# przykład klasy
class BadDimensionError(ValueError):
    def __init__(self, message):
        super().__init__(message)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A pełny kod będzie wyglądał następująco:
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
    #ValueError
    class BadDimensionError(ValueError):
        def __init__(self, message):
            super().__init__(message)

    class Kwadrat:
     def  __init__(self,x,y):
        self.x=x
        self.y=y
     def pole(self):
       if self.x < 0 or self.y <0:
          raise BadDimensionError("Złe wymiary")
       else:
        return self.x*self.y       #tu musi być self

    _k1=Kwadrat(-2,2)
    try:
     _k=_k1.pole()
    except Exception as e:
      print(e.args)
    else:
      print(_k)
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
    # kilka wyjątków
    try:
        _x = int("abc")  # Spowoduje ValueError
        #y=1/0
    except ValueError:
        print("Błąd: Nie można przekonwertować na liczbę.")
    except ZeroDivisionError:
        print("Błąd: Dzielenie przez zero.")
    except FileNotFoundError:
        print("Błąd: Plik nie istnieje.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Obiekt wyjątku zawiera wiele informacji, które mogą pomóc w diagnozowaniu i rozwiązywaniu problemu, w tym:

    typ wyjątku (BadDimensionError)
    pełną ścieżkę do modułu i pliku, w którym został zgłoszony wyjątek
    numer linii, w której został zgłoszony wyjątek
    stos wywołań, czyli kolejność wywołania funkcji prowadząca do miejsca zgłoszenia wyjątku
    Można wykorzystać te informacje do znalezienia źródła problemu i naprawienia go. Na przykład, patrząc na numer linii, można znaleźć miejsce w kodzie, gdzie wystąpił problem. Patrząc na stos wywołań, można znaleźć, która funkcja lub metoda była odpowiedzialna za wystąpienie wyjątku.

    Aby wyświetlić więcej informacji o obiekcie wyjątku, można użyć funkcji traceback.print_exception() z modułu traceback. Ta funkcja wyświetla szczegółowe informacje o wyjątku, w tym stos wywołań, na standardowym strumieniu błędów.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Zadanie:

    # Zbudować klasę Auto, wczytać dane: marka, rokp, cena, przebieg, typ (jedna linia, metoda input), zrobić obsługę wyjatków: rokp, cena, przebieg [liczby], marka, typ [dane z listy].
    """)
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
    class Auto:
        _DOZWOLONE_MARKI = ["Toyota", "BMW", "Audi", "Ford"]
        _DOZWOLONE_TYPY = ["sedan", "suv", "hatchback", "kombi"]

        def __init__(self, marka, _rokp, _cena, _przebieg, typ):
            self.marka = marka
            self._rokp = _rokp
            self._cena = _cena
            self._przebieg = _przebieg
            self.typ = typ

        def __str__(self):
            return f"{self.marka}, rok: {self._rokp}, _cena: {self._cena}, _przebieg: {self._przebieg}, typ: {self.typ}"


    while True:
        try:
            _dane = input("Podaj: marka rok _cena _przebieg typ: ").split()

            if len(_dane) != 5:
                raise ValueError("Musisz podać dokładnie 5 wartości")

            marka, _rokp, _cena, _przebieg, typ = _dane

            # konwersja liczb
            _rokp = int(_rokp)
            _cena = float(_cena)
            _przebieg = int(_przebieg)

            # walidacja marki
            if marka not in Auto._DOZWOLONE_MARKI:
                raise ValueError(f"Nieznana marka! Dozwolone: {Auto._DOZWOLONE_MARKI}")

            # walidacja typu
            if typ not in Auto._DOZWOLONE_TYPY:
                raise ValueError(f"Nieznany typ! Dozwolone: {Auto._DOZWOLONE_TYPY}")

            _auto = Auto(marka, _rokp, _cena, _przebieg, typ)
            print("Dodano _auto:")
            print(_auto)
            break

        except ValueError as e:
            print("Błąd:", e)
        except Exception:
            print("Nieprawidłowe _dane wejściowe!")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Zbować listę samochodów, posortować listę według wybranego kryterium np. rokp, cena, typ
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
    class Auto:
        _DOZWOLONE_MARKI = ["Toyota", "BMW", "Audi", "Ford"]
        _DOZWOLONE_TYPY = ["sedan", "suv", "hatchback", "kombi"]
        _lista_aut = []
        def __init__(self, marka, rokp, cena):
            self.marka = marka
            self.rokp = rokp
            self.cena = cena


        def __str__(self):
            return f"{self.marka}, rok: {self.rokp}, cena: {self.cena}"

    # Tu zaczyna się program
    _lista_aut = [Auto("BMW",2022,12000),Auto("Ford",2010,10000),Auto("Audi",1990,8000)]
    _lista_aut.sort(key=lambda x: x.cena)

    #_lista_aut.sort(key=lambda x: [-ord(c) for c in x.marka])
    for auto in _lista_aut:
        print(auto)
    return


if __name__ == "__main__":
    app.run()
