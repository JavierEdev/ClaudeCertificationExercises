# GOOGLE — Claude en Vertex AI

Los 14 notebooks usan `AnthropicVertex` y la API Messages de Claude en Google Cloud. Se organizan por los mismos temas que CLAUDE y BEDROCK:

| Subcarpeta | Notebooks | Contenido |
| --- | --- | --- |
| `PromptEngBuildingWithApi` | 2 | Evaluación de prompts y reportes JSON/HTML |
| `PromptEvalsBuildingWithApi` | 1 | Generación de un dataset de evaluación |
| `ToolsBuildingWithApi` | 7 | Etapas de herramientas, datos estructurados, editor y búsqueda web |
| `FeatsOfClaude` | 4 | Thinking, citas de PDF, imágenes y caché |

`CLIProject` contiene el cliente de terminal con MCP adaptado para Vertex. `Resources` conserva los ZIP originales y el PDF duplicado recibido.

## Configuración

Desde la raíz del repositorio:

```bash
.venv/bin/python -m pip install -r GOOGLE/requirements.txt
cp GOOGLE/.env.example GOOGLE/.env
gcloud auth application-default login
```

Configura `GOOGLE_CLOUD_PROJECT` con tu proyecto real. Necesitas Vertex AI habilitado, acceso al modelo Claude y permisos de inferencia. La autenticación utiliza ADC; en un despliegue puede obtener la identidad del entorno.

El modelo predeterminado es **Claude Sonnet 4.6**, con el identificador `claude-sonnet-4-6` y la región `global`. Está documentado para Google Cloud junto con Messages, thinking, herramientas, citas, caché y búsqueda web. [Configuración y capacidades de Claude en Google Cloud](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai).

Selecciona el kernel `.venv` y ejecuta las celdas en orden. La primera celda carga GOOGLE/.env y ajusta el directorio de trabajo a la subcarpeta del ejercicio. Reinicia el kernel después de cambiar la configuración o el proveedor. `VERTEX_MODEL_ID` y `CLOUD_ML_REGION` permiten seleccionar otro modelo/endpoint compatible.

## Ejercicios actualizados

- Temperatura y prefills se han eliminado. Las respuestas JSON se solicitan mediante instrucciones explícitas.
- Thinking usa `adaptive` y `output_config.effort`.
- Se conservan los bloques completos de las respuestas al continuar las conversaciones. Los ciclos de herramientas tienen un límite de 12 turnos.
- El editor utiliza `text_editor_20250728` y `str_replace_based_edit_tool`. Las rutas se limitan a la subcarpeta del ejercicio y el ejemplo inicial solo lista archivos. [Herramienta de edición](https://platform.claude.com/docs/en/agents-and-tools/tool-use/text-editor-tool).
- El ejercicio de citas envía `earth.pdf` como documento PDF en base64 y habilita citas.
- El ejercicio de visión usa la imagen incluida `FeatsOfClaude/images/prop3.png`; puedes sustituirla con `IMAGE_PATH`.
- El ejercicio de caché realiza dos solicitudes iguales, con caché en el sistema y las herramientas, y muestra sus contadores de uso.

Los archivos `001_tools`, `001_tools_007`, `001_tools_008` y `001_tools_009` son etapas diferentes del tutorial y se conservan por separado. El primero define las herramientas; los siguientes muestran la solicitud y ejecución de herramientas. Los recordatorios se imprimen localmente.

Los dos ejercicios de prompt engineering escriben dataset.json, output.json y output.html en su subcarpeta; una ejecución posterior puede reemplazar esos archivos.

## Proyecto CLI

```bash
.venv/bin/python -m pip install -r GOOGLE/CLIProject/requirements.txt
.venv/bin/python GOOGLE/CLIProject/main.py
```

El CLI utiliza GOOGLE/.env y las mismas credenciales ADC. Su adaptación cambia el cliente de Bedrock del ZIP original por `AsyncAnthropicVertex`, convierte los esquemas MCP al formato nativo de Claude y conserva el ciclo tool_use/tool_result. El servidor MCP de ejemplo mantiene sus documentos en memoria. Consulta [CLIProject](CLIProject/README.md).

Los ZIP se conservan como descargas originales; la versión utilizable está extraída en las subcarpetas correspondientes. El `.env` incluido en el ZIP del CLI no se extrajo: usa la plantilla de GOOGLE.

La validación local comprueba código y flujos sin llamar a Google Cloud. Una ejecución real requiere tu proyecto, credenciales y acceso al modelo.
