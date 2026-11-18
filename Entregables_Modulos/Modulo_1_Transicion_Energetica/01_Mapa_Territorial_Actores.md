# Módulo 1 — Mapa territorial y de actores

**Evidencia de aprendizaje:** Mapa territorial argumentado, matriz normativa y formulación del
problema que orientará el proyecto integrador.

## 1. Contexto territorial del caso

| Dimensión | Caracterización |
|---|---|
| **Ubicación** | San Andrés de Tumaco, Nariño. Coordenadas 1°48′24″N, 78°45′53″O. Pacífico Sur colombiano. |
| **Clima** | Tropical húmedo; temperatura media 26,7 °C (rango medido 24,0–31,1 °C), humedad relativa media 85,2 % (73,8–95,0 %). |
| **Sistema eléctrico** | Voltaje medido entre 98 y 124 V (media 110,0 V), con fluctuaciones, sobre tensiones y micro-cortes diarios. |
| **Conectividad** | Intermitencia prolongada del internet público: invalida arquitecturas IoT dependientes solo de nube. |
| **Corrosión** | Salinidad marina atmosférica acelera sulfatación de terminales: exige gabinetes IP65 y *conformal coating*. |
| **Caso seleccionado** | Institución educativa pública. Dos aulas de 48 m² (8 m × 6 m), aforo típico de 25 a 38 estudiantes. |
| **Aula 1** | HVAC Split 18 000 BTU + iluminación LED. Consumo medido: 87,81 kWh/semana. |
| **Aula 2** | Ventilación natural/ventilador 100 W + iluminación LED. Consumo medido: 10,86 kWh/semana. |

> Fuente de los valores medidos: `Prompt - Datasep/dataset_dos_aulas_tumaco.csv`, 2 016 registros,
> 2026-10-01 a 2026-10-07, intervalo de 5 min.

## 2. Mapa de actores

| Actor | Rol en el sistema | Interés / incidencia | Relación con el proyecto |
|---|---|---|---|
| **Institución educativa (directivos)** | Propietaria de la infraestructura y tomadora de decisiones | Reducir costos, cumplir meta de ahorro del 15 % en edificaciones públicas (Ley 2294/2023, art. 237) | Destinatarios del dashboard y de las recomendaciones |
| **Docentes** | Usuarios de las aulas y del sistema de climatización | Confort térmico, continuidad de la clase | Apropiación del tablero; cambio de hábitos de setpoint y apagado |
| **Estudiantes** | Ocupantes de los espacios | Bienestar, privacidad de sus datos | Conteo anónimo con sensor PIR (Ley 1581/2012); sensibilización |
| **Isaac Rengifo (estudiante investigador)** | Diseñador, instrumentador y analista | Opción de grado en Ingeniería Mecatrónica | Ejecuta medición, firmware, EDA, modelado y dashboard |
| **Unicomfacauca — Facultad de Ingeniería** | Entidad académica y garante del proceso | Formación, opción de grado, rigor técnico | Marco institucional y validación académica |
| **UPME** | Autoridad energética y administradora de incentivos | URE, medición inteligente, factores de emisión | Certificación de equipos para incentivos Ley 1715/2099; factor FE 2023 |
| **MinEnergía / DNP** | Formuladores de política pública | Transición justa, CONPES 4075 y 4144 | Marco normativo y de IA responsable |
| **Comunidad educativa y entorno (familias)** | Grupo de interés secondary | Apropiación social del conocimiento, continuidad del servicio | Receptores del producto transferible y del video de sensibilización |
| **Proveedores locales de energía y repuestos** | Contexto operativo | Disponibilidad de repuestos y servicio | Restricción de mantenimiento y disposición final de equipos |

## 3. Mapa de oportunidades energéticas priorizado (territorio caucano / Pacífico)

| # | Oportunidad | Aplicación al caso | Impacto esperado | Facilidad |
|---|---|---|---|---|
| 1 | Medición desagregada por aula con ESP32 + SCT-013 | Ya implementada: 2 nodos, buffer SD | Hace visible el 89 % del consumo que antes era invisible | Alta (ya ejecutada) |
| 2 | Optimización del setpoint del HVAC (24–25 °C) y apagado programado | Aula 1: HVAC 32,4 % del tiempo, 1 522 W.media al operar | 5–15 % del consumo del AC | Alta |
| 3 | Sellado hermético y aislamiento térmico de envolvente | Aula 1; reducir infiltración de calor | Disminución de carga térmica del compresor | Media |
| 4 | Autogeneración solar FV para autoconsumo (≈ 4,5 kWp) | Cubierta de la institución | ≈ 423 kWh/mes estimados | Media (requiere inversión) |
| 5 | Escalado a comunidad energética escolar (Decreto 2236/2023) | Todas las aulas del plantel | Gobernanza, apropiación y sostenibilidad | Media |
| 6 | Valorización de residuos electrónicos y baterías del sistema | Fin de vida de sensores y baterías | Circularidad y disposición responsable | Media |

## 4. Lectura territorial (por qué no extrapolar modelos urbanos)

- La interlección de **inestabilidad eléctrica + humedad + salinidad + mala conectividad**
  obliga a un diseño **Offline First**, distinto al de una institución urbana con red estable.
- La **carga térmica** es estructural: el aire acondicionado no es un lujo, es condición de
  habitabilidad; por eso la propuesta no plantea eliminarlo, sino **medirlo y optimizarlo**.
- El **conteo PIR anónimo** responde a la restricción ética de no capturar imágenes ni datos
  personales de menores.
- Las soluciones deben ser **escalables y de costo razonable**: se prioriza hardware de bajo costo
  (ESP32, SCT-013) frente a analizadores industriales.

## 5. Cierre del módulo

Este mapa argumentado permite formular el problema (ver `04_Formulacion_Problema.md`) y define
el alcance territorial del proyecto: **una institución educativa pública de San Andrés de
Tumaco, dos aulas,sin control físico de cargas, con enfoque de privacidad por diseño**.
