from style_profile import THEME

def format_text(text):
    lines = [l.strip() for l in text.strip().split("\n")]
    return "\n".join(f"[{THEME}] {l}" for l in lines)
