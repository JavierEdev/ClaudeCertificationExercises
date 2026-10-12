from typing import Dict
from core.vertex import Vertex
from mcp_client import MCPClient
from core.tools import ToolManager


class Chat:
    def __init__(self, vertex_service: Vertex, clients: dict[str, MCPClient]):
        self.vertex_service: Vertex = vertex_service
        self.clients: dict[str, MCPClient] = clients
        self.messages: list[Dict] = []

    async def _process_query(self, query: str):
        self.vertex_service.add_user_message(self.messages, query)

    async def run(
        self,
        query: str,
    ) -> str:
        final_text_response = ""

        await self._process_query(query)

        for turn in range(12):
            response = await self.vertex_service.chat(
                messages=self.messages,
                tools=await ToolManager.get_all_tools(self.clients),
            )

            self.vertex_service.add_assistant_message(
                self.messages, response["parts"]
            )

            if response["stop_reason"] == "tool_use":
                print(response["text"])
                tool_result_parts = await ToolManager.execute_tool_requests(
                    self.clients, response["parts"]
                )

                self.vertex_service.add_user_message(
                    self.messages, tool_result_parts
                )
            else:
                final_text_response = response["text"]
                break

        else:
            raise RuntimeError("Conversation exceeded 12 tool turns.")

        return final_text_response
