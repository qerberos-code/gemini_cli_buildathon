# Gemini API curl Guide

This guide shows how to use the Gemini API directly with curl commands.

## 🚀 Quick Start

### 1. Get Your API Key
```bash
# Visit: https://makersuite.google.com/app/apikey
# Sign in and create a new API key
```

### 2. Set Environment Variable
```bash
# Set your API key
export GEMINI_API_KEY="your_actual_api_key_here"

# Or use .env file (our project setup)
echo "GEMINI_API_KEY=your_actual_api_key_here" > .env
```

### 3. Test with curl
```bash
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent" \
  -H 'Content-Type: application/json' \
  -H 'X-goog-api-key: YOUR_ACTUAL_API_KEY' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'
```

## 📋 Available Models

### Gemini 2.0 Flash (Latest)
```bash
# Model: gemini-2.0-flash
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
```

### Gemini 1.5 Pro
```bash
# Model: gemini-1.5-pro
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro:generateContent"
```

### Gemini 1.5 Flash
```bash
# Model: gemini-1.5-flash
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
```

## 🛠️ Advanced Examples

### Multi-turn Conversation
```bash
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent" \
  -H 'Content-Type: application/json' \
  -H 'X-goog-api-key: YOUR_API_KEY' \
  -X POST \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [
          {
            "text": "Hello, how are you?"
          }
        ]
      },
      {
        "role": "model",
        "parts": [
          {
            "text": "Hello! I am doing well, thank you for asking. How can I help you today?"
          }
        ]
      },
      {
        "role": "user",
        "parts": [
          {
            "text": "What is the capital of France?"
          }
        ]
      }
    ]
  }'
```

### With Safety Settings
```bash
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent" \
  -H 'Content-Type: application/json' \
  -H 'X-goog-api-key: YOUR_API_KEY' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Your prompt here"
          }
        ]
      }
    ],
    "safetySettings": [
      {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
      }
    ],
    "generationConfig": {
      "temperature": 0.7,
      "topK": 40,
      "topP": 0.95,
      "maxOutputTokens": 1024
    }
  }'
```

### With System Instructions
```bash
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent" \
  -H 'Content-Type: application/json' \
  -H 'X-goog-api-key: YOUR_API_KEY' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Write a Python function to calculate fibonacci numbers"
          }
        ]
      }
    ],
    "systemInstruction": {
      "parts": [
        {
          "text": "You are a helpful Python programming assistant. Always provide clean, well-documented code with examples."
        }
      ]
    }
  }'
```

## 📊 Response Format

### Successful Response
```json
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "AI works by processing data through algorithms to recognize patterns and make predictions."
          }
        ],
        "role": "model"
      },
      "finishReason": "STOP",
      "index": 0,
      "safetyRatings": [
        {
          "category": "HARM_CATEGORY_HARASSMENT",
          "probability": "NEGLIGIBLE"
        }
      ]
    }
  ],
  "usageMetadata": {
    "promptTokenCount": 12,
    "candidatesTokenCount": 20,
    "totalTokenCount": 32
  }
}
```

### Error Response
```json
{
  "error": {
    "code": 400,
    "message": "API key not valid. Please pass a valid API key.",
    "status": "INVALID_ARGUMENT"
  }
}
```

## 🔧 Testing Scripts

### Our Project Test Script
```bash
# Test the API with our script
python test_api_curl.py

# This will:
# 1. Check API key configuration
# 2. Make the curl request
# 3. Parse and display the response
# 4. Show usage statistics
```

### Manual Testing
```bash
# Test with a simple prompt
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent" \
  -H 'Content-Type: application/json' \
  -H 'X-goog-api-key: YOUR_API_KEY' \
  -X POST \
  -d '{"contents":[{"parts":[{"text":"Hello!"}]}]}'
```

## 🚨 Common Issues

### 1. Invalid API Key
```bash
# Error: API key not valid
# Solution: Check your API key at https://makersuite.google.com/app/apikey
```

### 2. Quota Exceeded
```bash
# Error: Quota exceeded
# Solution: Wait or upgrade your plan
```

### 3. Model Not Found
```bash
# Error: Model not found
# Solution: Use correct model name (gemini-2.0-flash, gemini-1.5-pro, etc.)
```

### 4. Invalid JSON
```bash
# Error: Invalid JSON
# Solution: Validate your JSON payload
```

## 📚 Integration Examples

### With Python
```python
import requests
import os

api_key = os.getenv('GEMINI_API_KEY')
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

headers = {
    'Content-Type': 'application/json',
    'X-goog-api-key': api_key
}

data = {
    "contents": [
        {
            "parts": [
                {
                    "text": "Hello from Python!"
                }
            ]
        }
    ]
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```

### With JavaScript
```javascript
const apiKey = process.env.GEMINI_API_KEY;
const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent';

const response = await fetch(url, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'X-goog-api-key': apiKey
  },
  body: JSON.stringify({
    contents: [
      {
        parts: [
          {
            text: 'Hello from JavaScript!'
          }
        ]
      }
    ]
  })
});

const data = await response.json();
console.log(data);
```

## 🎯 Buildathon Usage

For your buildathon project:

1. **Test API connectivity**: Use our `test_api_curl.py` script
2. **Integrate with Python**: Use the `google-generativeai` library
3. **Direct API calls**: Use curl for testing and debugging
4. **Documentation**: Show judges how you're using the API

## 📖 Resources

- **API Documentation**: https://ai.google.dev/gemini-api/docs
- **API Key**: https://makersuite.google.com/app/apikey
- **Model List**: https://ai.google.dev/gemini-api/docs/models
- **Our Project**: https://github.com/qerberos-code/gemini_cli_buildathon

---

**Ready to test?** Run `python test_api_curl.py` after configuring your API key! 🚀
