# Módulo 3 — Esquema de operación y propuesta de sostenibilidad

**Evidencia:** Esquema de operación y propuesta de sostenibilidad para la solución renovable/comunitaria.

## 1. Principios de sostenibilidad aplicados

1. **Eficiencia primero:** no se dimensiona generación hasta agotar medidas operativas de bajo
   costo (Módulo 2, medidas M1–M4).
2. **Tecnología apropiada:** ESP32 y sensores SCT-013 de bajo costo, reparables localmente.
3. **Datos propios:** arquitectura *Offline First* y procesamiento local; no dependencia de nube.
4. **Gobernanza antes que hardware:** reglas de operación definidas antes de instalar paneles.
5. **Ciclo de vida completo:** disposición y reciclaje considerados desde el diseño (Módulo 4).

## 2. Esquema de operación del sistema híbrido (medición + generación)

| Elemento | Estado | Responsable | Frecuencia / lógica |
|---|---|---|---|
| Nodo ESP32 Aula 1/Aula 2 | Operativo | Estudiante / Comité | Muestreo 2 Hz, registro SD cada 5 min |
| Buffer SD/SPIFFS | Operativo | Sistema automático | Escritura local antes de transmisión |
| Envío MQTT/HTTP | Diferido | Sistema automático | Reintento cuando hay conectividad |
| HVAC Aula 1 | Observado, sin control | Docente / Comité | Setpoint 24–25 °C, apagado 18:00 |
| Paneles FV 4,95 kWp | Propuesto | Operación del Comité | Limpieza bimestral por salinidad |
| Inversor 5 kW on-grid | Propuesto | Proveedor + Comité | Revisión anual |
| Medidor bidireccional | Propuesto | Comité / UPME | Lectura mensual |
| Dashboard de EnPIs | Operativo | Comunicación | Actualización semanal |

## 3. Modelo financiero de sostenibilidad

| Concepto | Valor | Detalle |
|---|---:|---|
| Inversión inicial estimada | 18–25 M COP | 9 módulos, inversor, estructura, instalación |
| Ahorro por autoconsumo | ≈ 4,8 M COP/año | 5 600 kWh/año × 850 COP/kWh |
| Ahorro por eficiencia (M1–M4) | ≈ 0,6 M COP/año | 13,17 kWh/semana × 52 × 850 COP |
| Incentivo tributario potencial | Hasta 50 % deducción renta | Ley 1715/2099, previa certificación UPME |
| Exclusión de IVA y arancel | Aplicable a equipos | Ley 1715/2099 |
| Retorno simple estimado | 4–5 años | Sin considerar incentivos; mejora con ellos |
| Vida útil del sistema | 25 años | Módulos FV; inversor ~10 años |

**Estrategia de financiación escalonada:**

1. **Etapa 1 (sin inversión):** medidas operativas M1–M4 → ahorro inmediato ≈ 0,6 M COP/año.
2. **Etapa 2 (bajo costo):** réplica de nodos IoT a otras aulas (~1 M COP por nodo).
3. **Etapa 3 (inversión):** sistema FV con recursos propios, aportes de la asociación de padres
   o convocatorias públicas, más incentivos tributarios.

## 4. Plan de mantenimiento y reposición

| Activo | Acción | Frecuencia | Responsable | Costo estimado |
|---|---|---|---|---|
| Sensores SCT-013 | Verificación de offset | Semestral | Comité | Bajo |
| ESP32 y SD | Revisión de logs y espacio | Mensual | Operación | Bajo |
| Paneles FV | Limpieza por salinidad | Bimestral | Operación | Bajo |
| Inversor | Revisión eléctrica | Anual | Proveedor | Medio |
| Batería RTC | Reemplazo | Cada 2–3 años | Comité | Bajo |
| Módulos FV | Inspección de degradación | Anual | Proveedor | — |

## 5. Gestión del fin de vida (circularidad)

- Los módulos FV al final de su vida útil (≈ 25 años) se devuelven al fabricante o a un
  gestor autorizado mediante convenio incluido en el contrato de compra.
- Las baterías y sensores se clasifican como **residuos de aparatos eléctricos y electrónicos
  (RAEE)** y se entregan a puntos de recolección autorizados.
- Se conserva la trazabilidad de cada componente (ficha, serial, fecha de instalación) para
  facilitar la valorización (ver Módulo 4).

## 6. Indicadores de sostenibilidad del sistema

| Indicador | Meta | Cómo se mide |
|---|---|---|
| Disponibilidad del nodo IoT | ≥ 95 % | Registros válidos / registros esperados |
| Integridad de datos ante apagón | 100 % | Comparación buffer SD vs. serie temporal |
| Autoconsumo solar | ≥ 60 % | Generación consumida / generación total |
| Ahorro acumulado | ≥ 15 % vs. línea base | EnPI E1 del Módulo 2 |
| Costo de mantenimiento anual | < 3 % de la inversión | Registro de Finanzas |
| Componentes con fin de vida trazado | 100 % | Fichas de activos |

## 7. Conclusión del módulo

La solución renovable propuesta es **técnicamente viable** (9 módulos cubren la demanda en
el escenario pesimista), **económicamente razonable** (retorno 4–5 años) y **socialmente
sostenible** si se constituye la Comunidad Energética Escolar con reglas claras y una
estrategia de reinversión del ahorro. La ausencia de baterías en la primera etapa reduce el
costo y simplifica la gestión de residuos, sin comprometer la continuidad porque la demanda
es diurna y el plantel permanece conectado a la red.
