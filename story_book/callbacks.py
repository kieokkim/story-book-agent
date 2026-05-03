from google.adk.agents.callback_context import CallbackContext
from google.adk.models.llm_request import LlmRequest
from google.adk.models.llm_response import LlmResponse
from typing import Optional

def before_agent_callback(callback_context: CallbackContext) -> None:
    agent_name = callback_context.agent_name

    messages = {
        "StoryWriterAgent": "📝 스토리 작성 중...",
        "IllustratorAgent_Page1": "🎨 이미지 1/5 생성 중...",
        "IllustratorAgent_Page2": "🎨 이미지 2/5 생성 중...",
        "IllustratorAgent_Page3": "🎨 이미지 3/5 생성 중...",
        "IllustratorAgent_Page4": "🎨 이미지 4/5 생성 중...",
        "IllustratorAgent_Page5": "🎨 이미지 5/5 생성 중...",
    }

    if agent_name in messages:
        print(messages[agent_name])
        callback_context.state[f"status_{agent_name}"] = messages[agent_name]

def after_agent_callback(callback_context: CallbackContext) -> None:
    agent_name = callback_context.agent_name
    
    messages = {
        "StoryWriterAgent": "✅ 스토리 작성 완료!",
        "IllustratorAgent_Page1": "✅ 이미지 1/5 완료!",
        "IllustratorAgent_Page2": "✅ 이미지 2/5 완료!",
        "IllustratorAgent_Page3": "✅ 이미지 3/5 완료!",
        "IllustratorAgent_Page4": "✅ 이미지 4/5 완료!",
        "IllustratorAgent_Page5": "✅ 이미지 5/5 완료!",
    }
    
    if agent_name in messages:
        print(messages[agent_name])