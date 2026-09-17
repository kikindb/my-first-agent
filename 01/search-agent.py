from smolagents import CodeAgent, DuckDuckGoSearchTool, LiteLLMModel

# Initialize the search tool
search_tool = DuckDuckGoSearchTool()

# Initialize the model
model = LiteLLMModel(
    model_id='openai/qwen3-8b',
    api_base='http://127.0.0.1:1234/v1',
    api_key='lm-studio',
    custom_role_conversions=None,
    max_tokens=2096,
    temperature=0.5,
)

agent = CodeAgent(
    model=model,
    tools=[search_tool],
)

# Example usage
response = agent.run(
    "Search for luxury superhero-themed party ideas, including decorations, entertainment, and catering."
)
print(response)