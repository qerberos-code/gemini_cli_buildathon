# Gemini CLI Authentication Guide

This guide covers both **API Key** and **OAuth** authentication methods for the Gemini CLI.

## 🔐 Two Authentication Methods

### Method 1: API Key Authentication
- **Best for**: Scripts, automation, CI/CD
- **Setup**: Get API key from Google AI Studio
- **Usage**: Set `GEMINI_API_KEY` environment variable

### Method 2: OAuth Authentication (Recommended)
- **Best for**: Individual developers, interactive use
- **Setup**: Sign in with Google account
- **Benefits**: No API key management, better quotas

## 🚀 OAuth Authentication (Recommended)

### Benefits of OAuth
- 🎁 **Free tier**: 60 requests/min and 1,000 requests/day
- 🚀 **Gemini 2.5 Pro** with 1M token context window
- 🔐 **No API key management** - just sign in with Google account
- 🔄 **Automatic updates** to latest models
- 🏢 **Supports paid Code Assist Licenses** from organizations

### Quick OAuth Setup
```bash
# Start Gemini CLI and choose OAuth
npx https://github.com/google-gemini/gemini-cli

# Follow the browser authentication flow when prompted
# This will open your browser for Google sign-in
```

### For Paid Code Assist Licenses
```bash
# Set your Google Cloud Project
export GOOGLE_CLOUD_PROJECT="YOUR_PROJECT_NAME"

# Then start CLI
npx https://github.com/google-gemini/gemini-cli
```

## 🔑 API Key Authentication

### Get API Key
```bash
# Visit: https://makersuite.google.com/app/apikey
# Sign in and create a new API key
```

### Configure Environment
```bash
# Set API key
export GEMINI_API_KEY="your_actual_api_key_here"

# Or use .env file (our project setup)
echo "GEMINI_API_KEY=your_actual_api_key_here" > .env
```

## 🧪 Verification Commands

### Test OAuth Authentication
```bash
# Test OAuth (will open browser for authentication)
python verify_oauth.py

# Or test directly
npx https://github.com/google-gemini/gemini-cli -p "Hello from OAuth!"
```

### Test API Key Authentication
```bash
# Test API key
python verify_both_clis.py

# Or test directly
export GEMINI_API_KEY="your_key"
npx https://github.com/google-gemini/gemini-cli -p "Hello from API key!"
```

### Test Both Methods
```bash
# Comprehensive test
python verify_both_clis.py  # Tests API key
python verify_oauth.py      # Tests OAuth
```

## 📋 Usage Examples

### Interactive Mode (OAuth Recommended)
```bash
# Start interactive CLI with OAuth
npx https://github.com/google-gemini/gemini-cli

# This will:
# 1. Open browser for Google authentication
# 2. Start interactive chat session
# 3. No API key needed
```

### Non-Interactive Mode
```bash
# With OAuth (after initial authentication)
npx https://github.com/google-gemini/gemini-cli -p "Your prompt here"

# With API key
export GEMINI_API_KEY="your_key"
npx https://github.com/google-gemini/gemini-cli -p "Your prompt here"
```

### File Processing
```bash
# Process files with OAuth
npx https://github.com/google-gemini/gemini-cli -p "Summarize this file" < input.txt

# Include multiple files
npx https://github.com/google-gemini/gemini-cli -p "Analyze these files" @file1.txt @file2.txt
```

## 🔧 Troubleshooting

### OAuth Issues
1. **Browser doesn't open**
   ```bash
   # Check if browser is available
   which open  # macOS
   which xdg-open  # Linux
   ```

2. **Authentication fails**
   ```bash
   # Clear any cached credentials
   rm -rf ~/.config/gemini-cli
   # Try again
   npx https://github.com/google-gemini/gemini-cli
   ```

3. **Timeout during authentication**
   ```bash
   # Increase timeout or try again
   timeout 120 npx https://github.com/google-gemini/gemini-cli -p "test"
   ```

### API Key Issues
1. **Invalid API key**
   ```bash
   # Check your key
   echo $GEMINI_API_KEY
   # Verify at: https://makersuite.google.com/app/apikey
   ```

2. **Quota exceeded**
   ```bash
   # Check usage at: https://makersuite.google.com/app/apikey
   # Consider switching to OAuth for better quotas
   ```

## 🎯 Buildathon Recommendations

### For Demo Recording
- **Use OAuth**: Better quotas, no API key management
- **Interactive mode**: More engaging for judges
- **File processing**: Show real-time analysis

### For Development
- **Use API key**: Better for scripts and automation
- **Our Python SDK**: For structured output and file processing
- **Official CLI**: For interactive exploration

## 📊 Quota Comparison

| Method | Free Tier | Paid Tier |
|--------|-----------|-----------|
| **OAuth** | 60 req/min, 1,000 req/day | Based on Code Assist License |
| **API Key** | 15 req/min, 1,500 req/day | Based on billing |

## 🚀 Quick Start Commands

### OAuth (Recommended)
```bash
# 1. Start CLI with OAuth
npx https://github.com/google-gemini/gemini-cli

# 2. Complete browser authentication
# 3. Start chatting!

# For our project demo
python app.py demo  # Uses Python SDK with API key
```

### API Key
```bash
# 1. Get API key from: https://makersuite.google.com/app/apikey
# 2. Set environment variable
export GEMINI_API_KEY="your_key"

# 3. Test
python verify_both_clis.py
```

## 📚 Resources

- **OAuth Setup**: https://github.com/google-gemini/gemini-cli
- **API Key**: https://makersuite.google.com/app/apikey
- **Our Project**: https://github.com/qerberos-code/gemini_cli_buildathon
- **Documentation**: https://ai.google.dev/gemini-api/docs

---

**Ready to authenticate?** Choose OAuth for the best experience! 🎉
