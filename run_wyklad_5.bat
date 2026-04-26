@echo off
if not exist .venv (
    echo [BLAD] Nie znaleziono srodowiska wirtualnego. 
    echo Uruchom najpierw plik setup.bat!
    pause
    exit /b
)
.venv\Scripts\python.exe -m marimo edit pliki_py\W5_Obiektowosc_OOP.py
pause
