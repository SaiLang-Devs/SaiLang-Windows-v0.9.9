"""Entry point for SaiLang-IDLE.exe, the editor (opens without a console window)."""
import sys
from sailang.idle import main

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
