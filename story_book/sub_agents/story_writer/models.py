from pydantic import BaseModel, Field
from typing import List


class StoryOutput(BaseModel):

    id: int = Field(description="Story Page Number")
    story_text: str = Field(description="What the text of this story should write")
    visual_description: str = Field(description="Detailed description for image generation")
    embedded_text: str = Field(description="Text overlay for the image")
    embedded_text_location: str = Field(description="Where to position the text on the image (i.e 'top center','bottom left', 'middle right', 'center')")

class StoryPlanOutput(BaseModel):

    topic: str
    scenes: List[StoryOutput]