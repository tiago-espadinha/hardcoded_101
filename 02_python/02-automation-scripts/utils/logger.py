import sys

# ANSI Escape Sequences
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

def info(msg):
    print(f"{GREEN}[INFO]{RESET} {msg}")

def warn(msg):
    print(f"{YELLOW}[WARN]{RESET} {msg}")

def error(msg):
    print(f"{RED}[ERROR]{RESET} {msg}", file=sys.stderr)
