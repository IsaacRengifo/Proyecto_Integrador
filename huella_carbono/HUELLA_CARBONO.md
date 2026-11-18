# Huella de carbono del consumo eléctrico — Aulas Tumaco

Cálculo de las emisiones indirectas de gases de efecto invernadero (GEI) asociadas al
consumo eléctrico de dos aulas escolares de San Andrés de Tumaco (Nariño), una con aire
acondicionado y otra con ventilación natural.

---

## 1. Resultados principales

Periodo analizado: **1 al 7 de octubre de 2026** (7 días, 2 016 registros cada 5 minutos).

| Aula | Consumo (kWh) | Participación | Emisiones (kg CO₂e) |
|---|---:|---:|---:|
| Aula 1 — con aire acondicionado | 87,81 | 89,0 % | **15,54** |
| Aula 2 — ventilación natural | 10,86 | 11,0 % | **1,92** |
| **Total** | **98,67** | 100 % | **17,46** |

- Promedio diario: **14,09 kWh/día** → **2,49 kg CO₂e/día**.
- El aire acondicionado concentra el **89 % del consumo** y, por tanto, el **89 % de las emisiones**.
- Extrapolación anual (52 semanas con el mismo patrón): **≈ 5 131 kWh/año** → **≈ 908 kg CO₂e/año** (0,91 t CO₂e/año).

> La extrapolación anual es una estimación gruesa: solo se midió una semana y el uso del
> aire acondicionado varía con el clima y el calendario escolar.

### Dataset completo de 30 días

Con el dataset completo de `dashboard_energia` (septiembre de 2026, 5 760 registros):

| Aula | Consumo (kWh) | Emisiones (kg CO₂e) |
|---|---:|---:|
| AULA_CON_AC | 222,20 | 39,33 |
| AULA_SIN_AC | 66,34 | 11,74 |
| **Total** | **288,54** | **51,07** |

---

## 2. Metodología

### 2.1 Energía consumida

El dataset del repositorio registra **potencia instantánea** cada 5 minutos. La energía de
cada intervalo se obtiene integrando la potencia en el tiempo:

```
E_intervalo [kWh] = P [W] × Δt [h] / 1000
```

con `Δt = 5 min = 1/12 h`. El consumo total es la suma de todos los intervalos:

```
E_total = Σ (P_i × Δt) / 1000
```

### 2.2 Factor de emisión

Se usa el **factor de emisión de la red para inventarios de GEI o huella de carbono** del
Sistema Interconectado Nacional (SIN) para el año 2023:

> **FE = 0,177 t CO₂eq/MWh = 0,177 kg CO₂e/kWh**
> Resolución UPME 001198 del 26 de diciembre de 2024, artículo 2, literal B.

Este es el factor que la UPME indica específicamente para estimar emisiones indirectas por
consumo de electricidad en inventarios y huellas de carbono.

### 2.3 Emisiones

```
Emisiones [kg CO₂e] = E_total [kWh] × FE [kg CO₂e/kWh]
```

---

## 3. Datos utilizados

- Archivo: `Prompt - Datasep/dataset_dos_aulas_tumaco.csv`
- Frecuencia: 5 minutos
- Periodo: 2026-10-01 00:00 a 2026-10-07 23:55
- Variables usadas: `aula1_potencia_W` (aula con AC) y `aula2_potencia_W` (aula sin AC)
- Registros: 2 016 filas

---

## 4. Interpretación

1. **El aire acondicionado es el principal impulsor de la huella.** Multiplica el consumo
   por **8,1** respecto al aula ventilada naturalmente.
2. **Cada kWh ahorrado evita 0,177 kg CO₂e.** Una reducción del 10 % en el consumo del
   aula climatizada evitaría ≈ **8,78 kWh/semana** y ≈ **1,55 kg CO₂e/semana**
   (≈ 81 kg CO₂e/año en la extrapolación).
3. **Medir es el primer paso.** La telemetría IoT permite verificar el efecto real de cada
   medida y evita estimaciones basadas en potencias nominales de placa, que suelen
   sobreestimar el consumo.

---

## 5. Medidas de reducción sugeridas

| Medida | Efecto esperado |
|---|---|
| Ajustar el setpoint a 24–25 °C (en lugar de 18–20 °C) | Reduce 6–10 % del consumo del AC por cada grado |
| Mantenimiento de filtros y limpieza de serpentines | Recupera eficiencia pérdida; 5–15 % |
| Programar apagado automático fuera de horario escolar | Elimina consumo en vacancia |
| Sensores de presencia y apertura de puertas/ventanas | Evita climatizar espacios vacíos o abiertos |
| Cortinas y películas solares en ventanas | Reduce carga térmica |
| Autogeneración solar fotovoltaica | Disminuye el consumo de red y la huella asociada |

---

## 6. Limitaciones

- Solo se contabilizan **emisiones indirectas por electricidad** (alcance 2). No se incluyen
  gases refrigerantes del equipo de aire acondicionado (alcance 1), fabricación de equipos
  ni transporte (alcance 3).
- El factor de emisión es **anual y promedio**; la red cambia su mix a lo largo del día.
- La semana analizada puede no representar todo el año (clima, vacaciones, horarios).
- No se midió el consumo del aula en todos los circuitos (solo la telemetría disponible).

---

## 7. Reproducibilidad

```powershell
python calcula_huella.py "Prompt - Datasep/dataset_dos_aulas_tumaco.csv" --factor 0.177
```

El script imprime los resultados, escribe `resultados_huella.csv` y permite cambiar el
factor de emisión y el intervalo de muestreo:

```powershell
python calcula_huella.py ruta\al\dataset.csv --factor 0.177 --intervalo-min 5 --salida resultados.csv
```

Requisitos: Python 3.9+ (solo biblioteca estándar, sin dependencias externas).

---

## 8. Referencias

- UPME (2024). *Resolución 001198 del 26 de diciembre de 2024: por la cual se actualiza el
  factor de emisión del Sistema Interconectado Nacional del año 2023 para inventarios de
  emisiones de GEI y proyectos de mitigación de GEI.*
  <https://docs.upme.gov.co/Normatividad/1198_2024.pdf>
- UPME (2025). *Factores de emisión del Sistema Interconectado Nacional — SIN para el año
  2023.* <https://docs.upme.gov.co/SIMEC/Cambio-Climatico/Documents/Calculo-FE-del-SIN/Factores_de_emision_SIN_2023.pdf>
- Ley 2294 de 2023 (Plan Nacional de Desarrollo 2022–2026).
- Ley 1715 de 2014 y Ley 2099 de 2021 (transición energética).
- Ley 697 de 2001 (uso racional y eficiente de la energía, URE).
