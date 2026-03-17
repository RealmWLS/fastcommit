from setuptools import setup, find_packages

setup(
    name="fastcommit",
    version="0.1.0",
    description="AI-powered git commit message generator using Groq",
    author="RealmWLS",
    packages=find_packages(),
    install_requires=[
        "groq"
    ],
    entry_points={
        "console_scripts": [
            "fastcommit=fastcommit.cli:main"
        ]
    },
    python_requires=">=3.10",
)