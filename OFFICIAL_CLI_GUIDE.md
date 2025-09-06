# Official Gemini CLI Guide

This guide covers both the **Python SDK** and the **Official Gemini CLI** tool for the buildathon.

## 🛠️ Two CLI Approaches

### 1. Python SDK (google-generativeai)
- **What**: Python library for Gemini API
- **Use case**: Building applications, scripts, demos
- **Installation**: `pip install google-generativeai`

### 2. Official Gemini CLI (npx)
- **What**: Official command-line tool from Google
- **Use case**: Interactive CLI, quick testing, command-line usage
- **Installation**: `npx https://github.com/google-gemini/gemini-cli`

## 🚀 Quick Start

### Get Your API Key
```bash
# Visit: https://makersuite.google.com/app/apikey
# Sign in and create a new API key
```

### Configure Environment
```bash
# Edit .env file
nano .env

# Set your API key:
GEMINI_API_KEY=your_actual_api_key_here
```

## 🧪 Verification Commands

### Test Both CLIs
```bash
# Comprehensive test of both approaches
python verify_both_clis.py
```

### Test Python SDK Only
```bash
# Test Python SDK
python verify_cli.py
```

### Test Official CLI Only
```bash
# Test official CLI (requires API key in environment)
export GEMINI_API_KEY=your_actual_api_key_here
npx https://github.com/google-gemini/gemini-cli -p "Say 'Hello from Gemini CLI!'"
```

## 📋 Official CLI Usage Examples

### Basic Usage
```bash
# Interactive mode
npx https://github.com/google-gemini/gemini-cli

# Non-interactive mode
npx https://github.com/google-gemini/gemini-cli -p "Your prompt here"

# With specific model
npx https://github.com/google-gemini/gemini-cli -m gemini-1.5-flash -p "Your prompt"
```

### File Processing
```bash
# Process a file
npx https://github.com/google-gemini/gemini-cli -p "Summarize this file" < input.txt

# Include files in context
npx https://github.com/google-gemini/gemini-cli -p "Analyze these files" @file1.txt @file2.txt
```

### Advanced Options
```bash
# Debug mode
npx https://github.com/google-gemini/gemini-cli --debug -p "Your prompt"

# List extensions
npx https://github.com/google-gemini/gemini-cli --list-extensions

# Use specific extensions
npx https://github.com/google-gemini/gemini-cli -e file,web -p "Your prompt"
```

## 🔧 Environment Setup

### For Official CLI
```bash
# Set API key as environment variable
export GEMINI_API_KEY=your_actual_api_key_here

# Or use .env file (our project setup)
source .env  # Loads GEMINI_API_KEY
```

### For Python SDK
```bash
# Our project automatically loads from .env
# Or set directly:
export GEMINI_API_KEY=your_actual_api_key_here
python -c "import os; print(os.getenv('GEMINI_API_KEY'))"
```

## 📊 Expected Outputs

### Successful Python SDK Test
```
🤖 Gemini CLI Verification
==============================
✅ API key configured (ends with: ...abcd)
✅ Gemini library imported successfully
✅ Model instance created
🔄 Testing model with simple prompt...
✅ Model response received!
📝 Response: Python SDK works!

🎉 SUCCESS: Gemini CLI is working correctly!
```

### Successful Official CLI Test
```
🛠️  Testing Official Gemini CLI
----------------------------------------
🔄 Running: npx https://github.com/google-gemini/gemini-cli
✅ Official Gemini CLI working correctly
📝 Response: Official CLI works!
```

## 🎯 Buildathon Integration

### Our Project Uses Python SDK
- **Main demo**: `python app.py demo`
- **File processing**: Local File Wrangler pattern
- **Structured output**: JSON summaries
- **Reproducible**: Deterministic inputs

### Official CLI for Quick Testing
- **Verification**: Test API connectivity
- **Interactive exploration**: Try different prompts
- **File analysis**: Quick document processing

## 🔍 Troubleshooting

### Common Issues

1. **API Key Not Valid**
   ```bash
   # Check your key
   echo $GEMINI_API_KEY
   
   # Verify in .env file
   cat .env
   ```

2. **CLI Not Found**
   ```bash
   # Install Node.js if needed
   node --version
   npm --version
   
   # Test npx
   npx --version
   ```

3. **Timeout Issues**
   ```bash
   # Check internet connection
   ping google.com
   
   # Try with debug mode
   npx https://github.com/google-gemini/gemini-cli --debug -p "test"
   ```

## 📚 Resources

- **Official CLI Repo**: https://github.com/google-gemini/gemini-cli
- **Python SDK Docs**: https://ai.google.dev/gemini-api/docs/python-sdk
- **API Key**: https://makersuite.google.com/app/apikey
- **Our Project**: https://github.com/qerberos-code/gemini_cli_buildathon

## 🚀 Ready to Proceed?

Once both CLIs are verified:

1. **Run main demo**: `python app.py demo`
2. **Record demo**: Follow `demo/RECORDING_INSTRUCTIONS.md`
3. **Submit**: Share your GitHub repository

---

**Both CLIs working?** You're ready for the buildathon! 🎉
