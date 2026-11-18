# Módulo 7 — Guion de sustentación final

**Duración sugerida:** 12–15 minutos + 5–10 minutos de preguntas.
**Formato:** 7 bloques alineados con la rúbrica del diplomado.

---

## Bloque 1 — Presentación del problema (2 min)

> "Buenas tardes. Mi nombre es Isaac Rengifo y presento el proyecto *Sistema de monitoreo,
> análisis y predicción del consumo energético en dos aulas de una institución educativa de
> San Andrés de Tumaco*.
>
> El problema nace de una contradicción concreta: en Tumaco hace calor —26,7 grados y 85 % de
> humedad—, así que las aulas se climatizan; pero la institución solo conocía su consumo en la
> factura general. Nadie sabía cuánto consumía el aire acondicionado, cuánto influía el aforo
> ni cuánto se gastaba de noche con las aulas vacías.
>
> Sin ese dato no se puede ahorrar, no se puede verificar la meta legal del 15 % para edificios
> públicos y no se pueden gestionar incentivos. Ese es el vacío que cerró este proyecto."

**Apoyo visual:** mapa de actores y árbol de problemas (Módulo 1).

## Bloque 2 — Línea base y medición (2 min)

> "Instalé dos nodos con ESP32 y pinzas SCT-013, sensores de temperatura, humedad y presencia,
> con un diseño *Offline First*: los datos se graban primero en una tarjeta SD y después se
> intenta enviar. Así se sobrevive a los apagones y a la falta de internet de Tumaco.
>
> En siete días registré 2 016 mediciones cada cinco minutos. El resultado: 98,67 kilovatios-hora
> por semana. El aula con aire acondicionado consume 87,81, el aula ventilada 10,86. Ocho veces
> más. El 89 % de la huella de 17,46 kilos de CO₂ equivalente por semana viene del aula climatizada."

**Apoyo visual:** tablero de EnPIs (Módulo 2) y tabla de emisiones (Módulo 4).

## Bloque 3 — La solución (2 min)

> "Con esa evidencia prioricé seis medidas. Las tres primeras no cuestan casi nada: subir el
> termostato a 24–25 grados, apagar fuera del horario lectivo y mantener filtros. Juntas pueden
> bajar entre 5 y 15 % el consumo del aire acondicionado.
>
> Después propuse autogeneración: con 4,2 horas sol pico y un rendimiento del 75 %, se necesitan
> 4,47 kilovatios pico —nueve paneles de 550 vatios, 18 metros cuadrados—. Generarían unos 468
> kilovatios-hora al mes y evitarían cerca de una tonelada de CO₂ al año. Y cerré el ciclo con
> circularidad: reutilizar los nodos para medir la generación y devolver paneles y sensores al
> fin de su vida útil."

**Apoyo visual:** cartera de medidas y pre-dimensionamiento FV (Módulos 2 y 3).

## Bloque 4 — Analítica e IA (2 min)

> "En el componente digital, Python produjo los indicadores y un modelo Random Forest que pronostica
> la demanda semanal con R cuadrado de 0,968 y error medio de 1,85 kilovatios-hora —mejor que
> persistencia, red neuronal y XGBoost—. El dashboard de diez pestañas hace visible todo esto para
> los directivos.
>
> El asistente de IA corre **localmente**: Ollama con gemma3 de mil millones de parámetros,
> AnythingLLM y una base vectorial. No hay nube. Lo probé con catorce preguntas, incluidas cuatro
> que debía rechazar: acertó las catorce. Las cifras nunca las delegué al modelo: se calculan con
> scripts verificables."

**Apoyo visual:** métricas del modelo y pantalla del dashboard (Módulo 5).

## Bloque 5 — Viabilidad y sostenibilidad (2 min)

> "La inversión estimada está entre 14,7 y 25 millones de pesos. Con el ahorro de eficiencia más
> el solar, el retorno simple va de 2,75 a 4,7 años según el escenario —incluso descontando
> mantenimiento—. No incluí los incentivos de la Ley 1715 para ser conservador; si se obtienen,
> el retorno mejora.
>
> Para que esto dure, propongo una Comunidad Energética Escolar al amparo del Decreto 2236 de
> 2023, con reglas de propiedad, operación y reinversión del ahorro. El plan de implementación
> va en cuatro fases en 24 meses."

**Apoyo visual:** evaluación financiera y plan de implementación (Módulo 7).

## Bloque 6 — Consideraciones éticas y límites (1 min)

> "Quiero ser explícito sobre los límites: usé sensores PIR anónimos, sin cámaras, en cumplimiento
> de la Ley 1581. El sistema no corta energía: es observacional. Solo medí una semana y el
> factor de emisión es promedio anual, así que la extrapolación es una estimación. Tampoco medí el
> consumo eléctrico de la propia IA. Y los activos generativos —infografía, video y modelo 3D—
> se entregan como especificaciones y guiones por las restricciones de hardware; el dashboard es
> el producto visual real y verificable. Nada de lo generado por IA se presenta como evidencia
> física."

**Apoyo visual:** ficha de procedencia (Módulo 6) y autoevaluación (Módulo 7).

## Bloque 7 — Cierre (1 min)

> "Como conclusión: medir es el primer paso. Hoy la institución sabe que su aire acondicionado
> multiplica por ocho el consumo, que puede ahorrar al menos 15 % con acciones inmediatas y que
> una solución solar es financieramente viable. El proyecto entrega datos, código, un asistente
> local y un plan para que ese conocimiento se quede en la comunidad educativa de Tumaco.
>
> Quedo atento a sus preguntas."

---

## Preguntas probables y respuestas cortas

| Pregunta | Respuesta sugerida |
|---|---|
| ¿Por qué 87,81 kWh y no 128,8 como en la monografía? | La monografía muestra valores de pre-dimensionamiento; 87,81 es el cálculo reproducible sobre el dataset medido, coincidente con el informe de huella de carbono. Ambos están documentados. |
| ¿Por qué no usó baterías? | La demanda es diurna y el plantel está conectado a la red; las baterías encarecen la solución y complican el fin de vida. Se prevén como fase 2 de la comunidad energética. |
| ¿Cómo protege la privacidad? | Conteo PIR anónimo, sin cámaras ni identificadores; Ley 1581/2012. |
| ¿El sistema controla los equipos? | No. Es 100 % observacional: no hay relés ni cortes; solo mide y visualiza. |
| ¿Qué pasa si no hay internet? | El buffer SD/SPIFFS conserva los datos y el envío se reintenta después. |
| ¿Es reproducible? | Sí: cuatro scripts y el dashboard están en el repositorio, con supuestos y unidades documentados. |
| ¿Por qué IA local y no ChatGPT? | Soberanía de datos, continuidad sin internet y trazabilidad; CONPES 4144 de 2025. |
| ¿Qué haría diferente? | Repetir la medición en otra época del año e instrumentar el consumo del puesto de cómputo. |
