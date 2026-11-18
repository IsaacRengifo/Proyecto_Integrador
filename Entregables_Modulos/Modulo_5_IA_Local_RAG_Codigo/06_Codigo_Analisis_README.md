# Módulo 5 — Código fuente documentado para análisis y visualización

**Evidencia:** Repositorio de código documentado (aparte del asistente RAG).

## Inventario de código en el repositorio

| Archivo / carpeta | Función | Estado | Relación con el módulo |
|---|---|---|---|
| [`../Modulo_2_Eficiencia_Energetica/codigo/analisis_energetico.py`](../Modulo_2_Eficiencia_Energetica/codigo/analisis_energetico.py) | Línea base, SEU y EnPIs | ✅ Ejecutado y verificado | Análisis reproducible |
| [`../Modulo_3_Renovables_Comunidades/02_Modelo_Energetico.py`](../Modulo_3_Renovables_Comunidades/02_Modelo_Energetico.py) | Pre-dimensionamiento FV | ✅ Ejecutado y verificado | Modelo energético |
| [`../../../dashboard_energia/app_local.py`](../../../dashboard_energia/app_local.py) | Aplicación local Streamlit | ✅ Desplegada | Visualización e inferencia |
| [`../../../dashboard_energia/index.html`](../../../dashboard_energia/index.html) | Dashboard estático (Plotly incrustado) | ✅ Desplegado | 10 pestañas interactivas |
| [`../../../huella_carbono/calcula_huella.py`](../../../huella_carbono/calcula_huella.py) | Cálculo de emisiones | ✅ Ejecutado y verificado | Validación cruzada |
| [`../../../GUIA_ANYTHINGLLM.md`](../../../GUIA_ANYTHINGLLM.md) | Guía de operación del asistente | ✅ Vigente | Configuración RAG |

## Flujo de trabajo de código (reproducible)

```
dataset_dos_aulas_tumaco.csv
        │
        ├─► analisis_energetico.py  ──► EnPIs, SEU, línea base (Módulo 2)
        ├─► calcula_huella.py       ──► kg CO₂e/semana (Módulo 4)
        ├─► Modelo_Energetico.py    ──► kWp, módulos, área (Módulo 3)
        └─► dashboard_energia/      ──► EDA, modelos y visualización (Módulo 7)
```

## Decisiones de documentación de código

1. Cada script lleva docstring con **propósito, uso y requisitos** al inicio.
2. Las unidades se explican donde se calculan (p. ej. `P_W × 5/60 / 1000`).
3. Los supuestos (área, HSP, FE) se declaran como constantes con su fuente.
4. Todas las cifras reportadas en los informes se verifican ejecutando el script; la IA no
   sustituye este paso.
5. El dashboard es un producto transferible: funciona sin servidor ni internet.

## Resultados del dashboard (10 pestañas)

| Pestaña | Modelo / técnica | Métrica destacada |
|---|---|---|
| Regresión | MLP 64-32 | R² = 0,912 · MAE = 0,0092 kWh |
| Clasificación | Detección de consumo inusual | Exactitud 93,2 % · AUC 0,967 |
| Agrupación | K-Means (K=3) y DBSCAN | Agrupamiento espacial |
| Series temporales | LSTM vs GRU | RMSE ≈ 0,025–0,026 kWh |
| Simulación IoT | Telemetría virtual | Payload JSON personalizable |

> El modelo **Random Forest** del informe (R² = 0,968, MAE = 1,85 kWh/semana) predice la
> demanda **semanal acumulada**, mientras que el dashboard predice el consumo **por intervalo**;
> son problemas de regresión distintos y por eso sus métricas no son comparables entre sí.
