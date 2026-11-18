# Módulo 6 — Plan del paquete multimodal

**Evidencia exigida:** Paquete multimodal con imagen, video, modelo 3D, archivo fuente,
ficha de procedencia y criterios de validación técnica.

## 1. Estado de los activos

| Activo | Estado | Archivo | Observación |
|---|---|---|---|
| **Imagen técnica / infografía** | ⚠️ Especificada, pendiente de render | `02_Especificacion_Infografia.md` | La generación automática falló por credenciales del servicio de imágenes; se entrega el prompt exacto y los parámetros para generarla localmente |
| **Video corto de capacitación** | ✅ Guion completo | `03_Guion_Video.md` | 90 s, 6 escenas, con locución y textos |
| **Modelo 3D** | ✅ Ficha y ruta definidas | `04_Ficha_Modelo_3D.md` | Pendiente de ejecutar en TripoSR/Blender en el equipo con RTX 3050 |
| **Archivo fuente** | ✅ Incluido | Los `.md`, `.py` y este plan | Todos los entregables conservan su fuente |
| **Ficha de procedencia** | ✅ Incluida | `05_Ficha_Procedencia_Validacion.md` | Declara qué fue generado, por qué modelo y cómo se validó |

> **Nota de autenticidad:** el diplomado valora la coherencia problema→datos→decisión→evidencia,
> no la cantidad de herramientas. Entregar la especificación y el guion con datos verificados
> es preferible a un activo visual atractivo pero sin trazabilidad.

## 2. Criterios de calidad adoptados (sección 5.7 del diplomado)

1. **Utilidad sobre espectacularidad:** cada producto debe explicar, diseñar, capacitar,
   simular o documentar la solución.
2. **Datos reales:** toda cifra visible procede del dataset verificado (98,67 kWh; 17,46 kg CO₂e; R² 0,968).
3. **Procedencia explícita:** las imágenes sintéticas se identifican como tales.
4. **No suplantación:** el modelo 3D no se usa como plano de fabricación ni base de seguridad.
5. **Validación humana:** una persona revisa que el producto corresponda a la instalación real
   del caso antes de incluirlo en la sustentación.

## 3. Herramientas previstas (ruta según hardware disponible)

| Proceso | Herramienta | Ruta del diplomado | Estado en el equipo |
|---|---|---|---|
| Imagen conceptual | ComfyUI + Stable Diffusion / Stability Matrix | Intermedia (RTX 3050) | ⚠️ Requiere instalar paquetes |
| Video corto | Wan 2.1 / FFmpeg + Audacity | Intermedia/avanzada (baja resolución u offloading) | ⚠️ Diferido por RAM/GPU |
| 2D → 3D | TripoSR / Stable Fast 3D | Intermedia | ⚠️ Diferido |
| Depuración 3D | Blender / FreeCAD | Todas | ⚠️ Diferido |
| Fotogrametría | Meshroom / COLMAP | Avanzada | No aplicado al caso |
| Narración | Audacity + FFmpeg | Todas | ⚠️ Diferido |

> El equipo actual tiene 6 GB de RAM y sin GPU dedicada (ver Módulo 5). Por eso los activos
> pesados se entregan **planificados y documentados**, no renderizados. Esta decisión es
> coherente con la metodología del diplomado: tres rutas de hardware, mismas competencias.

## 4. Estructura del paquete

```
Modulo_6_IA_Multimodal_3D/
├── 01_Paquete_Multimodal_Plan.md          (este archivo)
├── 02_Especificacion_Infografia.md        (prompt + parámetros + validación)
├── 03_Guion_Video.md                      (6 escenas, 90 s)
├── 04_Ficha_Modelo_3D.md                  (ruta 2D→3D y depuración)
├── 05_Ficha_Procedencia_Validacion.md     (declaración de uso de IA)
└── infografia_sistema_tumaco.png          (pendiente de generar; ver nota)
```

## 5. Producto visual alternativo ya disponible

Mientras no se renderice la infografía generativa, el repositorio ya contiene un producto
visual **real y validado**: el dashboard interactivo de 10 pestañas
(`index.html` en la raíz y en `dashboard_ejemplo_final/`), que cumple la función de
"infografía/escena para una propuesta energética" con datos reales y interactividad.
Se recomienda usarlo en la sustentación y capturar una pantalla como evidencia.
