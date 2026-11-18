# MONOGRAFÍA DE PROYECTO DE GRADO: SISTEMA DE MONITOREO, ANÁLISIS Y PREDICCIÓN DEL CONSUMO ENERGÉTICO EN DOS AULAS DE UNA INSTITUCIÓN EDUCATIVA DE SAN ANDRÉS DE TUMACO MEDIANTE TECNOLOGÍAS IoT E INTELIGENCIA ARTIFICIAL

## 1. Identificación del Proyecto y Resumen Ejecutivo

La presente monografía documenta la propuesta técnica y metodológica desarrollada por Isaac Rengifo Quiñones como opción de grado para el programa de Ingeniería Mecatrónica de la Corporación Universitaria Comfacauca (Unicomfacauca), en articulación con los requerimientos formativos del Diplomado en Energía Circular Inteligente 5.0. El proyecto establece un marco riguroso de ingeniería para caracterizar, analizar y predecir el comportamiento energético en la infraestructura educativa del Pacífico colombiano.

### Ficha Técnica de Identificación

El proyecto consolida la información básica de formulación en una estructura estandarizada que guía su ejecución en campo:

| Elemento Formativo | Descripción y Delimitación Técnica |
| :--- | :--- |
| **Título Oficial** | Sistema de monitoreo, análisis y predicción del consumo energético en dos aulas de una institución educativa de San Andrés de Tumaco mediante tecnologías IoT e inteligencia artificial. |
| **Autor** | Isaac Rengifo Quiñones |
| **Programa Académico** | Ingeniería Mecatrónica |
| **Enfoque de Formación** | Diplomado en Energía Circular Inteligente 5.0 |
| **Institución Universitaria** | Corporación Universitaria Comfacauca (Unicomfacauca), Popayán, Cauca – Colombia |
| **Área Temática** | Eficiencia energética, medición inteligente, Internet de las Cosas (IoT), analítica de datos e inteligencia artificial. |
| **Lugar de Ejecución** | Institución educativa oficial en el municipio de San Andrés de Tumaco, Nariño. |
| **Unidades de Análisis** | Dos aulas de clase de condiciones comparables: una sin aire acondicionado y otra dotada con sistema de aire acondicionado. |
| **Enfoque Metodológico** | Cuantitativo, observacional, comparativo, con desarrollo tecnológico de telemetría y componente predictivo de demanda. |
| **Horizontes Temporales** | Periodo de referencia continuo de 8 a 12 semanas de adquisición de datos en campo. |

### Resumen Ejecutivo

El proyecto propone el desarrollo e implementación de un sistema integral de monitoreo, análisis exploratorio y predicción del consumo de energía eléctrica en dos aulas pertenecientes a una institución educativa en el municipio de San Andrés de Tumaco, Nariño. La investigación centra su estudio en la evaluación comparativa entre un aula que no dispone de climatización artificial (dependiente de ventilación natural o asistida por ventiladores) y un aula que cuenta con un sistema de aire acondicionado. En ambos espacios se registrarán continuamente variables eléctricas, térmicas y de ocupación durante periodos de actividad académica y periodos de desocupación o receso, con el propósito de caracterizar los perfiles de demanda, comparar la estructura del consumo y estudiar la relación entre la ocupación, las condiciones ambientales y el uso del aire acondicionado.

La arquitectura de adquisición de información se fundamenta en el despliegue de medidores de energía eléctrica independientes por aula y dispositivos de comunicación basados en el microcontrolador ESP32 bajo el paradigma del Internet de las Cosas (IoT). La telemetría capturada se estructurará en una base de datos histórica persistente y procesada mediante librerías especializadas del ecosistema Python. Posteriormente, se entrenarán y evaluarán modelos de pronóstico de series temporales y algoritmos de aprendizaje automático para predecir la demanda energética semanal futura. Los resultados se integrarán en un tablero interactivo de visualización en Streamlit destinado a socializar indicadores clave de gestión y apoyar procesos institucionales de sensibilización para el uso racional y eficiente de la energía.

*Palabras clave*: consumo energético, aulas educativas, ocupación, aire acondicionado, IoT, ESP32, inteligencia artificial, predicción, eficiencia energética.

---

## 2. Planteamiento del Problema y Pregunta de Investigación

