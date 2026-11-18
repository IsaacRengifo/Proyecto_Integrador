# Módulo 1 — Árbol de problemas y matriz de oportunidades

## 1. Árbol de problemas

```
                         EFECTO CENTRAL (problema)
        Ausencia de línea base energética desagregada por aula en una
        institución educativa pública de San Andrés de Tumaco
                                  │
        ┌─────────────────────────┼─────────────────────────┐
        ▼                         ▼                         ▼
  No se puede cuantificar    No se pueden priorizar     No se puede verificar
  el impacto del AC, el      medidas de eficiencia      el cumplimiento de la
  aforo ni el consumo        ni estimar ahorros         meta de ahorro del 15 %
  pasivo nocturno            reales                     (Ley 2294/2023, art. 237)
        │                         │                         │
        ▼                         ▼                         ▼
  Costos energéticos        Decisiones basadas en      Informes sin evidencia
  elevados y sin            potencias de placa         medible (riesgo de
  explicación               (sobreestimación)          greenwashing)
        │
        ▼
  Dificultad para gestionar incentivos de la Ley 1715/2099
  y para plantear una comunidad energética escolar
```

### Causas raíz identificadas

| # | Causa | Evidencia del caso |
|---|---|---|
| C1 | Medición solo a nivel de factura general del plantel | No existen medidores por aula; el consumo individual era invisible |
| C2 | Condiciones ambientales extremas (26,7 °C, 85 % HR) que obligan a climatizar | Datos ambientales del dataset (temp. media 26,68 °C, HR media 85,24 %) |
| C3 | Inestabilidad eléctrica (98–124 V) y micro-cortes | Rango de voltaje medido en el dataset |
| C4 | Conectividad intermitente que invalida IoT solo-nube | Restricción territorial documentada |
| C5 | Ausencia de indicadores de desempeño energético (EnPIs) | No había línea base ISO 50001 previa |
| C6 | Riesgo de capturar datos personales de menores al medir ocupación | Exige solución PIR anónima (Ley 1581/2012) |

## 2. Árbol de oportunidades (convertir causas en intervenciones)

```
       OPORTUNIDAD CENTRAL: Sistema de monitoreo, análisis y predicción
       del consumo energético con IoT + IA y privacidad por diseño
                                  │
   ┌──────────────┬──────────────┬──────────────┬──────────────┐
   ▼              ▼              ▼              ▼              ▼
 Medición      Resiliencia    Análisis      Predicción     Apropiación
 desagregada   Offline First  ISO 50001     con IA         y circulari-
 (ESP32)       (SD/SPIFFS)    (EnPIs/SEU)   (RF R²=0,968)  dad (ACV/FE)
```

| Oportunidad | Causa que atiende | Indicador de éxito |
|---|---|---|
| Instrumentación con ESP32 + SCT-013 en dos aulas | C1 | 2 016 registros válidos en 7 días |
| Firmware con buffer local SD/SPIFFS | C3, C4 | Integridad de datos ante apagones |
| Cálculo de EnPIs y usos significativos de energía | C2, C5 | 5 EnPIs documentados (Módulo 2) |
| Modelo Random Forest de demanda semanal | C5 | R² = 0,968; MAE = 1,85 kWh/semana |
| Conteo PIR anónimo (sin cámaras) | C6 | Cumplimiento Ley 1581/2012 |
| Huella de carbono con factor UPME 2023 | C5 | 17,46 kg CO₂e/semana |
| Dashboard de sensibilización de 10 pestañas | C1, C5 | Producto transferible a la institución |

## 3. Matriz de oportunidades (impacto vs. facilidad)

| Oportunidad | Impacto | Facilidad | Prioridad | Justificación |
|---|---|---|---|---|
| Medición desagregada y EnPIs | Alto | Alta | **1** | Ya ejecutada; habilita todas las demás |
| Ajuste de setpoint y apagado programado | Alto | Alta | **2** | 5–15 % del consumo del AC sin inversión mayor |
| Dashboard de sensibilización | Alto | Alta | **3** | Apropiación social del conocimiento |
| Sellado y aislamiento térmico | Medio | Media | **4** | Reduce carga térmica del compresor |
| Autogeneración FV ≈ 4,5 kWp | Alto | Media | **5** | Requiere inversión y gestión de incentivos |
| Comunidad energética escolar | Alto | Media | **6** | Requiere gobernanza y reglas de operación |
| Gestión de residuos electrónicos | Medio | Media | **7** | Cierre del ciclo de vida del sistema |

## 4. Preguntas de proyecto derivadas

1. ¿Cuál es la diferencia real de consumo entre el aula climatizada y la ventilada?
2. ¿Qué variables (temperatura, aforo, humedad, estado HVAC) explican mejor la demanda?
3. ¿Es posible pronosticar el consumo semanal con precisión suficiente para la planeación?
4. ¿Cuál es la huella de carbono asociada y qué reducción es alcanzable?
5. ¿Cómo comunicar los resultados sin vulnerar la privacidad de los estudiantes?

Estas preguntas se responden en los Módulos 2, 4 y 5 y se consolidan en el Módulo 7.
