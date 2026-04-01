@echo off
echo.
echo  Little Sisters of the Poor - Mombasa  ^|  Quick Start (Windows)
echo.

python --version >nul 2>&1 || (echo Python not found. Please install Python 3.10+. && exit /b 1)

if not exist venv (
  echo Creating virtual environment...
  python -m venv venv
)

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing dependencies...
pip install -q -r requirements.txt

if not exist .env (
  copy .env.example .env
)

if not exist logs mkdir logs

echo Running migrations...
python manage.py migrate

echo Loading sample data...
python load_sample_data.py

echo Collecting static files...
python manage.py collectstatic --noinput

echo.
echo  Setup complete!
echo.
echo  Start server:  python manage.py runserver
echo  Admin:         http://localhost:8000/admin/
echo  Website:       http://localhost:8000/
echo  Login:         admin / Admin@1234!
echo.