El funcionamiento cotidiano de las instituciones de educación primaria, secundaria y media requiere el suministro constante de energía eléctrica para alimentar circuitos de iluminación, sistemas de ventilación o climatización, equipamiento informático y dispositivos pedagógicos. No obstante, la magnitud, la distribución temporal y la eficiencia de esta demanda eléctrica varían sustancialmente en función de la dinámica de los horarios de clase, la densidad de ocupación por aula, la orientación solar de las edificaciones y la eficiencia nominal de las cargas instaladas.

### Diagnóstico de la Brecha Energética Institucional

En la gestión habitual de la infraestructura escolar pública, la ausencia de instrumentación eléctrica dedicada y desagregada a nivel de circuito o espacio físico genera una opacidad metrológica. La administración educativa recibe facturas globales que reflejan el consumo acumulado de todo el plantel, impidiendo identificar:

1. Los momentos u horarios del día en los cuales se registran los picos de potencia máxima.
2. El volumen de energía consumido en periodos de desocupación (noches, fines de semana y recesos escolares) debido a cargas pasivas o equipos dejados encendidos involuntariamente.
3. La proporción exacta de la demanda explicada por el funcionamiento de los sistemas de acondicionamiento de aire en comparación con la iluminación y la ventilación convencional.

En el contexto geográfico de San Andrés de Tumaco, la evaluación del consumo en espacios educativos adquiere una relevancia crítica debido a las condiciones climáticas del litoral pacífico, caracterizadas por temperaturas ambientales elevadas y altos índices de humedad relativa. Esta realidad ambiental impulsa la necesidad de instalar equipos de climatización para mantener condiciones mínimas de confort térmico en el proceso de enseñanza-aprendizaje. Sin embargo, en el análisis de ingeniería energética no debe asumirse a priori que las diferencias en la facturación o en la demanda entre dos espacios obedecen de forma exclusiva a la presencia del aire acondicionado; en dicha variabilidad intervienen factores de confusión como el volumen del aula, el tipo y cantidad de luminarias, la potencia nominal de las cargas adicionales, el aforo real y los hábitos de uso de la comunidad educativa.

### Formulación de la Pregunta de Investigación

Frente a la necesidad de disponer de información empírica desagregada y modelos de estimación robustos en el territorio, se formula la siguiente pregunta central de investigación:

> **Pregunta de Investigación**: ¿Cómo varía el consumo energético de dos aulas de una institución educativa de San Andrés de Tumaco —una sin aire acondicionado y otra con aire acondicionado— según sus condiciones de ocupación y operación, y en qué medida los datos históricos permiten predecir el consumo de semanas posteriores?

---

## 3. Justificación y Pertinencia del Estudio

La ejecución de este proyecto integrador se justifica desde una perspectiva multidimensional que abarca la ingeniería mecatrónica, la gestión energética, la educación ambiental y la pertinencia territorial en la región del Pacífico colombiano.

### Aporte Técnico e Ingeniería de Medición

Desde el componente de ingeniería, la propuesta transforma el consumo eléctrico pasivo e indeterminado en información digital medible, continua y auditable. La instalación de instrumentación dedicada permite erigir una línea base energética acorde con estándares internacionales, facilitando la detección de ineficiencias operativas y la cuantificación del consumo en vacío. La integración del microcontrolador ESP32 como nodo de telemetría IoT consolida un flujo continuo de adquisición, almacenamiento y depuración de datos que valida el uso de hardware accesible y tolerante a fallos en entornos de infraestructura vulnerable.

### Pertinencia Educativa, Social y Territorial

Desde la dimensión educativa y social, la información procesada alimenta un tablero interactivo de visualización que sirve como herramienta pedagógica. En lugar de imponer esquemas de automatización rígidos que puedan interferir con la autonomía del aula o generar rechazo institucional, el proyecto le apuesta a la sensibilización basada en datos. Al visibilizar el costo energético de dejar luces o equipos encendidos en aulas vacías, se empodera a estudiantes, docentes y directivos para adoptar patrones de consumo consciente.

En el plano territorial, el proyecto aporta evidencia directa generada en Tumaco, superando la práctica habitual de extrapolar modelos térmicos o energéticos diseñados para el interior del país que ignoran la humedad y salinidad del ambiente costero.

### Articulación con el Diplomado en Energía Circular Inteligente 5.0

