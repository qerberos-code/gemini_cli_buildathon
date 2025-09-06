#!/usr/bin/env python3
"""
Test script to verify Gemini CLI setup and configuration.
Run this before the main demo to ensure everything is working.
"""

import os
import sys
from pathlib import Path

def test_environment():
    """Test environment configuration."""
    print("🔧 Testing environment configuration...")
    
    # Check if .env exists
    if not Path(".env").exists():
        print("❌ .env file not found")
        return False
    
    # Load environment variables
    from dotenv import load_dotenv
    load_dotenv()
    
    # Check API key
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key or api_key == "your_gemini_api_key_here":
        print("❌ GEMINI_API_KEY not properly configured")
        return False
    
    print("✅ Environment configuration OK")
    return True

def test_dependencies():
    """Test required dependencies."""
    print("📚 Testing dependencies...")
    
    required_packages = [
        "google.generativeai",
        "dotenv",
        "rich",
        "pathlib"
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package}")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"❌ Missing packages: {', '.join(missing_packages)}")
        print("Run: pip install -r requirements.txt")
        return False
    
    print("✅ All dependencies available")
    return True

def test_gemini_api():
    """Test Gemini API connection."""
    print("🤖 Testing Gemini API connection...")
    
    try:
        import google.generativeai as genai
        import os
        
        api_key = os.getenv("GEMINI_API_KEY")
        genai.configure(api_key=api_key)
        
        # Test with a simple prompt
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content("Say 'Hello, Gemini!' in exactly those words.")
        
        if "Hello, Gemini!" in response.text:
            print("✅ Gemini API connection successful")
            return True
        else:
            print(f"❌ Unexpected response: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Gemini API test failed: {e}")
        return False

def test_data_files():
    """Test sample data files."""
    print("📁 Testing sample data files...")
    
    data_dir = Path("data")
    if not data_dir.exists():
        print("❌ data directory not found")
        return False
    
    # Check for sample files
    sample_files = ["sample_article.md", "meeting_notes.txt", "project_data.json"]
    missing_files = []
    
    for file_name in sample_files:
        file_path = data_dir / file_name
        if file_path.exists():
            print(f"✅ {file_name}")
        else:
            print(f"❌ {file_name}")
            missing_files.append(file_name)
    
    if missing_files:
        print(f"❌ Missing sample files: {', '.join(missing_files)}")
        return False
    
    print("✅ All sample data files present")
    return True

def main():
    """Run all tests."""
    print("🧪 Gemini CLI Buildathon Setup Test")
    print("=" * 40)
    
    tests = [
        test_environment,
        test_dependencies,
        test_gemini_api,
        test_data_files
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
            print()  # Add spacing
        except Exception as e:
            print(f"❌ Test failed with exception: {e}")
            print()
    
    print("=" * 40)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Ready to run the demo.")
        print("Run: python app.py demo")
        return 0
    else:
        print("❌ Some tests failed. Please fix the issues above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
