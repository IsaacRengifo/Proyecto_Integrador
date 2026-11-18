#!/usr/bin/env python3
"""
Calcula la huella de carbono del consumo electrico de las dos aulas de Tumaco.

Uso:
    python calcula_huella.py "Prompt - Datasep/dataset_dos_aulas_tumaco.csv"
    python calcula_huella.py datos.csv --factor 0.177 --intervalo-min 5 --salida resultados.csv

El dataset debe tener las columnas de potencia en vatios:
    aula1_potencia_W  -> aula con aire acondicionado
    aula2_potencia_W  -> aula con ventilacion natural

Formula:
    E_intervalo [kWh] = P [W] * (intervalo_min / 60) / 1000
    emisiones [kg CO2e] = E_total [kWh] * factor [kg CO2e/kWh]

Factor por defecto: 0.177 kg CO2e/kWh
    UPME, Resolucion 001198 de 2024, art. 2-B (factor SIN 2023 para
    inventarios de GEI o huella de carbono).
"""

from __future__ import annotations

import argparse
import csv
import os
from collections import OrderedDict

AULAS = OrderedDict(
    [
        ("Aula 1 (con aire acondicionado)", "aula1_potencia_W"),
        ("Aula 2 (ventilacion natural)", "aula2_potencia_W"),
    ]
)


def leer_potencias(ruta_csv: str, columna: str) -> list[float]:
    valores: list[float] = []
    with open(ruta_csv, newline="", encoding="utf-8-sig") as f:
        for fila in csv.DictReader(f):
            crudo = (fila.get(columna) or "").strip().replace(",", ".")
            if not crudo:
                continue
            try:
                valores.append(float(crudo))
            except ValueError:
                continue
    return valores


def main() -> int:
    parser = argparse.ArgumentParser(description="Huella de carbono del consumo electrico de dos aulas.")
    parser.add_argument("csv", help="Ruta al dataset (CSV)")
    parser.add_argument("--factor", type=float, default=0.177, help="Factor de emision en kg CO2e/kWh (default: 0.177)")
    parser.add_argument("--intervalo-min", type=float, default=5.0, help="Intervalo de muestreo en minutos (default: 5)")
    parser.add_argument("--salida", default="resultados_huella.csv", help="CSV de resultados (default: resultados_huella.csv)")
    args = parser.parse_args()

    if not os.path.isfile(args.csv):
        print(f"ERROR: no existe el archivo {args.csv}")
        return 1

    horas = args.intervalo_min / 60.0
    resultados = []
    total_kwh = 0.0

    for nombre, columna in AULAS.items():
        potencias = leer_potencias(args.csv, columna)
        if not potencias:
            print(f"AVISO: la columna {columna} esta vacia o no existe.")
            continue
        kwh = sum(potencias) * horas / 1000.0
        kg = kwh * args.factor
        total_kwh += kwh
        resultados.append((nombre, columna, len(potencias), kwh, kg))

    print()
    print("=" * 78)
    print(" HUELLA DE CARBONO - CONSUMO ELECTRICO AULAS TUMACO")
    print("=" * 78)
    print(f" Archivo        : {args.csv}")
    print(f" Factor emision : {args.factor} kg CO2e/kWh")
    print(f" Intervalo      : {args.intervalo_min} min")
    print("-" * 78)
    print(f" {'Aula':<36} {'Registros':>10} {'kWh':>10} {'kg CO2e':>10}")
    print("-" * 78)
    for nombre, _col, n, kwh, kg in resultados:
        print(f" {nombre:<36} {n:>10} {kwh:>10.2f} {kg:>10.2f}")
    print("-" * 78)
    kg_total = total_kwh * args.factor
    print(f" {'TOTAL':<36} {'':>10} {total_kwh:>10.2f} {kg_total:>10.2f}")
    print("=" * 78)

    if total_kwh > 0 and resultados:
        for nombre, _col, _n, kwh, _kg in resultados:
            print(f" Participacion {nombre}: {kwh / total_kwh * 100:.1f} %")

    with open(args.salida, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["aula", "columna", "registros", "consumo_kwh", "emisiones_kg_co2e", "factor_kg_co2e_kwh"])
        for nombre, columna, n, kwh, kg in resultados:
            w.writerow([nombre, columna, n, f"{kwh:.4f}", f"{kg:.4f}", args.factor])
        w.writerow(["TOTAL", "", "", f"{total_kwh:.4f}", f"{kg_total:.4f}", args.factor])

    print(f"\nResultados guardados en: {args.salida}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