La investigación se alinea de manera directa con los objetivos formativos del Diplomado en Energía Circular Inteligente 5.0 de Unicomfacauca, cumpliendo con los siguientes ejes de competencia:

* Levantamiento de líneas base energéticas y caracterización de consumos.
* Selección y definición de Indicadores de Desempeño Energético (EnPIs).
* Instrumentación física de variables eléctricas, ambientales y de ocupación.
* Desarrollo de aplicaciones orientadas al procesamiento y análisis de datos en Python.
* Documentación, validación metodológica y transferencia de productos técnicos.

---

## 4. Objetivos del Proyecto

Para dar respuesta a la pregunta de investigación y resolver la problemática planteada, se fijan los siguientes objetivos:

### 4.1 Objetivo General

Desarrollar un sistema de monitoreo, análisis y predicción del consumo energético en dos aulas de una institución educativa del municipio de San Andrés de Tumaco, mediante tecnologías IoT e inteligencia artificial, considerando las condiciones de ocupación y la utilización de aire acondicionado, con el propósito de identificar patrones de consumo, estimar la demanda energética futura y promover la conciencia sobre el uso racional y eficiente de la energía.

### 4.2 Objetivos Específicos

1. **Instrumentación**: Instrumentar dos aulas mediante dispositivos de medición eléctrica y sensores que permitan registrar variables de consumo energético, ocupación y condiciones ambientales.
2. **Adquisición Persistente**: Construir una base de datos histórica mediante la adquisición periódica de información energética, diferenciando los periodos de ocupación y desocupación de las aulas.
3. **Caracterización Comparativa**: Analizar y comparar los patrones de consumo eléctrico de las dos aulas, identificando la relación entre ocupación, condiciones ambientales y uso del aire acondicionado.
4. **Modelado Predictivo**: Desarrollar y evaluar modelos de inteligencia artificial para predecir el consumo energético de semanas posteriores a partir de los datos históricos recopilados.
5. **Visualización y Sensibilización**: Implementar un tablero de visualización que presente indicadores, comparaciones y predicciones para facilitar la interpretación de los resultados y fomentar la conciencia energética en la comunidad educativa.

---

## 5. Alcance y Delimitaciones del Estudio

La definición precisa de las fronteras del proyecto garantiza la viabilidad técnica, la rigurosidad científica y la claridad ética en la ejecución en campo.

### 5.1 Alcance del Proyecto

El marco de trabajo del proyecto abarca las siguientes fronteras operativas y analíticas:

* **Horizonte Temporal**: Monitoreo continuo de dos aulas durante un periodo de referencia de 8 a 12 semanas lectivas.
* **Variables Eléctricas**: Registro de energía activa acumulada ($kWh$), potencia activa ($W$), tensión ($V$), corriente ($A$) y factor de potencia mediante instrumentos certificados.
* **Variables de Ocupación**: Monitoreo binario de ocupación (aula ocupada / aula vacía) mediante sensores de presencia e inventario de horarios académicos y bitácoras.
* **Variables Ambientales**: Medición de temperatura ($^\circ C$) y humedad relativa ($\%$) para contextualizar el comportamiento microclimático interno.
* **Procesamiento e IA**: Estructuración de base de datos relacional/local, análisis exploratorio de datos (EDA), evaluación de modelos de pronóstico semanal y despliegue de una interfaz en Streamlit.

### 5.2 Delimitaciones Explícitas ("Fuera de Alcance")

En consonancia con la naturaleza observacional del proyecto integrador, se establecen las siguientes delimitaciones absolutas:

* **Ausencia de Control Físico**: No se automatizará ni controlará mediante relés el encendido o apagado de luminarias, ventiladores ni aire acondicionado.
* **Integridad de Instalaciones**: No se modificarán los circuitos eléctricos ni se intervendrá el funcionamiento interno de los equipos de la institución.
* **Sin Atribución Directa de Ahorro**: No se afirmará un ahorro energético atribuible a la implementación del proyecto, dado que se trata de un estudio observacional sin grupo de control ni intervención física.
* **Acotación Geográfica y Muestral**: Las conclusiones no se generalizarán a todas las escuelas de Tumaco; los resultados corresponderán a la muestra estudiada.
* **Protección de Datos**: No se utilizarán cámaras de video ni se recopilarán datos biométricos o identificadores personales de la comunidad escolar.

