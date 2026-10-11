# BEDROCK — Claude con Amazon Bedrock

Los 8 notebooks usan Boto3 y la API nativa `Converse`, con la misma organización por temas que CLAUDE.

| Subcarpeta | Notebooks | Tema |
| --- | --- | --- |
| `PromptEvalsBuildingWithApi` | `001_Prompt_Evals_complete.ipynb` | Dataset, evaluación y validación de sintaxis |
| `ToolsBuildingWithApi` | `002_tools_complete.ipynb` | Fechas y recordatorios |
| `ToolsBuildingWithApi` | `004_structured_data_complete.ipynb` | Extracción de datos mediante herramientas |
| `ToolsBuildingWithApi` | `005_text_editor_tool.ipynb` | Editor de texto |
| `FeatsOfClaude` | `001_thinking_completed.ipynb` | Razonamiento adaptativo |
| `FeatsOfClaude` | `002_images_completed.ipynb` | Visión |
| `FeatsOfClaude` | `003_pdf.ipynb` | Documentos PDF |
| `FeatsOfClaude` | `003_caching_completed.ipynb` | Caché de prompts |

## Configuración

Desde la raíz del repositorio:

```bash
.venv/bin/python -m pip install -r BEDROCK/requirements.txt
cp BEDROCK/.env.example BEDROCK/.env
```

Configura un perfil o una identidad AWS con acceso al modelo y permisos para usar Bedrock. Boto3 obtiene las credenciales de la cadena habitual de AWS; puedes seleccionar un perfil con `AWS_PROFILE`. Si tienes un perfil SSO ya configurado, autentícalo con `aws sso login --profile nombre-del-perfil`.

El modelo predeterminado es **Claude Sonnet 4.6**, con el identificador `us.anthropic.claude-sonnet-4-6` y la región `us-west-2`. AWS lo documenta como activo y compatible con Converse, imágenes, herramientas y caché. Se utiliza su identificador de Bedrock; los identificadores de la API directa de Anthropic tienen otro formato. [Referencia del modelo en AWS](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-anthropic-claude-sonnet-4-6.html).

Puedes ajustar `BEDROCK_MODEL_ID` y `AWS_REGION` en BEDROCK/.env para un modelo y una región compatibles con cada ejercicio. Selecciona el kernel `.venv` y ejecuta las celdas en orden. La primera celda carga BEDROCK/.env y fija el directorio de trabajo en la subcarpeta del ejercicio; datasets y salidas se guardan allí. Reinicia el kernel cuando cambies la configuración o el proveedor.

## Ajustes de los ejercicios

- Las solicitudes omiten temperatura y los helpers usan `maxTokens` y secuencias de parada opcionales.
- La generación y evaluación de JSON usan instrucciones explícitas, sin prefills de mensajes del asistente.
- Thinking usa `adaptive` y `output_config.effort` dentro de `additionalModelRequestFields`, como indica [AWS](https://docs.aws.amazon.com/bedrock/latest/userguide/claude-messages-adaptive-thinking.html).
- El editor es una herramienta Python de cliente con un esquema `toolSpec` para Converse. Conserva view/create/str_replace/insert/undo_edit y limita las rutas a la subcarpeta del ejercicio. El ejemplo inicial solo lista archivos.
- Los ciclos de herramientas conservan todos los bloques de la respuesta y tienen un límite de 12 turnos. Los recordatorios se imprimen localmente.
- El ejercicio de caché realiza dos solicitudes iguales y muestra sus contadores de uso; una lectura de caché depende de que el servicio haya almacenado el prompt y no haya expirado.

`FeatsOfClaude/earth.pdf` es una copia del documento original de CLAUDE. Para el ejercicio de visión, configura `IMAGE_PATH` con una ruta absoluta a una imagen PNG, JPEG, GIF o WebP, o coloca `prop3.png` dentro de `FeatsOfClaude/images/`.

Los notebooks están preparados para servicios reales y requieren credenciales AWS para ejecutar inferencia. La revisión local valida código y solicitudes sin llamar a AWS; no acredita el acceso al modelo en tu cuenta.
