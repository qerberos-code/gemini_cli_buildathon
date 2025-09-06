#!/bin/bash

# Gemini CLI Buildathon Demo Runner
# This script sets up and runs the demo

set -e  # Exit on any error

echo "🚀 Gemini CLI Buildathon Demo Setup"
echo "=================================="

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "⚠️  .env file not found. Creating from template..."
    cp .env.example .env
    echo "📝 Please edit .env file with your GEMINI_API_KEY"
    echo "   Get your API key from: https://makersuite.google.com/app/apikey"
    exit 1
fi

# Check if API key is set
if ! grep -q "GEMINI_API_KEY=your_gemini_api_key_here" .env; then
    echo "✅ Environment file configured"
else
    echo "❌ Please set your GEMINI_API_KEY in .env file"
    exit 1
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📚 Installing dependencies..."
pip install -r requirements.txt

# Run the demo
echo "🎬 Running demo..."
python app.py demo

echo "✅ Demo completed! Check the /demo directory for output files."
