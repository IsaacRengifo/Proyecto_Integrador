# Módulo 5 — Ficha técnica del modelo de IA local

| Campo | Valor |
|---|---|
| **Modelo** | `gemma3:1b` |
| **Proveedor / familia** | Google Gemma 3, distribuido vía Ollama |
| **Cuantización** | Q4 (≈ 0,75 GB en disco) |
| **Parámetros** | 1 000 millones (1 B) |
| **Licencia** | Gemma Terms of Use (verificar en el repositorio oficial antes de redistribuir) |
| **Captura de versión** | Modelo descargado y verificado en el equipo local, noviembre de 2026 |
| **Proveedor de ejecución** | Ollama local, `http://127.0.0.1:11434` |
| **Rol en el proyecto** | Generación de respuestas del asistente RAG; apoyo a redacción y revisión de código |
| **Modelo de embeddings** | `multilingual-e5-small` (incluye español) |
| **Base vectorial** | LanceDB |
| **Interfaz** | AnythingLLM Desktop, workspace `Monitoreo_Energia_Tumaco` |
| **Parámetros RAG** | topN = 2, umbral de similitud = 0,45, modo *query* |
| **Ventana de contexto** | Definida por el modelo cuantizado; suficiente para 2 fragmentos + pregunta |

## Requisitos y rendimiento

| Aspecto | Valor observado |
|---|---|
| RAM del equipo | 6 GB (sin GPU dedicada) |
| RAM requerida por el modelo | ~1 GB |
| Velocidad de generación | 8–10 palabras/segundo en CPU |
| Tiempo de respuesta típico | 20–40 s |
| Tiempo de embedding | ~1–2 min por documento |
| Disco libre disponible | ~7,4 GB |
| Flujo optimizado | Cerrar navegador y apps pesadas antes de usar el asistente |

## Usos permitidos y restringidos

| Uso | Estado | Condición |
|---|---|---|
| Consulta sobre documentos propios del proyecto | ✅ Permitido | Solo workspace *Monitoreo_Energia_Tumaco* |
| Apoyo a redacción de informes | ✅ Permitido | Con revisión humana y declaración de uso |
| Generación/revisión de código Python | ✅ Permitido | Validar siempre con el script reproducible |
| Cálculo de cifras energéticas | ❌ No delegar | Usar `analisis_energetico.py` |
| Carga de datos personales o identificables | ❌ Prohibido | Ley 1581/2012 |
| Respuestas sin cita documental | ❌ Prohibido | Modo *query* obligatorio |

## Riesgos identificados y mitigación

| Riesgo | Mitigación aplicada |
|---|---|
| Alucinaciones / referencias inventadas | Modo *query* estricto + 14 pruebas (ver `03_Conjunto_Pruebas_RAG.md`) |
| Sesgos del modelo | Revisión humana; el asistente no toma decisiones técnicas |
| Pérdida de privacidad | Corpus anonimizado; sin nombres ni imágenes |
| Licencias | Verificación de términos de Gemma antes de redistribuir el modelo |
| Consumo computacional | Modelo pequeño cuantizado; se eliminaron modelos no usados (2,46 GB) |
| Dependencia de versión | Ficha de versión y parámetros; repetir pruebas si se cambia el modelo |

## Declaración de uso de IA (criterio de autenticidad)

| Producto | Qué hizo la IA | Qué hicieron los humanos |
|---|---|---|
| Corpus RAG (fichas) | Borrador de redacción | Verificación de cada cifra contra el dataset y las normas |
| Informes de los módulos | Apoyo a estructura y redacción | Cálculos, decisiones técnicas, citas y validación final |
| Código Python | Sugerencia de estructura | Ejecución, depuración y verificación de resultados |
| Respuestas del chat | Generación asistida con citas | Contraste con las 14 pruebas de referencia |

> Ningún resultado numérico del proyecto depende de la salida del modelo: todos se calculan
> con scripts y se contrastan con el dataset original.
