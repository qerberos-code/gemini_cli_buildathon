#!/usr/bin/env python3
"""
Test Gemini API using curl command
This script demonstrates how to call the Gemini API directly via REST API
"""

import os
import subprocess
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_api_with_curl():
    """Test the Gemini API using curl command."""
    print("🧪 Testing Gemini API with curl")
    print("=" * 35)
    
    # Get API key from environment
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key or api_key == "your_gemini_api_key_here":
        print("❌ GEMINI_API_KEY not configured")
        print("📝 Please:")
        print("   1. Get your API key from: https://makersuite.google.com/app/apikey")
        print("   2. Edit .env file and replace 'your_gemini_api_key_here' with your actual key")
        print("   3. Run this script again")
        return False
    
    print(f"✅ API key configured (ends with: ...{api_key[-4:]})")
    
    # Prepare the curl command
    curl_command = [
        "curl",
        "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent",
        "-H", "Content-Type: application/json",
        "-H", f"X-goog-api-key: {api_key}",
        "-X", "POST",
        "-d", json.dumps({
            "contents": [
                {
                    "parts": [
                        {
                            "text": "Explain how AI works in a few words"
                        }
                    ]
                }
            ]
        })
    ]
    
    print("🔄 Making API call...")
    print(f"📡 URL: https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent")
    print(f"📝 Prompt: Explain how AI works in a few words")
    
    try:
        # Execute the curl command
        result = subprocess.run(
            curl_command,
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode == 0:
            print("✅ API call successful!")
            
            # Parse the response
            try:
                response_data = json.loads(result.stdout)
                
                if "candidates" in response_data:
                    # Extract the generated text
                    candidate = response_data["candidates"][0]
                    if "content" in candidate and "parts" in candidate["content"]:
                        generated_text = candidate["content"]["parts"][0]["text"]
                        print(f"📝 Response: {generated_text}")
                        
                        # Show usage info if available
                        if "usageMetadata" in response_data:
                            usage = response_data["usageMetadata"]
                            print(f"📊 Usage: {usage.get('promptTokenCount', 'N/A')} prompt tokens, {usage.get('candidatesTokenCount', 'N/A')} response tokens")
                        
                        return True
                    else:
                        print(f"⚠️  Unexpected response structure: {response_data}")
                        return False
                else:
                    print(f"❌ No candidates in response: {response_data}")
                    return False
                    
            except json.JSONDecodeError as e:
                print(f"❌ Failed to parse JSON response: {e}")
                print(f"Raw response: {result.stdout}")
                return False
                
        else:
            print(f"❌ API call failed: {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print("⏰ API call timed out")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def show_curl_example():
    """Show the exact curl command to run."""
    print("\n📋 Manual curl command:")
    print("=" * 25)
    
    api_key = os.getenv("GEMINI_API_KEY")
    if api_key and api_key != "your_gemini_api_key_here":
        print(f'curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent" \\')
        print(f"  -H 'Content-Type: application/json' \\")
        print(f"  -H 'X-goog-api-key: {api_key}' \\")
        print(f"  -X POST \\")
        print(f"  -d '{{")
        print(f'    "contents": [')
        print(f'      {{')
        print(f'        "parts": [')
        print(f'          {{')
        print(f'            "text": "Explain how AI works in a few words"')
        print(f'          }}')
        print(f'        ]')
        print(f'      }}')
        print(f'    ]')
        print(f"  }}'")
    else:
        print("❌ API key not configured")
        print("💡 Set GEMINI_API_KEY in .env file first")

def main():
    """Main function."""
    print("🚀 Gemini API curl Test")
    print("=" * 25)
    
    # Test the API
    success = test_api_with_curl()
    
    # Show manual command
    show_curl_example()
    
    print("\n" + "=" * 25)
    if success:
        print("🎉 API test successful!")
        print("✅ Gemini API is working correctly")
        print("🚀 Ready to use the API in your applications")
    else:
        print("❌ API test failed")
        print("🔧 Please check your API key configuration")
    
    return success

if __name__ == "__main__":
    import sys
    success = main()
    sys.exit(0 if success else 1)
