#!/bin/bash

# This script is for starting the Django server from within the WSL/Linux environment.
# Run this from your Ubuntu terminal.

echo "--- Starting PROJECT_UMBRELLA Django Server (WSL) ---"

# Navigate to the script's directory to ensure commands are run in the project root
cd "$(dirname "$0")"

echo "Step 1: Activating the Python virtual environment..."
# The activation command is different in bash
source venv/bin/activate

echo ""
echo "Step 2: Installing/updating Python dependencies from requirements.txt..."
pip install -r requirements.txt

echo ""
echo "Step 3: Starting the Django development server..."
echo "You can view your application at http://127.0.0.1:8000"
# Run the server. It will keep this terminal window busy.
python manage.py runserver

# This command will run after you stop the server with Ctrl+C
echo "Server stopped. Deactivating virtual environment."
deactivate

