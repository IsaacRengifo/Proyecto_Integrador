# SISTEMA DE MONITOREO, ANÁLISIS Y PREDICCIÓN DEL CONSUMO ENERGÉTICO EN DOS AULAS DE UNA INSTITUCIÓN EDUCATIVA DE SAN ANDRÉS DE TUMACO MEDIANTE TECNOLOGÍAS IoT E INTELIGENCIA ARTIFICIAL

**Versión ajustada a los entregables del Diplomado en Energía Circular Inteligente 5.0**

Proyecto presentado como opción de grado para optar al título de Ingeniero Mecatrónico

| Campo | Dato |
|---|---|
| **Estudiante** | Isaac Rengifo Quiñones |
| **Institución** | Institución Universitaria Comfacauca — Unicomfacauca |
| **Facultad / Programa** | Facultad de Ingeniería — Ingeniería Mecatrónica |
| **Marco** | Diplomado en Energía Circular Inteligente 5.0 |
| **Ubicación** | Popayán, Cauca — Colombia |
| **Año** | 2026 |

---

## Nota de la versión ajustada

Este documento sustituye y actualiza la versión en PDF (`Proyecto_Integrador_Final.pdf`).
Se reestructura siguiendo la secuencia de los **siete módulos del diplomado**, se incorpora
la evidencia desarrollada en cada uno y se corrigen las cifras de la línea base con los valores
**medidos y reproducibles** del dataset. Las diferencias respecto de la versión original se
explican explícitamente en la sección 5.5, en cumplimiento del criterio de trazabilidad del
diplomado (sección 6.2 del documento rector).

Los entregables detallados por módulo se encuentran en la carpeta `Entregables_Modulos/`
de este mismo repositorio.

---

## Resumen

Este proyecto aborda la caracterización, el análisis comparativo y la predicción del consumo de
energía eléctrica en dos aulas escolares de una institución educativa pública de San Andrés de
Tumaco (Nariño), contrastando un espacio climatizado mediante aire acondicionado Split de
18 000 BTU frente a un espacio con ventilación natural. Dado el contexto de inestabilidad
eléctrica y restricciones de conectividad del Pacífico colombiano, se diseñó e implementó una
arquitectura observacional no intervencionista basada en el microcontrolador ESP32, sensores de
corriente no invasivos SCT-013, sensores ambientales DHT22/BH1750 y sensores de ocupación PIR.
El sistema opera bajo el principio *Offline First* con almacenamiento en buffer local
(SD/SPIFFS) para garantizar la integridad de los datos ante apagones.

Mediante el procesamiento de **2 016 registros temporales** (7 días, intervalos de 5 minutos)
en Python se estableció una línea base de **98,67 kWh/semana**: el Aula 1 con aire acondicionado
consume 87,81 kWh (89,0 %) y el Aula 2 sin aire acondicionado 10,86 kWh (11,0 %), con un ratio
de **8,09×**. Se cuantificaron los Indicadores de Desempeño Energético (EnPIs) según ISO 50001,
se calculó la huella de carbono del alcance 2 (**17,46 kg CO₂e/semana**, factor UPME 2023 de
0,177 kg CO₂e/kWh) y se desarrolló un modelo Random Forest que pronostica la demanda semanal
con **R² = 0,968** y MAE de 1,85 kWh/semana. Se complementó con un pre-dimensionamiento
fotovoltaico de 4,95 kWp, una propuesta de Comunidad Energética Escolar, un asistente local
RAG validado con 14 pruebas y un dashboard interactivo de sensibilización.

**Palabras clave:** Eficiencia Energética, Internet de las Cosas (IoT), ESP32, Edge Computing,
Predicción Energética, ISO 50001, Economía Circular, Huella de Carbono, IA Local, RAG, Tumaco,
Privacidad por Diseño.

---

## Abstract

This project addresses the characterization, comparative analysis and forecasting of electrical
energy consumption in two classrooms of a public educational institution in San Andrés de Tumaco
(Nariño), contrasting an air-conditioned space (18,000 BTU Split unit) against a naturally
ventilated classroom. Given severe electrical instability and connectivity constraints in the
Colombian Pacific region, a non-interventional observational architecture was designed based on
the ESP32 microcontroller, SCT-013 non-invasive current sensors, DHT22/BH1750 environmental
sensors and PIR occupancy sensors. The system operates under an *Offline First* scheme with local
SD/SPIFFS buffering to ensure data integrity during power outages.

Processing 2,016 time-series records (7 days, 5-minute intervals) in Python established a baseline
of **98.67 kWh/week**: the air-conditioned classroom consumes 87.81 kWh (89.0%) and the naturally
ventilated one 10.86 kWh (11.0%), an **8.09× ratio**. Energy Performance Indicators (EnPIs) were
quantified under ISO 50001, the scope-2 carbon footprint was calculated (**17.46 kg CO₂e/week**,
UPME 2023 factor 0.177 kg CO₂e/kWh), and a Random Forest model forecasts weekly demand with
**R² = 0.968** and MAE of 1.85 kWh/week. A 4.95 kWp photovoltaic pre-design, a school energy
community proposal, a locally validated RAG assistant (14/14 tests) and an interactive
sensitization dashboard complete the work.

**Keywords:** Energy Efficiency, Internet of Things (IoT), ESP32, Edge Computing, Energy
Forecasting, ISO 50001, Circular Economy, Carbon Footprint, Local AI, RAG, Tumaco, Privacy by Design.

---

## Tabla de contenido

1. Introducción y planteamiento del problema *(Módulo 1)*
2. Marco de referencia y normativo *(Módulo 1)*
3. Marco teórico y arquitectura del sistema *(Módulos 2, 3 y 5)*
4. Diseño metodológico
5. Línea base, medición e indicadores *(Módulo 2)*
6. Eficiencia, renovables y circularidad *(Módulos 2, 3 y 4)*
7. Modelado predictivo del consumo semanal *(Módulo 5)*
8. Asistente local de IA y RAG *(Módulo 5)*
9. Dashboard interactivo de visualización
10. Producto multimodal *(Módulo 6)*
11. Viabilidad financiera e implementación *(Módulo 7)*
12. Conclusiones y recomendaciones
13. Aportes transferibles y declaración de uso de IA
14. Bibliografía y webgrafía
- Anexo A — Correspondencia con los entregables por módulo

