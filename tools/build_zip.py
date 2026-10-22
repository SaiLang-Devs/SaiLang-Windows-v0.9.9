"""Build the SaiLang release ZIP and a SHA-256 checksum file.

Usage (from the project folder):  python tools/build_zip.py [output_folder]
"""

import hashlib
import os
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VERSION = "1.0.0"
SKIP_DIRS = {"__pycache__", ".git", "dist", "build", ".pytest_cache"}
SKIP_SUFFIXES = (".pyc", ".zip", ".sha256")


def project_files():
    for folder, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in files:
            if name.endswith(SKIP_SUFFIXES) or name == "sai_example_notes.txt":
                continue
            full = os.path.join(folder, name)
            yield full, os.path.relpath(full, ROOT)


def main(out_dir):
    os.makedirs(out_dir, exist_ok=True)
    zip_path = os.path.join(out_dir, f"SaiLang-v{VERSION}.zip")
    count = 0
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as archive:
        for full, rel in project_files():
            archive.write(full, os.path.join(f"SaiLang-v{VERSION}", rel))
            count += 1
    digest = hashlib.sha256(open(zip_path, "rb").read()).hexdigest()
    with open(zip_path + ".sha256", "w", encoding="utf-8") as handle:
        handle.write(f"{digest}  SaiLang-v{VERSION}.zip\n")
    print(f"Wrote {zip_path} ({count} files)")
    print(f"SHA-256: {digest}")
    return zip_path


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "dist"))
