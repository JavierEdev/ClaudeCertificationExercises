"""Claude on Vertex AI with ADC and native Messages API content blocks."""
from anthropic import AsyncAnthropicVertex
from mcp.types import Tool, PromptMessage, TextContent


class Vertex:
    def __init__(self, project_id: str, region: str = "global", model_id: str = "claude-sonnet-4-6"):
        if not project_id:
            raise ValueError("Configure GOOGLE_CLOUD_PROJECT in GOOGLE/.env.")
        self.client = AsyncAnthropicVertex(project_id=project_id, region=region)
        self.model_id = model_id

    def add_user_message(self, messages: list, content: str | list):
        if isinstance(content, str) and not content.strip():
            raise ValueError("Message text must not be empty.")
        messages.append({"role": "user", "content": content})

    def add_assistant_message(self, messages: list, content: str | list):
        messages.append({"role": "assistant", "content": content})

    async def chat(self, messages: list, system: str | None = None, tools: list[Tool] | None = None,
                   tool_choice: str = "auto", thinking: bool = False, thinking_effort: str = "medium") -> dict:
        params = {"model": self.model_id, "max_tokens": 4000, "messages": messages}
        if system:
            params["system"] = system
        if tools:
            params["tools"] = to_vertex_tools(tools)
            params["tool_choice"] = {"type": tool_choice} if tool_choice in {"auto", "any"} else {"type": "tool", "name": tool_choice}
        if thinking:
            params["thinking"] = {"type": "adaptive"}
            params["output_config"] = {"effort": thinking_effort}
        message = await self.client.messages.create(**params)
        return {
            "parts": [block.model_dump(exclude_none=True) for block in message.content],
            "stop_reason": message.stop_reason,
            "text": "\n".join(block.text for block in message.content if block.type == "text"),
        }

    async def close(self):
        await self.client.close()


def to_vertex_tools(tools: list[Tool]) -> list[dict]:
    return [{"name": tool.name, "description": tool.description or "", "input_schema": tool.inputSchema} for tool in tools]


def to_vertex_messages(messages: list[PromptMessage]) -> list[dict]:
    return [{"role": message.role, "content": message.content.text} for message in messages if isinstance(message.content, TextContent)]
