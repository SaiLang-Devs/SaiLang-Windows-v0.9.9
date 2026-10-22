"""SaiLang IDLE launcher.

Double-click this file (or right-click a .sai file > Open with > Python) to open
the editor. Python's default install associates .pyw files with Python, so no
extra setup is needed. Nothing here is a .bat or .exe file.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "src"))

from sailang.idle import main  # noqa: E402

sys.exit(main(sys.argv[1:]))
