#!/bin/bash

# Virtual Environment Activation Script
# This script activates the virtual environment and shows helpful information

echo "🐍 Activating Python Virtual Environment"
echo "========================================"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found. Creating one..."
    python3 -m venv venv
    echo "✅ Virtual environment created"
fi

# Activate the virtual environment
source venv/bin/activate

# Show environment info
echo "✅ Virtual environment activated"
echo "📍 Python path: $(which python)"
echo "📍 Python version: $(python --version)"
echo "📍 Pip version: $(pip --version | cut -d' ' -f2)"

# Check if requirements are installed
if [ -f "requirements.txt" ]; then
    echo ""
    echo "📦 Checking installed packages..."
    pip list | grep -E "(google-generativeai|python-dotenv|rich|pandas)" || echo "⚠️  Some packages may not be installed"
fi

echo ""
echo "🚀 Ready to run the demo!"
echo "   Run: python app.py demo"
echo "   Or: python test_setup.py"
echo ""
echo "💡 To deactivate: deactivate"