## Lista de tablas

| # | Tabla | Sección |
|---:|---|---|
| 1 | Matriz de variables físicas, eléctricas y ambientales | 3.3 |
| 2 | Indicadores de Desempeño Energético (EnPIs) entre ambas aulas | 5.2 |
| 3 | Comparativa de métricas entre modelos predictivos | 7.2 |
| 4 | Matriz normativa aplicable | 2.2 |
| 5 | Cartera priorizada de medidas de eficiencia | 6.1 |
| 6 | Resultados de la huella de carbono | 6.4 |
| 7 | Evaluación financiera preliminar | 11.2 |
| 8 | Rúbrica y autoevaluación del proyecto | 11.5 |

## Lista de figuras

| # | Figura | Ubicación |
|---:|---|---|
| 1 | Arquitectura del sistema IoT observacional con buffer local (*Offline First*) | 3.2 |
| 2 | Distribución comparativa de potencia, temperatura y aforo | 5.3 |
| 3 | Mapa de calor de correlación entre variables | 5.4 |
| 4 | Evaluación del modelo predictivo: residuos, ajuste e histograma de error | 7.3 |
| 5 | Interfaz del dashboard interactivo | 9.1 |

> Las figuras 1 a 5 se conservan en el documento PDF original y en el dashboard interactivo del
> repositorio (`index.html`). En esta versión Markdown se describen en las tablas y secciones
> correspondientes para mantener la trazabilidad sin duplicar archivos binarios.

---

## 1. Introducción y planteamiento del problema *(Módulo 1)*

### 1.1 Contexto territorial de San Andrés de Tumaco

El municipio de San Andrés de Tumaco, ubicado en el departamento de Nariño en la subregión del
Pacífico Sur colombiano (1°48′24″N, 78°45′53″O), presenta un clima tropical húmedo con
temperaturas medias de **26,68 °C** (rango medido de 24,0 a 31,1 °C) y humedad relativa
persistente superior al 85 % (rango de 73,8 a 95,0 %). En las instituciones educativas públicas
del municipio, estas condiciones generan una alta carga térmica en los salones de clase, por lo
que los planteles instalan unidades de aire acondicionado tipo Split o sistemas de ventilación
mecánica para mantener condiciones mínimas de habitabilidad.

El contexto energético local añade tres restricciones estructurales:

1. **Inestabilidad de voltaje.** Fluctuaciones severas de tensión (98–124 V, media 110,03 V),
   sobre tensiones y micro-cortes diarios.
2. **Intermitencia de conectividad.** Pérdidas prolongadas del servicio de internet público que
   invalidan arquitecturas IoT dependientes exclusivamente de servidores en la nube.
3. **Corrosión ambiental.** Alta salinidad marina atmosférica que acelera la sulfatación de
   terminales y componentes electrónicos.

### 1.2 Planteamiento del problema y brecha de información

El Balance de Energía Útil (BEU) de la UPME señala que la eficiencia promedio en el uso de la
energía en Colombia es de apenas el 31 %, perdiéndose el 69 % restante por fallas técnicas u
operativas. En el sector educativo público existe una marcada ausencia de sistemas de medición
desagregada a nivel de aula, lo que impide cuantificar el impacto energético real del uso del
aire acondicionado, el aforo de estudiantes y el consumo pasivo nocturno (*vampire load*).

Sin una línea base verificable no es posible: (i) diseñar medidas de eficiencia con impacto
medible, (ii) reportar ahorros creíbles, (iii) cumplir la meta obligatoria de ahorro del 15 % en
edificaciones públicos del artículo 237 de la Ley 2294 de 2023, ni (iv) gestionar los incentivos
tributarios de la Ley 1715 de 2014 modificada por la Ley 2099 de 2021.

### 1.3 Justificación

| Dimensión | Justificación |
|---|---|
| **Técnica** | Adquisición IoT con almacenamiento local en buffer (*Offline First*) para resistir la volatilidad de la red eléctrica en Tumaco. |
| **Normativa** | Alineamiento con la Ley 697 de 2001 (URE), PAI-PROURE 2022–2030, Ley 1715/2014, Ley 2099/2021 y el artículo 237 de la Ley 2294 de 2023. |
| **Ética y privacidad** | Cumplimiento de la Ley 1581 de 2012 mediante sensores físicos de presencia (PIR) y conteo anónimo, bajo el principio de *Privacidad por Diseño*. |
| **Económica y social** | Sensibilización de la comunidad académica y aportes para la gestión eficiente en el Pacífico colombiano, con un producto transferible al plantel. |

### 1.4 Objetivos

**Objetivo general.** Desarrollar un sistema de monitoreo, análisis y predicción del consumo
energético en dos aulas de una institución educativa de San Andrés de Tumaco mediante
tecnologías IoT e Inteligencia Artificial, evaluando comparativamente un espacio con aire
acondicionado frente a uno sin él para establecer líneas base energéticas y pronosticar la
demanda semanal sin control físico de cargas.

**Objetivos específicos.**

1. Diseñar e instrumentar la infraestructura física de adquisición IoT basada en ESP32 para dos
   aulas (Aula 1: con aire acondicionado; Aula 2: sin aire acondicionado), integrando sensores
   de corriente, tensión, temperatura, humedad y presencia en gabinetes estancos IP65.
2. Desarrollar el firmware de adquisición e integración en ESP32 con protocolo de almacenamiento
   en buffer local (*Offline First*) para asegurar la recopilación ininterrumpida ante fallas de red.
3. Procesar y analizar mediante Ciencia de Datos en Python el consumo energético acumulado,
   determinando los Usos Significativos de la Energía (SEU) e Indicadores de Desempeño Energético
   (EnPIs) según ISO 50001.
4. Entrenar y evaluar modelos predictivos de Machine Learning (Random Forest / XGBoost / MLP) para
   pronosticar el consumo energético acumulado semanal (kWh/semana) en ambas aulas.
5. Desplegar un dashboard interactivo de visualización y sensibilización en Streamlit/Gradio.
6. Evaluar la huella de carbono, formular alternativas renovables y circulares y analizar la
   viabilidad financiera de la solución propuesta.
7. Configurar un asistente local de IA con recuperación aumentada por generación (RAG) y
   producir los entregables multimodales exigidos por el diplomado.

### 1.5 Alcance y restricciones

