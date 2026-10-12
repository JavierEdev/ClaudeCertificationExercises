import json
from mcp.types import Tool, TextContent
from mcp_client import MCPClient


class ToolManager:
    @classmethod
    async def get_all_tools(cls, clients: dict[str, MCPClient]) -> list[Tool]:
        tools = []
        for client in clients.values():
            tools.extend(await client.list_tools())
        return tools

    @classmethod
    async def execute_tool_requests(cls, clients: dict[str, MCPClient], parts: list[dict]) -> list[dict]:
        results = []
        for block in parts:
            if block.get("type") != "tool_use":
                continue
            result = {"type": "tool_result", "tool_use_id": block["id"]}
            try:
                selected = None
                for client in clients.values():
                    if any(tool.name == block["name"] for tool in await client.list_tools()):
                        selected = client
                        break
                if selected is None:
                    raise ValueError(f"Unknown tool: {block['name']}")
                output = await selected.call_tool(block["name"], block.get("input", {}))
                result["content"] = json.dumps([item.text for item in output.content if isinstance(item, TextContent)]) if output else "[]"
                result["is_error"] = bool(output and output.isError)
            except Exception as error:
                result.update(content=str(error), is_error=True)
            results.append(result)
        return results
