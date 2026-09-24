from format_kit.formatter import format_text

def test_format():
    assert "hello" in format_text("  hello  ")
