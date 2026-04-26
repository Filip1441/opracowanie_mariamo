import marimo

__generated_with = "0.23.3"
app = marimo.App()


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
    # Wykład 7: Systemy Współbieżne i CV
    """)
    return


@app.cell
def _():
    pass
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Tworzenie Wątków
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Definicja wątku:


    Wątek (ang. thread) – część programu wykonywana współbieżnie w obrębie jednego procesu.

    Różnica między zwykłym procesem a wątkiem polega na współdzieleniu przez wszystkie wątki działające w danym procesie przestrzeni adresowej oraz wszystkich innych struktur systemowych (np. listy otwartych plików, gniazd itp.) – z kolei procesy posiadają niezależne zasoby.

    Ta cecha ma dwie ważne konsekwencje:


    Dzięki współdzieleniu przestrzeni adresowej (pamięci) wątki jednego zadania mogą się między sobą komunikować w bardzo łatwy sposób. Przekazanie dowolnie dużej ilości danych wymaga przesłania jedynie wskaźnika, zaś odczyt (a niekiedy zapis) danych o rozmiarze nie większym od słowa maszynowego nie wymaga synchronizacji (procesor gwarantuje atomowość takiej operacji).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    W Pythonie mamy następujące metody tworzenia wątków:

    * użycie klasy Thread
    * dziedziczenie po Thread
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
    import time
    from threading import Thread

    def druk():
      for i in range (0,5):
        print(i)
    _t1=Thread(target=druk)
    _t2=Thread(target=druk)
    _t1.start()
    _t2.start()

    return Thread, time


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Iteracja**: Zastosowanie pętli `for` do przetwarzania elementów sekwencji.
    """)
    return


