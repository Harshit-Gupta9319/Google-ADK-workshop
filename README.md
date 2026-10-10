# Google ADK Workshop

A hands-on project exploring AI agent development using Google's Agent Development Kit (ADK) and Python.

## About the Project

This repository contains my practice work from the Google ADK Workshop, including AI agent implementations and an agent with tools.

## Technologies Used

- Python
- Google Agent Development Kit (ADK)
- Google AI Studio API
- Git and GitHub

## Project Structure

```text
Google-ADK-Workshop/
├── agent_with_tool/
│   ├── __init__.py
│   └── agent.py
├── myAgent/
│   ├── __init__.py
│   └── agent.py
├── main.py
├── .gitignore
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Harshit-Gupta9319/Google-ADK-workshop.git
cd Google-ADK-workshop
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Google ADK

```bash
pip install google-adk
```

### 4. Configure your API key

Create a `.env` file in the appropriate agent directory and add your Google AI Studio API key:

```text
GOOGLE_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your own key. Never commit `.env` or expose your API key publicly.

### 5. Run the project

Follow the execution instructions for the specific agent you want to run. The entry point and command may differ between the agents in this repository.

## Learning Goals

- Understand the fundamentals of AI agents.
- Explore tool-assisted agent workflows.
- Practice Python project organization.
- Learn Git and GitHub version control.

## Author

**Harshit Gupta**

- GitHub: [Harshit-Gupta9319](https://github.com/Harshit-Gupta9319)

---

This repository is part of my ongoing learning journey in Python, AI agents, and AI application development.