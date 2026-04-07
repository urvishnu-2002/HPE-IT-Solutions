try:
    from backend.app import app
    wsgi = app
    print("✅ Successfully imported Flask app")
except ImportError as e:
    print(f"❌ Import error: {e}")
    raise
except Exception as e:
    print(f"❌ Error initializing app: {e}")
    raise