@app.cell
def _():
    import time
    from threading import Thread

    def druk():
      for i in range (0,5):
        print(i)
        time.sleep(1)
    _t1=Thread(target=druk)
    _t2=Thread(target=druk)
    _t1.start()
    _t2.start()
    _t1.join()
    _t2.join()
    return Thread, time


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Wątek nadrzędny czeka na zakończenie działania wątków
    """)
    return


@app.cell
def _():
    pass
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Dodanie argumentów
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
    from threading import Thread

    def druk(n):
        for i in range(n):
            print(i)

    _t1 = Thread(target=druk, args=(3,))
    _t2 = Thread(target=druk, args=(5,))

    _t1.start()
    _t2.start()

    _t1.join()
    _t2.join()
    return (Thread,)


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
def _(time):
    import threading

    _saldo = 100

    def wyplata(name):
        global _saldo
        for _ in range(5):
           if _saldo > 0:
            _saldo1 = _saldo-1
           time.sleep(1)
           _saldo = _saldo1
           print(name, _saldo)
    _t1 = threading.Thread(target=wyplata, args=("w1",))
    _t2 = threading.Thread(target=wyplata, args=("w2",))

    _t1.start()
    _t2.start()

    _t1.join()
    _t2.join()

    print("Saldo końcowe:", _saldo)
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
def _(time):
    import threading

    _saldo = 100
    _lock = threading.Lock()
    def wyplata(name):
        global _saldo
        for _ in range(10):
           with _lock:
            if _saldo > 0:
             _saldo1 = _saldo-1
            time.sleep(1)
            _saldo = _saldo1
            print(name, _saldo)
    _t1 = threading.Thread(target=wyplata, args=("w1",))
    _t2 = threading.Thread(target=wyplata, args=("w2",))

    _t1.start()
    _t2.start()

    _t1.join()
    _t2.join()

    print("Saldo końcowe:", _saldo)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Dziedziczenie po klasie Thread
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
def _(Thread, time):
    class MyThread(Thread):
        def __init__(self, num,name):
            super().__init__()
            self._num = num
            self._name = name

        def run(self):
          for i in range(0,self._num):
            print(self._name," ",i)
            time.sleep(1)

    _t1=MyThread(2,"w1")
    _t2=MyThread(3,"w2")
    _t1.start()
    _t2.start()
    _t1.join()
    _t2.join()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Synchronizacja wątków,  zwiększamy wartość wspólnej zmiennej o 1, wynik jest niedeterministyczny
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Nowe zalecenia - określenie typów,  niestety nie mamy kontroli edydtora
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
    def func(x: int) -> int:
        return x + 1
    print(func(2.0))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Oczekiwania od aplikacji przetwarzania obrazów



    1.  Wczytywanie obrazów i filmów
    2.  Pobieranie obrazów z kamery
    3. Zapisywanie obrazów i tworzenie filmów
    4. Poprawa jakości obrazu ´
    5. Wykrywanie cech obrazu
    6. Operacje geometryczne - obrót, przesunięcie
    7. Zmiana przestrzenie barw
    8. Klasyfikacja obiektów widocznych na obrazie
    9. Wykrywanie cech
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Pakiety umożliwiające analizę obrazów



    1. OpenCV
    2. NumPy
    3. SciPy
    4. Pillow
    5. SimplyCV
    6. SimpleITK
    7. pgmagick
    8. scikit-image
    9. ImageAI
    10. Mahotas
    11. OpenAI
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
    #import cv2
    from google.colab import drive
    from google.colab.patches import cv2_imshow
    import os
    # Zamontuj dysk Google Drive
    drive.mount('/content/drive')


    # Ścieżka do pliku na dysku Google Drive
    _katalog = '/content/drive/MyDrive/pliki'



    # Wypisanie zawartości katalogu
    for folder, podfoldery, pliki in os.walk(_katalog):
        for plik in pliki:
            _pelna_sciezka = os.path.join(folder, plik)
            print(_pelna_sciezka)
    #path2 = '/content/drive/MyDrive/l2.png'
    return (cv2_imshow,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Jeśli korzystamy z google collab to musimy zamontować dysk googla, aby mieć dostęp do plików i dodatkowo zaimportować odpowiednie pakiety
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Obraz jako tablica liczb
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
    import cv2
    import numpy as np
    from google.colab.patches import cv2_imshow  #potrzebne w google colab
    # Ścieżka do pliku na dysku Google Drive
    _path = '/content/drive/MyDrive/pliki/l1.png'
    _img=cv2.imread(filename=_path)
    #cv2_imshow(_img)
    print(_img)
    return cv2, cv2_imshow, np


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Analiza**: Implementacja logiki algorytmu z wykorzystaniem standardowej składni i wbudowanych mechanizmów Pythona.
    """)
    return


@app.cell
def _(cv2_imshow, img):
    cv2_imshow(img)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Pakiet numpy

    biblioteka obliczeń numerycznych, ale ponieważ obraz jest tablicą więc w wielu przypadkach może być przydatna
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Przykładowe operacje
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
    _a=np.array([1,2,3])
    print(_a.min(),_a.max())
    print(any(_a==1))
    print(all(_a==1))
    return (np,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## OpenCV

    biblioteka funkcji wykorzystywanych podczas obróbki obrazu, oparta
    na otwartym kodzie. Zaletą jest to ze została zoptymalizowana, tak aby ˙
    obraz przetwarzac w czasie rzeczywistym, jest możliwość
    wykorzystania karty graficznej w procesie przetwarzania.
    Niektóre moduły openCV wymagają dodatkowo instalacji
    opencv-contrib-python

    pip install opencv-contrib-python
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
    # import bibliotek

    import cv2
    import numpy as np
    from google.colab.patches import cv2_imshow  #potrzebne w google colab

    return cv2, cv2_imshow, np


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Analiza**: Implementacja logiki algorytmu z wykorzystaniem standardowej składni i wbudowanych mechanizmów Pythona.
    """)
    return


@app.cell
def _(cv2, cv2_imshow):
    # Ścieżka do pliku na dysku Google Drive
    _path = '/content/drive/MyDrive/pliki/irys.jpg'
    _img=cv2.imread(filename=_path)
    cv2_imshow(_img)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Analiza**: Implementacja logiki algorytmu z wykorzystaniem standardowej składni i wbudowanych mechanizmów Pythona.
    """)
    return


