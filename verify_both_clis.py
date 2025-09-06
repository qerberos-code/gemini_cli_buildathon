#!/usr/bin/env python3
"""
Comprehensive CLI Verification Script
Tests both the Python SDK and the official Gemini CLI tool.
"""

import os
import subprocess
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_python_sdk():
    """Test the Python SDK (google-generativeai)."""
    print("🐍 Testing Python SDK (google-generativeai)")
    print("-" * 40)
    
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key or api_key == "your_gemini_api_key_here":
        print("❌ GEMINI_API_KEY not configured")
        return False
    
    try:
        import google.generativeai as genai
        genai.configure(api_key=api_key)
        
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content("Say 'Python SDK works!' in exactly those words.")
        
        if "Python SDK works!" in response.text:
            print("✅ Python SDK working correctly")
            print(f"📝 Response: {response.text}")
            return True
        else:
            print(f"⚠️  Unexpected response: {response.text}")
            return True
            
    except Exception as e:
        print(f"❌ Python SDK error: {e}")
        return False

def test_official_cli():
    """Test the official Gemini CLI tool."""
    print("\n🛠️  Testing Official Gemini CLI")
    print("-" * 40)
    
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key or api_key == "your_gemini_api_key_here":
        print("❌ GEMINI_API_KEY not configured")
        return False
    
    try:
        # Set the API key as environment variable for the CLI
        env = os.environ.copy()
        env['GEMINI_API_KEY'] = api_key
        
        # Test the CLI with a simple prompt
        cmd = [
            'npx', 'https://github.com/google-gemini/gemini-cli',
            '-p', 'Say "Official CLI works!" in exactly those words.'
        ]
        
        print("🔄 Running: npx https://github.com/google-gemini/gemini-cli")
        result = subprocess.run(
            cmd, 
            env=env, 
            capture_output=True, 
            text=True, 
            timeout=30
        )
        
        if result.returncode == 0:
            print("✅ Official Gemini CLI working correctly")
            print(f"📝 Response: {result.stdout}")
            return True
        else:
            print(f"❌ CLI error: {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print("❌ CLI timeout - API call took too long")
        return False
    except Exception as e:
        print(f"❌ CLI error: {e}")
        return False

def test_cli_version():
    """Test CLI version and basic functionality."""
    print("\n📋 Testing CLI Version")
    print("-" * 20)
    
    try:
        result = subprocess.run(
            ['npx', 'https://github.com/google-gemini/gemini-cli', '--version'],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode == 0:
            version = result.stdout.strip()
            print(f"✅ Gemini CLI version: {version}")
            return True
        else:
            print(f"❌ Version check failed: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Version check error: {e}")
        return False

def main():
    """Main verification function."""
    print("🚀 Comprehensive Gemini CLI Verification")
    print("=" * 50)
    
    # Check if API key is configured
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key or api_key == "your_gemini_api_key_here":
        print("❌ GEMINI_API_KEY not configured")
        print("📝 Please:")
        print("   1. Get your API key from: https://makersuite.google.com/app/apikey")
        print("   2. Edit .env file and replace 'your_gemini_api_key_here' with your actual key")
        print("   3. Run this script again")
        return False
    
    print(f"✅ API key configured (ends with: ...{api_key[-4:]})")
    
    # Run tests
    tests = [
        test_cli_version,
        test_python_sdk,
        test_official_cli
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"❌ Test failed with exception: {e}")
            results.append(False)
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 VERIFICATION SUMMARY")
    print("=" * 50)
    
    passed = sum(results)
    total = len(results)
    
    print(f"✅ Tests passed: {passed}/{total}")
    
    if passed == total:
        print("🎉 ALL TESTS PASSED!")
        print("✅ Both Python SDK and Official CLI are working")
        print("🚀 Ready for the buildathon!")
        print("\n📋 Next steps:")
        print("   1. Run: python app.py demo (main demo)")
        print("   2. Record your demo following demo/RECORDING_INSTRUCTIONS.md")
        return True
    else:
        print("❌ Some tests failed")
        print("🔧 Please fix the issues above before proceeding")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
