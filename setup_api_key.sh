#!/bin/bash

# Interactive API Key Setup Script (Shell version)
# Prompts user for Gemini API key and configures the .env file automatically.

echo "🚀 Gemini CLI Buildathon - API Key Setup"
echo "=========================================="
echo ""

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "📁 Creating .env file from template..."
    if [ -f ".env.example" ]; then
        cp .env.example .env
        echo "✅ .env file created"
    else
        echo "❌ .env.example not found. Cannot proceed."
        exit 1
    fi
fi

# Check if API key is already configured
if grep -q "GEMINI_API_KEY=" .env && ! grep -q "your_gemini_api_key_here" .env; then
    echo "⚠️  API key appears to be already configured."
    echo -n "🔍 Check current configuration? (y/n): "
    read -r check
    if [[ $check =~ ^[Yy]$ ]]; then
        current_key=$(grep "GEMINI_API_KEY=" .env | cut -d'=' -f2)
        if [ -n "$current_key" ]; then
            echo "📝 Current API key ends with: ...${current_key: -4}"
            echo "🧪 Testing API key..."
            # Simple test with curl
            response=$(curl -s "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent" \
                -H 'Content-Type: application/json' \
                -H "X-goog-api-key: $current_key" \
                -X POST \
                -d '{"contents":[{"parts":[{"text":"Say test successful!"}]}]}')
            
            if echo "$response" | grep -q "test successful"; then
                echo "✅ API key is working correctly!"
            else
                echo "❌ API key test failed"
            fi
        fi
    fi
    exit 0
fi

echo "📋 To get your API key:"
echo "   1. Visit: https://makersuite.google.com/app/apikey"
echo "   2. Sign in with your Google account"
echo "   3. Create a new API key"
echo "   4. Copy the key"
echo ""

# Prompt for API key
echo -n "🔐 Enter your Gemini API key: "
read -r api_key

# Validate API key
if [ -z "$api_key" ]; then
    echo "❌ API key cannot be empty."
    exit 1
fi

if [ ${#api_key} -lt 20 ]; then
    echo "❌ API key seems too short. Please check and try again."
    exit 1
fi

# Confirm the key
echo "📝 API key entered (ends with: ...${api_key: -4})"
echo -n "✅ Is this correct? (y/n): "
read -r confirm

if [[ ! $confirm =~ ^[Yy]$ ]]; then
    echo "❌ Setup cancelled."
    exit 1
fi

# Update .env file
echo "🔄 Updating .env file..."
sed -i '' "s/your_gemini_api_key_here/$api_key/g" .env

if [ $? -eq 0 ]; then
    echo "✅ .env file updated successfully!"
else
    echo "❌ Failed to update .env file."
    exit 1
fi

# Test the API key
echo ""
echo "🧪 Testing API key..."
response=$(curl -s "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent" \
    -H 'Content-Type: application/json' \
    -H "X-goog-api-key: $api_key" \
    -X POST \
    -d '{"contents":[{"parts":[{"text":"Say API key test successful!"}]}]}')

if echo "$response" | grep -q "API key test successful"; then
    echo "✅ API key test successful!"
else
    echo "⚠️  API key test had issues, but configuration is complete."
fi

# Show next steps
echo ""
echo "🚀 Setup Complete! Next Steps:"
echo "=============================="
echo ""
echo "🧪 Test your setup:"
echo "   python test_api_curl.py"
echo "   python verify_both_clis.py"
echo "   python verify_cli.py"
echo ""
echo "🎬 Run the main demo:"
echo "   python app.py demo"
echo ""
echo "🛠️  Use the Gemini CLI:"
echo "   npx https://github.com/google-gemini/gemini-cli"
echo ""
echo "📚 Read the documentation:"
echo "   - AUTHENTICATION_GUIDE.md"
echo "   - API_CURL_GUIDE.md"
echo "   - CLI_VERIFICATION_GUIDE.md"
