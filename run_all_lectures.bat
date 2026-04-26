@echo off
setlocal enabledelayedexpansion

if not exist .venv (
    echo [BLAD] Nie znaleziono srodowiska wirtualnego. 
    echo Uruchom najpierw plik setup.bat!
    pause
    exit /b
)

echo ======================================================
echo URUCHAMIANIE BIBLIOTEKI WYKLADOW (WSZYSTKIE PLIKI)
echo ======================================================

:: Pobieranie adresu IP laptopa
set "IP=127.0.0.1"
for /f "tokens=2 delims=:" %%a in ('ipconfig ^| findstr "IPv4"') do (
    set "tempIP=%%a"
    set "IP=!tempIP:~1!"
)

echo.
echo Twoj laptop udostepnia teraz caly folder z wykladami.
echo Aby otworzyc na iPadzie, wpisz w przegladarce:
echo http://!IP!:2718
echo.
echo Po wejsciu zobaczysz liste wszystkich 7 wykladow.
echo ======================================================

.venv\Scripts\python.exe -m marimo edit pliki_py\ --host 0.0.0.0
pause
