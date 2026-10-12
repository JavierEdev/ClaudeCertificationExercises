# MCP Chat — Claude en Vertex AI

Cliente de terminal con Claude en Google Cloud y herramientas MCP (Model Context Protocol). Esta versión usa `AsyncAnthropicVertex` y credenciales ADC. El ZIP original se conserva en `../Resources/cli_project_complete.zip`.

Desde la raíz del repositorio:

```bash
.venv/bin/python -m pip install -r GOOGLE/CLIProject/requirements.txt
cp GOOGLE/.env.example GOOGLE/.env
gcloud auth application-default login
.venv/bin/python GOOGLE/CLIProject/main.py
```

Configura `GOOGLE_CLOUD_PROJECT` en GOOGLE/.env. El modelo predeterminado es `claude-sonnet-4-6`, con `CLOUD_ML_REGION=global`. El CLI utiliza la configuración común de GOOGLE y puede cargar variables adicionales desde su propio .env.

El servidor MCP local ofrece documentos de ejemplo, herramientas de lectura/edición y el prompt `/format document_id`. Puedes mencionar un documento con `@plan.md` o pedir su contenido. Los documentos se mantienen en memoria mientras el servidor está activo. Las respuestas del modelo utilizan Vertex real.

Puedes añadir servidores Python MCP pasando sus rutas después de main.py. El CLI ejecuta los servidores con el mismo Python del entorno y conserva la conversación con bloques nativos tool_use/tool_result. Hay un máximo de 12 turnos de herramientas por consulta.

Se requiere Python 3.10 o superior. El proyecto conserva la API de MCP v1 (`mcp>=1.12,<2`) para las interfaces originales del tutorial.
