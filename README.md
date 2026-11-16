# ⚡ Dashboard Inteligente de Energía — Aulas Tumaco

Dashboard web interactivo sobre el consumo eléctrico de dos aulas escolares (con y sin
aire acondicionado) en Tumaco. Es la versión web del cuaderno `ejemplo final`, con los
datos reales del dataset (`dataset_dos_aulas_tumaco.csv`) y los modelos del cuaderno.

## Contenido

| Pestaña | Qué muestra |
|---|---|
| Inicio | Indicadores clave y simulador IoT rápido |
| Descripción | Contexto, objetivos, flujo de trabajo y tecnologías |
| Dataset & Estadísticas | Tabla de datos, diccionario de variables, descriptivos y comparativa por aula |
| Visualizaciones EDA | Distribución, climatización, boxplot, tendencia horaria, franjas, correlación y serie semanal |
| Regresión | MLP 64-32, métricas (R², MAE, RMSE, MAPE…) e inferencia directa |
| Clasificación | Detección de consumo inusual, matriz de confusión y curva ROC |
| Clustering | K-Means (K=3) y DBSCAN |
| Series Temporales | Pronóstico real vs. LSTM vs. GRU |
| Simulación IoT | Payload JSON, medidor de consumo e historial de lecturas |
| Conclusiones | Hallazgos y recomendaciones |

## Características

- **Un solo archivo**: `index.html` incluye datos y Plotly incrustados.
- **100 % estático**: no requiere servidor, base de datos ni internet.
- **Interactivo**: pestañas, selector de visualizaciones, tooltips y simuladores.

## Resultados principales

- Energía total: **98,67 kWh** en la semana (Aula 1 con AC: 87,81 kWh · Aula 2 sin AC: 10,86 kWh).
- El aire acondicionado multiplica el consumo por **8,1** y concentra el **89 %** del total.
- Regresión MLP: **R² = 0,912** · MAE = 0,0092 kWh.
- Clasificación de consumo inusual: **exactitud 93,2 %** · **AUC = 0,967**.
- Series temporales: LSTM y GRU con TensorFlow (RMSE ≈ 0,025–0,026 kWh).

## Despliegue en Vercel

Este proyecto no necesita build:

- **Framework Preset:** Other
- **Build Command:** *(vacío)*
- **Output Directory:** *(vacía)*
- **Root Directory:** la carpeta que contiene `index.html` y `vercel.json`

### Opción A — Vercel CLI

```powershell
cd deploy
npx vercel login
npx vercel --prod
```

### Opción B — Desde GitHub

1. Sube el contenido de esta carpeta a un repositorio.
2. En Vercel: **Add New → Project → Import Git Repository**.
3. Deja el preset en **Other** y pulsa **Deploy**.

### Opción C — Arrastrar y soltar

En <https://vercel.com/new> puedes importar el repositorio o desplegar el proyecto
desde la CLI. Si prefieres no instalar nada, usa la Opción B subiendo los archivos
desde la web de GitHub.

## Tecnologías

Python (pandas, scikit-learn, TensorFlow/Keras, Plotly) para el análisis y la generación
de figuras; HTML + CSS + JavaScript + Plotly.js para la página final.
