from google.adk.tools.tool_context import ToolContext

def get_story_output(tool_context: ToolContext) -> dict:
    """State에서 story_writer_output을 읽어서 반환"""
    return tool_context.state.get("story_writer_output", {})