---

## 6. Marco de Referencia y Fundamentación Teórica

El sustento teórico del proyecto integra conceptos de gestión de energía, metrología de potencia eléctrica, arquitecturas IoT y modelos de analítica de datos.

### 6.1 Contexto Territorial de San Andrés de Tumaco

El municipio de San Andrés de Tumaco se sitúa en la subregión del Pacífico Sur del departamento de Nariño. Su posición geográfica lo expone a un clima tropical húmedo caracterizado por temperaturas elevadas y humedad relativa elevada de forma permanente. Estas condiciones imponen retos severos a la electrónica de monitoreo: la acelerada sulfatación y corrosión de terminales por salinidad marina requiere alojar los dispositivos en gabinetes estancos protegidos y aplicar barnices aislantes dieléctricos (*conformal coating*).

### 6.2 Gestión y Desempeño Energético (ISO 50001)

La gestión energética estructurada parte de la definición de la Línea Base Energética (EnB), la cual cuantifica el desempeño consumido en un periodo histórico sin modificaciones. Sobre esta base se identifican los Usos Significativos de la Energía (SEU) y se formulan Indicadores de Desempeño Energético (EnPIs) que relacionan el consumo en $kWh$ con variables explicativas como las horas lectivas o el aforo.

### 6.3 Metrología de Potencia y Energía Eléctrica

La energía activa $E$ expresada en kilovatios-hora ($kWh$) representa la integración de la potencia activa $P(t)$ en el tiempo:

$$E = \int_{t_1}^{t_2} P(t) \, dt$$

Para un sistema monofásico en corriente alterna, la potencia activa instantánea $P(t)$ se define por la relación:

$$P(t) = V_{\text{RMS}}(t) \times I_{\text{RMS}}(t) \times \cos(\phi)$$

donde $V_{\text{RMS}}$ es la tensión eficaz, $I_{\text{RMS}}$ es la corriente eficaz y $\cos(\phi)$ es el factor de potencia. Para obtener mediciones de energía con validez de ingeniería, resulta insuficiente utilizar sensores de corriente aislados; se requieren medidores o analizadores que muestreen simultáneamente la tensión y el desfase de la onda.

### 6.4 Arquitectura IoT Resiliente con ESP32

El microcontrolador ESP32 opera exclusivamente como nodo de adquisición, estampar marca temporal (*timestamp*), almacenar localmente en un *buffer* y transmitir información. Para mitigar la fragilidad de la red en Tumaco, la arquitectura implementa tolerancia a fallos: ante cortes de energía o caídas de conectividad Wi-Fi, los registros se respaldan en memoria local (microSD o SPIFFS) y se re-sincronizan automáticamente con la base de datos al restablecerse el enlace.

---

## 7. Sistema de Variables e Indicadores Energéticos

La estructuración metrológica del proyecto define un inventario riguroso de variables medidas e indicadores calculados para caracterizar ambas aulas.

### 7.1 Matriz de Variables de Entrada y Contexto

El sistema captura y procesa las siguientes diez variables fundamentales:

| Variable Registrada | Unidad de Medida / Formato | Función en el Análisis Metrológico |
| :--- | :--- | :--- |
| **Energía Activa Acumulada** | $kWh$ | Variable principal para la agregación del consumo diario y semanal. |
| **Potencia Activa** | $W$ o $kW$ | Construcción del perfil de demanda horaria y detección de picos de carga. |
| **Tensión Eléctrica** | $V_{\text{RMS}}$ | Caracterización de la calidad de suministro y cálculo de potencia activa. |
| **Corriente Eléctrica** | $A_{\text{RMS}}$ | Caracterización del consumo por circuito de iluminación o climatización. |
| **Factor de Potencia** | Adimensional ($0$ a $1$) | Evaluación del desfase entre tensión y corriente en las cargas instaladas. |
| **Estado de Ocupación** | Binario (`Ocupada` / `Vacía`) | Separación y análisis del consumo con y sin presencia de estudiantes. |
| **Aforo de Personas** | Cantidad ($N^\circ$ personas) | Normalización del consumo por densidad ocupacional (cuando sea ejecutable). |
| **Temperatura Interior** | Graduación Celsius ($^\circ C$) | Contextualización térmica y evaluación de la carga del aire acondicionado. |
| **Humedad Relativa** | Porcentaje ($\%$) | Caracterización del microclima ambiente interno. |
| **Fecha y Hora** | Marca Temporal (`YYYY-MM-DD HH:MM:SS`) | Clave primaria para la sincronización y agregación en series temporales. |

