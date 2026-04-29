from google.adk.agents import SequentialAgent
from .prompt import ASSET_GENERATOR_DESCRIPTION
from .story_writer.agent import story_writer_agent
from .illustrator.agent import illustrator_agent

asset_generator_agent = SequentialAgent(
    name="AssetGeneratorAgent",
    description=ASSET_GENERATOR_DESCRIPTION,
    sub_agents=[
        story_writer_agent,
        illustrator_agent,
    ],
)