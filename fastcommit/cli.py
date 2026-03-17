from fastcommit.core import get_staged_diff, generate_message

def main():
    diff = get_staged_diff()
    if not diff.strip():
        print("No staged changes")
        return

    msg = generate_message(diff)
    print("Suggested commit message:\n")
    print(msg)
    confirm = input("Use this message? (y/n): ")
    if confirm.lower() == "y":
        import subprocess
        subprocess.run(["git", "commit", "-m", msg])
        print("Commit created")
    else:
        print("Aborted")