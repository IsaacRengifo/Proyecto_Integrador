# Módulo 2 — Tablero de Indicadores de Desempeño Energético (EnPIs)

**Marco:** ISO 50001:2018, ciclo PHVA. **Línea base:** semana del 1 al 7 de octubre de 2026.

## 1. Tablero principal (vista directiva)

| EnPI | Aula 1 (con AC) | Aula 2 (sin AC) | Tendencia /meta | Unidad | Frecuencia |
|---|---:|---:|---|---|---|
| **E1 — Consumo semanal** | 87,81 | 10,86 | ↓ 15 % (Ley 2294) | kWh/semana | Semanal |
| **E2 — Intensidad por área** | 1,829 | 0,226 | ↓ 10 % | kWh/m²-semana | Mensual |
| **E3 — Intensidad por persona-hora** ⭐ | 64,9 | 8,0 | ↓ 15 % | Wh/persona-hora | Mensual |
| **E4 — Consumo fuera de horario** | 3,93 | 3,56 | ↓ a < 2,0 | kWh/semana | Semanal |
| **E5 — Emisiones alcance 2** | 15,54 | 1,92 | ↓ 15 % | kg CO₂e/semana | Mensual |
| **E6 — Horas de operación HVAC** | 54,4 | n/a | Optimizar | h/semana | Semanal |
| **E7 — Tasa de desperdicio** | 11,1 | 9,5 | ↓ a < 5 | % registros | Semanal |

⭐ **EnPI principal seleccionado:** E3, porque normaliza por ocupación y permite comparación
entre espacios y seguimiento en el tiempo.

## 2. Semáforo de desempeño

| EnPI | Meta | Valor actual | Estado | Comentario |
|---|---|---:|---|---|
| Reducción consumo Aula 1 | −15 % | Línea base | 🟡 Línea base establecida | Requiere primer ciclo de verificación |
| Consumo fuera de horario | < 2,0 kWh | 3,93 + 3,56 | 🔴 Atención | Posible apagado programado |
| Tasa de desperdicio | < 5 % | 19,1 % global | 🔴 Atención | Revisar lógica de climatización en vacancia |
| Horas HVAC | ≤ 45 h/semana | 54,4 h | 🟡 Mejora posible | Ajustar setpoint y horarios |
| Cobertura de medición | 2 aulas | 2 aulas | 🟢 Cumplido | Escalable al resto del plantel |

## 3. Vista por franja horaria (potencia media, W)

| Hora | Aula 1 | Aula 2 | Lectura |
|---:|---:|---:|---|
| 00–06 | 30–51 | 28–42 | Consumo pasivo (vampire load) |
| 07 | 1 096 | 149 | Inicio de clase: HVAC arranca |
| 08–17 | ~1 080–1 102 | 75–90 | Operación sostenida del SEU |
| 18 | 39 | 42 | Fin de horario lectivo |
| 19–23 | 33–64 | 28–61 | Consumo residual |

La transición brusca a las 07:00 y 18:00 confirma que el **patrón de operación**, no solo la
temperatura, explica la demanda (r = 0,992 entre estado HVAC y potencia).

## 4. Diagrama de Pareto energético (Aula 1)

| Categoría | kWh/semana | Participación acumulada |
|---|---:|---:|
| HVAC Split 18 000 BTU | ≈ 75,5 | 86,0 % |
| Iluminación LED | ≈ 6,1 | 93,0 % |
| Consumo pasivo / espera | 3,93 | 97,5 % |
| Otros | ≈ 2,3 | 100 % |

> El 86 % del consumo está en una sola causa: actuar sobre el HVAC es la prioridad (regla 80/20).

## 5. Cuadro de mando para seguimiento (PHVA)

| Fase ISO 50001 | Acción del tablero | Evidencia |
|---|---|---|
| **Planificar** | Definir EnPIs y meta de −15 % | Este tablero + `04_Formulacion_Problema.md` (Módulo 1) |
| **Hacer** | Instrumentar ESP32 + SCT-013 y registrar en SD | Dataset de 2 016 registros |
| **Verificar** | Recalcular EnPIs cada semana con el script | `codigo/analisis_energetico.py` |
| **Actuar** | Ajustar setpoint, apagado y aislamiento | `05_Cartera_Medidas.csv` |

## 6. Nota de visualización

El tablero numérico de este documento se complementa con el **dashboard interactivo de 10
pestañas** entregado en el repositorio (`index.html` y `dashboard_energia/`), que incluye
EDA, regresión, clasificación, clustering, series temporales y simulación IoT.
