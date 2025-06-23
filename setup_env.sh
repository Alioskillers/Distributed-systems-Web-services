#!/bin/bash

# Check if venv directory exists, if not, create it
echo "Checking if virtual environment exists..."
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Detect OS and activate virtual environment accordingly
OS="$(uname -s)"

if [[ "$OS" == "Linux" || "$OS" == "Darwin" ]]; then
    echo "Detected macOS/Linux. Activating virtual environment..."
    source venv/bin/activate
elif [[ "$OS" == "CYGWIN" || "$OS" == "MINGW" || "$OS" == "MSYS" ]]; then
    echo "Detected Windows. Please run install_requirements.bat instead."
else
    echo "Unknown OS. Please activate the virtual environment manually."
fi

echo "Installing dependencies from requirements.txt..."

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

echo "Setup complete. Virtual environment is now activated."
echo "Run 'source venv/bin/activate' (Linux/macOS) or 'venv\\Scripts\\activate' (Windows) to activate manually."