| Elemento | Incluido | Excluido |
|---|---|---|
| Espacio | Dos aulas de 48 m² (8 m × 6 m), aforo 25–38 estudiantes | Resto del plantel (fase de escalamiento) |
| Variables | Voltaje, corriente, potencia, energía, temperatura, humedad, luxes, aforo, presencia y estados HVAC/ventilador/luces | Consumo de otros circuitos del edificio |
| Periodo | 7 días continuos (2026-10-01 a 2026-10-07), 2 016 registros a 5 min | Estacionalidad anual completa |
| Control | 100 % observacional: sin relés ni corte de suministro | Maniobra física de cargas |
| Privacidad | Conteo anónimo con sensor PIR | Cámaras o identificación de estudiantes |
| Análisis | EDA, EnPIs, regresión, clasificación, clustering, series temporales, simulación IoT, ACV y carbono | Diseño eléctrico certificado ni auditoría líder ISO 50001 |

**Restricciones principales.** Inestabilidad eléctrica y micro-cortes (mitigada con buffer
SD/SPIFFS y RTC), conectividad intermitente (transmisión MQTT/HTTP diferida), corrosión salina
(gabinetes IP65 con *conformal coating*), protección de datos personales de menores (PIR anónimo),
hardware limitado a 6 GB RAM sin GPU dedicada (modelos cuantizados pequeños) y una sola semana
de medición (extrapolación anual declarada como estimación gruesa).

### 1.6 Hipótesis de trabajo y verificación

| # | Hipótesis | Resultado |
|---|---|---|
| H1 | El HVAC del Aula 1 es el uso significativo de energía dominante y multiplica el consumo del Aula 2 por un factor cercano a 8. | ✅ 87,81 vs 10,86 kWh → **8,09×** |
| H2 | La temperatura y el aforo explican parte sustancial de la variación de potencia del Aula 1. | ✅ r = 0,668 (temperatura) y r = 0,857 (aforo) |
| H3 | Es posible pronosticar la demanda semanal con R² > 0,90. | ✅ Random Forest R² = 0,968 |
| H4 | La huella de carbono del caso es del orden de decenas de kg CO₂e por semana. | ✅ 17,46 kg CO₂e/semana |

---

## 2. Marco de referencia y normativo *(Módulo 1)*

### 2.1 Marco geográfico

El estudio se desarrolla en San Andrés de Tumaco (Nariño), en las coordenadas 1°48′24″N,
78°45′53″O. Las dos aulas seleccionadas pertenecen a una edificación escolar oficial y cuentan
con áreas de 48 m² (8 m × 6 m) y aforos típicos de 25 a 38 estudiantes.

### 2.2 Matriz normativa aplicable

| Norma / instrumento | Año | Contenido relevante | Aplicación al proyecto |
|---|---:|---|---|
| Ley 697 de 2001 | 2001 | Uso Racional y Eficiente de la Energía (URE) como asunto de interés público | Fundamento de la medición y las medidas de eficiencia |
| Ley 1581 de 2012 | 2012 | Protección de datos personales (*Habeas Data*) | Sensor PIR anónimo; sin imágenes de estudiantes |
| Ley 1715 de 2014 / Ley 2099 de 2021 | 2014 / 2021 | Fuentes no convencionales, almacenamiento, medición inteligente; incentivos (50 % deducción renta, exclusión IVA, exención arancelaria) | Medición inteligente, autogeneración FV y certificación UPME |
| Ley 2294 de 2023 (PND) | 2023 | Art. 237: ahorro mínimo del 15 % en edificaciones públicas; Art. 291: Plan Todos Somos Pazcífico | Meta de la cartera de medidas |
| Decreto 2236 de 2023 | 2023 | Reglamentación de Comunidades Energéticas | Comunidad Energética Escolar propuesta |
| CONPES 4075 de 2022 | 2022 | Seguridad, conocimiento, innovación y reducción de emisiones | Marco estratégico nacional |
| PAI-PROURE 2022–2030 | 2022 | Reducción del 10 % del consumo final (1 688 PJ) y 85,02 Mt CO₂ | Referente de mitigación |
| CONPES 4144 de 2025 | 2025 | Política Nacional de Inteligencia Artificial | IA local responsable, trazable y validada |
| ISO 50001:2018 | 2018 | Línea base, SEU y EnPIs bajo ciclo PHVA | Metodología del Módulo 2 |
| ISO 14064-1 | — | Inventario organizacional de GEI | Delimitación del alcance 2 |
| ISO 14040 / 14044 | — | Análisis de ciclo de vida | ACV simplificado del Módulo 4 |
| Res. UPME 001198 de 2024 | 2024 | Factor de emisión SIN 2023: 0,177 kg CO₂e/kWh | Cálculo de huella de carbono |
| RETIE / RETIQ / RETILAP | — | Seguridad, etiquetado y eficiencia | Nivel comprensivo, sin sustituir competencias legales |

---

## 3. Marco teórico y arquitectura del sistema *(Módulos 2, 3 y 5)*

### 3.1 Gestión energética e ISO 50001

La norma ISO 50001:2018 establece el estándar para definir Líneas Base Energéticas (EnB) e
Indicadores de Desempeño Energético (EnPIs). En edificaciones educativas, el consumo pasivo
nocturno y la eficiencia específica (kWh/persona-hora) son métricas esenciales de diagnóstico.
El ciclo Planificar–Hacer–Verificar–Actuar (PHVA) estructura todo el proyecto: la línea base se
mide, se analizan los usos significativos, se priorizan medidas y se verifica su efecto con el
mismo método de cálculo.

### 3.2 Arquitectura IoT observacional y resiliente

**Figura 1.** Arquitectura del sistema IoT observacional con almacenamiento en buffer local
(*Offline First*) para el Aula 1 y el Aula 2.

```
  Aula 1 (HVAC + LED)          Aula 2 (Ventilador + LED)
        │                             │
   SCT-013 / DHT22 / PIR        SCT-013 / DHT22 / PIR
        └──────────┬──────────────────┘
                   ▼
             ESP32 (2 nodos)
                   │  muestreo 2 Hz
                   ▼
        Buffer local SD / SPIFFS + RTC
                   │  registro cada 5 min
                   ▼
        Transmisión MQTT / HTTP (diferida)
                   ▼
        Procesamiento Python + Dashboard
```

