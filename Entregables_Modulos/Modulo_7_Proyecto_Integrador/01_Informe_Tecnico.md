# Módulo 7 — Informe técnico del proyecto integrador

**Título:** Sistema de monitoreo, análisis y predicción del consumo energético en dos aulas de
una institución educativa de San Andrés de Tumaco mediante tecnologías IoT e IA.
**Estudiante:** Isaac Rengifo Quiñones — Ingeniería Mecatrónica — Unicomfacauca.
**Modalidad:** Opción de grado en el marco del Diplomado en Energía Circular Inteligente 5.0.
**Fecha:** Noviembre de 2026.

---

## 1. Caracterización del contexto, actores, problema, alcance y restricciones

San Andrés de Tumaco (Nariño) presenta clima tropical húmedo (26,7 °C, 85 % HR), inestabilidad
eléctrica (98–124 V), micro-cortes diarios e intermitencia de internet. En una institución
educativa pública del municipio, dos aulas de 48 m² (25–38 estudiantes) eran monitoreadas solo
a nivel de factura general, sin información desagregada del impacto del aire acondicionado, el
aforo o el consumo pasivo nocturno.

**Problema:** sin línea base verificable no era posible diseñar medidas de eficiencia, reportar
ahorros creíbles ni cumplir la meta del 15 % en edificaciones públicos (Ley 2294/2023, art. 237).

**Alcance:** dos aulas, 7 días de medición (2 016 registros a 5 min), sensores eléctricos y
ambientales, enfoque 100 % observacional y anónimo. **Restricciones:** sin control de cargas,
sin cámaras (Ley 1581/2012), hardware de 6 GB RAM sin GPU y una sola semana de datos.
Detalle en `../Modulo_1_Transicion_Energetica/04_Formulacion_Problema.md`.

## 2. Línea base energética, medición e indicadores

| Indicador | Aula 1 (con AC) | Aula 2 (sin AC) |
|---|---:|---:|
| Energía semanal | 87,81 kWh | 10,86 kWh |
| Energía diaria | 12,54 kWh | 1,55 kWh |
| Potencia media / pico | 522,7 / 1 981,8 W | 64,6 / 374,5 W |
| Intensidad por área | 1,829 kWh/m²-sem | 0,226 kWh/m²-sem |
| Intensidad por persona-hora | 64,9 Wh/ph | 8,0 Wh/ph |
| Consumo fuera de horario | 3,93 kWh | 3,56 kWh |
| Emisiones alcance 2 | 15,54 kg CO₂e | 1,92 kg CO₂e |

**Total: 98,67 kWh/semana · 17,46 kg CO₂e/semana · Ratio 8,09×.**
El SEU es la climatización del Aula 1 (≈ 86 % del consumo del aula; 1 523 W al operar,
32,4 % del tiempo). Ver `../Modulo_2_Eficiencia_Energetica/01_Informe_Auditoria_Energetica.md`.

> Nota de trazabilidad: la monografía reporta valores de pre-dimensionamiento (128,8 kWh/semana
> para el Aula 1); este informe adopta los valores medidos y reproducibles (87,81 kWh), en
> coherencia con el informe de huella de carbono del repositorio.

## 3. Solución de eficiencia, renovables y circularidad

- **Eficiencia (6 medidas priorizadas):** setpoint 24–25 °C, apagado programado, mantenimiento
  de filtros, sellado térmico, autogeneración FV y comunidad energética.
  Ahorro potencial del 5–15 % del AC = 4,39–13,17 kWh/semana.
- **Renovables:** pre-dimensionamiento de **4,47 kWp** → **9 módulos de 550 W** (4,95 kWp),
  18 m², ≈ 468 kWh/mes, ≈ 1 007 kg CO₂e/año evitados (HSP 4,2, PR 0,75).
- **Circularidad:** mapa de flujos, jerarquía de valor (prevención → reducción → reutilización
  → reparación → reciclaje), ACV simplificado e indicadores de circularidad.
  Ver módulos 3 y 4.

## 4. Sistema IoT, código y analítica

- **Hardware:** ESP32 + SCT-013 + DHT22/BH1750 + PIR + SD/SPIFFS + RTC, gabinetes IP65 con
  *conformal coating*. Firmware en C++, muestreo 2 Hz, registro 5 min, *Offline First*.
