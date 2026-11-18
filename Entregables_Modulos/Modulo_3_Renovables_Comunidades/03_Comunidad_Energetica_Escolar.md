# Módulo 3 — Diseño conceptual de Comunidad Energética Escolar

**Marco normativo:** Decreto 2236 de 2023 (reglamentación parcial de comunidades energéticas),
Ley 1715/2014 y Ley 2099/2021 (generación distribuida y autogeneración).
**Evidencia:** Diseño conceptual con mapa de actores, reglas de operación y modelo de gobernanza.

## 1. Justificación del modelo asociativo

El escalamiento del nodo IoT a todas las aulas del plantel y la instalación del sistema
fotovoltaico de 4,95 kWp requieren algo más que equipos: necesitan **quién opera, quién paga,
quién decide y cómo se distribuyen los beneficios**. La figura de comunidad energética permite
estructurar esa sostenibilidad con base en la recomendación final de la monografía y en el
Decreto 2236 de 2023.

## 2. Mapa de actores de la comunidad energética

| Actor | Rol | Aporte | Beneficio |
|---|---|---|---|
| Institución educativa (rectoría) | Anfitriona y titular de la infraestructura | Cubierta, tableros, autorización | Ahorro en factura, cumplimiento meta Ley 2294 |
| Docentes y directivos | Usuarios y operadores primarios | Datos de operación, hábitos | Confort y tablero de indicadores |
| Estudiantes | Beneficiarios y futuros operadores | Apoyo en sensibilización y mantenimiento básico | Formación, apropiación tecnológica |
| Asociación de padres/padres de familia | Alternativa de financiación comunitaria | Aportes o gestiones de recursos | Transparencia y reducción de costos |
| Unicomfacauca | Acompañamiento técnico y validación | Conocimiento, extensión, seguimiento | Producto transferible y evidencia académica |
| UPME / MinEnergía | Registro, focalización y priorización | Marco regulatorio, incentivos | Reporte de generación distribuida |
| Proveedor local FV | Instalador y garantía | Equipos, instalación, mantenimiento | Contrato de largo plazo |

## 3. Modelo de gobernanza propuesto

```
                    Asamblea General (directivos, docentes, familias)
                                  │
                       Comité de Energía (5 personas)
                    ┌─────────────┼─────────────┐
                    ▼             ▼             ▼
              Operación      Finanzas       Comunicación
              (HVAC y        (factura y     (tablero y
               paneles)       aportes)       formación)
                    └─────────────┼─────────────┘
                                  ▼
                   Registro y reporte ante UPME
```

| Órgano | Responsabilidad | Frecuencia |
|---|---|---|
| Asamblea General | Aprobar reglas, presupuesto y reinversión de ahorros | Semestral |
| Comité de Energía | Seguir EnPIs, autorizar medidas, coordinar mantenimiento | Mensual |
| Operación | Revisar setpoints, limpieza de paneles y sensores | Quincenal |
| Finanzas | Registrar ahorro y gestionar incentivos/impuestos | Mensual |
| Comunicación | Publicar tablero y producir materiales de sensibilización | Trimestral |

## 4. Reglas de operación (borrador)

1. El sistema FV opera en **autoconsumo on-grid**; el excedente se vierte a la red según la
   regulación vigente y se registra en el medidor bidireccional.
2. El **ahorro económico** se reinvierte en: (a) mantenimiento, (b) reposición de sensores,
   (c) ampliación a nuevas aulas, en ese orden de prioridad.
3. Los **datos de ocupación** son anónimos (PIR) y nunca se usan para identificar estudiantes
   (Ley 1581/2012).
4. Toda intervención en tableros eléctricos debe ser ejecutada por personal competente; el
   equipo IoT es estrictamente observacional.
5. El tablero de indicadores es público para la comunidad educativa; las decisiones se
   documentan en actas del Comité de Energía.
6. La propiedad de los equipos se define en el acta de constitución: los módulos instalados
   en la cubierta pertenecen a la institución o a la asociación según el esquema de financiación.

## 5. Indicadores de la comunidad energética

| Indicador | Meta | Verificación |
|---|---|---|
| Cobertura de medición | 100 % de aulas del plantel en 24 meses | Nodo ESP32 por aula |
| Autoconsumo solar | ≥ 60 % de la generación consumida en sitio | Medidor bidireccional |
| Ahorro en factura | ≥ 15 % vs. línea base (Ley 2294 art. 237) | EnPI E1 |
| Participación | ≥ 2 reuniones del Comité por semestre | Actas |
| Apropiación | 1 video y 1 infografía por cohorte | Entregables Módulo 6 |
| Sostenibilidad financiera | Fondo de mantenimiento activo | Registro de ahorro reinvertido |

## 6. Riesgos de gobernanza y mitigación

| Riesgo | Mitigación |
|---|---|
| Rotación de docentes y directivos | Reglas escritas y actas; inducción anual |
| Confusión sobre la propiedad de los equipos | Acta constitutiva clara desde el inicio |
| Reparto inequitativo de beneficios | Ahorro reinvertido en el propio plantel (beneficio común) |
| Dependencia de un solo proveedor | Especificaciones abiertas y al menos 2 cotizaciones |
| Incumplimiento registral ante UPME | Designar responsable del trámite en el Comité |

## 7. Fases de implementación

| Fase | Duración | Actividad |
|---|---|---|
| 1. Formación | Mes 1–2 | Sensibilización y elección del Comité de Energía |
| 2. Instrumentación | Mes 2–4 | Replicar nodos IoT en las demás aulas (ESP32 + SCT-013) |
| 3. Inversión | Mes 4–8 | Gestión de incentivos e instalación FV |
| 4. Operación | Mes 8 en adelante | Seguimiento de EnPIs, mantenimiento y reportes |

> El detalle financiero y el cronograma consolidado se presentan en el Módulo 7.
