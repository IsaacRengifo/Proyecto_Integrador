# Cómo subir la huella de carbono a GitHub

Repositorio: <https://github.com/isaacrengifo/Proyecto_Integrador>

## Paso 1 — Abrir el repo

Entra a <https://github.com/isaacrengifo/Proyecto_Integrador> con tu cuenta.
Debes tener permiso de escritura (eres el dueño o colaborador).

## Paso 2 — Subir la carpeta

1. Pulsa **Add file → Upload files**.
2. Abre el Explorador de Windows en:

   `C:\Users\USUARIO\Documents\Proyecto predeterminado\`

3. **Arrastra la carpeta `huella_carbono` completa** a la zona de carga de GitHub.
   (Arrastrar la carpeta conserva la ruta `huella_carbono/...`. Si arrastras solo los
   archivos sueltos, quedarán en la raíz del repo.)

   La carpeta contiene:

   | Archivo | Qué es |
   |---|---|
   | `HUELLA_CARBONO.md` | Informe completo con metodología, resultados y referencias |
   | `calcula_huella.py` | Script reproducible (solo Python estándar) |
   | `resultados_huella.csv` | Resultados del cálculo |
   | `dataset_dos_aulas_tumaco.csv` | Datos usados (para que el cálculo sea reproducible) |

4. Espera a que aparezcan los 4 archivos en la lista.

## Paso 3 — Confirmar

1. En **Commit changes** escribe:

   ```
   Agrega cálculo de huella de carbono (factor UPME 2023)
   ```

2. Pulsa **Commit changes**.

Listo. En unos segundos verás la carpeta en el repo.

---

## Paso 4 (opcional) — Enlazarlo desde el README

Abre `README.md` en GitHub → icono del lápiz → pega este bloque después de
"Resultados principales":

```markdown
## Huella de carbono

El consumo eléctrico de la semana analizada (98,67 kWh) equivale a **17,46 kg CO₂e**,
aplicando el factor de emisión del SIN 2023 de la UPME (0,177 kg CO₂e/kWh,
Resolución 001198 de 2024). El aula con aire acondicionado concentra el **89 %** de esas
emisiones (15,54 kg CO₂e).

📄 Informe completo y script reproducible: [`huella_carbono/`](huella_carbono/HUELLA_CARBONO.md)
```

→ **Commit changes**.

---

## Nota sobre lo que había en AnythingLLM

La respuesta del chat de AnythingLLM **no era un documento válido**: mezclaba BTU con
julios, multiplicaba BTU/día por horas y meses sin convertir unidades, y el YAML apuntaba
a `/ruta/al/archivo/datos_energia_aula.csv` (una ruta de ejemplo). Por eso se reemplazó
por este cálculo, hecho con el dataset real y el factor oficial de la UPME.
