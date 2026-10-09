# AI-Powered Math Tutor Agent

An interactive AI-powered math tutor built using Google's Agent Development Kit (ADK) and Gemini. The agent guides students through algebra problems step by step, encouraging them to understand the solution rather than simply providing the final answer.

## Features

- **Step-by-Step Guidance:** Breaks algebra problems into manageable steps.
- **Interactive Learning:** Asks questions to help students discover solutions.
- **Conversational AI:** Uses Gemini to generate helpful, context-aware responses.
- **Session Management:** Supports user sessions and conversational interactions.
- **Multiple Interfaces:** Supports testing through the ADK Web UI and command-line interface.

## Tech Stack

- Python
- Google Agent Development Kit (ADK)
- Google Gemini API
- YAML configuration
- Git and GitHub

## Project Structure

```text
adk-workspace/
├── my_first_agent/
│   ├── __init__.py
│   ├── agent.py
│   └── .env
├── my_agent/
│   ├── root_agent.yaml
│   └── .env
├── .gitignore
└── README.md
```

*Note: The project structure may vary depending on your configuration. Never upload `.env` files or API keys to GitHub.*

## Prerequisites

- Python 3.10 or later, compatible with your installed ADK version
- Google Gemini API key
- Git
- Visual Studio Code (recommended)

## Installation

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd <YOUR_REPOSITORY_FOLDER>
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install Google ADK

```powershell
pip install google-adk
```

### 4. Configure your API key

Create a `.env` file inside the agent directory and add:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

Replace the placeholder with your own API key. Keep this file private and exclude it from Git.

## Run the Agent

From the workspace directory:

```powershell
adk web
```

Open the local URL displayed in the terminal and select `my_first_agent` to interact with the math tutor.

To run the agent in the terminal:

```powershell
adk run my_first_agent
```

## Example Interaction

**User:** How do I solve `2x + 5 = 13`?

**Agent:** Let's solve it step by step. What should we subtract from both sides to isolate the term containing `x`?

**User:** Subtract 5 from both sides.

**Agent:** Correct! This gives `2x = 8`. What should we do next to find `x`?

**User:** Divide both sides by 2.

**Agent:** Exactly! Therefore, `x = 4`.

## Learning Outcomes

- Understanding AI agent development with Google ADK.
- Integrating a Gemini model into an interactive application.
- Configuring agents using Python and YAML.
- Managing user sessions and testing conversational workflows.
- Using Git and GitHub for version control.

## Future Enhancements

- Add support for more mathematical topics.
- Introduce difficulty levels and personalized learning.
- Add progress tracking and practice questions.
- Improve mathematical expression formatting.

## Security

Never commit API keys, credentials, or private environment files to version control.

## Author

**Pradeepa A**

Computer Science and Engineering — AI & Machine Learning
