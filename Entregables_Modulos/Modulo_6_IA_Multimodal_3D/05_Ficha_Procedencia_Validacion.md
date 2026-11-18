# Módulo 6 — Ficha de procedencia y validación técnica

**Criterio atendido:** Los productos generados por IA deben conservar archivos fuente,
versiones, parámetros esenciales y validación humana (sección 5.8 del diplomado).

## 1. Declaración general

Los entregables de este paquete se construyeron con una combinación de:
- **Datos primarios medidos** (dataset de 2 016 registros, verificado con scripts).
- **Redacción asistida por IA local** (`gemma3:1b` vía Ollama/AnythingLLM, ver Módulo 5).
- **Especificaciones de activos generativos** pendientes de render en hardware adecuado.

No se presenta ningún activo sintético como evidencia real de la instalación.

## 2. Matriz de procedencia por producto

| Producto | Tipo | Origen | Parámetros esenciales | Validación humana | Estado |
|---|---|---|---|---|---|
| Infografía del sistema | Imagen (especificada) | Prompt en `02_Especificacion_Infografia.md` | 1344×768, CFG 6,5–7,5, 25–30 pasos, semilla fijar | Cotejo de 10 textos con el Módulo 2 | ⚠️ Pendiente de render |
| Video de capacitación | Guion + prompts | `03_Guion_Video.md` | 90 s, 1280×720, 24 fps, Wan 2.1 | Revisión de 6 ítems (checklist) | ✅ Guion listo |
| Modelo 3D del nodo | Ficha de ruta | `04_Ficha_Modelo_3D.md` | TripoSR 512×512, GLB, escala gabinete 20×15×10 cm | Escala, malla, texturas y licencias | ⚠️ Pendiente de render |
| Resúmenes e informes | Texto | Asistente local `gemma3:1b` + revisión humana | Modo *query*, topN=2, umbral 0,45 | Cifras contrastadas con scripts | ✅ Validado |
| Código Python | Código | Apoyo de IA + depuración humana | Python 3.12.6, pandas 2.3.3 | Ejecución y verificación de salida | ✅ Validado |
| Dashboard | Software | Proyecto previo del repositorio | Plotly embebido, 10 pestañas | Revisión de métricas | ✅ Desplegado |

## 3. Parámetros esenciales conservados

| Activo | Parámetro | Valor |
|---|---|---|
| Modelo de lenguaje | Identificador | `gemma3:1b` (Q4) |
| Modelo de lenguaje | Licencia | Gemma Terms of Use (verificar antes de redistribuir) |
| Embeddings | Modelo | `multilingual-e5-small` |
| RAG | topN / umbral / modo | 2 / 0,45 / *query* |
| Imagen | Resolución / semilla | 1344×768 / fijar y registrar |
| Video | Duración / fps | 90 s / 24 fps |
| 3D | Formato / escala | GLB / gabinete ~20×15×10 cm |

## 4. Criterios de validación técnica aplicados

1. **Precisión de unidades:** kWh/semana, kg CO₂e, W y % se usan de forma consistente;
   no se mezclan BTU con julios (error detectado en una respuesta previa de AnythingLLM y
   corregido en `huella_carbono/COMO_SUBIR_A_GITHUB.md`).
2. **Trazabilidad:** cada cifra remite a un script o a una ficha del corpus RAG.
3. **Coherencia:** problema → medición → EnPIs → emisiones → predicción → comunicación.
4. **Ética:** sin rostros identificables, sin cámaras, sin suplantación de evidencia real.
5. **Licencias:** se verifica el modelo de lenguaje; los activos generativos se producen con
   modelos de licencia abierta y se registra la versión antes de publicar.
6. **Transparencia:** se informa explícitamente qué activos están pendientes de render por
   restricciones de hardware y falló la generación automática de imagen por credenciales.

## 5. Límites declarados

- El consumo energético **del equipo de cómputo** usado para IA no se midió (Módulo 5).
- La infografía y el video no se renderizaron: se entregan prompt, parámetros y checklist.
- El modelo 3D no se reconstruyó: se entrega la ruta y los criterios de depuración.
- Estas limitaciones son **declaradas**, no ocultas, en coherencia con el criterio de
  autenticidad del diplomado.

## 6. Firma de validación

| Responsable | Función | Fecha |
|---|---|---|
| Isaac Rengifo Quiñones | Validación técnica de datos, cálculos y coherencia del paquete | Noviembre de 2026 |
| Revisión académica (Unicomfacauca) | Pendiente en la sustentación final | — |
