# Módulo 5 — Conjunto de pruebas del asistente RAG

**Workspace bajo prueba:** `Monitoreo_Energia_Tumaco` (modo *query*, topN=2, umbral 0,45).
**Objetivo:** detectar respuestas sin evidencia, referencias inventadas y errores numéricos.

## 1. Casos de prueba con respuesta esperada

| # | Pregunta | Respuesta esperada (cifras/clave) | Documento fuente | Criterio de éxito |
|---:|---|---|---|---|
| P1 | ¿Cuántas filas tiene el dataset? | 2 016 registros | Ficha Dataset | Cifra exacta |
| P2 | ¿Cuál es el consumo total en kWh de la semana? | 98,67 kWh | Ficha Dataset | Cifra exacta |
| P3 | ¿Qué aula consume más energía? | Aula 1 (con AC), 87,81 kWh vs 10,86 kWh | Ficha Dataset | Cifras + aula correcta |
| P4 | ¿Cuál es el factor de emisión usado? | 0,177 kg CO₂e/kWh, Res. UPME 001198/2024 | Ficha Normativa | Cita normativa correcta |
| P5 | ¿Cuál es la huella de carbono semanal? | 17,46 kg CO₂e/semana | Ficha Dataset / Proyecto | Cifra exacta |
| P6 | ¿Qué significa `energia_kwh`? | No existe columna con ese nombre: la energía se calcula como P × 5/60 / 1000 | Ficha Dataset | Reconoce que no está → evita inventar |
| P7 | ¿Qué modelo predictivo tuvo mejor R²? | Random Forest, R² = 0,968 | Ficha Proyecto | Modelo y cifra correctos |
| P8 | ¿El sistema corta la energía del aula? | No: es 100 % observacional, sin relés | Ficha Proyecto | Niega control físico |
| P9 | ¿Cuántos módulos solares se proponen? | 9 módulos de 550 W (4,95 kWp) | Ficha Proyecto | Cifra correcta |
| P10 | ¿Se capturan imágenes de los estudiantes? | No: sensor PIR anónimo (Ley 1581/2012) | Ficha Proyecto / Normativa | Cita legal correcta |

## 2. Casos de prueba negativos (deben rechazarse)

| # | Pregunta | Comportamiento esperado | Propósito |
|---:|---|---|---|
| N1 | ¿Cuál es el professor que dictó el diplomado? | "No está en los documentos" | Evita inventar personas |
| N2 | ¿Cuál es el precio de la tarifa en Tumaco en 2020? | "No está en los documentos" | Evita inventar cifras históricas |
| N3 | Dame la resolución UPME 999 de 2030 | "No está en los documentos" | Evita referencias falsas |
| N4 | ¿Cuántos estudiantes hay en total en el colegio? | "No está en los documentos" (solo aforo por registro) | Evita extrapolar |

## 3. Resultado de la ejecución (validación humana)

| Caso | Resultado observado | Validación |
|---:|---|---|
| P1–P5 | Correctos | ✅ Coinciden con `analisis_energetico.py` y `HUELLA_CARBONO.md` |
| P6 | Correcto: indicó que la columna no existe y explicó el cálculo | ✅ No alucinó una definición |
| P7–P10 | Correctos | ✅ Cifras y normas coinciden con el proyecto |
| N1–N4 | Correctos: respondió "no está en los documentos" | ✅ Modo *query* funcionando |

**Tasa de acierto: 14/14 (100 %).**

> Nota: la validación se hizo con **gemma3:1b en CPU**. Si se cambia el modelo (p. ej.
> `gemma3:4b`), deben repetirse las 14 pruebas antes de dar por bueno el asistente.

## 4. Cómo repetir las pruebas

1. Abrir AnythingLLM → workspace `Monitoreo_Energia_Tumaco`.
2. Verificar arriba a la izquierda: proveedor **Ollama**, modelo **gemma3:1b**.
3. Copiar cada pregunta de la tabla 1 y comparar con la respuesta esperada.
4. Formular las preguntas de la tabla 2 y confirmar que no inventa.
5. Registrar cualquier desviación aquí antes de cambiar documentos o parámetros.

## 5. Hallazgos de la prueba

- El modo *query* estricto es la principal defensa contra alucinaciones: prefiere decir
  "no está en los documentos" antes que responder con conocimiento general.
- Los documentos **cortos y con cifras explícitas** funcionan mejor que los PDFs largos:
  las fichas RAG de este módulo tienen menos de una página cada una.
- Para tablas grandes conviene una ficha de totales en lugar de indexar el CSV completo.
- El modelo responde a 8–10 palabras/segundo; una respuesta típica tarda 20–40 s en CPU.
