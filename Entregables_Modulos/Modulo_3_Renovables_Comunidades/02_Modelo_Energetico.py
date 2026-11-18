#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Modelo energético reproducible — Pre-dimensionamiento FV (Módulo 3).

Estima la potencia pico requerida, el número de módulos, el área y la generación
mensual a partir de la línea base medida del caso Tumaco.

Uso (desde la raíz del repositorio):
    python "Entregables_Modulos\\Modulo_3_Renovables_Comunidades\\02_Modelo_Energetico.py"

Requisitos: Python 3.9+ y pandas.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

RUTA = Path("Prompt - Datasep/dataset_dos_aulas_tumaco.csv")


def linea_base(ruta: Path) -> float:
    """Energía diaria promedio (kWh/día) a partir de potencia instantánea a 5 min."""
    df = pd.read_csv(ruta, parse_dates=["timestamp"])
    dt_h = 5 / 60
    kwh = (df["aula1_potencia_W"] + df["aula2_potencia_W"]) * dt_h / 1000
    dias = df["timestamp"].dt.date.nunique()
    return float(kwh.sum() / dias)


def dimensionar(e_diaria: float, hsp: float, pr: float,
                 w_modulo: int = 550, area_modulo: float = 2.0) -> dict:
    pico_kwp = e_diaria / (hsp * pr)
    n_modulos = int(-(-pico_kwp * 1000 // w_modulo))  # techo
    pico_instalado = n_modulos * w_modulo / 1000
    return {
        "e_diaria": e_diaria,
        "hsp": hsp,
        "pr": pr,
        "pico_requerido_kwp": pico_kwp,
        "n_modulos": n_modulos,
        "pico_instalado_kwp": pico_instalado,
        "area_m2": n_modulos * area_modulo,
        "generacion_mensual_kwh": pico_kwp * hsp * pr * 30,
        "generacion_mensual_instalada_kwh": pico_instalado * hsp * pr * 30,
        "co2_evitado_anual_kg": pico_instalado * hsp * pr * 365 * 0.177,
    }


def imprimir(r: dict) -> None:
    print("=" * 62)
    print("PRE-DIMENSIONAMIENTO FOTOVOLTAICO — CASO TUMACO")
    print("=" * 62)
    print(f"Demanda diaria (línea base):     {r['e_diaria']:8.2f} kWh/día")
    print(f"HSP asumido:                     {r['hsp']:8.2f} kWh/m²/día")
    print(f"Performance Ratio:               {r['pr']:8.2f}")
    print("-" * 62)
    print(f"Potencia pico requerida:         {r['pico_requerido_kwp']:8.2f} kWp")
    print(f"Módulos de 550 W:                {r['n_modulos']:8d} unidades")
    print(f"Potencia instalada:              {r['pico_instalado_kwp']:8.2f} kWp")
    print(f"Área requerida:                  {r['area_m2']:8.1f} m²")
    print(f"Generación mensual (requerida):  {r['generacion_mensual_kwh']:8.0f} kWh")
    print(f"Generación mensual (instalada):  {r['generacion_mensual_instalada_kwh']:8.0f} kWh")
    print(f"CO₂e evitado anual:              {r['co2_evitado_anual_kg']:8.0f} kg/año")
    print("=" * 62)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("ruta", nargs="?", type=Path, default=RUTA)
    ap.add_argument("--hsp", type=float, default=4.2)
    ap.add_argument("--pr", type=float, default=0.75)
    args = ap.parse_args()
    if not args.ruta.exists():
        raise SystemExit(f"No se encontró el dataset: {args.ruta}")
    imprimir(dimensionar(linea_base(args.ruta), args.hsp, args.pr))


if __name__ == "__main__":
    main()
