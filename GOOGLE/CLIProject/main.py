import asyncio
import os
import sys
from contextlib import AsyncExitStack
from pathlib import Path

from dotenv import load_dotenv
from mcp_client import MCPClient
from core.vertex import Vertex
from core.cli_chat import CliChat
from core.cli import CliApp

cli_root = Path(__file__).resolve().parent
load_dotenv(cli_root.parent / ".env", override=False)
load_dotenv(cli_root / ".env", override=False)


async def main():
    project_id = os.getenv("GOOGLE_CLOUD_PROJECT")
    if not project_id:
        raise ValueError("Configura GOOGLE_CLOUD_PROJECT en GOOGLE/.env.")
    service = Vertex(
        project_id=project_id,
        region=os.getenv("CLOUD_ML_REGION", "global"),
        model_id=os.getenv("VERTEX_MODEL_ID", "claude-sonnet-4-6"),
    )
    server_scripts = [str(Path(arg).expanduser().resolve()) for arg in sys.argv[1:]]
    original_dir = Path.cwd()
    os.chdir(cli_root)
    try:
        async with AsyncExitStack() as stack:
            doc_client = await stack.enter_async_context(MCPClient(command=sys.executable, args=[str(cli_root / "mcp_server.py")]))
            clients = {"doc_client": doc_client}
            for i, script in enumerate(server_scripts):
                clients[f"client_{i}"] = await stack.enter_async_context(MCPClient(command=sys.executable, args=[script]))
            chat = CliChat(doc_client=doc_client, clients=clients, vertex_service=service)
            cli = CliApp(chat)
            await cli.initialize()
            await cli.run()
    finally:
        await service.close()
        os.chdir(original_dir)


if __name__ == "__main__":
    asyncio.run(main())
