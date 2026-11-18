# Módulo 5 — Reporte de consumo de recursos y comparación de rutas

**Evidencia:** Reporte de consumo de recursos del entorno de IA local (sección 5.6 del diplomado).

## 1. Medición del entorno actual (ruta básica, CPU)

| Recurso | Valor medido / estimado | Método |
|---|---|---|
| RAM total del equipo | 6 GB | Administrador de tareas / sistema |
| RAM del modelo `gemma3:1b` | ~1 GB | Monitor del sistema durante inferencia |
| Velocidad de generación | 8–10 palabras/s | Cronómetro sobre respuestas de prueba |
| Latencia de primera respuesta | 20–40 s | Tras recarga del modelo en RAM |
| Tiempo de embedding | 1–2 min por documento | Observado al cargar las fichas RAG |
| Espacio en disco del modelo | ~0,75 GB | `C:\Users\USUARIO\.ollama\models\` |
| Espacio de índice vectorial | Variable (LanceDB) | `...\storage\lancedb\` |
| Disco libre | ~7,4 GB | Tras liberar 2,46 GB de modelos no usados |
| Consumo energético de IA | No instrumentado | ⚠️ Limitación declarada: el proyecto mide el aula, no el equipo de cómputo |

> **Limitación importante:** el diplomado pide "medir tiempos, memoria y consumo aproximado".
> Se reportan tiempos y memoria. El consumo eléctrico del equipo **no se midió** y no se
> estima para no inventar un dato; se propone como trabajo futuro instrumentar el puesto
> con el mismo enfoque IoT del proyecto.

## 2. Comparación de rutas de hardware (según el diplomado)

| Ruta | Hardware | Modelos | Tiempo de respuesta | Calidad | Aplicable al caso |
|---|---|---|---|---|---|
| **Básica** (usada) | CPU, 6 GB RAM | `gemma3:1b` Q4 | 20–40 s | Suficiente con RAG corto | ✅ Entorno real del estudiante |
| Intermedia | NVIDIA RTX 3050 | Modelos cuantizados 7–8 B, flujos ComfyUI optimizados | 3–8 s | Alta | Recomendada para video/3D |
| Avanzada | Servidor/estación compartida | Modelos grandes, video, Hunyuan3D | Variable | Máxima | No disponible; diferida |

## 3. Comparación con/sin RAG

| Configuración | Resultado en las 14 pruebas | Observación |
|---|---|---|
| Sin RAG (modelo base) | No evaluado en production | Respondería con conocimiento general: riesgo de inventar normas |
| Con RAG (modo *query*, topN=2, umbral 0,45) | **14/14 correctas** | Citas documentales y rechazo de preguntas fuera del corpus |

## 4. Optimizaciones aplicadas

1. Modelo cuantizado Q4 en lugar de precisión completa: reduce RAM de ~2 GB a ~0,75 GB.
2. Modelo de 1 B parámetros en CPU en lugar de 4 B: permite 8–10 palabras/s.
3. Fichas RAG de una página: menos tokens de contexto, embeddings más rápidos.
4. Cierre de aplicaciones pesadas durante la inferencia.
5. Eliminación de modelos de transcripción no usados: 2,46 GB liberados.
6. Workspace separado (`Chat General`) para no cargar documentos en tareas de redacción libre.

## 5. Recomendaciones

- Si se dispone de RTX 3050, migrar a un modelo 7–8 B cuantizado y repetir las 14 pruebas.
- Instrumentar el consumo eléctrico del puesto de cómputo para completar el reporte de
  "costo energético de la IA" exigido por el diplomado.
- Registrar versión exacta de Ollama y AnythingLLM en una ficha de entorno antes de
  actualizar software.

## 6. Trazabilidad de versiones

| Componente | Versión registrada | Fecha de verificación |
|---|---|---|
| Python | 3.12.6 | Noviembre 2026 |
| pandas | 2.3.3 | Noviembre 2026 |
| scikit-learn | 1.9.1 | Noviembre 2026 |
| Modelo LLM | gemma3:1b (Q4) | Noviembre 2026 |
| Embeddings | multilingual-e5-small | Noviembre 2026 |
| Base vectorial | LanceDB | Noviembre 2026 |
