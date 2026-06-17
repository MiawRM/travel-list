#!/usr/bin/env python3
"""Apply save-button fix: copies index.patched.html -> index.html when unlocked."""
import shutil
from pathlib import Path

root = Path(__file__).resolve().parent
src = root / "index.patched.html"
dst = root / "index.html"

if not src.is_file():
    raise SystemExit("index.patched.html not found")

shutil.copy2(src, dst)
print("Applied:", dst)
