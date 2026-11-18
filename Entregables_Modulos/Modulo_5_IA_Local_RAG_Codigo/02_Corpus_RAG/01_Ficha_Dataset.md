# Ficha RAG — Dataset de consumo eléctrico (Tumaco)

Documento corto para el workspace `Monitoreo_Energia_Tumaco`. Toda cifra aquí aparece en
`Prompt - Datasep/dataset_dos_aulas_tumaco.csv`.

## Identificación
- Archivo: `dataset_dos_aulas_tumaco.csv` (2 016 filas, 20 columnas).
- Frecuencia: 5 minutos. Periodo: 2026-10-01 00:00 a 2026-10-07 23:55 (7 días).
- Origen: dos nodos ESP32 con sensores no invasivos SCT-013; conteo de ocupación con PIR anónimo.

## Variables principales
- `timestamp`: fecha y hora (RTC).
- `aula1_potencia_W`: potencia del aula con aire acondicionado (W). Media 522,7; máx 1 981,8.
- `aula2_potencia_W`: potencia del aula sin aire acondicionado (W). Media 64,6; máx 374,5.
- `aforo_estudiantes`: ocupación anónima (0–37, media 8).
- `temp_ambiente_C`: 24,0–31,1 °C (media 26,68).
- `humedad_relativa_pct`: 73,8–95,0 % (media 85,24).
- `voltaje_VAC`: 98–124 V (media 110,03).
- `aula1_hvac_estado`: 1 el 32,4 % del tiempo (54,4 h/semana).
- `presencia_PIR`: 1 el 31,6 % del tiempo.
- `desperdicio_global`: 1 el 19,1 % de los registros.

## Totales verificados (energía = P × 5/60 / 1000)
- Aula 1 (con AC): **87,81 kWh/semana** (89,0 %), 12,54 kWh/día.
- Aula 2 (sin AC): **10,86 kWh/semana** (11,0 %), 1,55 kWh/día.
- Total: **98,67 kWh/semana**. Ratio Aula 1 / Aula 2 = **8,09×**.
- Emisiones (FE 0,177 kg CO₂e/kWh, UPME 2023): **15,54 + 1,92 = 17,46 kg CO₂e/semana**.

## Perfil horario
- 00:00–06:00: consumo pasivo (~30–51 W en Aula 1).
- 07:00–18:00: operación lectiva; Aula 1 ≈ 1 080–1 100 W, Aula 2 ≈ 75–90 W.
- 18:00 en adelante: caída brusca a ~39 W (Aula 1).
- Fin de semana (días 3 y 4): Aula 1 cae a 1,04 y 1,02 kWh/día (sin clases).

## Correlaciones con potencia del Aula 1
- Estado HVAC: 0,992 · Presencia PIR: 0,960 · Aforo: 0,857 · Temperatura: 0,668 · Humedad: −0,572.

## Uso significativo de energía (SEU)
- Climatización del Aula 1: ≈ 86 % del consumo del aula. Potencia media HVAC encendido 1 523 W
  frente a 44 W apagado.
