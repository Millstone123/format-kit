import style_profile

def format_text(text):
    lines = [l.strip() for l in text.strip().split("\n")]
    return "\n".join(lines)
