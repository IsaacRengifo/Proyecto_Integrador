# Módulo 6 — Ficha del modelo 3D (ruta 2D → 3D y depuración)

**Estado:** Ruta definida y documentada; pendiente de ejecutar en estación con RTX 3050.
**No usar como plano de fabricación ni base de seguridad** (sección 5.7 del diplomado).

## 1. Objetivo del activo 3D

Representar de forma comprensible el **nodo de adquisición IoT** instalado en cada aula:
gabinete IP65 con ESP32, pinza SCT-013, tarjeta SD y sensores. El modelo apoya la
capacitación de mantenimiento y la comunicación del proyecto; no sustituye planos eléctricos.

## 2. Dos rutas complementarias (según el diplomado)

| Ruta | Herramienta | Entrada | Salida | Cuando usarla |
|---|---|---|---|---|
| **A — Reconstrucción generativa** | TripoSR / Stable Fast 3D (Hunyuan3D en modo baja memoria si hay servidor) | 1 fotografía del gabinete | Malla GLB/OBJ | Rápida, ideal para una sola imagen disponible |
| **B — Fotogrametría** | Meshroom / COLMAP | 15–25 fotografías multivista | Nube de puntos → malla | Cuando se requiera fidelidad dimensional del espacio |

> Para el caso se recomienda la **Ruta A** por disponibilidad de una sola fotografía del
> equipo y por las restricciones de hardware. La Ruta B queda como opción de extensión.

## 3. Parámetros de la Ruta A (TripoSR)

| Parámetro | Valor sugerido | Nota |
|---|---|---|
| Resolución de entrada | 512 × 512 px | Foto del gabinete con fondo neutro y buena luz |
| Semilla | Fijar y registrar | Reproducibilidad |
| Formato de salida | `.glb` (texturas incrustadas) | Fácil de importar en Blender y web |
| Preproceso | Recorte y corrección de perspectiva | Mejora la reconstrucción |
| Postproceso | Escala real, malla limpia, texturas PBR | En Blender |

## 4. Depuración en Blender (pasos obligatorios)

1. Importar `.glb` y verificar escala: gabinete ≈ 20 × 15 × 10 cm (referencia del montaje real).
2. Aplicar transformaciones y corregir normales; eliminar caras sueltas.
3. Simplificar malla (Decimate) manteniendo las formas reconocibles.
4. Ajustar materiales PBR: plástico IP65 gris, conector negro, etiqueta con texto legible.
5. Configurar iluminación neutra y cámara ortográfica para la imagen de presentación.
6. (Opcional) Animación simple: giro 360° para el video del Módulo 6.
7. Exportar: `nodo_iot_tumaco.glb` para web/AR y `nodo_iot_tumaco.blend` como archivo fuente.

## 5. Gemelo digital simplificado (integración con datos)

El diplomado pide integrar **un indicador o dato de sensor** en un gemelo digital simplificado:

| Elemento del modelo | Dato vinculado | Origen | Visualización |
|---|---|---|---|
| Barra LED sobre el ESP32 | Estado `presencia_PIR` (0/1) | Dataset | Se enciende cuando hay presencia |
| Icono de tarjeta SD | Nº de registros buffer | 2 016 registros | Contador animado |
| Pinza SCT-013 | Potencia activa (W) | Dataset | Aguja/barra con valor instantáneo |
| Etiqueta del aula | kWh/semana | Módulo 2 | Texto 87,81 / 10,86 kWh |

> Implementación sugerida: exportar el GLB y mostrarlo en el dashboard con Three.js,
> actualizando los valores desde el mismo dataset. Esto cierra el ciclo dato → modelo →
> comunicación exigido por el módulo.

## 6. Validación técnica

| Criterio | Cómo verificarlo |
|---|---|
| Escala plausible | Comparar con las dimensiones reales del gabinete IP65 |
| Topología limpia | Sin mallas no manifold evidentes; normales correctas |
| Texturas legibles | Etiqueta y conectores reconocibles en render |
| No engaña | Se declara que es una reconstrucción generativa, no un plano técnico |
| Archivo fuente conservado | `.blend` + `.glb` + foto de entrada en el repositorio |
| Licencias | Modelo y texturas con licencia de uso verificada (ficha `05_Ficha_Procedencia_Validacion.md`) |

## 7. Exportaciones previstas

| Archivo | Uso |
|---|---|
| `nodo_iot_tumaco.blend` | Archivo fuente editable |
| `nodo_iot_tumaco.glb` | Web / realidad aumentada / presentación |
| `nodo_iot_tumaco.stl` | Impresión 3D (maqueta didáctica, no pieza funcional) |
| `render_nodo_iot.png` | Imagen para el informe y la infografía |

## 8. Estado actual

No se ha ejecutado la reconstrucción: el entorno de trabajo cuenta con 6 GB de RAM y sin GPU
dedicada (ruta básica). La ficha conserva todos los parámetros y pasos para ejecutarla en la
ruta intermedia (RTX 3050) del diplomado, sin perder trazabilidad.