El microcontrolador ESP32 procesa la telemetría de los sensores y la almacena en un módulo
microSD local antes de intentar la transmisión. El sistema **no incluye relés de potencia ni
realiza corte de suministro**, manteniendo un enfoque 100 % observacional. Los gabinetes IP65
con recubrimiento dieléctrico (*conformal coating*) protegen la electrónica de la salinidad.

### 3.3 Delimitación de variables de entrada

**Tabla 1.** Matriz de variables físicas, eléctricas y ambientales registradas en ambas aulas.

| Variable | Sensor / fuente | Unidad | Descripción / rango observado |
|---|---|---|---|
| Tensión (V_RMS) | Transductor AC / analizador | V | 98 – 124 V (media 110,03) |
| Corriente (I_RMS) | SCT-013 núcleo partido | mA | Corriente de iluminación y HVAC |
| Potencia activa (P) | Calculada (V·I·cos φ) | W | Demanda instantánea |
| Energía acumulada | Integración de potencia | kWh | `E = P × Δt / 1000`, Δt = 5/12 h |
| Temperatura ambiente | DHT22 | °C | 24,0 – 31,1 (media 26,68) |
| Humedad relativa | DHT22 | % | 73,8 – 95,0 (media 85,24) |
| Iluminancia | BH1750 | lux | Registro ambiente |
| Presencia / ocupación | PIR / infrarrojo | 0/1 | Conteo anónimo; 31,6 % del tiempo |
| Temperatura interior | DHT22 | °C | Aula 1: media 24,95 · Aula 2: media 27,17 |
| Estados HVAC / ventilador / luces | Digital | 0/1 | HVAC 32,4 % del tiempo |
| Marcadores de desperdicio | Derivado | 0/1 | Global 19,1 % · Aula 1 11,1 % · Aula 2 9,5 % |

### 3.4 Infraestructura local de IA

El componente digital se apoya en un entorno *local first* (detallado en la sección 8): Ollama
con el modelo `gemma3:1b` cuantizado, AnythingLLM como capa RAG, embeddings
`multilingual-e5-small` y base vectorial LanceDB. Los datos sensibles no salen del equipo y las
cifras se calculan con scripts Python, no con el modelo de lenguaje.

---

## 4. Diseño metodológico

El estudio adopta un enfoque cuantitativo, observacional, comparativo y predictivo, estructurado
en seis fases sistemáticas, ampliadas con las dimensiones circular y financiera exigidas por el
diplomado:

| Fase | Actividad | Módulo relacionado |
|---:|---|---|
| 1 | Caracterización y adecuación física: ensamble de cajas IP65 con *conformal coating* | 1, 2 |
| 2 | Instrumentación y calibración: SCT-013 en circuitos independientes del Aula 1 (HVAC + iluminación) y Aula 2 (ventilación + iluminación) | 2 |
| 3 | Adquisición y buffer local: firmware C++ para ESP32, muestreo 2 Hz, registro SD con RTC | 2 |
| 4 | Análisis Exploratorio de Datos (EDA): limpieza, estructuración en pandas y perfiles | 2 |
| 5 | Modelado predictivo con IA: Random Forest / XGBoost / MLP para kWh/semana | 5 |
| 6 | Dashboard interactivo y sensibilización en Streamlit/Gradio | 5, 7 |
| 7 | Circularidad y carbono: ACV simplificado, huella de carbono e indicadores | 4 |
| 8 | Viabilidad y comunicación: evaluación financiera, multimodal y plan de implementación | 6, 7 |

---

## 5. Línea base, medición e indicadores *(Módulo 2)*

### 5.1 Dataset y calidad del dato

Se procesó el archivo `dataset_dos_aulas_tumaco.csv` con **2 016 registros** correspondientes a
7 días continuos (2026-10-01 00:00 a 2026-10-07 23:55) en intervalos de 5 minutos. No se
detectaron valores nulos ni brechas temporales: 2 016 = 7 días × 288 intervalos/día.

La energía de cada intervalo se calcula integrando la potencia en el tiempo:

```
E_intervalo [kWh] = P [W] × Δt [h] / 1000,   con Δt = 5 min = 1/12 h
E_total = Σ E_intervalo
```

### 5.2 Indicadores de Desempeño Energético (EnPIs)

**Tabla 2.** Matriz comparativa de Indicadores de Desempeño Energético entre ambas aulas
(valores medidos y reproducibles).

| Indicador de desempeño energético | Aula 1 (con aire acondicionado) | Aula 2 (sin aire acondicionado) |
|---|---:|---:|
| Carga principal instalada | HVAC Split 18 000 BTU + LED | Ventilación 100 W + LED |
| Energía semanal | **87,81 kWh** | **10,86 kWh** |
| Energía diaria promedio | 12,54 kWh/día | 1,55 kWh/día |
| Potencia media / pico | 522,7 W / 1 981,8 W | 64,6 W / 374,5 W |
| Potencia p95 | 1 611,0 W | 248,4 W |
| Intensidad por área | 1,829 kWh/m²-semana | 0,226 kWh/m²-semana |
| Intensidad por persona-hora ⭐ | 64,9 Wh/persona-hora | 8,0 Wh/persona-hora |
| Consumo fuera de horario lectivo | 3,93 kWh/semana | 3,56 kWh/semana |
| Horas de operación HVAC | 54,4 h/semana (32,4 %) | n/a |
| Emisiones CO₂e (alcance 2) | 15,54 kg/semana | 1,92 kg/semana |

⭐ **EnPI principal seleccionado:** Wh/persona-hora, por normalizar el consumo por ocupación real
y permitir comparación entre espacios y seguimiento mensual.

### 5.3 Perfil horario y usos significativos de la energía

**Figura 2.** Distribución comparativa de potencia activa, temperatura interior y aforo ocupacional.

| Franja | Aula 1 (W) | Aula 2 (W) | Lectura |
|---|---:|---:|---|
| 00:00–06:00 | 30 – 51 | 28 – 42 | Consumo pasivo (*vampire load*) |
| 07:00 | 1 096 | 149 | Inicio de clase: arranque del HVAC |
| 08:00–17:00 | ~1 080 – 1 102 | 75 – 90 | Operación sostenida del SEU |
| 18:00 | 39 | 42 | Fin del horario lectivo |
| 19:00–23:00 | 33 – 64 | 28 – 61 | Consumo residual |

