import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from format_kit.formatter import format_text

def test_format():
    assert format_text("  hello  \n  world  ") == "hello\nworld"
