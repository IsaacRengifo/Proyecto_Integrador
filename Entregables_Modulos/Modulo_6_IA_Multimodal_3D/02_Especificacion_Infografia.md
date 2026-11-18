# Módulo 6 — Especificación de la infografía técnica

**Estado:** Prompt y parámetros listos. **Pendiente:** render local (la generación automática
falló por credenciales del proveedor de imágenes; no se reintentó para no duplicar el error).

## 1. Prompt maestro (copiar tal cual)

```
Technical infographic poster in Spanish for an engineering project, clean modern educational
style, light background with soft blue, teal and orange accents, flat vector diagram aesthetic,
no photorealism. Title at top: "MONITOREO IoT E IA PREDICTIVA — AULAS DE TUMACO". Subtitle:
"Sistema observacional Offline First · San Andrés de Tumaco, Nariño · 2026". Central diagram:
an ESP32 microcontroller board connected by clean lines to sensor icons labeled "SCT-013",
"DHT22", "PIR", "BH1750", and to a microSD card icon labeled "Buffer local SD/SPIFFS", then
to an arrow labeled "MQTT/HTTP" leading to a small dashboard icon labeled "Dashboard Streamlit
/ 10 pestañas". Below, two side-by-side comparison cards. Left card in orange tones:
"AULA 1 — CON AIRE ACONDICIONADO", "87,81 kWh/semana", "15,54 kg CO2e", "89 % del consumo",
"HVAC Split 18.000 BTU". Right card in teal tones: "AULA 2 — VENTILACIÓN NATURAL",
"10,86 kWh/semana", "1,92 kg CO2e", "11 % del consumo", "Ventilador 100 W". Bottom banner with
three metric chips: "2.016 registros · 5 min", "Ratio 8,1x", "Random Forest R² = 0,968".
Small footer text: "Datos reales · ISO 50001 · Privacidad por diseño · Diplomado en Energía
Circular Inteligente 5.0 — Unicomfacauca". All text must be crisp, correctly spelled in
Spanish, with clear hierarchy and generous whitespace. Professional academic infographic,
16:9 landscape composition.
```

## 2. Parámetros sugeridos (ComfyUI / Stability Matrix)

| Parámetro | Valor recomendado | Justificación |
|---|---|---|
| Resolución | 1344 × 768 (16:9) | Compatible con RTX 3050 (4 GB) usando tiled VAE si hace falta |
| Sampling steps | 25–30 | Equilibrio calidad/tiempo |
| CFG scale | 6,5–7,5 | Evita saturación de colores |
| Semilla | Fijar (p. ej. 20261001) | Reproducibilidad: conservar en la ficha |
| Modelo | SD 1.5 / SDXL ligero cuantizado | Según memoria disponible |
| Control | ControlNet (opcional) con layout de 3 bloques | Asegura la jerarquía título-diagrama-tarjetas |
| Postproceso | Corrección manual de textos en Blender/Inkscape | Los modelos suelen deformar letras: **validación humana obligatoria** |

## 3. Textos que deben aparecer (verificación literal)

| Zona | Texto | Fuente del dato |
|---|---|---|
| Título | MONITOREO IoT E IA PREDICTIVA — AULAS DE TUMACO | Título de la monografía |
| Subtítulo | Sistema observacional Offline First · San Andrés de Tumaco, Nariño · 2026 | Resumen y marco geográfico |
| Nodos | ESP32 · SCT-013 · DHT22 · PIR · BH1750 · SD/SPIFFS · MQTT/HTTP | Arquitectura IoT |
| Tarjeta izquierda | Aula 1 · 87,81 kWh/semana · 15,54 kg CO₂e · 89 % · HVAC 18 000 BTU | Dataset + huella de carbono |
| Tarjeta derecha | Aula 2 · 10,86 kWh/semana · 1,92 kg CO₂e · 11 % · Ventilador 100 W | Dataset + huella de carbono |
| Chips inferiores | 2.016 registros · 5 min · Ratio 8,1x · Random Forest R² = 0,968 | EDA y modelado |
| Pie | Datos reales · ISO 50001 · Privacidad por diseño · Unicomfacauca | Marco normativo |

## 4. Criterios de validación técnica

| Criterio | Cómo verificarlo |
|---|---|
| Cifras correctas | Comparar cada número con `Modulo_2/04_Tablero_Indicadores_EnPIs.md` |
| Unidades correctas | kWh/semana, kg CO₂e, W, % — sin mezclar BTU con julios |
| Arquitectura fiel | El diagrama muestra **buffer local antes de la transmisión** (Offline First) |
| Sin control de cargas | No aparecen relés ni interruptores: es sistema observacional |
| Privacidad | El sensor de presencia es PIR (ánonimo), no una cámara |
| Transparencia | PIE de imagen identifica que es una representación sintética con datos reales |
| Legibilidad | Textos corregidos manualmente; ninguna palabra deformada |

## 5. Alternativa sin IA generativa (recomendada si no hay GPU)

Si no se dispone de RTX 3050, producir la infografía con **Plotly + HTML** (ya dominado en el
dashboard) o con Inkscape a partir de los datos del Módulo 2. Esto cumple el mismo propósito
formativo con **trazabilidad total**, y coincide con la recomendación del diplomado de no
premiar la cantidad de herramientas sino la coherencia de la evidencia.

## 6. Registro del intento de generación automática

| Campo | Valor |
|---|---|
| Fecha | Noviembre de 2026 |
| Herramienta intentada | Servicio de generación de imágenes del entorno de trabajo |
| Resultado | Error `Invalid credential` |
| Acción tomada | No se reintentó; se entrega esta especificación para ejecución local |
| Impacto en la evidencia | Ninguno: el paquete conserva archivo fuente, prompt, parámetros y validación |