@app.cell
def _(cv2, cv2_imshow):

    # imread nie sygnalizuje braku pliku
    _path = '/content/drive/MyDrive/l3.png'
    _img=cv2.imread(filename=_path)
    cv2_imshow(_img)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Kontrola Przepływu**: Implementacja logiki warunkowej sterującej wykonaniem bloku kodu.
    """)
    return


@app.cell
def _(cv2, cv2_imshow):
    # brak pliku musimy sprawdzić sami
    import os

    _path = '/content/drive/MyDrive/l3.png'
    if os._path.isfile(_path):
     _img=cv2.imread(filename=_path)
     cv2_imshow(_img)
    else:
      print("blad")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Korzystając z OpenCV możemy umieszczać rysunki w nazwanych oknach i przesuwać te okna, ale jest to trudne w środowisku google collab, zostanie pokazane później
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Parametry dodatkowe imread

    * cv2.IMREAD_COLOR = 1
    * cv2.IMREAD_GRAYSCALE =0
    * cv2.IMREAD_UNCHANGED = -1
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Formaty które możemy czytać:

    * Portable Network Graphics – *.png
    * Portable image format – *.pbm, *.pgm, *.ppm *.pxm, *.pnm
    * Windows bitmaps – *.bmp
    * JPEG files – *.jpeg, *.jpg, *.jpe
    * JPEG 2000 files – *.jp2
    * WebP – *.webp
    * PFM files – *.pfm
    * Sun rasters – *.sr, *.ras
    * Image files – *.exr
    * Radiance HDR – *.hdr, *.pic
    * TIFF files – *.tiff, *.tif
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
def _(cv2, cv2_imshow):
    # pliku video
    import time
    _path2 = '/content/drive/MyDrive/pliki/Shrimp.avi'
    _cap = cv2.VideoCapture(_path2)
    _frame_width = int(_cap.get(3))
    _frame_height = int(_cap.get(4))
    for _ in range(3):
       # Capture frame−by−frame
     ret , frame = _cap.read( )
     print(ret)
     _img = cv2.cvtColor(frame, 1)
     cv2_imshow(_img)
     time.sleep(5)
    return (time,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Analiza**: Implementacja logiki algorytmu z wykorzystaniem standardowej składni i wbudowanych mechanizmów Pythona.
    """)
    return


@app.cell
def _(cv2):
    #Odczytywanie dodatkowych parametrów
    _path2 = '/content/drive/MyDrive/pliki/Shrimp.avi'
    _cap = cv2.VideoCapture(_path2)
    _w=_cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    _h=_cap.get (cv2.CAP_PROP_FRAME_HEIGHT)
    _fps=_cap.get (cv2.CAP_PROP_FPS)
    _fc=_cap.get (cv2.CAP_PROP_FRAME_COUNT)
    print('_w=',_w,' _h=',_h, ' _fps=',int(_fps),' _fc=',int(_fc))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Operacje na obrazach
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## zmiana wymiarów
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
def _(cv2_imshow):
    import cv2
    import numpy as np
    import matplotlib.pyplot as plt
    #p1 = '/content/drive/MyDrive/pliki/rys.png'
    _p2 = '/content/drive/MyDrive/pliki/irys.jpg'
    _image = cv2.imread(_p2)
    # Loading the _image
    _half = cv2.resize(_image, (0, 0), fx = 0.5, fy = 0.5)
    cv2_imshow(_image)
    cv2_imshow(_half)
    return cv2, np


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Analiza**: Implementacja logiki algorytmu z wykorzystaniem standardowej składni i wbudowanych mechanizmów Pythona.
    """)
    return


@app.cell
def _(cv2, cv2_imshow, image):
    _img200 = cv2.resize(image, (200, 200))
    cv2_imshow(_img200)
    _img500 = cv2.resize(image, (500, 500),
                  _interpolation = cv2.INTER_NEAREST)
    cv2_imshow(_img500)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Analiza**: Implementacja logiki algorytmu z wykorzystaniem standardowej składni i wbudowanych mechanizmów Pythona.
    """)
    return


