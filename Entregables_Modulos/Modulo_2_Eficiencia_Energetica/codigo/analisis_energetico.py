#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Análisis energético reproducible — Aulas Tumaco (Módulo 2).

Calcula línea base, usos significativos de la energía (SEU) e indicadores de
desempeño energético (EnPIs) bajo el enfoque ISO 50001:2018.

Uso (desde la raíz del repositorio):
    python Entregables_Modulos\\Modulo_2_Eficiencia_Energetica\\codigo\\analisis_energetico.py

Requisitos: Python 3.9+ y pandas.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

RUTA_POR_DEFECTO = Path("Prompt - Datasep/dataset_dos_aulas_tumaco.csv")
INTERVALO_MIN = 5
FE_CO2 = 0.177  # kg CO2e/kWh — Res. UPME 001198 de 2024 (SIN 2023)
AREA_M2 = 48.0  # área de cada aula (8 m x 6 m)


def cargar(ruta: Path) -> pd.DataFrame:
    df = pd.read_csv(ruta, parse_dates=["timestamp"])
    df["hora"] = df["timestamp"].dt.hour
    df["dia"] = df["timestamp"].dt.date
    df["fin_de_semana"] = df["timestamp"].dt.dayofweek >= 5
    dt_h = INTERVALO_MIN / 60.0
    df["aula1_kwh"] = df["aula1_potencia_W"] * dt_h / 1000.0
    df["aula2_kwh"] = df["aula2_potencia_W"] * dt_h / 1000.0
    return df


def enpis(df: pd.DataFrame, area_m2: float = AREA_M2) -> dict:
    dt_h = INTERVALO_MIN / 60.0
    energia = {"Aula 1 (con AC)": df["aula1_kwh"].sum(),
               "Aula 2 (sin AC)": df["aula2_kwh"].sum()}
    total = sum(energia.values())
    persona_hora = float((df["aforo_estudiantes"] * dt_h).sum())
    horas_lectivo = float(((df["hora"] >= 7) & (df["hora"] < 18)).sum() * dt_h)
    out = {
        "total_kwh": total,
        "energia": energia,
        "participacion": {k: v / total * 100 for k, v in energia.items()},
        "ratio": energia["Aula 1 (con AC)"] / energia["Aula 2 (sin AC)"],
        "persona_hora": persona_hora,
        "horas_lectivo": horas_lectivo,
        "kwh_m2": {k: v / area_m2 for k, v in energia.items()},
        "wh_persona_h": {k: v * 1000 / persona_hora for k, v in energia.items()},
        "co2_kg": {k: v * FE_CO2 for k, v in energia.items()},
        "consumo_fuera_lectivo": {
            "Aula 1 (con AC)": energia["Aula 1 (con AC)"] - df.loc[
                (df["hora"] >= 7) & (df["hora"] < 18), "aula1_kwh"].sum(),
            "Aula 2 (sin AC)": energia["Aula 2 (sin AC)"] - df.loc[
                (df["hora"] >= 7) & (df["hora"] < 18), "aula2_kwh"].sum(),
        },
        "hvac_fraccion": float(df["aula1_hvac_estado"].mean()),
        "potencia_hvac_on": float(df.loc[df["aula1_hvac_estado"] == 1,
                                         "aula1_potencia_W"].mean()),
        "potencia_hvac_off": float(df.loc[df["aula1_hvac_estado"] == 0,
                                          "aula1_potencia_W"].mean()),
    }
    return out


def imprimir(r: dict, df: pd.DataFrame) -> None:
    print("=" * 68)
    print("LÍNEA BASE ENERGÉTICA — AULAS TUMACO (ISO 50001)")
    print("=" * 68)
    print(f"Registros: {len(df)} | Periodo: {df['timestamp'].min()} a {df['timestamp'].max()}")
    print(f"Energía total semana: {r['total_kwh']:.2f} kWh")
    for aula in r["energia"]:
        print(f"\n{aula}:")
        print(f"  Energía:            {r['energia'][aula]:8.2f} kWh/semana")
        print(f"  Participación:      {r['participacion'][aula]:8.1f} %")
        print(f"  Intensidad área:    {r['kwh_m2'][aula]:8.3f} kWh/m²-semana")
        print(f"  Intensidad persona: {r['wh_persona_h'][aula]:8.1f} Wh/persona-hora")
        print(f"  Emisiones (alcance 2): {r['co2_kg'][aula]:6.2f} kg CO₂e/semana")
        print(f"  Fuera de horario lectivo: {r['consumo_fuera_lectivo'][aula]:.2f} kWh")
    print(f"\nRatio Aula 1 / Aula 2: {r['ratio']:.2f}x")
    print(f"HVAC encendido: {r['hvac_fraccion']*100:.1f} % del tiempo")
    print(f"Potencia media HVAC ON: {r['potencia_hvac_on']:.0f} W | OFF: {r['potencia_hvac_off']:.0f} W")
    print(f"Factor de emisión usado: {FE_CO2} kg CO₂e/kWh (UPME 2023)")
    print("=" * 68)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("ruta", nargs="?", type=Path, default=RUTA_POR_DEFECTO)
    ap.add_argument("--area", type=float, default=AREA_M2, help="Área por aula en m²")
    args = ap.parse_args()
    if not args.ruta.exists():
        raise SystemExit(f"No se encontró el dataset: {args.ruta}")
    df = cargar(args.ruta)
    imprimir(enpis(df, args.area), df)


if __name__ == "__main__":
    main()