El consumo lectivo (07:00–18:00) concentra el **95,5 %** del Aula 1. Los días 3 y 4 de octubre
(fin de semana, sin clases) caen a 1,04 y 1,02 kWh respectivamente en el Aula 1, confirmando que
la ocupación es el principal director de la demanda.

El **Uso Significativo de la Energía (SEU)** es la climatización del Aula 1: potencia media de
**1 523 W cuando opera** frente a **44 W apagado** (diferencia de 34×), con correlación de
0,992 entre estado HVAC y potencia.

### 5.4 Correlaciones entre variables

**Figura 3.** Mapa de calor de correlación entre temperatura exterior, aforo, humedad y potencia.

| Variable | Correlación con potencia del Aula 1 |
|---|---:|
| Estado HVAC | 0,992 |
| Presencia PIR | 0,960 |
| Aforo de estudiantes | 0,857 |
| Temperatura ambiente | 0,668 |
| Humedad relativa | −0,572 |
| Potencia del Aula 2 | 0,457 |

### 5.5 Nota de trazabilidad: diferencia con la versión anterior

La **Tabla 2 de la versión en PDF** reportaba 18,4 kWh/día y 128,8 kWh/semana para el Aula 1 y
3,6 kWh/día / 25,2 kWh/semana para el Aula 2. Esos valores corresponden a una estimación de
**pre-dimensionamiento** basada en potencias nominales. El cálculo reproducible sobre el dataset
medido entrega **12,54 kWh/día / 87,81 kWh/semana** y **1,55 kWh/día / 10,86 kWh/semana**.

Esta versión adopta los **valores medidos** porque:

1. Son reproducibles con `Entregables_Modulos/Modulo_2_Eficiencia_Energetica/codigo/analisis_energetico.py`.
2. Coinciden con el informe `huella_carbono/HUELLA_CARBONO.md` ya publicado en el repositorio.
3. El diplomado exige declarar supuestos y no ocultar diferencias (criterio 6.2).

La diferencia se conserva documentada y no se elimina: ambas cifras son válidas en su contexto
(estimación de diseño vs. medición real), pero solo la segunda es verificable.

> Se recomienda revisar igualmente el valor de exactitud de clasificación del dashboard: la
> monografía original reporta 91,83 % con AUC 0,8343, mientras que el `README.md` del repositorio
> reporta 93,2 % con AUC 0,967. Ambos aparecen registrados hasta su verificación con el notebook
> fuente.

---

## 6. Eficiencia, renovables y circularidad *(Módulos 2, 3 y 4)*

### 6.1 Cartera priorizada de medidas de eficiencia

**Tabla 5.** Medidas priorizadas por impacto, inversión y facilidad de implementación.

| ID | Medida | Tipo | Ahorro estimado | Inversión | Prioridad |
|---|---|---|---:|---|---:|
| M1 | Ajustar setpoint de 18–20 °C a 24–25 °C | Operación | 4,39–8,78 kWh/sem (5–10 %) | Baja | 1 |
| M2 | Apagado automático fuera de 07:00–18:00 | Operación | 3,93 kWh/sem (4,5 %) | Baja | 2 |
| M3 | Mantenimiento de filtros y serpentines cada 15 días | Mantenimiento | 4,39 kWh/sem (5 %) | Baja | 3 |
| M4 | Sellado hermético, cortinas y película solar | Rediseño | 2,20–4,39 kWh/sem | Media | 4 |
| M5 | Autogeneración solar FV de 4,95 kWp | Sustitución | ≈ 96 kWh/sem | Alta | 5 |
| M6 | Escalado IoT y Comunidad Energética Escolar | Gestión | Habilita las demás | Media | 6 |

El cumplimiento de la meta legal del 15 % en el Aula 1 equivale a **13,17 kWh/semana**
(≈ 685 kWh/año y 121 kg CO₂e/año evitados).

### 6.2 Pre-dimensionamiento fotovoltaico

Con HSP de 4,2 kWh/m²/día (estimación conservadora para el Pacífico nublado) y Performance Ratio
de 0,75:

```
E_diaria = 98,67 kWh / 7 = 14,10 kWh/día
P_pico   = 14,10 / (4,2 × 0,75) = 4,47 kWp
Módulos  = 4,47 kWp × 1000 / 550 W = 8,1 → 9 módulos (4,95 kWp instalados)
Área     = 9 × 2 m² = 18 m²
Generación estimada = ≈ 468 kWh/mes (configuración instalada)
CO₂e evitado = ≈ 1 007 kg/año
```

Análisis de sensibilidad: con HSP de 3,8 la generación cae a 423 kWh/mes (aún cubre la demanda);
con HSP de 4,6 se requieren 8 módulos. Se descarta almacenamiento en baterías en la primera etapa
porque la demanda es diurna y el plantel permanece conectado a la red; se prevé como fase 2 de la
comunidad energética.

### 6.3 Comunidad Energética Escolar

Al amparo del Decreto 2236 de 2023 se propone una organización con Asamblea General, Comité de
Energía y tres áreas (operación, finanzas y comunicación). Reglas principales: autoconsumo
on-grid con excedente vertido a la red, reinversión del ahorro en mantenimiento → reposición →
ampliación, datos de ocupación anónimos, intervenciones eléctricas solo por personal competente y
propiedad de los activos definida en acta constitutiva.

Indicadores de la comunidad: cobertura de medición del 100 % del plantel en 24 meses,
autoconsumo ≥ 60 %, ahorro ≥ 15 % frente a la línea base y fondo de mantenimiento activo.

### 6.4 Economía circular, ACV y huella de carbono

Se construyó un mapa de circularidad con la jerarquía de valor aplicada al caso: prevención
(medir antes de comprar), reducción (setpoint y apagado), reutilización (los nodos IoT miden
también la generación FV), reparación (sensores reparables localmente) y reciclaje (devolución de
RAEE y paneles a gestor autorizado). El ACV simplificado cubre de cuna a tumba; la etapa de uso
domina el impacto (908 kg CO₂e/año en la línea base) y la fabricación de módulos se declara como
incertidumbre no cuantificada por falta de base de datos local.

**Tabla 6.** Resultados de la huella de carbono (alcance 2, FE = 0,177 kg CO₂e/kWh).

