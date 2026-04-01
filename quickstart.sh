#!/bin/bash
# ─────────────────────────────────────────────────────────────
#  Little Sisters of the Poor – Mombasa  |  Quick Start (Linux/Mac)
# ─────────────────────────────────────────────────────────────
set -e

echo ""
echo "╔══════════════════════════════════════════════════════╗"
echo "║   Little Sisters of the Poor – Mombasa              ║"
echo "║   Django Web System Quick Start                      ║"
echo "╚══════════════════════════════════════════════════════╝"
echo ""

# Python check
if ! command -v python3 &>/dev/null; then
  echo "❌  Python 3 not found. Please install Python 3.10+."
  exit 1
fi

# Virtual environment
if [ ! -d "venv" ]; then
  echo "→  Creating virtual environment..."
  python3 -m venv venv
fi

echo "→  Activating virtual environment..."
source venv/bin/activate

echo "→  Installing dependencies..."
pip install -q --upgrade pip
pip install -q -r requirements.txt

# .env
if [ ! -f ".env" ]; then
  echo "→  Creating .env from example..."
  cp .env.example .env
fi

# Logs directory
mkdir -p logs

echo "→  Running migrations..."
python manage.py migrate

echo "→  Loading sample data..."
python load_sample_data.py

echo "→  Collecting static files..."
python manage.py collectstatic --noinput --verbosity 0

echo ""
echo "✅  Setup complete!"
echo ""
echo "   Start the server:   python manage.py runserver"
echo "   Admin panel:        http://localhost:8000/admin/"
echo "   Website:            http://localhost:8000/"
echo "   Login:              admin / Admin@1234!"
echo "   API:                http://localhost:8000/api/"
echo ""
