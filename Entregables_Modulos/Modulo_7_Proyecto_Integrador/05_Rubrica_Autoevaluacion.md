# Módulo 7 — Rúbrica resumida y autoevaluación

**Fuente:** Sección 6.3 del documento del diplomado (rúbrica del proyecto integrador, 25 % de la
nota final). Se diligencia antes de la sustentación para identificar brechas.

## 1. Rúbrica oficial y autoevaluación

| Criterio | Peso | Evidencia que se presenta | Autoevaluación (1–5) | Observaciones |
|---|---:|---|---:|---|
| Problema, alcance y contexto territorial | 10 % | `Modulo_1/01`, `03`, `04` | 5 | Caso territorial argumentado; actores, normas y restricciones documentados |
| Línea base, medición e indicadores | 15 % | `Modulo_2/01`, `02`, `04`; scripts | 5 | 2 016 registros verificables; 7 EnPIs; script ejecutado |
| Solución de eficiencia, renovables y circularidad | 20 % | `Modulo_2/05`, `Modulo_3/01`, `04`, `Modulo_4/01`, `02`, `04` | 4 | Cartera priorizada, FV dimensionado, ACV declarado como simplificado; falta ejecución física |
| Sistema IoT, código y analítica | 15 % | `Modulo_2/codigo`, `Modulo_5/06`; dashboard | 5 | Firmware y sensor documentados, 4 scripts verificados, dashboard de 10 pestañas |
| Asistente local de IA y validación | 10 % | `Modulo_5/01`–`05` | 5 | RAG funcionando, 14/14 pruebas, ficha de modelo y reporte de recursos |
| Imagen, video y modelo 3D | 10 % | `Modulo_6/01`–`05` | 3 | Guion y especificaciones completos; activos renderizados pendientes por hardware/credenciales |
| Viabilidad, riesgos y plan de implementación | 10 % | `03_Evaluacion_Financiera.md`, `04_Plan_Implementacion.md` | 5 | Supuestos, sensibilidad, RACI, hitos y riesgos |
| Informe, repositorio y sustentación | 10 % | `01_Informe_Tecnico.md`, `02_Resumen_Ejecutivo.md`, `06_Guion_Sustentacion.md` | 4 | Informe y guion listos; sustentación pendiente |
| **Promedio ponderado** | **100 %** | | **4,5** | |

> Cálculo: (10×5 + 15×5 + 20×4 + 15×5 + 10×5 + 10×3 + 10×5 + 10×4) / 100 = 4,5.

## 2. Criterios transversales (verificación)

| Criterio del diplomado (6.2) | Cumplido | Evidencia |
|---|---|---|
| Precisión técnica y uso correcto de unidades | ✅ | kWh, kg CO₂e, W y % consistentes; corrección del error BTU/julio documentada |
| Trazabilidad de datos, supuestos, modelos y versiones | ✅ | Scripts, fichas y README de cada módulo |
| Coherencia diagnóstico → intervención → evidencia | ✅ | Árbol de problemas → medidas → EnPIs → resultados |
| Seguridad eléctrica, informática y de laboratorio | ✅ | SCT-013 no invasivo, IP65, sin manipulación de tableros, datos anonimizados |
| Validación humana de resultados de IA | ✅ | 14/14 pruebas RAG; cifras calculadas con scripts, no delegadas |
| Pertinencia territorial y viabilidad de sostenimiento | ✅ | Tumaco, comunidad energética, retorno 2,75–4,7 años |
| Calidad de documentación y comunicación | ✅ | Índice general, README por módulo, guion de sustentación |
| Cumplimiento ético, legal y de propiedad intelectual | ✅ | Ley 1581, CONPES 4144, licencias de modelos declaradas |

## 3. Brechas identificadas y plan de cierre

| Brecha | Criticidad | Acción | Momento |
|---|---|---|---|
| Infografía no renderizada | Media | Generar localmente con el prompt del Módulo 6 o usar captura del dashboard | Antes de la sustentación |
| Video no renderizado | Media | Producir con el guion de 90 s en RTX 3050 o presentar el guion + storyboard | Antes de la sustentación |
| Modelo 3D no reconstruido | Media | Ejecutar TripoSR → Blender siguiendo la ficha | Extensión post-sustentación |
| Consumo eléctrico de IA no medido | Baja | Declarado como limitación; instrumentar el puesto como trabajo futuro | Mejora futura |
| Aportes individuales (opción de grado) | Alta | El proyecto es individual: se documenta en la ficha de procedencia | Sustentación |

## 4. Requisitos adicionales de opción de grado (sección 6.4)

| Requisito | Estado | Observación |
|---|---|---|
| Aprobación previa del tema | ✅ | Propuesta `Rengifo Quiñones, I. (2026)` citada en la monografía |
| Memoria técnica con estructura completa | ✅ | `01_Informe_Tecnico.md` |
| Repositorio organizado con código, datos y manual | ✅ | Esta carpeta + carpeta raíz del repo |
| Evidencia de aporte individual | ✅ | Proyecto desarrollado por un estudiante |
| Informe de originalidad y declaración de IA | ✅ | Módulos 5 y 6 (fichas de procedencia) |
| Sustentación ante jurados | ⏳ | Guion preparado en `06_Guion_Sustentacion.md` |
| Producto transferible | ✅ | Dashboard, scripts, corpus RAG y plan de implementación |

## 5. Conclusión de la autoevaluación

El proyecto cumple la totalidad de los criterios de autenticidad y siete de ocho criterios de la
rúbrica en nivel alto. La brecha principal es la **renderización de activos generativos**,
declarada y mitigada con especificaciones completas y un producto visual alternativo real
(el dashboard). Se recomienda cerrarla antes de la sustentación si se dispone de RTX 3050.
