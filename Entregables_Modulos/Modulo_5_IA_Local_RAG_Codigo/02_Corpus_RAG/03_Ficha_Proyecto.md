# Ficha RAG — Resumen del proyecto

Documento corto para el workspace `Monitoreo_Energia_Tumaco`.

## Identificación
- Título: Sistema de monitoreo, análisis y predicción del consumo energético en dos aulas de
  una institución educativa de San Andrés de Tumaco mediante tecnologías IoT e IA.
- Estudiante: Isaac Rengifo Quiñones — Ingeniería Mecatrónica — Unicomfacauca, 2026.
- Ubicación: San Andrés de Tumaco, Nariño (1°48′24″N, 78°45′53″O). Dos aulas de 48 m²,
  aforo de 25 a 38 estudiantes.

## Arquitectura del sistema
- Microcontrolador **ESP32**, sensores de corriente no invasivos **SCT-013**, sensores
  ambientales **DHT22/BH1750** y de presencia **PIR**.
- Filosofía **Offline First**: almacenamiento en buffer local SD/SPIFFS antes de intentar
  transmisión MQTT/HTTP. Muestreo interno a 2 Hz y registro cada 5 minutos con estampa RTC.
- Gabinetes IP65 con recubrimiento *conformal coating* por la salinidad marina.
- **100 % observacional**: no hay relés ni corte de suministro; no se manipulan tableros
  energizados sin autorización.

## Metodología (6 fases)
1. Caracterización y adecuación física. 2. Instrumentación y calibración.
3. Adquisición y buffer local. 4. EDA con pandas. 5. Modelado predictivo (Random Forest /
XGBoost). 6. Dashboard interactivo en Streamlit/Gradio.

## Resultados
- Línea base: 98,67 kWh/semana (Aula 1 con AC: 87,81; Aula 2 sin AC: 10,86). Ratio 8,09×.
- SEU: climatización del Aula 1 (86 % del consumo del aula).
- Indicadores (EnPIs): 1,829 vs 0,226 kWh/m²-semana; 64,9 vs 8,0 Wh/persona-hora.
- Huella de carbono: 17,46 kg CO₂e/semana (≈ 0,91 t/año extrapolados), FE UPME 0,177.
- Modelo predictivo: Random Forest R² = 0,968, MAE = 1,85 kWh/semana (supera a persistencia
  0,712, MLP 0,924 y XGBoost 0,959).
- Dashboard: 10 pestañas (Inicio, Descripción, Dataset, EDA, Regresión, Clasificación,
  Agrupación, Series Temporales, Simulación IoT, Conclusión).

## Recomendaciones principales
- Ajustar setpoint a 24–25 °C y programar apagado fuera de horario.
- Sellado térmico y cortinas en el Aula 1.
- Certificar equipos ante UPME para incentivos de la Ley 1715/2099.
- Escalar a una Comunidad Energética escolar (Decreto 2236/2023).
- Autogeneración FV de 4,95 kWp (9 módulos de 550 W, ≈ 468 kWh/mes).

## Privacidad
- Sensor PIR de conteo anónimo; sin cámaras ni datos personales (Ley 1581/2012).
