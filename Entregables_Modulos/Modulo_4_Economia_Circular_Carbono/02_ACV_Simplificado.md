# Módulo 4 — Análisis de ciclo de vida simplificado (ACV)

**Marco:** ISO 14040 / ISO 14044. **Enfoque:** ACV simplificado de carácter educativo,
no una declaración ambiental de producto certificada.

## 1. Objetivo y alcance

| Elemento | Definición |
|---|---|
| **Objetivo** | Comparar cualitativa y cuantitativamente el ciclo de vida del sistema de monitoreo IoT y de la alternativa fotovoltaica propuesta, identificando etapas de mayor carga ambiental. |
| **Unidad funcional** | Monitoreo y gestión energética de dos aulas escolares durante 1 año (52 semanas). |
| **Límites del sistema** | De "cuna a tumba": fabricación → transporte → instalación → uso → fin de vida. Se excluye la construcción del edificio y el comportamiento de ocupación ajeno al sistema. |
| **Público objetivo** | Comunidad educativa, directivos y jurado del diplomado. |
| **Datos** | Primarios para el uso (dataset medido); secundarios y supuestos para fabricación y fin de vida. |
| **Restricciones** | Sin acceso a base de datos LCA licenciada (openLCA no ejecutado); se usa ACV simplificado con factores públicos y supuestos declarados. |

## 2. Inventario de ciclo de vida (simplificado)

| Etapa | Flujo | Cantidad | Fuente / supuesto |
|---|---|---|---|
| **Fabricación IoT** | 2 ESP32 + sensores + SD + RTC | ~0,5 kg equipo | Pesos típicos de placa y sensores |
| **Fabricación FV** | 9 módulos 550 W + inversor | ~250 kg módulos + ~15 kg inversor | Datos de fabricante (supuesto) |
| **Transporte** | Equipos Popayán ↔ Tumaco | Distancia regional | No cuantificado en CO₂ (excluido) |
| **Instalación** | Gabinetes IP65, cableado, estructura | Consumibles | — |
| **Uso — electricidad** | 5 131 kWh/año | Alcance 2 | Res. UPME 1198/2024: 0,177 kg CO₂e/kWh |
| **Uso — mantenimiento** | Limpieza, reposición de baterías RTC | Baja | — |
| **Fin de vida** | RAEE y módulos FV | Gestor autorizado (propuesto) | Sin factor de emisión local disponible |

## 3. Impactos cuantificados (etapa de uso)

| Escenario | Energía | Emisiones | Base |
|---|---:|---:|---|
| Línea base (sin intervención) | 5 131 kWh/año | 908 kg CO₂e/año | 98,67 kWh/sem × 52 × 0,177 |
| Con eficiencia M1–M4 (−15 % Aula 1) | ≈ 4 446 kWh/año | ≈ 787 kg CO₂e/año | Ahorro 13,17 kWh/sem |
| Con FV 4,95 kWp | ≈ 5 600 kWh/año generados | ≈ −1 007 kg CO₂e/año evitados | Generación estimada × FE |
| Combinado (eficiencia + FV) | — | ≈ −1 128 kg CO₂e/año neto | Suma de efectos |

> Nota: el escenario "combinado" asume que toda la generación FV sustituye energía de red.
> En la práctica, parte puede vertirse a la red; el impacto real depende del contrato y del
> mix marginal. Esto se declara como incertidumbre.

## 4. Interpretación de resultados

1. **La etapa de uso domina el impacto del caso** (electricidad), con 908 kg CO₂e/año en la
   línea base. Las medidas de eficiencia son la intervención de mayor retorno ambiental inmediato.
2. **La fabricación de los módulos FV** representa un impacto "incorporado" que no se cuantifica
   por falta de datos locales; se reconoce explícitamente como limitación (evita greenwashing).
3. **El tiempo de retorno energético (*EPBT*)** de sistemas FV en climas tropicales suele ser
   de 1–3 años; con 25 años de vida útil, el balance neto es favorable, pero debe verificarse
   con la ficha del fabricante.
4. **El fin de vida es el eslabón más débil** del sistema actual:sin convenio firmado aún.
   La propuesta de circularidad del Módulo 4 lo subsana con devolución al proveedor.

## 5. Mapa de impactos por etapa (calificación cualitativa)

| Etapa | Energía | Materiales | Emisiones | Incertidumbre | Prioridad de mejora |
|---|---|---|---|---|---|
| Fabricación | Media | Alta | Media | Alta | Elegir proveedor con declaración ambiental |
| Transporte | Baja | Baja | Baja | Alta | Optimizar logística regional |
| Instalación | Baja | Media | Baja | Media | Reutilizar gabinetes y soportes |
| **Uso** | **Alta** | Baja | **Alta** | Baja | **Máxima: eficiencia + FV** |
| Fin de vida | Baja | Alta | Media | Alta | Convenio de recolección |

## 6. Acciones de mejora derivadas del ACV

| # | Acción | Etapa impactada | Indicador |
|---|---|---|---|
| A1 | Ajuste de setpoint y apagado programado | Uso | −13,17 kWh/semana |
| A2 | Autogeneración FV 4,95 kWp | Uso | −1 007 kg CO₂e/año evitados |
| A3 | Especificar módulos con bajo contenido de carbono en la ficha | Fabricación | Declaración del fabricante |
| A4 | Convenio de devolución de RAEE y paneles | Fin de vida | 100 % trazado |
| A5 | Reutilizar nodos IoT para medir la generación FV | Fabricación/Instalación | 2 nodos reutilizados |

## 7. Limitaciones

- No se ejecutó openLCA por ausencia de base de datos licenciada en el entorno local.
- Los impactos de fabricación y transporte no se cuantifican en CO₂e: se reportan cualitativamente.
- El factor de emisión es promedio anual del SIN, no marginal horario.
- La extrapolación a 52 semanas asume un patrón estable (ver Módulo 2).
- Este ACV es una herramienta de aprendizaje y decisión, **no una certificación ISO 14044**.