### 7.2 Indicadores de Desempeño Energético (EnPIs)

A partir de las variables registradas, se calculan seis indicadores clave de desempeño energético:

| Indicador Energético | Definición y Ecuación Matemático-Analítica |
| :--- | :--- |
| **Consumo Diario ($E_{\text{diario}}$)** | Diferencia de lecturas acumuladas: $E_{\text{diario}} = E_{\text{final\_día}} - E_{\text{inicio\_día}} \quad [kWh/\text{día}]$ |
| **Consumo Semanal ($E_{\text{semanal}}$)** | Sumatorio de consumos diarios: $E_{\text{semanal}} = \sum_{d=1}^{7} E_{\text{diario}}(d) \quad [kWh/\text{semana}]$ |
| **Potencia Promedio ($\bar{P}$)** | Valor medio de potencia activa en un intervalo $T$: $\bar{P} = \frac{1}{T} \sum_{t=1}^{T} P(t) \quad [kW]$ |
| **Consumo en Desocupación ($E_{\text{vacío}}$)** | Energía registrada en intervalos etiquetados como aula vacía: $E_{\text{vacío}} = \sum_{t \in \text{Vacío}} P(t) \cdot \Delta t \quad [kWh]$ |
| **Consumo Específico ($IE_{\text{persona}}$)** | Relación de energía por aforo acumulado: $IE = \frac{E_{\text{total}}}{\sum (N^\circ \text{personas} \times \text{Horas})} \quad [kWh/\text{persona-hora}]$ |
| **Error de Pronóstico (MAE / RMSE)** | Evaluación del desfase entre el consumo real $y_t$ y el estimado $\hat{y}_t$. |

Las ecuaciones para la evaluación del modelo predictivo se expresan matemáticamente como:

$$\text{MAE} = \frac{1}{n} \sum_{t=1}^{n} |y_t - \hat{y}_t|$$

$$\text{RMSE} = \sqrt{\frac{1}{n} \sum_{t=1}^{n} (y_t - \hat{y}_t)^2}$$

$$\text{sMAPE} = \frac{100\%}{n} \sum_{t=1}^{n} \frac{|y_t - \hat{y}_t|}{(|y_t| + |\hat{y}_t|) / 2}$$

---

## 8. Diseño Metodológico

El estudio adopta un enfoque cuantitativo de tipo observacional y comparativo, desarrollado en seis fases metodológicas secuenciales:

* **Fase 1: Reconocimiento e Inventario de Cargas**: Se tramitan las autorizaciones ante la directiva del colegio en Tumaco y se efectúa el inventario de la potencia nominal de las luminarias, ventiladores, aire acondicionado y equipos de cómputo en ambas aulas.
* **Fase 2: Instrumentación y Telemetría IoT**: Se instala un medidor eléctrico certificado por aula conectado al módulo ESP32. Los sensores ambientales (temperatura y humedad) y de presencia se posicionan en ubicaciones representativas, evitando la radiación solar directa o corrientes del aire acondicionado.
* **Fase 3: Depuración de Datos**: El pipeline en Python procesa las lecturas crudas, detecta datos faltantes, elimina registros duplicados y diferencia los cortes de energía eléctrica (donde no hay lectura) de los consumos cero legítimos.
* **Fase 4: Análisis Exploratorio Comparativo (EDA)**: Se construyen los perfiles de demanda horaria para días lectivos y fines de semana. Se evalúa el consumo en desocupación y se compara estadísticamente el peso de la climatización en el Aula 1.
* **Fase 5: Modelado Predictivo Semanal**: La variable objetivo es el consumo semanal acumulado ($kWh/\text{semana}$). Se compara un modelo base de persistencia (repetir el consumo de la semana previa) frente a modelos supervisados (*Random Forest*, *XGBoost* o *ARIMA*). La división de datos respeta estrictamente el orden cronológico (*Train/Validation/Test*) para evitar la fuga de información (*data leakage*).
* **Fase 6: Dashboard y Socialización**: Se construye una aplicación interactiva en Streamlit que presenta de forma transparente las gráficas de consumo, las comparaciones entre aulas y el módulo de consulta de pronósticos futuros.

