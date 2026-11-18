# Entregables por módulo — Diplomado en Energía Circular Inteligente 5.0

**Proyecto:** Sistema de monitoreo, análisis y predicción del consumo energético en dos aulas
de una institución educativa de San Andrés de Tumaco mediante tecnologías IoT e IA.
**Estudiante:** Isaac Rengifo Quiñones — Unicomfacauca — Popayán, Cauca, 2026.

Este conjunto de carpetas organiza la **evidencia de aprendizaje** exigida en el documento
_del diplomado_ para cada uno de los siete módulos, aplicada al caso real del proyecto integrador.

---

## Estructura

| Carpeta | Módulo | Evidencia de aprendizzaje del diplomado | Entregables incluidos |
|---|---|---|---|
| [`Modulo_1_Transicion_Energetica/`](Modulo_1_Transicion_Energetica/) | Transición energética, política pública y contexto territorial | Mapa territorial argumentado, matriz normativa y formulación del problema | Mapa de actores, matriz normativa, árbol de problemas, formulación del problema |
| [`Modulo_2_Eficiencia_Energetica/`](Modulo_2_Eficiencia_Energetica/) | Eficiencia energética, medición e ISO 50001 | Informe de auditoría, dataset documentado, código, tablero de indicadores y cartera de medidas | Informe, diccionario de datos, script Python, EnPIs, cartera priorizada |
| [`Modulo_3_Renovables_Comunidades/`](Modulo_3_Renovables_Comunidades/) | Renovables, almacenamiento y comunidades energéticas | Pre-dimensionamiento, modelo energético, esquema de operación y sostenibilidad | Pre-dimensionamiento FV, modelo Python, propuesta de comunidad energética escolar |
| [`Modulo_4_Economia_Circular_Carbono/`](Modulo_4_Economia_Circular_Carbono/) | Economía circular, ciclo de vida y gestión de carbono | Mapa circular, ACV simplificada, huella de carbono y modelo de intervención | Mapa de circularidad, ACV, huella de carbono, indicadores de circularidad |
| [`Modulo_5_IA_Local_RAG_Codigo/`](Modulo_5_IA_Local_RAG_Codigo/) | IA local, datos, RAG y código | Asistente RAG, código, pruebas, ficha técnica y reporte de recursos | Configuración, corpus RAG, pruebas, ficha de modelo, reporte de recursos |
| [`Modulo_6_IA_Multimodal_3D/`](Modulo_6_IA_Multimodal_3D/) | IA generativa multimodal, video, 2D a 3D y gemelos digitales | Paquete multimodal, ficha de procedencia y validación | Infografía, guion de video, ficha de modelo 3D, procedencia y validación |
| [`Modulo_7_Proyecto_Integrador/`](Modulo_7_Proyecto_Integrador/) | Proyecto integrador | Informe técnico, resumen ejecutivo, viabilidad, repositorio y sustentación | Informe, resumen, evaluación financiera, plan de implementación, rúbrica, guion de sustentación |

---

## Notas sobre trazabilidad y coherencia de datos

1. ** Fuente primaria de datos.** Todos los cálculos se reproducen desde
   `Prompt - Datasep/dataset_dos_aulas_tumaco.csv` (2 016 registros, 5 minutos,
   2026-10-01 a 2026-10-07). Los valores verificados son:
   - Aula 1 (con AC): **87,81 kWh/semana** → **15,54 kg CO₂e/semana**.
   - Aula 2 (sin AC): **10,86 kWh/semana** → **1,92 kg CO₂e/semana**.
   - Total: **98,67 kWh/semana** → **17,46 kg CO₂e/semana**. Factor UPME 2023: 0,177 kg CO₂e/kWh.

2. ** Diferencia con la monografía.** La Tabla 2 de `Proyecto_Integrador_Final.pdf`
   reporta 128,8 kWh/semana (Aula 1) y 25,2 kWh/semana (Aula 2) como valores de
   **diseño/pre-dimensionamiento**. Los entregables usan los valores **medidos y
   reproducibles** del dataset (98,67 kWh combinados), que coinciden con
   `huella_carbono/HUELLA_CARBONO.md`. Esta diferencia se documenta explícitamente
   en el Módulo 2 para cumplir el criterio de trazabilidad del diplomado.

3. ** IA responsable.** Los productos generados con IA conservan su ficha de
   procedencia, parámetros esenciales y validación humana, conforme al criterio de
   autenticidad del diplomado (sección 5.8 y 6.2 del documento rector).

4. ** Reproducibilidad.** Los scripts incluidos usan Python 3.9+ y bibliotecas
   estándar/pandas. Para ejecutarlos desde la raíz del repositorio:

   ```powershell
   python Entregables_Modulos\Modulo_2_Eficiencia_Energetica\codigo\analisis_energetico.py
   ```

---

## Cómo subirlo a GitHub (arrastrar y soltar)

1. Entra a <https://github.com/IsaacRengifo/Proyecto_Integrador>.
2. Pulsa **Add file → Upload files**.
3. Arrastra la carpeta **`Entregables_Modulos`** completa (no los archivos sueltos).
4. En *Commit changes* escribe: `Agrega entregables por módulo del diplomado`.
5. Pulsa **Commit changes**.

> Si lo subes como ZIP, descomprímelo primero: GitHub no descomprime archivos al cargarlos.
