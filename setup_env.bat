@echo off

:: Check if virtual environment exists, if not, create it
echo Checking if virtual environment exists...
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

:: Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate

:: Install dependencies
echo Installing dependencies from requirements.txt...
pip install --upgrade pip
pip install -r requirements.txt

echo Setup complete. Virtual environment is now activated.
echo Run "venv\Scripts\activate" to manually activate it.
