# ClaudeCertificationExercises

Los ejercicios están organizados por proveedor:

| Carpeta | API | Notebooks |
| --- | --- | --- |
| [CLAUDE](CLAUDE/README.md) | API directa de Anthropic | 11 originales, con sus datos y resultados |
| [BEDROCK](BEDROCK/README.md) | Amazon Bedrock, Boto3/Converse | 8 ejercicios organizados y actualizados |
| [GOOGLE](GOOGLE/README.md) | Claude en Vertex AI, AnthropicVertex | 14 ejercicios organizados y actualizados, más CLI/MCP |

Las tres carpetas agrupan los notebooks por tema. Sigue el README del proveedor para configurar su autenticación y sus dependencias.

Para CLAUDE, desde la raíz del repositorio:

```bash
.venv/bin/python -m pip install -r CLAUDE/requirements.txt
```

Configura `ANTHROPIC_API_KEY` en el `.env` de la raíz o en `CLAUDE/.env`, selecciona el kernel `.venv` y ejecuta cada notebook desde la carpeta de su ejercicio.

BEDROCK usa credenciales AWS y su propio BEDROCK/.env. Sus notebooks cargan la configuración y ajustan las rutas en la primera celda.

GOOGLE usa Application Default Credentials y GOOGLE/.env para el proyecto, modelo y región. Sus notebooks también ajustan las rutas en la primera celda.
