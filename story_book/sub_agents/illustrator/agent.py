from google.adk.agents import ParallelAgent
from .page_agents.page1_agent import page1_agent
from .page_agents.page2_agent import page2_agent
from .page_agents.page3_agent import page3_agent
from .page_agents.page4_agent import page4_agent
from .page_agents.page5_agent import page5_agent

illustrator_agent = ParallelAgent(
    name="IllustratorAgent",
    description="Generates all 5 illustrations simultaneously",
    sub_agents=[
        page1_agent,
        page2_agent,
        page3_agent,
        page4_agent,
        page5_agent,
    ]
)