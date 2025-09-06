# Gemini CLI Verification Guide

This guide helps you verify that the Gemini CLI is working correctly before starting the buildathon.

## 🚀 Quick Verification Steps

### 1. Get Your API Key
```bash
# Visit: https://makersuite.google.com/app/apikey
# Sign in with your Google account
# Create a new API key
# Copy the key
```

### 2. Configure Environment
```bash
# Edit .env file
nano .env  # or use your preferred editor

# Replace this line:
GEMINI_API_KEY=your_gemini_api_key_here

# With your actual key:
GEMINI_API_KEY=your_actual_api_key_here
```

### 3. Run Verification
```bash
# Activate virtual environment
source venv/bin/activate

# Run quick verification
python verify_cli.py

# Or run full setup test
python test_setup.py
```

## ✅ Expected Success Output

When everything is working, you should see:

```
🤖 Gemini CLI Verification
==============================
✅ API key configured (ends with: ...abcd)
✅ Gemini library imported successfully
✅ Model instance created
🔄 Testing model with simple prompt...
✅ Model response received!
📝 Response: Hello from Gemini!

🎉 SUCCESS: Gemini CLI is working correctly!
✅ You can now run the full demo: python app.py demo
```

## 🔧 Troubleshooting

### API Key Issues
- **Error**: "API key not valid"
  - **Solution**: Double-check your API key in .env file
  - **Verify**: No extra spaces or quotes around the key

### Import Issues
- **Error**: "No module named 'google.generativeai'"
  - **Solution**: `pip install google-generativeai`

### Network Issues
- **Error**: Connection timeout
  - **Solution**: Check internet connection
  - **Verify**: No firewall blocking the request

## 📋 Verification Checklist

- [ ] API key obtained from Google AI Studio
- [ ] .env file configured with real API key
- [ ] Virtual environment activated
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Verification script runs successfully
- [ ] Model responds with expected output
- [ ] Ready to run full demo

## 🎯 Next Steps After Verification

Once verification passes:

1. **Run full setup test**: `python test_setup.py`
2. **Run main demo**: `python app.py demo`
3. **Record your demo**: Follow instructions in `demo/RECORDING_INSTRUCTIONS.md`

## 🚨 Security Reminders

- ✅ Never commit your .env file to git
- ✅ Use placeholder values in .env.example
- ✅ Keep your API key secure
- ✅ Don't share your API key publicly

---

**Ready to verify?** Run `python verify_cli.py` after configuring your API key!