@app.cell
def _(cv2, cv2_imshow):
    # zmiana wymiarów bardziej inteligentna, konieczny import imutils

    import imutils
    _p1 = '/content/drive/MyDrive/pliki/irys.jpg'

    #chcemy zmienić jeden wymiar, a pozostałe powinny się dostosować
    _img = cv2.imread(_p1, 1)
    _res=imutils.resize(image=_img, width=100)
    cv2_imshow(_img)
    cv2_imshow(_res)


    return (imutils,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Generowanie losowych obrazów
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
def _(cv2_imshow, np):
    _array=np.random.randint(low=0,high=256,size=(300,300,3))
    cv2_imshow(_array)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Analiza**: Implementacja logiki algorytmu z wykorzystaniem standardowej składni i wbudowanych mechanizmów Pythona.
    """)
    return


@app.cell
def _(cv2, cv2_imshow, np):
    _array=np.full((300,300,3),fill_value=200)
    cv2_imshow(_array)
    _p1 = '/content/drive/MyDrive/pliki/test.jpg'
    cv2.imwrite(_p1, _array)

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Analiza**: Implementacja logiki algorytmu z wykorzystaniem standardowej składni i wbudowanych mechanizmów Pythona.
    """)
    return


@app.cell
def _(cv2):
    _p2='/content/drive/MyDrive/pliki/test.jpg'
    cv2.imread(_p2,-1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Proste operacje rysowania
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
def _(cv2, cv2_imshow):
    _p1 = '/content/drive/MyDrive/pliki/rys2.png'

    _img = cv2.imread(_p1, 1)
    cv2_imshow(_img)
    cv2.line(_img, pt1=(0,0),pt2=(100,100), color=(0,0,255),thickness=3)
    cv2.rectangle(_img, pt1=(100,100),pt2=(200,200), color=(255,0,0),thickness=2)
    cv2_imshow(_img)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Dodawanie i odejmowanie obrazów

    Aby dodać lub odjąć obrazy muszą mieć takie same wymiary
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
def _(cv2_imshow, p1):
    import cv2
    import numpy as np
    _img=cv2.imread(p1,1)
    _p2 = '/content/drive/MyDrive/pliki/irys.jpg'
    _img1=cv2.imread(_p2,1)
    _img = cv2.resize(_img, (200, 200))    # zmiana rozmiaru
    _img1 = cv2.resize(_img1, (200, 200))
    _img3 = cv2.addWeighted(_img, 1.0, _img1, 1.0, 0)  #dodawanie obrazów
    #_img3=cv2.subtract(_img,_img1)
    _combined = cv2.hconcat([_img,_img1,_img3])    #łączenie obrazów
    cv2_imshow(_combined)
    return cv2, np


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Przekształcenia geometryczne
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Obrót
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
def _(cv2, cv2_imshow, p2):
    _img=cv2.imread(p2,1)
    (rows, cols) = _img.shape[:2]  #pobieramy wymiary obrazu
    print(rows,cols)
    #help(cv2.getRotationMatrix2D)
    # tworzymy macierz rotacji, środek obrotu, kąt obrotu, skalowanie
    _M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
    #dokonujemy przekształcenia
    _res = cv2.warpAffine(_img, _M, (cols, rows))
    _combined = cv2.hconcat([_img,_res])
    cv2_imshow(_combined)
    return cols, rows


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Przesunięcie
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
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    """)
    return


@app.cell
def _(cols, cv2, cv2_imshow, img, np, rows):
    _M = np.float32([ [ 0,1,50],[1,0,50]])
    _res = cv2.warpAffine(img, _M, (cols, rows))
    _combined = cv2.hconcat([img,_res])
    cv2_imshow(_combined)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Wycinanie fragmentów obrazu
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
def _(cv2_imshow):
    import cv2
    import numpy as np
    import matplotlib.pyplot as plt
    _p1 = '/content/drive/MyDrive/pliki/irys.jpg'
    _p2 = '/content/drive/MyDrive/rys2.png'
    _image = cv2.imread(_p1, 1)
    _img=_image[100:200,100:200]
    #cv2_imshow(_image)
    cv2_imshow(_img)
    return cv2, np


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    """)
    return


