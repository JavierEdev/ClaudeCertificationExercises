# CLAUDE — API directa de Anthropic

Los 11 notebooks están organizados en cuatro carpetas:

- `PromptEngBuildingWithApi`: prompt engineering y reportes.
- `PromptEvalsBuildingWithApi`: generación de datasets y evaluación.
- `ToolsBuildingWithApi`: herramientas y streaming.
- `FeatsOfClaude`: thinking, documentos, imágenes, caché y archivos.

Desde la raíz del repositorio:

```bash
.venv/bin/python -m pip install -r CLAUDE/requirements.txt
```

Configura `ANTHROPIC_API_KEY` en el `.env` de la raíz o en `CLAUDE/.env`. Selecciona el kernel `.venv` y ejecuta cada notebook desde la carpeta de su ejercicio.

Se conservan los ejercicios, datos y resultados originales. `Feats3` contiene el paso TODO de la imagen y `Feats4` los TODO de caché.