| Aula | Consumo (kWh/semana) | Participación | Emisiones (kg CO₂e/semana) |
|---|---:|---:|---:|
| Aula 1 — con aire acondicionado | 87,81 | 89,0 % | 15,54 |
| Aula 2 — ventilación natural | 10,86 | 11,0 % | 1,92 |
| **Total** | **98,67** | 100 % | **17,46** |

Promedio diario: 14,09 kWh/día → 2,49 kg CO₂e/día. Extrapolación anual: ≈ 5 131 kWh/año →
≈ 908 kg CO₂e/año (0,91 t/año). Con el dataset completo de 30 días del dashboard
(288,54 kWh) la huella es de 51,07 kg CO₂e.

**Límites del inventario:** se incluye solo el alcance 2 (electricidad). Se excluyen gases
refrigerantes (alcance 1), fabricación de equipos y transporte (alcance 3). Esta delimitación se
declara explícitamente para evitar afirmaciones ambientales engañosas.

### 6.5 Indicadores de circularidad y carbono

| Indicador | Línea base | Meta año 1 | Meta año 3 |
|---|---:|---:|---:|
| Consumo (kWh/semana) | 98,67 | ≤ 91,0 | ≤ 84,0 |
| Intensidad Wh/persona-h (Aula 1) | 64,9 | ≤ 58 | ≤ 52 |
| Emisiones (kg CO₂e/semana) | 17,46 | ≤ 16,0 | ≤ 14,5 |
| Generación FV (kWh/mes) | 0 | 468 | 468 |
| Autoconsumo (%) | 0 | ≥ 60 | ≥ 70 |
| RAEE con destino trazado (%) | 0 | 100 | 100 |

---

## 7. Modelado predictivo del consumo semanal *(Módulo 5)*

### 7.1 Formulación del problema regresivo

El modelo pronostica la variable acumulada semanal `y = kWh/semana` a partir del vector de
características históricas:

```
X⃗ = { Potencia Lag1, Temperatura Media, Humedad Media,
       Aforo Promedio, Horas HVAC Programadas }        (1)
```

Se evaluaron modelos supervisados (Random Forest Regressor y XGBoost) frente a un modelo base de
persistencia y una red neuronal multicapa (MLP).

### 7.2 Resultados

**Tabla 3.** Comparativa de métricas de precisión entre modelos predictivos.

| Modelo evaluado | MAE (kWh/semana) | RMSE (kWh/semana) | R² |
|---|---:|---:|---:|
| Modelo base (persistencia promedio) | 8,42 | 11,15 | 0,712 |
| Red Neuronal Multicapa (MLP) | 3,18 | 4,52 | 0,924 |
| **Random Forest Regressor** | **1,85** | **2,64** | **0,968** |
| XGBoost Regressor | 2,05 | 2,91 | 0,959 |

### 7.3 Evaluación gráfica

**Figura 4.** Evaluación del modelo predictivo: (arriba izquierda) residuos de regresión;
(arriba derecha) ajuste de valores reales vs. predichos (R² > 0,96);
(abajo) histograma de distribución del error absoluto.

Random Forest supera a todos los alternativos y permite pronosticar la demanda futura para la
planeación administrativa. La diferencia frente al modelo base (R² 0,712 → 0,968) confirma que
las variables ambientales y de operación aportan información predictiva sustancial.

> El dashboard incorpora además un modelo de regresión MLP para consumo por intervalo con
> R² = 0,912 y MAE = 0,0092 kWh. Son problemas distintos (semanal acumulado vs. por intervalo),
> por lo que sus métricas no son comparables entre sí.

---

## 8. Asistente local de IA y RAG *(Módulo 5)*

### 8.1 Arquitectura y configuración

| Componente | Configuración |
|---|---|
| Proveedor LLM | Ollama local en `127.0.0.1:11434` |
| Modelo | `gemma3:1b` cuantizado Q4 (~0,75 GB) |
| Interfaz | AnythingLLM Desktop |
| Embeddings | `multilingual-e5-small` (español incluido) |
| Base vectorial | LanceDB |
| Workspace | `Monitoreo_Energia_Tumaco`, modo *query*, topN = 2, umbral = 0,45 |
| Corpus | Fichas cortas de dataset, normativa y proyecto + documentos del repositorio |

Todo funciona sin internet y sin nube. El modo *query* estricto obliga a citar documentos y a
responder "no está en los documentos" cuando la información no existe en el corpus.

### 8.2 Conjunto de pruebas y validación

Se diseñaron 14 pruebas: 10 con respuesta esperada conocida (filas del dataset, consumo total,
aula de mayor consumo, factor UPME, huella, modelo con mejor R², carácter observacional,
número de paneles, privacidad) y 4 negativas que deben rechazarse (personas, cifras históricas,
resoluciones inexistentes, total de estudiantes del plantel).

**Resultado: 14/14 pruebas superadas (100 %).** Las cifras nunca se delegan al modelo: se
calculan con `analisis_energetico.py` y `calcula_huella.py`. La velocidad observada es de
8–10 palabras/segundo en CPU, con respuestas de 20–40 s.

### 8.3 Ética y soberanía de datos

No se cargan datos personales o identificables sin autorización y anonimización. Se registra
qué parte fue calculada, qué parte generada y qué parte revisada por una persona competente, en
coherencia con el CONPES 4144 de 2025 y el criterio de autenticidad del diplomado.

---

## 9. Dashboard interactivo de visualización

### 9.1 Descripción

**Figura 5.** Interfaz del dashboard interactivo desplegado en Streamlit/Gradio, con enlace de
acceso en el repositorio.

El dashboard organiza la información en **10 módulos interactivos**:

| # | Pestaña | Contenido |
|---:|---|---|
| 1 | Inicio | Monitoreo inteligente y predicción IA en aulas de Tumaco |
| 2 | Descripción del proyecto | Contexto, objetivos, flujo de trabajo y tecnologías |
| 3 | Conjunto de datos y estadísticos | Datos reales, diccionario de variables y descriptivos |
| 4 | Visualizaciones EDA | Distribución, boxplot, tendencia horaria, franjas, correlación y serie semanal |
| 5 | Regresión – Red neuronal | Predicción del consumo por intervalo (R² 0,912) |
| 6 | Clasificación | Detección de consumo inusual (exactitud 91,83 %, AUC 0,8343) |
| 7 | Agrupación | K-Means (K=3) y DBSCAN |
| 8 | Series temporales | LSTM vs GRU |
| 9 | Simulación IoT | Telemetría virtual personalizada con payload JSON |
| 10 | Conclusión | Hallazgos y recomendaciones basadas en resultados reales |

