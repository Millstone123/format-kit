from style_profile import THEME

def format_text(text, theme=None):
    lines = [l.strip() for l in text.strip().split("\n")]
    prefix = f"[{theme or THEME}] "
    return "\n".join(prefix + l for l in lines)