- **Código:** `analisis_energetico.py` (EnPIs), `calcula_huella.py` (emisiones),
  `Modelo_Energetico.py` (FV), todos ejecutados y verificados.
- **Modelado:** Random Forest (R² = 0,968; MAE = 1,85 kWh/semana) supera a persistencia
  (0,712), MLP (0,924) y XGBoost (0,959). Variables: potencia lag, temperatura, humedad,
  aforo y horas HVAC.
- **Dashboard:** 10 pestañas con EDA, regresión MLP (R² 0,912), clasificación (91,8 % / AUC
  0,834), clustering K-Means/DBSCAN, series LSTM vs GRU y simulación IoT.

## 5. Asistente local de IA y validación

Entorno *local first*: Ollama + `gemma3:1b` (Q4) + AnythingLLM + LanceDB + embeddings
`multilingual-e5-small`, workspace `Monitoreo_Energia_Tumaco` en modo *query* (topN 2,
umbral 0,45). Corpus de 3 fichas cortas + documentos existentes. **14/14 pruebas superadas**,
incluidos 4 casos negativos que deben rechazar preguntas fuera del corpus. Las cifras nunca
se delegan al modelo: se calculan con scripts. Ver Módulo 5.

## 6. Imagen, video y modelo 3D

Paquete multimodal con infografía especificada (pendiente de render por fallo de credenciales
del servicio de imágenes), guion de video de 90 s y ficha de modelo 3D (TripoSR → Blender),
con archivos fuente y ficha de procedencia. Ver Módulo 6.

## 7. Viabilidad, riesgos y plan de implementación

Inversión FV estimada 18–25 M COP, retorno simple 4–5 años, incentivos de la Ley 1715/2099.
Riesgos: corrosión salina, variabilidad de HSP, gobernanza, capacidad del tablero y fin de vida
de equipos. Cronograma en 4 fases (formación → instrumentación → inversión → operación).
Detalle en `03_Evaluacion_Financiera.md` y `04_Plan_Implementacion.md`.

## 8. Conclusiones

1. Se instrumentó con éxito una arquitectura IoT observacional y resiliente (*Offline First*)
   en dos aulas de Tumaco, con 2 016 registros íntegros.
2. El aire acondicionado multiplica por **8,09×** el consumo y concentra el 89 % de la huella;
   el SEU es la climatización (86 % del Aula 1).
3. El modelo Random Forest alcanza R² = 0,968 y MAE = 1,85 kWh/semana, permitiendo planificar.
4. La huella es de 17,46 kg CO₂e/semana (≈ 0,91 t/año extrapolados), con reducciones
   alcanzables de 121 kg CO₂e/año por eficiencia y ≈ 1 007 kg/año por autogeneración.
5. El dashboard y el asistente RAG promueven la apropiación sin intervenir circuitos ni
   vulnerar la privacidad (Ley 1581/2012).

## 9. Recomendaciones

1. Ajustar setpoint a 24–25 °C y programar apagado fuera de 07:00–18:00.
2. Ejecutar mantenimiento quincenal de filtros y serpentines.
3. Sellar herméticamente el Aula 1 e instalar cortinas/película solar.
4. Certificar equipos de medición ante UPME para solicitar incentivos.
5. Escalar nodos IoT y constituir una Comunidad Energética Escolar (Decreto 2236/2023).
6. Instalar 9 módulos FV de 550 W con convenio de devolución al fin de vida.

## 10. Aportes transferibles

Dataset documentado · scripts reproducibles · tablero de EnPIs · cartera de medidas ·
pre-dimensionamiento FV · huella de carbono · asistente RAG con Corpus y pruebas · dashboard de
10 pestañas · informes por módulo · guion multimodal · plan de implementación.

## 11. Declaración de originalidad y uso de IA

El proyecto usa datos medidos propios y cálculos reproducibles. La IA local apoyó la redacción
y la revisión, con Declaración detallada en `../Modulo_5_IA_Local_RAG_Codigo/04_Ficha_Modelo.md`
y `../Modulo_6_IA_Multimodal_3D/05_Ficha_Procedencia_Validacion.md`. No se presentan activos
sintéticos como evidencia real.
