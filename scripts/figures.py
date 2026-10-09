# -*- coding: utf-8 -*-
"""Regenerate Figures 1-3 of the manuscript from the coding data.

Fig 1 (annual counts) needs a completed data/yearly_counts.csv; if absent the
script prints a notice and skips Fig 1. Figs 2-3 are produced from
data/coding_aggregates.csv.
"""
import csv
import os
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figures"
OUT.mkdir(exist_ok=True)
AGG = ROOT / "data" / "coding_aggregates.csv"
YEARLY = ROOT / "data" / "yearly_counts.csv"

for p in ("C:/Windows/Fonts/msyh.ttc", "C:/Windows/Fonts/simhei.ttf",
          "C:/Windows/Fonts/simsun.ttc"):
    if os.path.exists(p):
        fm.fontManager.addfont(p)
        plt.rcParams["font.family"] = fm.FontProperties(fname=p).get_name()
        break
plt.rcParams["axes.unicode_minus"] = False
C = "#2E5A88"


def rows():
    return list(csv.DictReader(AGG.open(encoding="utf-8-sig")))


def barh(dimension, title, fname, accent_first=False):
    sub = [r for r in rows() if r["dimension"] == dimension]
    labels = [r["category"] for r in sub]
    vals = [int(r["n"]) for r in sub]
    pcts = [float(r["pct"]) for r in sub]
    colors = [("#C0392B" if i == 0 and accent_first else C) for i in range(len(sub))]
    fig, ax = plt.subplots(figsize=(8.2, 4.0))
    y = range(len(sub))
    ax.barh(list(y), vals, color=colors)
    ax.set_yticks(list(y)); ax.set_yticklabels(labels); ax.invert_yaxis()
    for i, (v, p) in enumerate(zip(vals, pcts)):
        ax.text(v + 0.2, i, f"{v}  ({p}%)", va="center", fontsize=9)
    ax.set_xlabel("文献数（篇）"); ax.set_title(title)
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    ax.grid(axis="x", linestyle="--", alpha=0.35)
    fig.tight_layout(); fig.savefig(OUT / fname, dpi=300); plt.close(fig)
    print("wrote", fname)


def fig1():
    if not YEARLY.exists():
        print("[skip] Fig1: data/yearly_counts.csv missing")
        return
    ys, cnt = [], []
    for r in csv.DictReader(YEARLY.open(encoding="utf-8-sig")):
        if r["n_articles"].strip():
            ys.append(int(r["year"])); cnt.append(int(r["n_articles"]))
    n = len(ys)
    if n < 2:
        print("[skip] Fig1: yearly_counts.csv empty"); return
    xs = [float(x) for x in ys]
    mx, my = sum(xs) / n, sum(cnt) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, cnt))
    slope = sxy / sxx
    intercept = my - slope * mx
    ss_tot = sum((y - my) ** 2 for y in cnt)
    ss_res = sum((y - (intercept + slope * x)) ** 2 for x, y in zip(xs, cnt))
    r2 = 1 - ss_res / ss_tot if ss_tot else float("nan")
    fig, ax = plt.subplots(figsize=(8.2, 4.2))
    b = ax.bar(xs, cnt, color=C, width=0.62)
    xmin, xmax = min(xs), max(xs)
    ax.plot([xmin, xmax], [intercept + slope * xmin, intercept + slope * xmax],
            "--", color="#C0392B", lw=1.6)
    ax.text(xmin + 0.2, intercept + slope * xmin + 0.8,
            f"斜率={slope:.3f}，R²={r2:.3f}", color="#C0392B", fontsize=9)
    for bb, c in zip(b, cnt):
        ax.text(bb.get_x() + bb.get_width() / 2, c + 0.25, str(c),
                ha="center", va="bottom", fontsize=9)
    ax.set_xlabel("年份"); ax.set_ylabel("发文量（篇）")
    ax.set_title("图1  2014—2025年中医住培临床技能考核相关文献发文量")
    ax.set_xticks(xs); ax.set_xticklabels([str(int(x)) for x in xs], rotation=45)
    ax.set_xlim(xmin - 0.7, xmax + 0.7)
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    ax.grid(axis="y", linestyle="--", alpha=0.35)
    fig.tight_layout(); fig.savefig(OUT / "图1_年发文趋势.png", dpi=300); plt.close(fig)
    print(f"wrote 图1_年发文趋势.png (slope={slope:.3f}, R2={r2:.3f}, total={sum(cnt)})")


if __name__ == "__main__":
    fig1()
    barh("teaching_method", "图2  教学方法分布（n=38，明确报告者）", "图2_教学方法分布.png")
    barh("evaluation_tool", "图3  评价工具分布（n=15，明确报告者）", "图3_评价工具分布.png", accent_first=True)
