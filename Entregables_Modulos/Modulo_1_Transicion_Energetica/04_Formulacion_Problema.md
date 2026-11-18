# Módulo 1 — Formulación del problema, alcance y restricciones

**Evidencia:** Formulación del problema que orientará el proyecto integrador (sección 5.2
del documento del diplomado).

## 1. Enunciado del problema

En las instituciones educativas públicas de San Andrés de Tumaco (Nariño), las condiciones
climáticas —temperatura media de 26,7 °C y humedad relativa del 85 %— obligan a climatizar
los espacios de clase, mientras el sistema eléctrico presenta fluctuaciones de 98 a 124 V,
micro-cortes diarios e intermitencia de conectividad. En este contexto **no existe medición
desagregada a nivel de aula**, por lo que directivos y docentes desconocen cuánto consume el
aire acondicionado, cuál es el efecto del aforo estudiantil y cuál es el consumo pasivo
nocturno (*vampire load*).

La UPME estima que la eficiencia promedio en el uso de la energía en Colombia es de apenas
31 %, con pérdidas del 69 % por fallas técnicas u operativas. Sin línea base verificable,
**no es posible diseñar medidas de eficiencia, reportar ahorros creíbles ni cumplir la meta
de ahorro del 15 % en edificaciones públicas** exigida por el artículo 237 de la Ley 2294
de 2023.

## 2. Objetivo general

Desarrollar un sistema de monitoreo, análisis y predicción del consumo energético en dos aulas
de una institución educativa de San Andrés de Tumaco mediante tecnologías IoT e IA,
evaluando comparativamente un espacio con aire acondicionado frente a uno sin él para
establecer líneas base energéticas y pronosticar la demanda semanal sin control físico de cargas.

## 3. Objetivos específicos

1. Diseñar e instrumentar la infraestructura física de adquisición IoT basada en ESP32 para
   dos aulas, integrando sensores de corriente, tensión, temperatura, humedad y presencia en
   gabinetes estancos IP65.
2. Desarrollar el firmware de adquisición con protocolo de almacenamiento en buffer local
   (*Offline First*) ante fallas de red.
3. Procesar y analizar en Python el consumo acumulado, determinando usos significativos de la
   energía (SEU) e indicadores de desempeño energético (EnPIs) según ISO 50001.
4. Entrenar y evaluar modelos de Machine Learning (Random Forest / XGBoost / MLP) para
   pronosticar el consumo semanal (kWh/semana).
5. Desplegar un dashboard interactivo de visualización y sensibilización en Streamlit/Gradio.

## 4. Alcance

| Elemento | Incluido | Excluido |
|---|---|---|
| Espacio | Dos aulas de 48 m² (Aula 1 con AC, Aula 2 sin AC) | Resto del plantel (fase de escalamiento) |
| Variables | Voltaje, corriente, potencia, energía, temperatura, humedad, luxes, aforo, presencia, estados HVAC/ventilador/luces | Consumo de otros circuitos del edificio |
| Periodo | 7 días continuos (2026-10-01 a 2026-10-07), 2 016 registros a 5 min | Estacionalidad anual completa (se extrapola con cautela) |
| Control | 100 % observacional: sin relés ni corte de suministro | Maniobra física de cargas |
| Privacidad | Conteo anónimo con sensor PIR | Cámaras, reconocimiento facial o identificación de estudiantes |
| Análisis | EDA, EnPIs, regresión, clasificación, clustering, series temporales, simulación IoT | Diseño eléctrico certificado ni auditoría líder ISO 50001 |

## 5. Restricciones

| Tipo | Restricción | Estrategia de mitigación |
|---|---|---|
| **Técnica** | Inestabilidad de voltaje y micro-cortes | Buffer local SD/SPIFFS y estampa de tiempo RTC |
| **Técnica** | Conectividad intermitente | Arquitectura *Offline First*; transmisión MQTT/HTTP diferida |
| **Ambiental** | Corrosión salina | Gabinetes IP65 y recubrimiento *conformal coating* |
| **Legal** | Ley 1581/2012 (datos personales de menores) | Sensor PIR de conteo anónimo; sin imágenes |
| **Legal** | Intervención en tableros eléctricos | Medición no invasiva con pinza SCT-013; sin manipulación sin autorización |
| **Computacional** | Equipos con 6 GB de RAM sin GPU dedicada | Modelos cuantizados pequeños (gemma3:1b) en CPU; flujos ligeros |
| **Datos** | Una sola semana medida | Extrapolación anual explícitamente señalada como estimación gruesa |
| **Ética** | Uso de IA generativa | Fichas de procedencia, parámetros y validación humana (CONPES 4144) |

## 6. Hipótesis de trabajo

- **H1:** El sistema HVAC del Aula 1 es el uso significativo de energía dominante y multiplica
  el consumo del Aula 2 por un factor cercano a 8.
  *Verificación:* 87,81 vs 10,86 kWh/semana → ratio **8,09×** (Módulo 2). ✅
- **H2:** La temperatura ambiente y el aforo explican una parte sustancial de la variación
  de potencia en el Aula 1.
  *Verificación:* correlación de potencia con temperatura 0,668 y con aforo 0,857 (Módulo 2). ✅
- **H3:** Es posible pronosticar la demanda semanal con R² > 0,90 usando variables
  ambientales y de operación.
  *Verificación:* Random Forest R² = 0,968 (Módulo 5 / Módulo 7). ✅
- **H4:** La huella de carbono del caso es del orden de decenas de kg CO₂e por semana.
  *Verificación:* 17,46 kg CO₂e/semana (Módulo 4). ✅

## 7. Aportes esperados (productos transferibles)

1. Dataset documentado y código reproducible de análisis energético.
2. Tablero de EnPIs y cartera priorizada de medidas.
3. Pre-dimensionamiento de autogeneración FV y propuesta de comunidad energética escolar.
4. Huella de carbono básica del alcance 2 con factor oficial UPME.
5. Asistente local RAG con corpus normativo y conjunto de pruebas.
6. Dashboard interactivo de 10 pestañas para sensibilización directiva.
7. Informe técnico, resumen ejecutivo y plan de implementación.
