@echo off
REM Run this on Windows, inside the project folder (where build.spec is).

where py >nul 2>nul
if errorlevel 1 (
    echo Python not found. Install it from python.org and check "Add to PATH".
    pause
    exit /b 1
)

if not exist venv (
    py -m venv venv
)

call venv\Scripts\activate.bat
pip install --upgrade pip
pip install -r requirements.txt
pip install pyinstaller

pyinstaller build.spec

echo.
echo Done. The exe is at dist\ShamsiCalWidget.exe
pause
