# Módulo 2 — Informe de auditoría energética (nivel introductorio)

**Caso:** Dos aulas de institución educativa pública, San Andrés de Tumaco (Nariño).
**Periodo:** 2026-10-01 a 2026-10-07 (7 días, 2 016 registros cada 5 minutos).
**Norma de referencia:** ISO 50001:2018 — línea base, SEU y EnPIs.
**Nivel:** Auditoría introductoria (no sustituye una auditoría certificada ni el diseño eléctrico legal).

---

## 1. Resumen ejecutivo

La línea base medida es de **98,67 kWh en la semana**. El Aula 1 (con aire acondicionado)
consume **87,81 kWh (89,0 %)** y el Aula 2 (ventilación natural) **10,86 kWh (11,0 %)**:
el HVAC multiplica por **8,09×** el consumo del espacio ventilado. El uso significativo de
la energía (SEU) es el sistema de climatización: opera el 32,4 % del tiempo a una potencia
media de 1 523 W frente a 44 W cuando está apagado. Las emisiones indirectas (alcance 2)
suman **17,46 kg CO₂e/semana**. Se identifican 6 medidas priorizadas, encabezadas por el
ajuste de setpoint y la programación de apagado, con un ahorro potencial del 5–15 % del
consumo del AC sin inversión de capital significativa.

## 2. Metodología

1. **Inventario de cargas:** Aula 1 = HVAC Split 18 000 BTU + iluminación LED;
   Aula 2 = ventilador 100 W + iluminación LED.
2. **Instrumentación:** ESP32 + pinzas no invasivas SCT-013, sensores DHT22/BH1750 y PIR,
   gabinetes IP65 con *conformal coating*, muestreo a 2 Hz y registro en SD cada 5 min.
3. **Integración energética:** `E_intervalo [kWh] = P [W] × Δt [h] / 1000`, con Δt = 5/12 h.
4. **Limpieza:** 2 016 registros válidos, sin valores nulos en las variables eléctricas.
5. **Cálculo de EnPIs:** intensidades por área, por persona-hora y consumo fuera de horario.
6. **Verificación:** todos los valores se reproducen con
   `codigo/analisis_energetico.py` sobre el dataset original.

### Nota de trazabilidad (importante)

La Tabla 2 de `Proyecto_Integrador_Final.pdf` presenta valores de **pre-dimensionamiento**
(18,4 kWh/día y 128,8 kWh/semana para el Aula 1). El cálculo sobre el **dataset medido**
entrega 12,54 kWh/día y 87,81 kWh/semana. Este informe adopta los **valores medidos** por
ser verificables y reproducibles, en coherencia con `huella_carbono/HUELLA_CARBONO.md`.
La diferencia se conserva documentada para no ocultar supuestos (criterio 6.2 del diplomado).

## 3. Usos significativos de la energía (SEU)

| SEU | Aula | Evidencia | Participación |
|---|---|---|---:|
| **Climatización (HVAC Split 18 000 BTU)** | Aula 1 | 1 523 W media al operar; 32,4 % del tiempo; r = 0,992 con potencia | ~86 % del Aula 1 |
| Iluminación LED | Ambas | Estados de luz registrados; potencia base 44 W (A1) / ~35 W (A2) | ~5–10 % |
| Ventilación (ventilador 100 W) | Aula 2 | Estado `aula2_ventilador_estado`, r = 0,448 con potencia | ~10 % del Aula 2 |
| Carga pasiva / espera (*vampire load*) | Ambas | 3,93 kWh (A1) + 3,56 kWh (A2) fuera de 07:00–18:00 | ~7,6 % del total |

## 4. Línea base y EnPIs

| Indicador (EnPI) | Aula 1 (con AC) | Aula 2 (sin AC) | Unidad |
|---|---:|---:|---|
| Energía semanal | 87,81 | 10,86 | kWh/semana |
| Energía diaria promedio | 12,54 | 1,55 | kWh/día |
| Potencia media | 522,7 | 64,6 | W |
| Potencia pico | 1 981,8 | 374,5 | W |
| Intensidad por área | 1,829 | 0,226 | kWh/m²-semana |
| Intensidad por persona-hora | 64,9 | 8,0 | Wh/persona-hora |
| Consumo fuera de horario lectivo | 3,93 | 3,56 | kWh/semana |
| Emisiones alcance 2 | 15,54 | 1,92 | kg CO₂e/semana |
| Horas HVAC | 54,4 | — | h/semana |

**EnPI principal seleccionado:** `Wh/persona-hora`, porque normaliza el consumo por ocupación
real y permite comparar ambos espacios y hacer seguimiento mensual (ISO 50001, 6.4).

## 5. Perfil operativo y variables relevantes

| Variable | Media | Rango | Correlación con potencia Aula 1 |
|---|---:|---:|---:|
| Temperatura ambiente | 26,68 °C | 24,0 – 31,1 °C | 0,668 |
| Humedad relativa | 85,24 % | 73,8 – 95,0 % | −0,572 |
| Voltaje | 110,03 V | 98 – 124 V | — |
| Aforo de estudiantes | 8,0 (máx. 37) | 0 – 37 | 0,857 |
| Presencia PIR | 31,6 % del tiempo | 0/1 | 0,960 |
| Estado HVAC | 32,4 % del tiempo | 0/1 | 0,992 |

- El consumo lectivo (07:00–18:00) concentra el **95,5 %** del Aula 1.
- Los días 3 y 4 de octubre (fin de semana, sin clases) caen a 1,04 y 1,02 kWh en el Aula 1,
  confirmando que la ocupación es el principal director de la demanda.
- El voltaje cae por debajo de 105 V en varios registros, coherente con la inestabilidad reportada.

## 6. Hallazgos

1. **El HVAC es el SEU dominante**: 86 % del consumo del Aula 1.
2. **Existe consumo evitable fuera de horario**: 7,49 kWh/semana entre ambas aulas (7,6 % del total).
3. **La huella es pequeña en términos absolutos** pero creciente si se escala: 17,46 kg CO₂e/semana
   → ≈ 0,91 t CO₂e/año extrapolados para el par de aulas.
4. **La medición desagregada corrige la percepción**: las potencias de placa habrían sobreestimado
   el consumo real.
5. **La calidad del dato es adecuada**: 2 016 registros consecutivos, sin brechas, con estampa RTC.

## 7. Recomendaciones de auditoría

| # | Recomendación | Horizonte |
|---|---|---|
| R1 | Fijar setpoint de 24–25 °C y programar apagado automático a las 18:00 | Inmediato |
| R2 | Mantenimiento de filtros y limpieza de serpentines cada 15 días | Corto plazo |
| R3 | Instalar cortinas/película solar y sellar infiltraciones en el Aula 1 | Corto plazo |
| R4 | Verificar el consumo pasivo nocturno de ambos circuitos | Corto plazo |
| R5 | Certificar equipos de medición ante UPME para incentivos Ley 1715/2099 | Mediano plazo |
| R6 | Repetir la campaña de medición en época de mayor carga térmica | Mediano plazo |

## 8. Alcance y limitaciones

- Solo se midieron dos circuitos; no se incluyen otras dependencias del plantel.
- El factor de emisión es anual y promedio (no captura variaciones horarias del mix).
- No se incluyen gases refrigerantes (alcance 1) ni fabricación/transporte (alcance 3).
- La extrapolación anual asume 52 semanas con el mismo patrón: es una estimación gruesa.
- La auditoría es introductoria: no sustituye una certificación ISO 50001 ni una intervención
  en tableros por personal legalmente competente.
