from google.adk.agents import Agent
from google.adk.apps import App

from .guardrails import PiiRedactionPlugin


def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city."""
    return {"status": "success", "city": city, "time": "10:30 AM"}


root_agent = Agent(
    name="simple_agent",
    model="gemini-flash-latest",
    description="Tells the current time in a specified city.",
    instruction=(
        "You are a helpful assistant that tells the current time in a city. "
        "Use the 'get_current_time' tool for this purpose."
    ),
    tools=[get_current_time],
)

app = App(
    name="simple_agent",
    root_agent=root_agent,
    plugins=[PiiRedactionPlugin()],
)
