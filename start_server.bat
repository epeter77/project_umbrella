@echo off
REM This script automates the startup process for the PROJECT_UMBRELLA Django server on Windows.
REM Place this file in the root directory of your project.

TITLE PROJECT_UMBRELLA Server

echo --- Starting PROJECT_UMBRELLA Django Server ---

REM Navigate to the script's directory to ensure commands are run in the project root
cd /d "%~dp0"

echo Step 1: Activating the Python virtual environment...
call venv\Scripts\activate.bat

echo.
echo Step 2: Installing/updating Python dependencies from requirements.txt...
pip install -r requirements.txt

echo.
echo Step 3: Starting the Django development server...
echo You can view your application at http://127.0.0.1:8000
python manage.py runserver

echo ------------------------------------------
echo The server is running in this window.
echo Press CTRL+C in this window to stop the server.
echo ------------------------------------------

pause

