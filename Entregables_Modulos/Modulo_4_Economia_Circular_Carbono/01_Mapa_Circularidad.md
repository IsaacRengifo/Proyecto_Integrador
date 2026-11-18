# Módulo 4 — Mapa de circularidad del sistema de monitoreo

**Unidad funcional:** Monitoreo y gestión energética de dos aulas escolares durante un año
(52 semanas), incluyendo los equipos IoT y la propuesta fotovoltaica.

## 1. Flujo de materiales y energía (mapa de flujo)

```
   ENTRADAS                      SISTEMA                        SALIDAS
 ┌──────────────┐
 │ Electricidad │───► [Aulas: HVAC + iluminación]──► Servicio de confort (útil)
 │ 98,67 kWh/sem│              │                       │
 └──────────────┘              ▼                       ▼
 ┌──────────────┐        [Pérdidas 69 % UPME]    Emisiones 17,46 kg CO₂e/sem (alcance 2)
 │ Energía solar│───► [9 módulos FV 4,95 kWp]──► 468 kWh/mes autoconsumo
 │ 4,2 kWh/m2/d │              │
 └──────────────┘              ▼
 ┌──────────────┐        [Inversor + tablero]
 │  ESP32 x2    │───► [Sensores SCT-013, DHT22, PIR, BH1750]
 │  SD / RTC    │───► [Buffer local] ──► Dashboard (información)
 └──────────────┘              │
                               ▼
                    RAEE / fin de vida (baterías, sensores,
                    inversor, módulos FV) ──► Valorización
```

## 2. Jerarquía de valor aplicada

| Estrategia | Aplicación al caso | Estado | Impacto |
|---|---|---|---|
| **Prevención** | Medir antes de comprar; evitar sobre-dimensionamiento del FV | ✅ Aplicada | Evita inversión innecesaria |
| **Reducción** | Setpoint 24–25 °C, apagado programado, mantenimiento | ✅ Propuesta (M2) | 5–15 % del AC |
| **Reutilización** | Reutilizar la arquitectura IoT para monitorear la generación FV | ✅ Propuesta | Sin hardware adicional |
| **Reparación** | Sensores y ESP32 reparables localmente; stock de repuestos | 🔧 Prevista | Extiende vida útil |
| **Remanufactura** | No aplicable a escala escolar | — | — |
| **Reciclaje** | RAEE y módulos FV a gestor autorizado | 📋 Convenio propuesto | Recupera materiales |
| **Recuperación de energía** | No aplicable (no hay residuo combustible en el caso) | — | — |

## 3. Balances de materiales (simplificados)

| Flujo | Entrada | Salida / destino | Comentario |
|---|---|---|---|
| Electricidad de red | 5 131 kWh/año (extrapolado) | Uso final + pérdidas | Alcance 2: 908 kg CO₂e/año |
| Generación FV | 5 600 kWh/año (estimado) | Autoconsumo + excedente a red | Evita ≈ 1 007 kg CO₂e/año |
| Sensores (2 juegos) | 2 ESP32, 2 SCT-013, 2 DHT22, 2 PIR, 2 BH1750 | En servicio; al fin de vida → RAEE | Trazabilidad por serial |
| Almacenamiento | 2 tarjetas SD, 2 RTC con batería | En servicio; reposición 2–3 años | Baterías → recolección |
| Paneles (fase propuesta) | 9 módulos × 550 W ≈ 250 kg | En servicio 25 años → gestor autorizado | Convenio de devolución |
| Embalajes | Cajas IP65, cables, conectores | Reutilizables / reciclables | Clasificación en obra |

## 4. Puntos de pérdida identificados

| Punto de pérdida | Magnitud | Estrategia circular |
|---|---|---|
| HVAC operando en vacancia | 11,1 % de registros con marcador de desperdicio | Apagado programado + sensor PIR |
| Consumo fuera de horario | 7,49 kWh/semana (7,6 %) | Programación y verificación |
| Humedad/salinidad que degradan equipos | Corrosión acelerada | Gabinetes IP65 + coating → más vida útil |
| Pérdidas del sistema FV (PR 0,75) | 25 % de la generación teórica | Limpieza y mantenimiento preventivo |

## 5. Oportunidades de simbiosis industrial (territorio caucano)

Aunque el caso es una institución escolar, el mapa se conecta con cadenas del Cauca:

| Residuo / subproducto | Actor potencial | Oportunidad | Viabilidad para el caso |
|---|---|---|---|
| Residuos orgánicos de cocina/comedor | Restaurante escolar | Compostaje o biogás para cocina | Conceptual (Módulo 4, no implementado) |
| Cascajo de café | Productores de Tumaco/Popayán | Biomasa para secado | No disponible en el plantel |
| RAEE de otras dependencias | Talleres y comercios | Recolección conjunta | Factible como extensión de la comunidad energética |
| Baterías usadas | Comercios locales | Punto de recolección | Factible con convenio |

## 6. Modelo de negocio circular aplicable

**Servitización ligera:** en lugar de vender los paneles, el proveedor podría ofrecer
"energía como servicio" con mantenimiento incluido, reteniendo la propiedad de los equipos y
respondiendo por su recuperación al final de la vida útil. Esto alinea incentivos de eficiencia
y cierra el ciclo del producto.

## 7. Indicadores de circularidad

| Indicador | Fórmula | Meta |
|---|---|---|
| Tasa de reutilización de infraestructura | Nodos IoT reutilizados para FV / total | ≥ 50 % |
| Tasa de recuperación RAEE | Componentes devueltos / componentes instalados | 100 % |
| Vida útil efectiva | Años de servicio / vida útil diseño | ≥ 90 % |
| Intensidad de material por kWh | kg de equipo / kWh generado en vida útil | Tendencia ↓ |
| Contenido reciclado en reposiciones | kg reciclados / kg nuevos | ≥ 20 % |

## 8. Criterio anticreenwashing

Toda afirmación ambiental de este entregable indica: **unidad funcional, límites, fuente del
dato, supuestos y exclusiones**. No se declara "energía 100 % verde" ni "cero emisiones":
la generación FV reduce el consumo de red, pero la fabricación de equipos y el uso de
refrigerante quedan fuera del inventario documentado.
