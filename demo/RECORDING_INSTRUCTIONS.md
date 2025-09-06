# Demo Recording Instructions

## Pre-Recording Setup

1. **Environment Setup**
   ```bash
   # Copy environment file
   cp .env.example .env
   
   # Edit .env with your actual API key
   # GEMINI_API_KEY=your_actual_api_key_here
   
   # Install dependencies
   pip install -r requirements.txt
   ```

2. **Verify Setup**
   ```bash
   # Test that Gemini API is working
   python -c "import google.generativeai as genai; import os; genai.configure(api_key=os.getenv('GEMINI_API_KEY')); print('✅ API key configured')"
   ```

## Recording Script

### 1. Introduction (30 seconds)
- "Welcome to the Gemini CLI Buildathon demo"
- "This is a Local File Wrangler that processes documents using Gemini AI"
- "I'll show you how it extracts key facts from various file formats"

### 2. Show Project Structure (30 seconds)
```bash
# Show the clean project structure
ls -la
tree . # if available, or ls -R
```

### 3. Demonstrate the Demo (2-3 minutes)
```bash
# Run the main demo
python app.py demo
```

**Key points to highlight during execution:**
- Files being processed from `/data` directory
- Real-time logging output
- Individual analysis files being created
- Summary report generation
- Beautiful console output with colors

### 4. Show Results (1 minute)
```bash
# Show the generated files
ls -la demo/

# Show a sample analysis
cat demo/sample_article_analysis.json | head -20

# Show the summary report
cat demo/summary_report.json | head -30
```

### 5. Explain Architecture (1 minute)
- "This follows the Local File Wrangler pattern"
- "Chain-of-thought processing with intermediate artifacts"
- "Structured JSON output for reproducibility"
- "Secure credential management with environment variables"

## Recording Tips

- **Keep it under 5 minutes total**
- **Show the terminal output clearly**
- **Explain what's happening as it runs**
- **Highlight the structured output format**
- **Mention the reproducible nature of the demo**

## Expected Output Files

After running the demo, you should see:
- `demo/sample_article_analysis.json` - Analysis of the healthcare article
- `demo/meeting_notes_analysis.json` - Analysis of meeting notes
- `demo/project_data_analysis.json` - Analysis of project data
- `demo/summary_report.json` - Consolidated summary report

## Troubleshooting

If the demo fails:
1. Check that `GEMINI_API_KEY` is set in `.env`
2. Verify internet connection
3. Ensure all dependencies are installed
4. Check that files exist in `/data` directory

## Post-Recording

- Upload the recording to your preferred platform
- Include a brief description mentioning:
  - Gemini CLI integration
  - Local file processing
  - Structured output generation
  - Reproducible demo with deterministic inputs
