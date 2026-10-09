# -*- coding: utf-8 -*-
"""Descriptive statistics for the content analysis.

Two modes:
  1. Verify the aggregated coding table (data/coding_aggregates.csv) is
     internally consistent (row totals vs stated denominators).
  2. If data/yearly_counts.csv (completed by the author from the CNKI export)
     is present, recompute the annual trend regression (slope, R^2).
"""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AGG = ROOT / "data" / "coding_aggregates.csv"
YEARLY = ROOT / "data" / "yearly_counts.csv"


def verify_aggregates():
    rows = list(csv.DictReader(AGG.open(encoding="utf-8-sig")))
    print("=== aggregated coding table ===")
    for dim in ("research_theme", "assessment_format", "teaching_method", "evaluation_tool"):
        sub = [r for r in rows if r["dimension"] == dim]
        tot = sum(int(r["n"]) for r in sub)
        den = sub[0]["denominator"]
        print(f"  {dim:20s} sum(n)={tot:3d}  denominator={den}")
    print("  (teaching_method / assessment_format may sum > denominator due to multi-label / overlap)")


def annual_trend():
    if not YEARLY.exists():
        print("\n[skip] data/yearly_counts.csv not found -- complete it from the "
              "CNKI year-tagged export to reproduce the annual trend regression.")
        return
    ys, cnt = [], []
    for r in csv.DictReader(YEARLY.open(encoding="utf-8-sig")):
        if not r["n_articles"].strip():
            continue
        ys.append(int(r["year"]))
        cnt.append(int(r["n_articles"]))
    n = len(ys)
    if n < 2:
        print("\n[skip] yearly_counts.csv is empty.")
        return
    mx = sum(ys) / n
    my = sum(cnt) / n
    sxx = sum((x - mx) ** 2 for x in ys)
    sxy = sum((x - mx) * (y - my) for x, y in zip(ys, cnt))
    slope = sxy / sxx
    intercept = my - slope * mx
    ss_tot = sum((y - my) ** 2 for y in cnt)
    ss_res = sum((y - (intercept + slope * x)) ** 2 for x, y in zip(ys, cnt))
    r2 = 1 - ss_res / ss_tot if ss_tot else float("nan")
    print(f"\n=== annual trend (n={n} years) ===")
    print(f"  total articles = {sum(cnt)}")
    print(f"  slope  = {slope:.3f}")
    print(f"  R^2    = {r2:.3f}")


if __name__ == "__main__":
    verify_aggregates()
    annual_trend()
