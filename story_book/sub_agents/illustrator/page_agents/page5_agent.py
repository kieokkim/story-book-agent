from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from ..prompt import ILLUSTRATOR_DESCRIPTION, get_page_illustrator_prompt
from ..tools import generate_page_image
from story_book.callbacks import before_agent_callback, after_agent_callback

MODEL = LiteLlm(model="openai/gpt-4o")

page5_agent=Agent(
    name="IllustratorAgent_Page5",
    description=ILLUSTRATOR_DESCRIPTION,
    instruction=get_page_illustrator_prompt(5),
    model=MODEL,
    tools=[generate_page_image],
    before_agent_callback=before_agent_callback,
    after_agent_callback=after_agent_callback,
)