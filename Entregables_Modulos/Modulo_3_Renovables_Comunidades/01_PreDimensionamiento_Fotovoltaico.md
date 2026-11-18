# Módulo 3 — Pre-dimensionamiento fotovoltaico para autoconsumo

**Evidencia:** Pre-dimensionamiento argumentado y modelo energético reproducible para una
solución renovable pertinente al caso Tumaco.

## 1. Justificación de la alternativa

La línea base del Módulo 2 muestra **98,67 kWh/semana (14,10 kWh/día)** en las dos aulas, con
un SEU dominante (HVAC) que opera en horario diurno lectivo (07:00–18:00). Esta coincidencia
entre **perfil de generación solar** y **perfil de demanda** hace del autoconsumo fotovoltaico
la alternativa renovable más pertinente, antes de considerar biomasa o pequeña hidráulica
(sin recurso hídrico aprovechable documentado en el caso) o almacenamiento (que encarece la
solución sin necesidad crítica, dada la operación diurna).

> El orden de decisión respeta el diplomado: **primero eficiencia** (Módulo 2: setpoint,
> apagado, mantenimiento) **y luego renovables**. El dimensionamiento se calcula sobre la
> línea base *sin* restar el ahorro de eficiencia, lo que lo hace conservador.

## 2. Supuestos y parámetros

| Parámetro | Valor | Fuente / justificación |
|---|---:|---|
| Demanda diaria (línea base) | 14,10 kWh/día | Dataset medido: 98,67 kWh / 7 días |
| HSP (horas sol pico) | 4,2 kWh/m²/día | Estimación conservadora para Tumaco (clima nublado del Pacífico) |
| Performance Ratio (PR) | 0,75 | Pérdidas por inversor, cableado, temperatura y suciedad |
| Potencia de módulo | 550 W | Módulo comercial típico monocristalino |
| Área por módulo | ~2,0 m² | Dato de fabricante |
| Vida útil estimada | 25 años | Garantía típica de módulos |
| Degradación anual | 0,5 %/año | Supuesto estándar de industria |

## 3. Cálculo

```
E_día = 98,67 kWh / 7 = 14,10 kWh/día

P_pico = E_día / (HSP × PR) = 14,10 / (4,2 × 0,75) = 4,47 kWp

N_módulos = 4,47 kWp × 1000 / 550 W = 8,1 → 9 módulos (redondeo hacia arriba)

Potencia instalada = 9 × 550 W = 4,95 kWp
Área requerida     = 9 × 2,0 m² = 18 m²
Generación mensual = 4,95 × 4,2 × 0,75 × 30 ≈ 468 kWh/mes
```

> El JVM del modelo energético (`02_Modelo_Energetico.py`) usa 4,47 kWp como potencia
> **requerida** y reporta 423 kWh/mes con ese valor; la configuración comercial de 9 módulos
> (4,95 kWp) entrega ≈ 468 kWh/mes. Ambos escenarios se presentan para transparencia.

### Análisis de sensibilidad (HSP)

| HSP (kWh/m²/día) | kWp requeridos | Módulos de 550 W | Generación mensual (4,95 kWp) |
|---:|---:|---:|---:|
| 3,8 (pesimista) | 4,95 | 9 | 423 kWh |
| 4,2 (base) | 4,47 | 9 | 468 kWh |
| 4,6 (optimista) | 4,08 | 8 | 513 kWh |

Incluso en el escenario pesimista, 9 módulos cubren la demanda semanal medida.

## 4. Esquema de operación propuesto

```
  Paneles (9 × 550 W)  →  Inversor on-grid 5 kW  →  Tablero AC del plantel
                                  │
                        Medidor bidireccional (Ley 1715/2099)
                                  │
                 ESP32 (nodo existente) registra generación y consumo
                                  │
                   Dashboard: autoconsumo vs. red (%)
```

- **Configuración:** on-grid sin baterías en una primera etapa; el excedente se vierte a la red
  bajo el marco de generación distribuida (Ley 1715/2099).
- **Monitoreo:** se reutiliza la arquitectura IoT ya implementada, agregando una medición de
 generación DC/AC para verificar el PR real.
- **Seguridad:** inversor con protección anti-isla, puesta a tierra y protecciones AC/DC;
  instalación ejecutada por personal legalmente competente (RETIE).
- **Mantenimiento:** limpieza de módulos cada 2 meses por salinidad marina; revisión anual de
  conexiones y estructura.

## 5. Evaluación preliminar (detalle en Módulo 7)

| Concepto | Valor estimado |
|---|---:|
| Inversión aproximada (9 módulos + inversor + estructura + instalación) | 18 – 25 M COP |
| Generación anual | ≈ 5 600 kWh/año |
| Ahorro anual en energía (tarifa supuesta 850 COP/kWh) | ≈ 4,8 M COP/año |
| CO₂e evitado anual (FE 0,177) | ≈ 0,99 t CO₂e/año |
| Retorno simple estimado | 4 – 5 años |
| Incentivos aplicables | 50 % deducción renta, exclusión IVA, exención aranceles (Ley 1715/2099) |

## 6. Restricciones y riesgos

| Restricción | Mitigación |
|---|---|
| Corrosión salina en estructura y conectores | Materiales galvánicos/ aluminio anodizado y conectores IP67 |
| Sombras de árboles o edificaciones | Levantamiento de sombras previo a la instalación (QGIS / visita) |
| Capacidad del tablero existente | Verificación por ingeniero electricista antes de conectar |
| Variabilidad de HSP real | Monitoreo del PR y ajuste de la estrategia de limpieza |
| Disposición final de módulos al fin de vida | Convenio de recolección con proveedor (ver Módulo 4) |

## 7. Alternativas consideradas y descartadas

| Alternativa | Motivo de descarte / diferimiento |
|---|---|
| Biomasa de residuos agroindustriales | No hay residuo disponible documentado en la institución escolar; se evalúa a nivel conceptual en el Módulo 4 |
| Almacenamiento con baterías | La demanda es diurna; el costo no se justifica en la primera etapa. Se recomienda como fase 2 si se construye comunidad energética |
| Microrred aislada | La institución está conectada a la red; el objetivo es autoconsumo, no independencia total |
