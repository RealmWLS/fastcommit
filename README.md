# fastcommit

fastcommit is a command-line tool that generates git commit messages using AI. It analyzes staged changes and produces concise commit messages following the Conventional Commits standard. The tool is powered by Groq for fast inference.

## Project Description

Writing consistent and meaningful commit messages improves project history and collaboration. fastcommit automates this process by reading your staged git diff and generating structured commit messages.

It integrates into your workflow and helps maintain clean and readable commit logs.

## Installation

Clone the repository and install locally:

```bash
git clone https://github.com/MrRealmWLS/fastcommit.git
cd fastcommit
pip install .
```

Set your Groq API key:

```bash
export GROQ_API_KEY="your_api_key"
```

On Windows:

```bash
set GROQ_API_KEY=your_api_key
```

## Features

* Generate commit messages from staged changes
* Follow Conventional Commits format
* Simple command-line interface
* Fast AI inference using Groq
