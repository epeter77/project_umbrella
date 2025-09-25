@echo off
TITLE PROJECT_UMBRELLA WSL Launcher

REM This Windows Batch script launches the corresponding .sh script inside WSL.
REM It automatically converts the script's line endings to prevent errors.

echo --- Launching WSL to start the Django Server ---
echo.
echo A new terminal window will open to run the server.
echo You can close that new window to stop the server.
echo.

REM This command chain does three things:
REM 1. cd: Changes to the correct Linux project directory.
REM 2. dos2unix: Converts the shell script from Windows to Unix line endings.
REM 3. bash: Executes the now-corrected script.
wsl.exe bash -c "cd /home/epeter77/PROJECT_UMBRELLA && dos2unix -q ./start_server.sh && bash ./start_server.sh"

echo ---
echo The script has been launched in a new WSL window.
pause