@app.cell
def _(cv2_imshow):
    import cv2
    import numpy as np
    import matplotlib.pyplot as plt
    _p1 = '/content/drive/MyDrive/pliki/irys.jpg'
    _p2 = '/content/drive/MyDrive/rys2.png'
    _image = cv2.imread(_p1, 1)
    _img=_image[-250:,-250:]      #uwaga na położenie :
    #cv2_imshow(_image)
    cv2_imshow(_img)
    return cv2, np


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    """)
    return


@app.cell
def _(cv2_imshow):
    import cv2
    import numpy as np
    import matplotlib.pyplot as plt
    _p1 = '/content/drive/MyDrive/pliki/irys.jpg'
    _p2 = '/content/drive/MyDrive/rys2.png'
    _image = cv2.imread(_p1, 1)
    _img=_image[100:200,100:200]
    #cv2_imshow(_image)
    cv2_imshow(_img)
    return cv2, np


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    """)
    return


@app.cell
def _(cv2_imshow):
    import cv2
    import numpy as np
    import matplotlib.pyplot as plt
    _p1 = '/content/drive/MyDrive/pliki/irys.jpg'
    _p2 = '/content/drive/MyDrive/rys2.png'
    _image = cv2.imread(_p1, 1)
    _img=_image[100:200,100:200]
    #cv2_imshow(_image)
    cv2_imshow(_img)
    return cv2, np


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## jak wyciąć środkowy fragment obrazka?
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
def _(image):
    # musimy znać wymiary
    x,y,_= image.shape
    print(x,y)
    return x, y


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    """)
    return


@app.cell
def _(cv2_imshow, image, x, y):
    # określamy środek
    _xs=x//2   # dzielenie całkowite
    _ys=y//2
    _dl=50  #długość to 100
    # współrzędne prawego górnego i lewego dolengo rogu
    _xp=_xs-_dl
    _yp=_ys-_dl
    _xl=_xs+_dl
    _yl=_ys+_dl
    _img=image[_xp:_xl,_yp:_yl]
    cv2_imshow(_img)

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    """)
    return


@app.cell
def _(cv2_imshow, image, xl, xp, yl, yp):
    ## Zmiana barw wybranego fragmentu

    image[xp:xl,yp:yl]=(0,100,0)
    cv2_imshow(image)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    """)
    return


@app.cell
def _(cv2, cv2_imshow, p1, x, y):
    # określamy środek
    _image = cv2.imread(p1, 1)
    _xs=x//2   # dzielenie całkowite
    _ys=y//2
    _dl=50  #długość to 100
    # współrzędne prawego górnego i lewego dolengo rogu
    _xp=_xs-_dl
    _yp=_ys-_dl
    _oko=_image[_xp:_xs,_yp:_ys]
    cv2_imshow(_oko)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    """)
    return


@app.cell
def _(cv2_imshow, image, oko, xp, xs, yp, ys):
    #A teraz możemy powielić fragment w kilku miejscach
    image[xp-40:xs-40,yp-40:ys-40]=oko
    image[xp+40:xs+40,yp+40:ys+40]=oko
    _p=60
    image[xp+40+_p:xs+40+_p,yp+40+_p:ys+40+_p]=oko
    _p=-160
    image[xp+40+_p:xs+40+_p,yp+40+_p:ys+40+_p]=oko
    cv2_imshow(image)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Analiza**: Implementacja logiki algorytmu z wykorzystaniem standardowej składni i wbudowanych mechanizmów Pythona.
    """)
    return


@app.cell
def _(cv2, cv2_imshow):
    ## Tworzenie ramek na około obrazka
    _p1 = '/content/drive/MyDrive/pliki/irys.jpg'
    _image=cv2.imread(_p1,1)
    _ramka=cv2.copyMakeBorder(_image,20,20,20,20,borderType=cv2.BORDER_REPLICATE)
    cv2_imshow(_image)
    cv2_imshow(_ramka)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Analiza**: Implementacja logiki algorytmu z wykorzystaniem standardowej składni i wbudowanych mechanizmów Pythona.
    """)
    return


