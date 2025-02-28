from datetime import datetime
from pathlib import Path
import os

root = Path(__file__).parent

html_folders = root / "sofifa-html"

if not html_folders.exists():
    os.mkdir(html_folders)

def save_html(content : str):
    now = datetime.now().strftime("%Y-%m-%dT%H_%M_%SZ") 
    filename = "SOFIFA" + now + ".html"
    full_name = html_folders / filename
    with open(full_name, "w", encoding="utf-8") as f:
        f.write(content)
