# Módulo 4 — Huella de carbono básica (alcance 2)

**Norma:** ISO 14064-1 (inventario organizacional básico).
**Factor:** Resolución UPME 001198 de 2024 — FE SIN 2023 = 0,177 kg CO₂e/kWh.
**Informe completo y script:** ver [`huella_carbono/HUELLA_CARBONO.md`](../../../huella_carbono/HUELLA_CARBONO.md).

## 1. Resultado principal (semana del 1 al 7 de octubre de 2026)

| Aula | Consumo (kWh) | Participación | Emisiones (kg CO₂e) |
|---|---:|---:|---:|
| Aula 1 — con aire acondicionado | 87,81 | 89,0 % | **15,54** |
| Aula 2 — ventilación natural | 10,86 | 11,0 % | **1,92** |
| **Total** | **98,67** | 100 % | **17,46** |

- Promedio diario: **14,09 kWh/día** → **2,49 kg CO₂e/día**.
- Extrapolación anual (52 semanas): **≈ 5 131 kWh/año** → **≈ 908 kg CO₂e/año (0,91 t/año)**.

## 2. Dataset completo de 30 días (dashboard_energia)

| Aula | Consumo (kWh) | Emisiones (kg CO₂e) |
|---|---:|---:|
| AULA_CON_AC | 222,20 | 39,33 |
| AULA_SIN_AC | 66,34 | 11,74 |
| **Total** | **288,54** | **51,07** |

## 3. Metodología (reproducible)

```
E_intervalo [kWh] = P [W] × Δt [h] / 1000      (Δt = 5 min = 1/12 h)
E_total           = Σ E_intervalo
Emisiones [kg CO₂e] = E_total [kWh] × 0,177 [kg CO₂e/kWh]
```

```powershell
python huella_carbono\calcula_huella.py "Prompt - Datasep\dataset_dos_aulas_tumaco.csv" --factor 0.177
```

## 4. Límites del inventario

| Alcance | Incluido | Estado |
|---|---|---|
| **Alcance 1** (emisiones directas) | Gases refrigerantes del Split 18 000 BTU | ❌ Excluido (sin datos de carga/fuga) |
| **Alcance 2** (electricidad) | Consumo eléctrico de ambas aulas | ✅ Incluido |
| **Alcance 3** (indirectas) | Fabricación de equipos, transporte, residuos | ❌ Excluido (ver ACV simplificado) |

> Esta delimitación se declara explícitamente para evitar afirmaciones ambientales
> engañosas: el proyecto reporta **solo emisiones indirectas por electricidad**.

## 5. Escenarios de reducción

| Escenario | Ahorro kWh/semana | CO₂e evitado kg/semana | CO₂e evitado kg/año |
|---|---:|---:|---:|
| Eficiencia −5 % Aula 1 | 4,39 | 0,78 | 41 |
| Eficiencia −10 % Aula 1 | 8,78 | 1,55 | 81 |
| Eficiencia −15 % Aula 1 (meta legal) | 13,17 | 2,33 | 121 |
| Eficiencia −20 % Aula 1 | 17,56 | 3,11 | 162 |
| Autogeneración FV 4,95 kWp | ≈ 96,3 | ≈ 17,0 | ≈ 1 007 |

## 6. Indicadores de carbono vinculados a decisiones

| Indicador | Valor | Uso |
|---|---|---|
| kg CO₂e por kWh | 0,177 | Factor de conversión oficial |
| kg CO₂e por persona-hora (Aula 1) | 0,0115 | Comparación entre aulas |
| kg CO₂e por m²-semana (Aula 1) | 0,324 | Seguimiento de eficiencia |
| t CO₂e evitadas/año con FV | ≈ 1,01 | Reporte a la comunidad energética |

## 7. Incertidumbre

- El factor FE es **anual y promedio**: no refleja variaciones horarias del mix de generación.
- Solo se midió una semana: la extrapolación es una estimación gruesa.
- No se midió el consumo de todos los circuitos del edificio.
- No se incluyen fugas de refrigerante (podrían ser significativas en el Aula 1).

## 8. Validación humana

Los cálculos fueron verificados de forma independiente mediante dos rutas:
1. `huella_carbono/calcula_huella.py` (biblioteca estándar).
2. `Modulo_2/codigo/analisis_energetico.py` (pandas), que reproduce 15,54 y 1,92 kg CO₂e.

Ambas coinciden: **17,46 kg CO₂e/semana**. ✅
