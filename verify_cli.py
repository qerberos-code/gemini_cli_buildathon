#!/usr/bin/env python3
"""
Quick CLI Verification Script
Based on the official Gemini docs quickstart example.
This script verifies that the Gemini API is working correctly.
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def verify_gemini_cli():
    """Verify Gemini CLI/API is working with a simple test."""
    print("🤖 Gemini CLI Verification")
    print("=" * 30)
    
    # Check if API key is set
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key or api_key == "your_gemini_api_key_here":
        print("❌ GEMINI_API_KEY not configured")
        print("📝 Please:")
        print("   1. Get your API key from: https://makersuite.google.com/app/apikey")
        print("   2. Edit .env file and replace 'your_gemini_api_key_here' with your actual key")
        print("   3. Run this script again")
        return False
    
    print(f"✅ API key configured (ends with: ...{api_key[-4:]})")
    
    try:
        # Import and configure Gemini
        import google.generativeai as genai
        genai.configure(api_key=api_key)
        
        print("✅ Gemini library imported successfully")
        
        # Create model instance
        model = genai.GenerativeModel('gemini-1.5-flash')
        print("✅ Model instance created")
        
        # Test with a simple prompt (following official docs pattern)
        print("🔄 Testing model with simple prompt...")
        response = model.generate_content("Say 'Hello from Gemini!' in exactly those words.")
        
        print("✅ Model response received!")
        print(f"📝 Response: {response.text}")
        
        # Verify the response
        if "Hello from Gemini!" in response.text:
            print("🎉 SUCCESS: Gemini CLI is working correctly!")
            print("✅ You can now run the full demo: python app.py demo")
            return True
        else:
            print(f"⚠️  Unexpected response: {response.text}")
            print("✅ Model is responding, but with unexpected content")
            return True
            
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("📦 Run: pip install google-generativeai")
        return False
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("🔧 Check your API key and internet connection")
        return False

def main():
    """Main verification function."""
    success = verify_gemini_cli()
    
    if success:
        print("\n🚀 Ready to proceed with the buildathon!")
        print("📋 Next steps:")
        print("   1. Run: python test_setup.py (full setup test)")
        print("   2. Run: python app.py demo (main demo)")
        sys.exit(0)
    else:
        print("\n❌ Setup incomplete. Please fix the issues above.")
        sys.exit(1)

if __name__ == "__main__":
    main()
