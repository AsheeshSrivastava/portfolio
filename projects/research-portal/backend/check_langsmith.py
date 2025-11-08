"""Check LangSmith configuration."""

import os
from app.core.config import get_settings

settings = get_settings()

print("\n" + "="*80)
print("LANGSMITH CONFIGURATION CHECK")
print("="*80)

print("\nEnvironment Variables:")
print(f"  LANGCHAIN_TRACING_V2: {os.getenv('LANGCHAIN_TRACING_V2', 'NOT SET')}")
print(f"  LANGCHAIN_API_KEY: {'SET' if os.getenv('LANGCHAIN_API_KEY') else 'NOT SET'}")
print(f"  LANGCHAIN_PROJECT: {os.getenv('LANGCHAIN_PROJECT', 'NOT SET')}")

print("\nSettings Object:")
print(f"  langsmith_api_key: {'SET' if settings.langsmith_api_key else 'NOT SET'}")
print(f"  langsmith_project: {settings.langsmith_project or 'NOT SET'}")
print(f"  enable_tracing: {settings.enable_tracing}")

print("\nLangSmith Integration:")
if settings.langsmith_api_key and os.getenv('LANGCHAIN_TRACING_V2') == 'true':
    print("  ✓ LangSmith is ENABLED")
    print(f"  ✓ Project: {os.getenv('LANGCHAIN_PROJECT', 'default')}")
    print("  ✓ All LangChain/LangGraph calls will be traced")
elif settings.langsmith_api_key:
    print("  ⚠ LangSmith API key present but LANGCHAIN_TRACING_V2 not set to 'true'")
    print("  → Tracing may not be active")
else:
    print("  ✗ LangSmith is DISABLED (no API key)")

print("\n" + "="*80 + "\n")



