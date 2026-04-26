@echo off
if not exist .venv (
    echo [BLAD] Nie znaleziono srodowiska wirtualnego. 
    echo Uruchom najpierw plik setup.bat!
    pause
    exit /b
)
.venv\Scripts\python.exe -m marimo edit pliki_py\W7_Wielowatkowosc_i_Wizja.py
pause