@app.cell
def _(cv2, cv2_imshow):
    ## Tworzenie ramek na około obrazka
    _p1 = '/content/drive/MyDrive/pliki/irys.jpg'
    _image=cv2.imread(_p1,1)
    _ramka=cv2.copyMakeBorder(_image,20,20,20,20,borderType=cv2.BORDER_WRAP)
    cv2_imshow(_ramka)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Analiza**: Implementacja logiki algorytmu z wykorzystaniem standardowej składni i wbudowanych mechanizmów Pythona.
    """)
    return


@app.cell
def _(cv2, cv2_imshow):
    ## Tworzenie ramek na około obrazka
    _p1 = '/content/drive/MyDrive/pliki/irys.jpg'
    _image=cv2.imread(_p1,1)
    _ramka=cv2.copyMakeBorder(_image,20,20,20,20,borderType=cv2.BORDER_ISOLATED)
    cv2_imshow(_ramka)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Poprawa jakości

    * filtr mediamowy
    * filtr uśredniający
    * filtr Gaussa
    * wyostrzanie obrazu
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
def _(cv2, cv2_imshow, p1):
    # filtr medianowy
    _img=cv2.imread(p1,1)
    _img1 = cv2.medianBlur(_img,25)
    _combined = cv2.hconcat([_img,_img1])
    cv2_imshow(_combined)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    """)
    return


@app.cell
def _(cv2, cv2_imshow, img, np):
    # filtr uredniający

    _kernel = np.array([[0.1, 0.1, 0.1],
                       [0.1, 0.2, 0.1],
                       [0.1, 0.1, 0.1]])

    #filter the source image
    _img1 = cv2.filter2D(img,-1,_kernel)
    _combined = cv2.hconcat([img,_img1])
    cv2_imshow(_combined)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    """)
    return


@app.cell
def _(cv2_imshow):
    # filtr Gaussa
    import cv2
    import numpy as np
    _path = '/content/drive/MyDrive/pliki/irys.jpg'
    _img=cv2.imread(filename=_path)
    cv2_imshow(_img)
    _img1=cv2.GaussianBlur(_img,[7,7],0.7)
    _edge=cv2.Canny(_img1,100,270)
    cv2_imshow(_edge)
    return cv2, np


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    """)
    return


@app.cell
def _(cv2, cv2_imshow, img, np):
    # wyostrzanie
    _kernel = np.array([[-1, -1, -1],
                       [-1, 9, -1],
                       [-1, -1, -1]])

    #filter the source image
    _img1 = cv2.filter2D(img,-1,_kernel)
    _combined = cv2.hconcat([img,_img1])
    cv2_imshow(_combined)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Operacje progowania

    Progowanie to proces podziału obrazu na obszary o różnych poziomach jasności. Progowanie często jest stosowane w celu poprawy kontrastu obrazu i wyróżnienia cech, takich jak krawędzie.
    W bibliotece OpenCV, funkcja cv2.threshold() służy do progowania obrazu, opcje:

    1. cv2.THRESH_BINARY
    2. cv2.THRESH_BINARY_INV
    3. cv2.THRESH_TRUNC
    4. cv2.THRESH_TOZERO
    5. cv2.THRESH_TOZERO_INV
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
def _(cv2, cv2_imshow, img):
    _, th0 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    #img=cv2.imread(path,0)
    #_, th0 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)  działa tylko dla obrazów w stpniach szarości
    _combined = cv2.hconcat([img,th0])
    cv2_imshow(_combined)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Zmiana barw
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
def _(cv2_imshow):
    import cv2
    import numpy as np
    _path2 = '/content/drive/MyDrive/pliki/blb.png'
    _img = cv2.imread(_path2, 1)
    cv2_imshow(_img)
    # axis=2 - sprawdzane są wszystkie kanały
    _img[np.where((_img == [0,0,0]).all(axis = 2))] = [0,255,0]    #zmieniamy czarny na zielony
    cv2_imshow(_img)
    return cv2, np


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Zmiana przestrzeni barw
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
def _(cv2_imshow):
    import cv2
    import numpy as np
    import matplotlib.pyplot as plt
    _path2 = '/content/drive/MyDrive/pliki/blb.png'
    _img = cv2.imread(_path2, 1)
    cv2_imshow(_img)
    _hsv = cv2.cvtColor(_img, cv2.COLOR_BGR2HSV)
    h,s,v = cv2.split(_hsv)
    _combined = cv2.hconcat([h,s,v])
    cv2_imshow(_combined)

    # odcień - h
    # nasycenie - s
    # jasność - v
    return cv2, np


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    """)
    return


@app.cell
def _(cv2, cv2_imshow, hsv, np):
    _path2 = '/content/drive/MyDrive/pliki/blb.png'
    _img = cv2.imread(_path2, 1)

    _lower_black = np.array([0,0,0])
    _upper_black = np.array([10,10,10])
    _mask0 = cv2.inRange(hsv, _lower_black, _upper_black)

    cv2_imshow(_mask0)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    """)
    return


