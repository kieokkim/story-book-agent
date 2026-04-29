import base64
from openai import OpenAI
from google.genai import types
from google.adk.tools.tool_context import ToolContext

client = OpenAI()


async def generate_images(tool_context:ToolContext):
    story_output = tool_context.state.get("story_writer_output")
    pages = story_output.get("scenes")
    
    existing_artifacts = await tool_context.list_artifacts()

    generated_images = []
    
    for page in pages:
        page_id = page.get("id")
        visual_description = page.get("visual_description")
        filename = f"page_{page_id}_image.jpeg"

        if filename in existing_artifacts:
            generated_images.append(
                {
                    "page_id": page_id,
                    "prompt": visual_description[:100],
                    "filename": filename
                }
            )
            continue
        
        image = client.images.generate(
            model="gpt-image-1",
            prompt=visual_description,
            n=1,
            quality="low",
            moderation="low",
            output_format="jpeg",
            background="opaque",
            size="1024x1024", 
        )

        image_bytes = base64.b64decode(image.data[0].b64_json)

        artifact = types.Part(
            inline_data= types.Blob(
                mime_type="image/jpeg",
                data=image_bytes
            )
        )

        await tool_context.save_artifact(filename=filename, artifact=artifact)

        generated_images.append(
            {
                "page_id": page_id,
                "prompt": visual_description[:100],
                "filename": filename
            }
        )

    return {
        "total_images": len(generated_images),
        "status":"complete",
    }
