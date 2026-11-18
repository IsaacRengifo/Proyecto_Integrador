# Módulo 4 — Modelo de intervención circular con indicadores

**Evidencia:** Modelo de intervención con indicadores de circularidad y carbono vinculados a
decisiones operativas.

## 1. Matriz de intervención circular

| # | Intervención | Palanca circular | Indicador afectado | Meta | Responsable |
|---|---|---|---|---|---|
| I1 | Medición desagregada y tablero de EnPIs | Prevención / información | Cobertura de medición | 2 aulas → 100 % plantel | Operación |
| I2 | Setpoint 24–25 °C + apagado 18:00 | Reducción | E1, E4, CO₂e/semana | −15 % Aula 1 | Docentes |
| I3 | Mantenimiento de filtros y serpentines | Extensión de vida útil | E6, vida útil HVAC | +2 años | Mantenimiento |
| I4 | Reutilización del nodo IoT para medir FV | Reutilización | Nodos reutilizados | 2 de 2 | Operación |
| I5 | Convenio de devolución de RAEE y paneles | Reciclaje | Tasa de recuperación | 100 % | Comité / Finanzas |
| I6 | Autogeneración FV 4,95 kWp | Sustitución de fuente | CO₂e evitado | ≈ 1 t/año | Comité |
| I7 | Comunidad energética escolar | Modelo de negocio circular | Ahorro reinvertido | ≥ 80 % del ahorro | Asamblea |

## 2. Indicadores de circularidad y carbono (cuadro integrado)

| Indicador | Línea base | Meta año 1 | Meta año 3 | Fuente |
|---|---:|---:|---:|---|
| Consumo (kWh/semana) | 98,67 | ≤ 91,0 | ≤ 84,0 | Dataset + script M2 |
| Intensidad Wh/persona-h (Aula 1) | 64,9 | ≤ 58 | ≤ 52 | EnPI E3 |
| Emisiones kg CO₂e/semana | 17,46 | ≤ 16,0 | ≤ 14,5 | FE UPME 2023 |
| Consumo fuera de horario (kWh) | 7,49 | ≤ 4,0 | ≤ 2,0 | EnPI E4 |
| Generación FV (kWh/mes) | 0 | 468 | 468 | Modelo M3 |
| Autoconsumo (%) | 0 | ≥ 60 | ≥ 70 | Medidor bidireccional |
| RAEE con destino trazado (%) | 0 | 100 | 100 | Fichas de activos |
| Nodos IoT reutilizados (%) | 0 | 100 | 100 | Registro de operación |
| Costo energía (M COP/año) | ≈ 4,36 | ≈ 4,0 | ≈ 3,5 | Tarifa 850 COP/kWh |

## 3. Lógica de intervención (causa → acción → indicador)

```
   Consumo elevado (98,67 kWh/sem)
            │
   ┌────────┴────────┐
   ▼                 ▼
 SEU: HVAC 86 %   Consumo pasivo 7,6 %
   │                 │
 I2 (setpoint)     I1/I4 (medir y programar)
   │                 │
   ▼                 ▼
 E1 ↓ 15 %        E4 ↓ a < 2 kWh
   │                 │
   └────────┬────────┘
            ▼
   Emisiones ↓ 121 kg CO₂e/año (eficiencia)
            +
   I6: FV → 1 007 kg CO₂e/año evitados
            ▼
   I5/I7: circularidad y gobernanza cierran el ciclo
```

## 4. Priorización multicriterio

| Intervención | Impacto ambiental | Impacto económico | Facilidad | Riesgo | Puntaje (1–5) | Prioridad |
|---|---:|---:|---:|---:|---:|---:|
| I2 Setpoint y apagado | 5 | 5 | 5 | 2 | **4,5** | 1 |
| I1 Medición y tablero | 4 | 4 | 5 | 1 | **4,3** | 2 |
| I3 Mantenimiento | 4 | 4 | 4 | 2 | **3,8** | 3 |
| I6 Fotovoltaico | 5 | 4 | 2 | 3 | **3,5** | 4 |
| I4 Reutilización nodos | 3 | 4 | 4 | 1 | **3,3** | 5 |
| I5 Convenio RAEE | 3 | 2 | 3 | 2 | **2,5** | 6 |
| I7 Comunidad energética | 4 | 3 | 2 | 3 | **3,0** | 7 |

> Puntaje = promedio simple de los cuatro criterios (1 = bajo, 5 = alto; en Riesgo, 5 = bajo riesgo).

## 5. Verificación y reporte

| Frecuencia | Qué se reporta | A quién | Formato |
|---|---|---|---|
| Semanal | E1, E4, kg CO₂e/semana | Comité de Energía | Tablero dashboards |
| Mensual | EnPIs, generación FV, autoconsumo | Directivos | `04_Tablero_Indicadores_EnPIs.md` (M2) |
| Semestral | Circularidad, RAEE, ahorro reinvertido | Asamblea / UPME | Acta + informe |
| Anual | Huella de carbono y ACV actualizado | Comunidad educativa | Informe consolidado |

## 6. Criterios de autenticidad aplicados

- Cada indicador tiene **fuente de dato** y **método de cálculo** documentados.
- Las afirmaciones ambientales indican **unidad funcional, límites, supuestos y exclusiones**.
- No se usa el sistema de medición para controlar cargas (enfoque 100 % observacional).
- La IA utilizada para producir esta documentación se declara en el Módulo 6 (ficha de procedencia).
