# Módulo 7 — Resumen ejecutivo

**Proyecto:** Monitoreo IoT e IA predictiva del consumo energético en dos aulas de Tumaco.
**Dirigido a:** Directivos de la institución educativa, Unicomfacauca y jurado del diplomado.

## El problema

En una institución educativa pública de San Andrés de Tumaco se climatizaban las aulas sin
saber cuánto costaba. El clima (26,7 °C, 85 % de humedad) obliga a usar aire acondicionado,
pero la medición solo existía en la factura general del plantel. Sin datos desagregados no era
posible ahorrar, verificar la meta legal del 15 % ni gestionar incentivos.

## Lo que se hizo

Se instalaron dos nodos **ESP32** con sensores no invasivos (SCT-013, DHT22, PIR) y almacenamiento
local SD/SPIFFS (*Offline First*) para resistir apagones y falta de internet. Durante 7 días se
registraron **2 016 mediciones cada 5 minutos**. Los datos se analizaron en Python bajo enfoque
ISO 50001 y se entrenó un modelo de Machine Learning para pronosticar la demanda semanal.

## Los hallazgos clave

| Hallazgo | Cifra |
|---|---|
| Consumo total de las dos aulas | **98,67 kWh/semana** |
| Aula 1 (con aire acondicionado) | 87,81 kWh (89 %) |
| Aula 2 (ventilación natural) | 10,86 kWh (11 %) |
| El AC multiplica el consumo | **8,09×** |
| Huella de carbono (alcance 2) | **17,46 kg CO₂e/semana** (≈ 0,91 t/año) |
| SEU principal | Climatización del Aula 1 (86 %) |
| Precisión del pronóstico | Random Forest **R² = 0,968**, MAE 1,85 kWh/sem |

## La solución propuesta

1. **Sin inversión:** subir el setpoint a 24–25 °C y apagar fuera de horario → 5–15 % de ahorro
   en el AC (hasta 13,17 kWh/semana y 121 kg CO₂e/año).
2. **Bajo costo:** mantenimiento de filtros, sellado térmico y cortinas.
3. **Con inversión:** 9 paneles solares de 550 W (4,95 kWp) → ≈ 468 kWh/mes y ≈ 1 t CO₂e
   evitada al año; retorno estimado de 4–5 años con incentivos de la Ley 1715/2099.
4. **Sostenibilidad:** Comunidad Energética Escolar (Decreto 2236/2023) para operar, mantener
   y reinvertir el ahorro.

## El valor del proyecto

- **Técnico:** arquitectura resiliente y no intervencionista, reproducible con scripts.
- **Ambiental:** línea base de carbono con el factor oficial de la UPME y escenarios de reducción.
- **Social:** dashboard de 10 pestañas y materiales de sensibilización, sin cámaras ni datos
  personales (Ley 1581/2012).
- **Formativo:** inteligencia artificial local con trazabilidad, fichas de modelo y pruebas;
  14/14 pruebas del asistente RAG superadas.

## Llamado a la acción

**Medir es el primer paso.** Se recomienda aprobar de inmediato las medidas operativas (sin
costo), gestionar la certificación de los equipos ante la UPME y programar la instalación
fotovoltaica con el acompañamiento de Unicomfacauca.

> Informe técnico completo: [`01_Informe_Tecnico.md`](01_Informe_Tecnico.md).
