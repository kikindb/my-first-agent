# My First Agent

A lightweight Gradio-powered AI agent built with `smolagents` and a local model served through LM Studio. The app demonstrates how to build a coding agent with tools for web search, webpage browsing, timezone lookups, and a custom tool scaffold.

## What this project does

This project creates an agent that can:

- Answer questions using a local LLM backend
- Search the web for information
- Visit and summarize web pages
- Check the current time in a given timezone
- Use a small custom tool pattern for extending agent capabilities

It is designed as a simple starter project for learning how agent tools and a chat UI fit together.

## Tech stack

- Python
- `smolagents`
- Gradio
- LM Studio local OpenAI-compatible endpoint
- `duckduckgo-search` via the project tool integrations

## Project structure

- `app.py` — creates the agent and launches the Gradio interface
- `Gradio_UI.py` — chat UI and streaming logic for the agent
- `tools/` — agent tool implementations
- `prompts.yaml` — prompt templates used by the agent workflow
- `agent.json` — configuration metadata
- `requirements.txt` — Python dependencies

## Quick start

1. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

   On Windows PowerShell:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Start LM Studio and run a local model endpoint.

   This project is configured to call:

   ```text
   http://127.0.0.1:1234/v1
   ```

   with the model ID:

   ```text
   openai/qwen3-8b
   ```

4. Launch the app:

   ```bash
   python app.py
   ```

5. Open the local Gradio URL shown in the terminal and start chatting with the agent.

## Customization ideas

You can extend the agent by:

- adding new typed tools in `app.py`
- improving the system prompt in `prompts.yaml`
- swapping the model for another local or remote endpoint
- adding a more advanced UI or analytics layer

## Example tools included

- `my_custom_tool` — placeholder tool to demonstrate the basic tool pattern
- `get_current_time_in_timezone` — returns the current time in a requested timezone
- `visit_webpage` — fetches content from a web page
- `web_search` — searches the web for relevant results
- `final_answer` — standard final response wrapper for the agent

## Notes

This is a beginner-friendly example project intended to help you understand how to wire together:

- an LLM model,
- tool-enabled agent behavior,
- and a simple user interface.

It is a solid base for experimenting with more capable custom agents.

## License

This project is intended for learning and experimentation. Check the repository and package licenses for any dependencies you use in your own environment.
