import argparse
from fastcommit.core import get_staged_diff, generate_message
from fastcommit.utils import print_header, print_error
import subprocess

def main():
    parser = argparse.ArgumentParser(description="AI git commit tool using Groq")
    parser.add_argument("--no-confirm", action="store_true", help="Skip confirmation")
    args = parser.parse_args()

    print_header()
    diff = get_staged_diff()
    if not diff.strip():
        print_error("No staged changes")
        return

    msg = generate_message(diff)
    print("Suggested commit message:\n")
    print(msg)
    print()

    if not args.no_confirm:
        confirm = input("Use this message? (y/n): ")
        if confirm.lower() != "y":
            print("Aborted")
            return

    subprocess.run(["git", "commit", "-m", msg])
    print("Commit created")