@app.cell
def _(cv2_imshow):
    import cv2
    import numpy as np
    _path2 = '/content/drive/MyDrive/pliki/testl.png'
    _img = cv2.imread(_path2)
    _gray = cv2.cvtColor(_img,cv2.COLOR_BGR2GRAY)   #zamiana na odcienie szarości
    #Create default Fast Line Detector (FSD)
    _fld = cv2.ximgproc.createFastLineDetector()   #generowanie matody wykrywania linii

    #Detect _lines in the image
    _lines = _fld.detect(_gray)
    print(_lines)
    #Draw detected _lines in the image
    _dlimg = _fld.drawSegments(_gray,_lines)

    _combined = cv2.hconcat([_img,_dlimg])
    cv2_imshow(_combined)

    return cv2, np


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Wykrywanie krawędzi
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
def _(cv2_imshow):
    # Ścieżka do pliku na dysku Google Drive
    import cv2
    import numpy as np
    _path2 = '/content/drive/MyDrive/pliki/blb2.png'
    _img = cv2.imread(_path2, 0)
    cv2_imshow(_img)
    _edge=cv2.Canny(_img,180,270)
    cv2_imshow(_edge)
    return cv2, np


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Określanie krawędzi
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
def _(cv2_imshow, edge, img):
    import cv2

    # Wczytanie obrazu z pliku
    #img = cv2.imread('nazwa_obrazu.jpg')

    # Konwersja obrazu do odcieni szarości
    _gray = img.copy()


    # Znalezienie konturów na obrazie
    contours, hierarchy = cv2.findContours(edge, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Iteracja po wszystkich konturach
    for contour in contours:
        # Obliczenie przybliżonego kształtu konturu
        _approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
     #   cv2.drawContours(img, [_approx], 0, (0, 255, 0), 2)
        # Sprawdzenie, czy kontur ma 4 boki (czyli czy jest kwadratem)
        if len(_approx) == 4:
            # Narysowanie prostokąta wokół konturu
            cv2.drawContours(img, [_approx], 0, (0, 255, 0), 2)
            print("Na obrazie znaleziono prostokąt.")
            cv2_imshow(img)
            break
    else:
        print("Na obrazie nie znaleziono kwadratu.")
    return contours, cv2


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    """)
    return


@app.cell
def _(cv2, edge, imutils):
    # Wyznaczenie konturów
    _contours = cv2.findContours(image=edge.copy(),
                                _mode=cv2.RETR_TREE,
                                _method=cv2.CHAIN_APPROX_SIMPLE)
    _contours = imutils.grab_contours(_contours)

    _contours = sorted(_contours, key=cv2.contourArea, reverse=True)[:10]
    print(_contours)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 💻 ANALIZA TECHNICZNA
    - **Struktury Danych**: Operacje na listach (inicjalizacja, rzutowanie lub list comprehension).
    """)
    return


@app.cell
def _(contours, cv2, cv2_imshow, img):
    #rysujemy kontur
    _cnt1 = cv2.drawContours(image=img.copy(), contours=[contours[0]], contourIdx=0,
                            _color=(0, 255, 0), thickness=3)
    cv2_imshow(_cnt1)
    return


