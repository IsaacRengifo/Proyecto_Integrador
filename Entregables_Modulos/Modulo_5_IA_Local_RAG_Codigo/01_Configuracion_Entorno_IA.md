# Módulo 5 — Configuración del entorno local de IA

**Evidencia:** Asistente local RAG funcional, repositorio de código, conjunto de pruebas,
ficha técnica y reporte de consumo de recursos.

## 1. Arquitectura del entorno (local first)

```
  ┌──────────────────────────────────────────────────────────┐
  │                  EQUIPO LOCAL (6 GB RAM, sin GPU)        │
  │                                                          │
  │  Documentos (.md/.csv/.pdf)                              │
  │        │  chunking + embeddings                          │
  │        ▼                                                 │
  │  multilingual-e5-small  ──►  LanceDB (índice vectorial)   │
  │        │                                                 │
  │        ▼  recuperación (topN=2, umbral 0.45)              │
  │  AnythingLLM (workspace Monitoreo_Energia_Tumaco)         │
  │        │  contexto + pregunta                            │
  │        ▼                                                 │
  │  Ollama API local (127.0.0.1:11434)                       │
  │        │                                                 │
  │        ▼                                                 │
  │  gemma3:1b (Q4, ~0,75 GB) ──► respuesta con citas         │
  └──────────────────────────────────────────────────────────┘
```

> Todo funciona **sin internet y sin nube**: los documentos del proyecto no salen del equipo.
> La descarga inicial de modelos se hizo en una ventana controlada de conectividad.

## 2. Componentes instalados

| Componente | Versión / modelo | Rol | Ubicación |
|---|---|---|---|
| Ollama | Servicio local en `127.0.0.1:11434` | Ejecución del LLM | `C:\Users\USUARIO\.ollama\models\` |
| Modelo LLM | `gemma3:1b` (cuantizado Q4, ~0,75 GB) | Generación de respuestas | Vía Ollama |
| AnythingLLM Desktop | versión de escritorio | Interfaz RAG y gestión de workspaces | `C:\Users\USUARIO\AppData\Roaming\anythingllm-desktop\storage\` |
| Modelo de embeddings | `multilingual-e5-small` | Vectores en español | Integrado en AnythingLLM |
| Base vectorial | LanceDB | Índice RAG | `...\storage\lancedb\` |
| Base de datos | anythingllm.db | Workspaces y chats | `...\storage\anythingllm.db\` |
| Documentos | 9 indexados | Corpus del workspace | `...\storage\documents\custom-documents\` |

## 3. Workspaces configurados

| Workspace | Documentos | Modo | topN | Umbral | Uso |
|---|---|---|---:|---:|---|
| **Monitoreo_Energia_Tumaco** | 9 (dataset, guías, informes) | *query* (estricto) | 2 | 0,45 | Preguntas sobre datos y proyecto: **solo responde con los documentos** |
| **Chat General** | 0 | *automatic* | — | — | Redacción y lluvia de ideas, sin citas |

**Regla de uso:** si la pregunta es sobre los datos → *Monitoreo_Energia_Tumaco*;
si es charla general → *Chat General*. En modo *query*, si la respuesta no está en los
documentos, el asistente dice explícitamente "no está en los documentos". Esto es intencional
y evita alucinaciones.

## 4. Corpus RAG incluido en este entregable

Los documentos "ficha" de `02_Corpus_RAG/` están redactados para ser **cortos y claros**
(1 página cada uno), porque así funcionan mejor con un modelo de 1 B parámetros:

1. `01_Ficha_Dataset.md` — columnas, unidades y totales verificados.
2. `02_Ficha_Normativa.md` — normas aplicables y factor de emisión.
3. `03_Ficha_Proyecto.md` — arquitectura IoT, resultados y dashboard.

## 5. Procedimiento de carga (reproducible)

1. Abrir AnythingLLM y seleccionar el workspace **Monitoreo_Energia_Tumaco**.
2. Pulsar el icono de subir (flecha hacia arriba) junto al campo de texto.
3. Arrastrar los archivos de `02_Corpus_RAG/`.
4. Marcar **"Move to Workspace and Save"** y pulsar **Upload**.
5. Esperar el *embedding*: ~1–2 min por documento en CPU (la CPU se pone al 100 %).
6. Verificar con una pregunta de prueba del archivo `03_Conjunto_Pruebas_RAG.md`.

## 6. Ajustes de rendimiento aplicados

- Cerrar Chrome y otras apps pesadas antes de chatear (causa #1 de lentitud con 6 GB de RAM).
- Primera respuesta tras inactividad: más lenta (el modelo se recarga en RAM).
- Velocidad esperada: **8–10 palabras/segundo** en CPU; respuestas de 20–40 s son normales.
- Si hay error de conexión, verificar que Ollama esté corriendo (icono de llama en la bandeja).
- Para liberar RAM se eliminaron modelos de transcripción no usados (2,46 GB).

## 7. Uso de la API local desde Python (opcional)

```python
import requests

resp = requests.post(
    "http://127.0.0.1:11434/api/generate",
    json={
        "model": "gemma3:1b",
        "prompt": "Según el dataset, ¿cuál aula consume más energía? Responde con cifras.",
        "stream": False,
    },
    timeout=120,
)
print(resp.json()["response"])
```

## 8. Ética y soberanía de datos

- No se cargan datos personales, comerciales o comunitarios reales sin autorización y
  anonimización (Ley 1581/2012).
- El modo *query* obliga a citar el documento de origen.
- Cada respuesta generada por IA se valida contra `codigo/analisis_energetico.py`:
  **lo calculado no se delega al modelo**.
- Se registra qué parte fue calculada, qué parte fue generada y qué parte fue revisada
  por una persona competente (ficha `04_Ficha_Modelo.md`).
