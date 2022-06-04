import sys

def show_progress(current, total, prefix="", suffix="", length=50, fill="¦"):
    percent = ("{0:.1f}").format(100 * (current / float(total)))
    filled_length = int(length * current // total)
    bar = fill * filled_length + "-" * (length - filled_length)
    sys.stdout.write(f"\r{prefix} |{bar}| {percent}% {suffix}")
    sys.stdout.flush()
    if current == total:
        print()
