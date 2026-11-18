# Módulo 2 — Dataset documentado (diccionario de datos)

**Archivo:** `Prompt - Datasep/dataset_dos_aulas_tumaco.csv`
**Registros:** 2 016 filas × 20 columnas. **Frecuencia:** 5 minutos.
**Periodo:** 2026-10-01 00:00:00 a 2026-10-07 23:55:00.
**Origen:** Telemetría de dos nodos ESP32 con sensores no invasivos (medición observacional).

## 1. Esquema general

| Columna | Tipo | Unidad | Descripción | Rango observado |
|---|---|---|---|---|
| `timestamp` | datetime | — | Estampa de tiempo del registro (RTC) | 2026-10-01 00:00 → 2026-10-07 23:55 |
| `temp_ambiente_C` | float | °C | Temperatura ambiente exterior | 24,0 – 31,1 (media 26,68) |
| `humedad_relativa_pct` | float | % | Humedad relativa ambiente | 73,8 – 95,0 (media 85,24) |
| `luxes_ambiente` | float | lux | Iluminancia ambiental (sensor BH1750) | 0,6 – típico < 100 |
| `voltaje_VAC` | float | V | Tensión de red medida | 98 – 124 (media 110,03) |
| `aforo_estudiantes` | int | personas | Conteo anónimo de ocupación (PIR) | 0 – 37 (media 8,0) |
| `presencia_PIR` | binario | 0/1 | Estado de presencia detectada | 31,6 % en 1 |

## 2. Variables del Aula 1 (con aire acondicionado)

| Columna | Tipo | Unidad | Descripción | Estadístico relevante |
|---|---|---|---|---|
| `aula1_potencia_W` | float | W | Potencia activa instantánea | media 522,7 · mediana 8,0 · máx 1 981,8 · p95 1 611,0 |
| `aula1_corriente_mA` | float | mA | Corriente medida con pinza SCT-013 | — |
| `aula1_temp_interior_C` | float | °C | Temperatura interior del aula | 22,7 – 30,1 (media 24,95) |
| `aula1_hvac_estado` | binario | 0/1 | Estado del HVAC Split 18 000 BTU | 32,4 % en 1 (54,4 h/semana) |
| `aula1_luces_estado` | binario | 0/1 | Estado de iluminación LED | — |
| `aula1_desperdicio` | binario | 0/1 | Marcador de consumo en vacancia/ineficiente | 11,1 % en 1 |

## 3. Variables del Aula 2 (sin aire acondicionado)

| Columna | Tipo | Unidad | Descripción | Estadístico relevante |
|---|---|---|---|---|
| `aula2_potencia_W` | float | W | Potencia activa instantánea | media 64,6 · mediana 5,0 · máx 374,5 · p95 248,4 |
| `aula2_corriente_mA` | float | mA | Corriente medida con pinza SCT-013 | — |
| `aula2_temp_interior_C` | float | °C | Temperatura interior del aula | 24,0 – 33,1 (media 27,17) |
| `aula2_ventilador_estado` | binario | 0/1 | Estado del ventilador de 100 W | — |
| `aula2_luces_estado` | binario | 0/1 | Estado de iluminación LED | — |
| `aula2_desperdicio` | binario | 0/1 | Marcador de consumo en vacancia/ineficiente | 9,5 % en 1 |

## 4. Variable derivada

| Columna | Tipo | Unidad | Descripción |
|---|---|---|---|
| `desperdicio_global` | binario | 0/1 | Marcador agregado de consumo ineficiente | 19,1 % en 1 |

> **No incluida en el CSV original:** la energía por intervalo. Se calcula en el análisis como
> `E_kWh = P_W × (5/60) / 1000`. Esta decisión se documenta para evitar ambigüedad de unidades.

## 5. Calidad y gobierno del dato

| Aspecto | Resultado |
|---|---|
| Filas nulas | 0 en variables eléctricas y ambientales |
| Brechas temporales | Ninguna: 2 016 intervalos consecutivos = 7 días × 288 intervalos/día |
| Frecuencia de muestreo | 5 min ( agregación de muestreo interno a 2 Hz en el firmware) |
| Precisión reportada | 1 decimal en potencias, temperaturas y humedades |
| Privacidad | Sin nombres, cámaras ni identificadores: conteo PIR anónimo (Ley 1581/2012) |
| Licencia de uso | Datos anonimizados del caso de estudio académico; uso autorizado por la institución |

## 6. Control de calidad aplicado en el análisis

1. Verificación de rango de voltaje (98–124 V) coherente con la inestabilidad reportada.
2. Comprobación de coherencia: cuando `aula1_hvac_estado = 0`, potencia media = 44 W;
   cuando es 1, potencia media = 1 523 W. Diferencia de 34×: consistente con el SEU identificado.
3. Validación cruzada: el consumo total (98,67 kWh) coincide con el informe de huella de carbono.
4. Revisión manual de los días 3 y 4 (fin de semana) como etiqueta de "sin clase" para el
   modelo de clasificación del dashboard.
