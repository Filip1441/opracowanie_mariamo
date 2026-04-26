@echo off
setlocal enabledelayedexpansion

echo [1/3] Checking Python...
set "PY_CMD="
py -3.12 -c "pass" > nul 2>&1 && set "PY_CMD=py -3.12"
if defined PY_CMD goto FOUND
py -3.11 -c "pass" > nul 2>&1 && set "PY_CMD=py -3.11"
if defined PY_CMD goto FOUND
py -3.10 -c "pass" > nul 2>&1 && set "PY_CMD=py -3.10"
if defined PY_CMD goto FOUND
if exist "%LOCALAPPDATA%\Programs\Python\Python312\python.exe" (
    set "PY_CMD=\"%LOCALAPPDATA%\Programs\Python\Python312\python.exe\""
    goto FOUND
)

echo [2/3] Downloading/Installing Python (if needed)...
set "INSTALLER=python_312_installer.exe"
if not defined PY_CMD (
    curl -L -o %INSTALLER% https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe
    start /wait %INSTALLER% /quiet InstallAllUsers=0 PrependPath=1 Include_test=0 Include_doc=0
    del %INSTALLER%
    set "PY_CMD=\"%LOCALAPPDATA%\Programs\Python\Python312\python.exe\""
)

:FOUND
echo [3/3] Setting up Environment...
:: Tylko tworzymy venv, jesli nie istnieje. Jesli istnieje, pip go po prostu zaktualizuje.
if not exist .venv (
    %PY_CMD% -m venv .venv
)

.venv\Scripts\python.exe -m pip install marimo pandas numpy matplotlib opencv-python

echo.
echo Done.
pause
