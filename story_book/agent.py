from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from google.adk.models.lite_llm import LiteLlm

from .prompt import STORY_BOOK_DESCRIPTION, STORY_BOOK_PROMPT
from .sub_agents.agent import asset_generator_agent

MODEL = LiteLlm(model="openai/gpt-4o")

story_book_agent = Agent(
    name="StoryBookAgent",
    model=MODEL,
    description=STORY_BOOK_DESCRIPTION,
    instruction=STORY_BOOK_PROMPT,
    tools=[AgentTool(agent=asset_generator_agent)],
)

root_agent = story_book_agent