---

## 9. Arquitectura Funcional, Recursos e Instrumentos Requeridos

El proyecto especifica las capas del sistema y los requerimientos físicos iniciales.

### 9.1 Matriz de Capas Funcionales

| Capa del Sistema | Componentes Físicos / Lógicos | Función Principal |
| :--- | :--- | :--- |
| **1. Medición Eléctrica** | Medidor de energía monofásico / analizador certificado por aula. | Capturar energía activa ($kWh$), potencia ($W$), tensión y corriente. |
| **2. Contexto Ambiental** | Sensores de presencia (PIR), temperatura/humedad (DHT22) y bitácoras. | Registrar la ocupación y las condiciones microclimáticas internas. |
| **3. Adquisición IoT** | Microcontroladores ESP32 con almacenamiento local microSD. | Leer, estampar marca de tiempo, almacenar en *buffer* y transmitir telemetría. |
| **4. Almacenamiento** | Base de datos local/servidor (CSV / SQLite / PostgreSQL). | Garantizar la persistencia e integridad histórica de los registros. |
| **5. Analítica en Python** | Entorno Python (`pandas`, `scikit-learn`, `statsmodels`). | Depurar datos, generar agregaciones, ejecutar EDA y entrenar modelos. |
| **6. Visualización** | Dashboard interactivo en Streamlit. | Presentar indicadores, comparativas y pronósticos a la comunidad. |

### 9.2 Inventario Estimado de Recursos Técnicos

| Recurso Técnico | Cantidad Estimada | Observaciones de Selección |
| :--- | :---: | :--- |
| Medidor de energía / analizador de red | 2 | Uno por aula; verificación de precisión y puertos de comunicación. |
| Medición dedicada de aire acondicionado | 1 (Opcional) | Para aislar el consumo directo del Split en el Aula 1. |
| Microcontrolador ESP32 y accesorios | 2 | Módulos de adquisición y almacenamiento temporal. |
| Sensor de ocupación (PIR) | 2 | Cobertura amplia, sin captura de imágenes ni biometría. |
| Sensor de temperatura y humedad | 2 | Ubicación estandarizada dentro de cada aula. |
| Gabinetes estancos y protecciones | Según diseño | Grado IP65 con recubrimiento dieléctrico contra humedad de Tumaco. |

---

## 10. Plan de Análisis, Gestión de Riesgos, Seguridad y Privacidad

La conducción del estudio contempla un marco riguroso de gestión de riesgos y protección ética.

### 10.1 Matriz de Riesgos y Mitigación

| Riesgo Identificado | Impacto Operativo | Estrategia de Mitigación |
| :--- | :--- | :--- |
| **Cortes eléctricos o de internet** | Pérdida de marcas de tiempo y datos. | *Buffer* de almacenamiento local en microSD y auto-sincronización. |
| **Ambiente salino y humedad** | Corrosión y fallo de sensores. | Uso de gabinetes estancos IP65 y recubrimiento *conformal coating*. |
| **Datos incompletos por fallas** | Sesgo en indicadores de consumo. | Criterios explícitos de depuración y registro en bitácoras. |
| **Poco histórico de datos** | Modelos predictivos inestables. | Uso prioritario de modelo base de referencia y reporte de incertidumbre. |

### 10.2 Consideraciones de Seguridad y Privacidad

1. **Seguridad Eléctrica**: El montaje de medidores será realizado por personal calificado bajo los lineamientos del RETIE, priorizando métodos de medición no invasivos.
2. **Habeas Data y Privacidad (Ley 1581 de 2012)**: Se garantiza que no se capturarán imágenes, audio ni identidades personales. Los datos de ocupación serán puramente numéricos o binarios.

### 10.3 Productos Finales Esperados

* Inventario técnico de cargas y fichas de caracterización de las dos aulas.
* Base de datos histórica, estructurada, anonimizada y depurada en formato CSV/SQLite.
* Informe comparativo de la línea base energética entre el aula climatizada y la no climatizada.
* Modelo predictivo de consumo semanal validado frente a un modelo base.
* Dashboard interactivo en Streamlit para visualización y sensibilización de la comunidad escolar de Tumaco.


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