@app.cell
def _():
    pass
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Przepływ optyczny
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
    import cv2
    import numpy as np
    import cv2
    from google.colab import drive
    from google.colab.patches import cv2_imshow
    import os
    import matplotlib.pyplot as plt
    # Zamontuj dysk Google Drive


    # rozpoznanie obiektu
    def identify_shape(image_path):
        try:
            # ładujemy obraz
            _img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            if _img is None:
                return "Error: Could not load _image."

            # usuwamy szum
            _img = cv2.GaussianBlur(_img, (5, 5), 0)
            _, thresh = cv2.threshold(_img, 127, 255, cv2.THRESH_BINARY_INV)


            # Find contours
            contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            if not contours:
              return "No shapes detected."


            for contour in contours:
                # Approximate the contour to a polygon
                _epsilon = 0.04 * cv2.arcLength(contour, True)
                _approx = cv2.approxPolyDP(contour, _epsilon, True)

                # klasysfikacja na podstawie liczby wierzchołków
                _vertices = len(_approx)

                if _vertices == 3:
                    return "Triangle"
                elif _vertices == 4:
                    # Further check for square/rectangle
                    x, y, w, h = cv2.boundingRect(_approx)
                    _aspect_ratio = float(w) / h
                    if 0.95 <= _aspect_ratio <= 1.05:
                        return "Square"
                    else:
                        return "Rectangle"
                elif _vertices == 5:
                    return "Pentagon"
                elif _vertices == 6:
                    return "Hexagon"
                elif _vertices == 8:  # Octagon
                  return "Octagon"
                elif _vertices > 10 :
                    return "Circle"  # Approximate circle
                else:
                    return "Unknown Polygon"
        except Exception as e:
            return f"Error: {e}"


    drive.mount('/content/drive/')

    # Ścieżka do pliku na dysku Google Drive

    _path2 = '/content/drive/MyDrive/sq.jpg'
    _image=cv2.imread(_path2)
    plt.imshow(_image)
    _shape = identify_shape(_path2)
    print(f"The identified _shape is: {_shape}")
    return cv2, cv2_imshow, np


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Przykładowe cmap

    viridis – Domyślna mapa kolorów w Matplotlib, dobrze nadaje się do wizualizacji.

    plasma – Kolorowa skala o cieplejszych barwach, bardziej nasycona.

    inferno – Ciemna skala kolorów z intensywnymi czerwonymi i żółtymi.

    magma – Mapa cieplna o ciemniejszych barwach.

    cividis – Kolorowa mapa dla osób z problemami z widzeniem kolorów.

    Greys – Skala szarości.
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
    import numpy as np
    import matplotlib.pyplot as plt

    # Generowanie przykładowych danych
    _x = np.linspace(0, 1, 300)
    _y = np.linspace(0, 1, 300)
    X, Y = np.meshgrid(_x, _y)
    _heatmap_data = np.sin(10*X) * np.cos(10*Y)  # Przykładowe dane sinusoidalne

    # Tworzenie mapy cieplnej
    plt.imshow(_heatmap_data, cmap='cividis', interpolation='nearest')

    # Dodanie paska kolorów
    plt.colorbar(label='Intensywność')

    # Tytuł i etykiety
    plt.title('Mapa Cieplna z Paskiem Kolorów')
    plt.xlabel('X')
    plt.ylabel('Y')

    # Wyświetlanie obrazu
    plt.show()
    return (np,)


@app.cell
def _():
    pass
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Zaawansowane przetwarzanie obrazów wykorzystując skimage https://scikit-image.org/docs/stable/api/skimage.data.html

    Rejestracja obrazów

    Etapy:

    określenie przesunięcia między obrazami (metodą przepływu optycznego)

    przesunięcie obrazu

    złożenie obrazu
    """)
    return


@app.cell
def _():
    pass
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    https://pillow.readthedocs.io/en/stable/
    """)
    return


if __name__ == "__main__":
    app.run()
