# Gemini CLI Buildathon Project

A fast, local-first prototype built for the Gemini CLI buildathon.

## Quick Start

### Option 1: Automated Setup (Recommended)
```bash
# Run the automated setup script
./run_demo.sh
```

### Option 2: Manual Setup
1. **Create and activate virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your GEMINI_API_KEY from https://makersuite.google.com/app/apikey
   ```

4. **Test your setup:**
   ```bash
   python test_setup.py
   ```

5. **Run the demo:**
   ```bash
   python app.py demo
   ```

### Option 3: Quick Activation
```bash
# Use the activation script for easy environment management
./activate.sh
```

## Project Structure

- `/src` - Scripts that call Gemini CLI or API
- `/data` - Sample input files and synthetic data
- `/demo` - Recording instructions and example output files
- `app.py` - Main demo script with end-to-end flow
- `test_setup.py` - Setup verification script
- `run_demo.sh` - Automated setup and demo runner
- `requirements.txt` - Python dependencies (flexible versions)
- `requirements-lock.txt` - Exact package versions for reproducibility
- `.env.example` - Environment variables template
- `activate.sh` - Virtual environment activation helper

## Data Flow

This prototype reads from:
- Local files in `/data` directory
- Environment variables for API credentials

This prototype writes to:
- `/demo` directory for output files
- Console logs for real-time feedback

## Gemini Integration

The project demonstrates:
- **Python SDK**: Local file processing with `google-generativeai`
- **Official CLI**: Command-line tool via `npx https://github.com/google-gemini/gemini-cli`
- Structured output generation
- Chain-of-thought processing with intermediate artifacts
- Reproducible demo with deterministic inputs

### CLI Verification

Test both CLI approaches:
```bash
# Test Python SDK and Official CLI
python verify_both_clis.py

# Test Python SDK only
python verify_cli.py

# Test Official CLI only (requires API key)
export GEMINI_API_KEY=your_key
npx https://github.com/google-gemini/gemini-cli -p "Hello from Gemini CLI!"
```

## Architecture Pattern

This project follows the **Local File Wrangler** pattern:
- Parse local files (PDFs/markdown)
- Extract key facts using Gemini
- Produce structured JSON summaries
- Save intermediate and final outputs for debugging