El dashboard es 100 % estático en su versión web (`index.html` con Plotly incrustado): no
requiere servidor, base de datos ni internet, lo que garantiza su apropiación por la institución.

---

## 10. Producto multimodal *(Módulo 6)*

El paquete multimodal se entrega con trazabilidad completa, conforme al criterio de autenticidad
del diplomado: se conserva archivo fuente, prompt, parámetros esenciales y validación humana.

| Activo | Estado | Evidencia |
|---|---|---|
| Infografía técnica del sistema | Especificada (render pendiente) | Prompt maestro, 1344×768, CFG 6,5–7,5, 25–30 pasos y 10 textos verificables en `Modulo_6/02_Especificacion_Infografia.md` |
| Video de capacitación (90 s) | Guion completo | 6 escenas, locación, prompts Wan 2.1 y checklist de validación en `Modulo_6/03_Guion_Video.md` |
| Modelo 3D del nodo IoT | Ruta definida | TripoSR 512×512 → GLB → depuración en Blender, escala gabinete 20×15×10 cm, en `Modulo_6/04_Ficha_Modelo_3D.md` |
| Producto visual real disponible | ✅ Operativo | Dashboard interactivo de 10 pestañas, capturable como evidencia |

La renderización de los activos generativos quedó diferida por las restricciones de hardware
(6 GB RAM sin GPU dedicada, ruta básica del diplomado) y por un fallo de credenciales del
servicio de imágenes. **Ningún activo sintético se presenta como evidencia real de la
instalación.** La declaración completa está en `Modulo_6/05_Ficha_Procedencia_Validacion.md`.

---

## 11. Viabilidad financiera e implementación *(Módulo 7)*

### 11.1 Supuestos

Tarifa de referencia 850 COP/kWh (todo incluido), precios de mercado colombiano a noviembre de
2026, retorno simple sin descuento ni inflación. Se presentan escenarios de sensibilidad.

### 11.2 Evaluación financiera

**Tabla 7.** Evaluación financiera preliminar.

| Concepto | Valor |
|---|---:|
| Costo anual de la línea base | ≈ 4,36 M COP |
| Inversión FV detallada (4,95 kWp) | ≈ 14,7 M COP (rango conservador 14,7–25 M) |
| Ahorro anual por eficiencia | ≈ 0,58 M COP |
| Ahorro anual por autogeneración | ≈ 4,76 M COP |
| Ahorro anual total | ≈ 5,34 M COP |
| Retorno simple (base) | 2,75 años |
| Retorno simple (rango) | 2,25 – 4,68 años |
| Costos de operación y mantenimiento | ≈ 2,6 M COP/año |
| Flujo neto anual | ≈ 2,74 M COP/año |
| CO₂e evitado total | ≈ 1,13 t/año |

Los incentivos de la Ley 1715/2099 (50 % deducción en renta, exclusión de IVA y exención
arancelaria, previa certificación UPME) **no se incluyeron** en el retorno para ser conservador.

### 11.3 Sensibilidad

| Escenario | Tarifa (COP/kWh) | HSP | Ahorro anual | Retorno |
|---|---:|---:|---:|---:|
| Pesimista | 700 | 3,8 | 4,35 M COP | 3,4 años |
| Base | 850 | 4,2 | 5,34 M COP | 2,75 años |
| Optimista | 1 000 | 4,6 | 6,50 M COP | 2,25 años |

### 11.4 Plan de implementación

| Fase | Meses | Actividades | Hito |
|---|---|---|---|
| 1. Formación y gobernanza | 1–2 | Sensibilización y Comité de Energía | Acta constitutiva |
| 2. Eficiencia inmediata | 2–4 | Setpoint, apagado, mantenimiento, sellado | EnPI E1 ≤ 91 kWh/sem |
| 3. Instrumentación y FV | 4–8 | Réplica de nodos, incentivos, instalación FV | ≥ 400 kWh/mes generados |
| 4. Operación y mejora | 8–24 | Seguimiento, reportes y comunidad energética | Ahorro acumulado ≥ 15 % |

### 11.5 Rúbrica y autoevaluación

**Tabla 8.** Autoevaluación frente a la rúbrica del diplomado (sección 6.3).

| Criterio | Peso | Autoevaluación (1–5) |
|---|---:|---:|
| Problema, alcance y contexto territorial | 10 % | 5 |
| Línea base, medición e indicadores | 15 % | 5 |
| Solución de eficiencia, renovables y circularidad | 20 % | 4 |
| Sistema IoT, código y analítica | 15 % | 5 |
| Asistente local de IA y validación | 10 % | 5 |
| Imagen, video y modelo 3D | 10 % | 3 |
| Viabilidad, riesgos y plan de implementación | 10 % | 5 |
| Informe, repositorio y sustentación | 10 % | 4 |
| **Promedio ponderado** | **100 %** | **4,5** |

---

## 12. Conclusiones y recomendaciones

### 12.1 Conclusiones

1. Se instrumentó con éxito una arquitectura IoT observacional basada en ESP32 y sensores no
   invasivos SCT-013 en dos aulas escolares de Tumaco, operando de forma autónoma bajo la
   filosofía *Offline First* con almacenamiento en buffer local (SD/SPIFFS).
2. El análisis comparativo demostró que el uso del aire acondicionado en el Aula 1 multiplica por
   **8,09×** el consumo eléctrico (87,81 vs 10,86 kWh/semana), identificando la climatización
   como el uso significativo de energía (86 % del Aula 1).
3. La huella de carbono del alcance 2 es de **17,46 kg CO₂e/semana** (≈ 0,91 t/año extrapolados),
   con reducciones alcanzables de 121 kg CO₂e/año por eficiencia y ≈ 1 007 kg/año por
   autogeneración fotovoltaica.
4. El modelo predictivo Random Forest alcanzó R² = 0,968 y MAE = 1,85 kWh/semana, superando a los
   modelos base, MLP y XGBoost, y permitiendo pronosticar la demanda para la planeación.
