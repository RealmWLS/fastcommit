import subprocess
import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_staged_diff():
    try:
        return subprocess.check_output(
            ["git", "diff", "--staged"],
            text=True
        )
    except subprocess.CalledProcessError:
        return ""

def generate_message(diff):
    prompt = f"""
Write a concise git commit message using Conventional Commits.

Rules:
- Format: type(scope): message
- Max 1-2 lines
- Be specific and technical
- No emojis

Diff:
{diff}
"""

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )

    return response.choices[0].message.content.strip()