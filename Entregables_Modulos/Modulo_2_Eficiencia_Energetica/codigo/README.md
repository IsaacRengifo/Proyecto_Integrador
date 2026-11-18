# Código de análisis — Módulo 2

## `analisis_energetico.py`

Script reproducible que calcula la línea base, los usos significativos de la energía y los
indicadores de desempeño energético (EnPIs) del caso Tumaco.

### Ejecución

Desde la **raíz del repositorio**:

```powershell
$env:PYTHONIOENCODING="utf-8"
python "Entregables_Modulos\Modulo_2_Eficiencia_Energetica\codigo\analisis_energetico.py"
```

Con un dataset distinto o área diferente:

```powershell
python "...\analisis_energetico.py" "ruta\al\dataset.csv" --area 48
```

### Requisitos

- Python 3.9+
- `pandas` (`pip install pandas`)

> La codificación UTF-8 de la consola solo es necesaria en Windows para que los acentos
> se impriman correctamente; no afecta los cálculos.

### Salida esperada (dataset original)

```
Energía total semana: 98.67 kWh
Aula 1 (con AC): 87.81 kWh/semana (89,0 %) | 1,829 kWh/m²-semana | 64,9 Wh/persona-h | 15,54 kg CO₂e
Aula 2 (sin AC): 10.86 kWh/semana (11,0 %) | 0,226 kWh/m²-semana |  8,0 Wh/persona-h |  1,92 kg CO₂e
Ratio Aula 1 / Aula 2: 8.09x
HVAC encendido: 32,4 % del tiempo | Potencia ON 1523 W / OFF 44 W
```

### Decisiones de cálculo

| Concepto | Decisión | Justificación |
|---|---|---|
| Energía por intervalo | `P_W × (5/60) / 1000` | El dataset reporta potencia, no energía |
| Área por aula | 48 m² (8 × 6 m) | Dato del marco geométrico de la monografía |
| Factor de emisión | 0,177 kg CO₂e/kWh | Res. UPME 001198/2024, SIN 2023 |
| Horario lectivo | 07:00–18:00 | Perfil horario observado en el dataset |
| Persona-hora | `Σ(aforo × Δt)` | Normaliza el EnPI por ocupación real |