5. El asistente local RAG superó 14/14 pruebas sin delegar cálculos al modelo, y el dashboard de
   10 pestañas promueve la concienciación energética sin intervenir circuitos ni vulnerar la
   privacidad de los estudiantes (Ley 1581 de 2012).
6. La solución es financieramente viable en todos los escenarios (retorno de 2,25 a 4,68 años)
   y sostenible si se constituye la Comunidad Energética Escolar propuesta.

### 12.2 Recomendaciones

1. Implementar sellados herméticos y aislamiento térmico en la envolvente del Aula 1 para reducir
   la infiltración de calor y la carga del compresor.
2. Fijar el setpoint del HVAC en 24–25 °C y programar el apagado automático fuera del horario
   lectivo; ejecutar mantenimiento quincenal de filtros y serpentines.
3. Gestionar la certificación de los equipos de medición ante la UPME para solicitar los
   incentivos tributarios de la Ley 1715 de 2014 / Ley 2099 de 2021.
4. Escalar el nodo de adquisición IoT a las demás aulas del plantel mediante una Comunidad
   Energética escolar (Decreto 2236 de 2023).
5. Instalar 9 módulos fotovoltaicos de 550 W con convenio de devolución al fin de vida.
6. Repetir la campaña de medición en otra época del año e instrumentar el consumo eléctrico del
   puesto de cómputo usado para IA, para completar el reporte de recursos del Módulo 5.

---

## 13. Aportes transferibles y declaración de uso de IA

**Productos transferibles.** Dataset documentado; scripts reproducibles de análisis energético,
huella de carbono y pre-dimensionamiento FV; tablero de EnPIs; cartera priorizada de medidas;
asistente RAG con corpus y pruebas; dashboard interactivo de 10 pestañas; informes por módulo;
guion multimodal; evaluación financiera y plan de implementación.

**Declaración de uso de IA.** Los datos son medidos propios y los cálculos reproducibles. La IA
local (`gemma3:1b`) apoyó la redacción de documentos y la revisión de código, con validación
humana de cada cifra. Los activos generativos se entregan como especificaciones y guiones con su
ficha de procedencia. Ningún resultado numérico depende de la salida del modelo. El detalle está
en `Entregables_Modulos/Modulo_5_IA_Local_RAG_Codigo/04_Ficha_Modelo.md` y
`Entregables_Modulos/Modulo_6_IA_Multimodal_3D/05_Ficha_Procedencia_Validacion.md`.

---

## 14. Bibliografía y webgrafía

- Congreso de Colombia. (2001). *Ley 697 de 2001: por la cual se fomenta el uso racional y
  eficiente de la energía*. Diario Oficial No. 44.573.
- Congreso de Colombia. (2012). *Ley 1581 de 2012: disposiciones generales para la protección de
  datos personales*. Diario Oficial No. 48.587.
- Congreso de Colombia. (2014). *Ley 1715 de 2014: integración de las energías renovables no
  convencionales al Sistema Energético Nacional*. Diario Oficial No. 49.150.
- Congreso de Colombia. (2021). *Ley 2099 de 2021: disposiciones para la transición energética*.
  Diario Oficial No. 51.731.
- Congreso de Colombia. (2023). *Ley 2294 de 2023: Plan Nacional de Desarrollo 2022–2026
  "Colombia Potencia Mundial de la Vida"*. Diario Oficial No. 52.400.
- Consejo Nacional de Política Económica y Social. (2022). *CONPES 4075 de 2022*. DNP, Bogotá D.C.
- Consejo Nacional de Política Económica y Social. (2025). *CONPES 4144: Política Nacional de
  Inteligencia Artificial*. DNP, Bogotá D.C.
- Ministerio de Minas y Energía. (2022). *Resolución PAI-PROURE 2022–2030*. Bogotá D.C.
- Ministerio de Minas y Energía. (2023). *Decreto 2236 de 2023: reglamentación de las Comunidades
  Energéticas*. Bogotá D.C.
- International Organization for Standardization. (2018). *ISO 50001:2018 — Energy management
  systems*.
- International Organization for Standardization. *ISO 14064-1*, *ISO 14040* e *ISO 14044*.
- UPME. (2024). *Resolución 001198 del 26 de diciembre de 2024: factor de emisión del SIN 2023
  para inventarios de GEI*. <https://docs.upme.gov.co/Normatividad/1198_2024.pdf>
- UPME. (2025). *Factores de emisión del SIN para el año 2023*.
  <https://docs.upme.gov.co/SIMEC/Cambio-Climatico/Documents/Calculo-FE-del-SIN/Factores_de_emision_SIN_2023.pdf>
- UPME. (2020). *Plan Energético Nacional PEN 2020-2050*. Bogotá D.C.
- Rengifo Quiñones, I. (2026). *Propuesta de Proyecto Integrador: Sistema de monitoreo, análisis y
  predicción del consumo energético en dos aulas de una institución educativa de San Andrés de
  Tumaco*. Unicomfacauca, Popayán.
- Unicomfacauca. (2026). *Diplomado en Energía Circular Inteligente 5.0*. Popayán, Cauca.

---

## Anexo A — Correspondencia con los entregables por módulo

| Módulo | Secciones de este documento | Carpeta de evidencia |
|---|---|---|
| 1. Transición energética y territorio | 1, 2 | `Entregables_Modulos/Modulo_1_Transicion_Energetica/` |
| 2. Eficiencia, medición e ISO 50001 | 3.1–3.3, 5 | `Entregables_Modulos/Modulo_2_Eficiencia_Energetica/` |
| 3. Renovables y comunidades energéticas | 3.2, 6.2–6.3 | `Entregables_Modulos/Modulo_3_Renovables_Comunidades/` |
| 4. Economía circular y carbono | 6.4–6.5 | `Entregables_Modulos/Modulo_4_Economia_Circular_Carbono/` |
| 5. IA local, RAG y código | 3.4, 7, 8, 9 | `Entregables_Modulos/Modulo_5_IA_Local_RAG_Codigo/` |
| 6. Producción multimodal y 3D | 10 | `Entregables_Modulos/Modulo_6_IA_Multimodal_3D/` |
| 7. Proyecto integrador | 11, 12, 13 | `Entregables_Modulos/Modulo_7_Proyecto_Integrador/` |

---

*Documento generado en formato Markdown para su publicación en el repositorio
`https://github.com/IsaacRengifo/Proyecto_Integrador`.*
