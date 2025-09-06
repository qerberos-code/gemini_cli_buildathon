#!/usr/bin/env python3
"""
Interactive API Key Setup Script
Prompts user for Gemini API key and configures the .env file automatically.
"""

import os
import sys
from pathlib import Path
from getpass import getpass

def get_api_key_from_user():
    """Prompt user for API key with validation."""
    print("🔑 Gemini API Key Setup")
    print("=" * 25)
    print()
    print("📋 To get your API key:")
    print("   1. Visit: https://makersuite.google.com/app/apikey")
    print("   2. Sign in with your Google account")
    print("   3. Create a new API key")
    print("   4. Copy the key")
    print()
    
    while True:
        # Use getpass to hide the input for security
        api_key = getpass("🔐 Enter your Gemini API key: ").strip()
        
        if not api_key:
            print("❌ API key cannot be empty. Please try again.")
            continue
            
        if len(api_key) < 20:
            print("❌ API key seems too short. Please check and try again.")
            continue
            
        # Confirm the key
        print(f"📝 API key entered (ends with: ...{api_key[-4:]})")
        confirm = input("✅ Is this correct? (y/n): ").strip().lower()
        
        if confirm in ['y', 'yes']:
            return api_key
        else:
            print("🔄 Let's try again...")
            continue

def update_env_file(api_key):
    """Update the .env file with the provided API key."""
    env_file = Path(".env")
    
    if not env_file.exists():
        print("❌ .env file not found. Creating from template...")
        # Copy from .env.example
        example_file = Path(".env.example")
        if example_file.exists():
            env_file.write_text(example_file.read_text())
        else:
            print("❌ .env.example not found either. Cannot proceed.")
            return False
    
    # Read current content
    content = env_file.read_text()
    
    # Replace the placeholder
    old_line = "GEMINI_API_KEY=your_gemini_api_key_here"
    new_line = f"GEMINI_API_KEY={api_key}"
    
    if old_line in content:
        content = content.replace(old_line, new_line)
        env_file.write_text(content)
        print("✅ .env file updated successfully!")
        return True
    else:
        # Check if API key is already set
        if f"GEMINI_API_KEY={api_key}" in content:
            print("✅ API key is already configured!")
            return True
        elif "GEMINI_API_KEY=" in content and "your_gemini_api_key_here" not in content:
            print("⚠️  API key appears to be already set with a different value.")
            overwrite = input("🔄 Overwrite existing API key? (y/n): ").strip().lower()
            if overwrite in ['y', 'yes']:
                # Find and replace any existing API key line
                lines = content.split('\n')
                for i, line in enumerate(lines):
                    if line.startswith('GEMINI_API_KEY='):
                        lines[i] = new_line
                        break
                env_file.write_text('\n'.join(lines))
                print("✅ .env file updated successfully!")
                return True
            else:
                print("❌ Setup cancelled.")
                return False
        else:
            print("❌ Could not find the expected placeholder in .env file.")
            return False

def test_api_key(api_key):
    """Test the API key by making a simple request."""
    print("\n🧪 Testing API key...")
    
    try:
        import requests
        
        url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
        headers = {
            'Content-Type': 'application/json',
            'X-goog-api-key': api_key
        }
        data = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": "Say 'API key test successful!' in exactly those words."
                        }
                    ]
                }
            ]
        }
        
        response = requests.post(url, headers=headers, json=data, timeout=10)
        
        if response.status_code == 200:
            result = response.json()
            if "candidates" in result:
                text = result["candidates"][0]["content"]["parts"][0]["text"]
                if "API key test successful!" in text:
                    print("✅ API key test successful!")
                    print(f"📝 Response: {text}")
                    return True
                else:
                    print(f"⚠️  Unexpected response: {text}")
                    return True  # Still consider it working
            else:
                print(f"❌ Unexpected response format: {result}")
                return False
        else:
            print(f"❌ API test failed: {response.status_code}")
            print(f"Error: {response.text}")
            return False
            
    except ImportError:
        print("⚠️  requests library not available. Skipping API test.")
        print("💡 Install with: pip install requests")
        return True
    except Exception as e:
        print(f"❌ API test error: {e}")
        return False

def show_next_steps():
    """Show what to do next after successful setup."""
    print("\n🚀 Setup Complete! Next Steps:")
    print("=" * 35)
    print()
    print("🧪 Test your setup:")
    print("   python test_api_curl.py")
    print("   python verify_both_clis.py")
    print("   python verify_cli.py")
    print()
    print("🎬 Run the main demo:")
    print("   python app.py demo")
    print()
    print("🛠️  Use the Gemini CLI:")
    print("   npx https://github.com/google-gemini/gemini-cli")
    print()
    print("📚 Read the documentation:")
    print("   - AUTHENTICATION_GUIDE.md")
    print("   - API_CURL_GUIDE.md")
    print("   - CLI_VERIFICATION_GUIDE.md")

def main():
    """Main setup function."""
    print("🚀 Gemini CLI Buildathon - API Key Setup")
    print("=" * 45)
    print()
    
    # Check if .env already has a real API key
    env_file = Path(".env")
    if env_file.exists():
        content = env_file.read_text()
        if "GEMINI_API_KEY=" in content and "your_gemini_api_key_here" not in content:
            print("⚠️  API key appears to be already configured.")
            check = input("🔍 Check current configuration? (y/n): ").strip().lower()
            if check in ['y', 'yes']:
                # Extract current API key
                for line in content.split('\n'):
                    if line.startswith('GEMINI_API_KEY='):
                        current_key = line.split('=', 1)[1]
                        if current_key:
                            print(f"📝 Current API key ends with: ...{current_key[-4:]}")
                            test_api_key(current_key)
                        break
            return True
    
    try:
        # Get API key from user
        api_key = get_api_key_from_user()
        
        # Update .env file
        if update_env_file(api_key):
            # Test the API key
            if test_api_key(api_key):
                show_next_steps()
                return True
            else:
                print("\n❌ API key test failed.")
                print("🔧 Please check your API key and try again.")
                return False
        else:
            print("\n❌ Failed to update .env file.")
            return False
            
    except KeyboardInterrupt:
        print("\n\n❌ Setup cancelled by user.")
        return False
    except Exception as e:
        print(f"\n❌ Setup failed: {e}")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
