#!/usr/bin/env python3
"""
OAuth Authentication Verification Script
Tests the official Gemini CLI with OAuth login (no API key required).
"""

import subprocess
import sys
import os

def test_oauth_cli():
    """Test the official Gemini CLI with OAuth authentication."""
    print("🔐 Testing Official Gemini CLI with OAuth")
    print("-" * 45)
    
    try:
        # Test CLI version first
        print("📋 Checking CLI version...")
        result = subprocess.run(
            ['npx', 'https://github.com/google-gemini/gemini-cli', '--version'],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode == 0:
            version = result.stdout.strip()
            print(f"✅ Gemini CLI version: {version}")
        else:
            print(f"❌ Version check failed: {result.stderr}")
            return False
        
        # Test OAuth authentication with a simple prompt
        print("🔄 Testing OAuth authentication...")
        print("   (This will open a browser for Google authentication)")
        
        # Use a simple prompt that should work with OAuth
        cmd = [
            'npx', 'https://github.com/google-gemini/gemini-cli',
            '-p', 'Say "OAuth authentication works!" in exactly those words.'
        ]
        
        print(f"🛠️  Running: {' '.join(cmd)}")
        
        # Run with timeout to prevent hanging
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=60  # Longer timeout for OAuth flow
        )
        
        if result.returncode == 0:
            print("✅ OAuth authentication successful!")
            print(f"📝 Response: {result.stdout}")
            return True
        else:
            print(f"❌ OAuth authentication failed: {result.stderr}")
            print("💡 Make sure you:")
            print("   1. Have a Google account")
            print("   2. Complete the browser authentication")
            print("   3. Have internet connectivity")
            return False
            
    except subprocess.TimeoutExpired:
        print("⏰ OAuth flow timed out")
        print("💡 This might mean:")
        print("   1. Browser authentication is waiting for user input")
        print("   2. Network connectivity issues")
        print("   3. Authentication process is taking longer than expected")
        return False
    except Exception as e:
        print(f"❌ OAuth test error: {e}")
        return False

def test_google_cloud_project():
    """Test if Google Cloud Project is set (for paid licenses)."""
    print("\n☁️  Testing Google Cloud Project Configuration")
    print("-" * 45)
    
    project = os.getenv('GOOGLE_CLOUD_PROJECT')
    if project:
        print(f"✅ Google Cloud Project set: {project}")
        print("💡 You're using a paid Code Assist License")
        return True
    else:
        print("ℹ️  No Google Cloud Project set")
        print("💡 You're using the free tier (60 requests/min, 1,000 requests/day)")
        print("💡 To use paid license, set: export GOOGLE_CLOUD_PROJECT='YOUR_PROJECT_NAME'")
        return True  # This is not an error, just informational

def show_oauth_benefits():
    """Show the benefits of OAuth authentication."""
    print("\n✨ OAuth Authentication Benefits")
    print("-" * 35)
    print("🎁 Free tier: 60 requests/min and 1,000 requests/day")
    print("🚀 Gemini 2.5 Pro with 1M token context window")
    print("🔐 No API key management - just sign in with Google account")
    print("🔄 Automatic updates to latest models")
    print("🏢 Supports paid Code Assist Licenses from organizations")

def main():
    """Main verification function."""
    print("🚀 Gemini CLI OAuth Verification")
    print("=" * 35)
    
    show_oauth_benefits()
    
    # Test Google Cloud Project configuration
    test_google_cloud_project()
    
    # Test OAuth CLI
    success = test_oauth_cli()
    
    print("\n" + "=" * 35)
    print("📊 OAUTH VERIFICATION SUMMARY")
    print("=" * 35)
    
    if success:
        print("🎉 OAUTH AUTHENTICATION SUCCESSFUL!")
        print("✅ Official Gemini CLI is working with OAuth")
        print("🚀 Ready for the buildathon!")
        print("\n📋 Next steps:")
        print("   1. Run: python app.py demo (main demo)")
        print("   2. Record your demo following demo/RECORDING_INSTRUCTIONS.md")
        print("   3. Use OAuth for interactive CLI: npx https://github.com/google-gemini/gemini-cli")
        return True
    else:
        print("❌ OAuth authentication failed")
        print("🔧 Please try:")
        print("   1. Check internet connectivity")
        print("   2. Complete browser authentication")
        print("   3. Try again: python verify_oauth.py")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
