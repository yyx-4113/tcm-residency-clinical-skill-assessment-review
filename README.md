# TCM Residency Clinical-Skill Assessment — Content Analysis (107 articles, 2014–2025)

Reproducibility package for the manuscript:

> **Current status and reflections on clinical skill assessment in Traditional Chinese Medicine residency training: a content analysis of 107 articles** — Yang Y. (submitted to *Chinese Medicine Education* / 《中医教育》).

This repository contains the coded data, the analysis/plotting scripts, and the metadata required to reproduce the descriptive statistics and figures reported in the manuscript.

---

## Repository layout

```
.
├── README.md
├── CITATION.cff
├── LICENSE
├── MANIFEST.txt                 # SHA-256 checksums of all tracked files
├── GITHUB_DEPOSIT_SOP.md        # deposit / verification SOP (Chinese)
├── author_verification_statement.md
├── data/
│   ├── coding_aggregates.csv    # EXACT aggregated results reported in the paper
│   ├── bibliography_template.csv# 36 core references cited in the paper (coding columns blank)
│   └── yearly_counts_template.csv # annual counts (to be completed from CNKI export)
├── scripts/
│   ├── descriptives.py          # descriptive statistics + annual trend regression
│   └── figures.py               # regenerates Figures 1–3
└── .github/workflows/release.yml
```

---

## Data provenance and **important caveats**

- **Source.** All 107 articles were retrieved from the **CNKI journal database** (search date **2025-06-10**), publication window **2014-01-01 – 2025-12-31**, using the Boolean search string documented in the manuscript (Section 2.1).
- **What is exact here.** `data/coding_aggregates.csv` reproduces **verbatim** the counts/percentages reported in the manuscript (research theme; assessment format; teaching method; evaluation tool; TCM-specific and emergency-skill flags; year-segment totals). These are directly verifiable against the published tables.
- **What the author must complete.** The full **107-row** bibliographic table (title / author / year / source / codes) is **not** included in this scaffold. The author must export it from CNKI (search date 2025-06-10) and append the rows to `data/bibliography_template.csv`, then fill `data/yearly_counts_template.csv` with the per-year counts.
- **Figure 1 caveat.** The exact **per-year** counts (2014–2025) were not available as a machine-readable file when this package was assembled. The manuscript's Figure 1 was therefore rendered from a series **reconstructed** to satisfy every published constraint — the year-segment totals (10 / 40 / 33 / 24) and the four named single-year peaks (2018 = 14, 2019 = 16, 2023 = 14, 2025 = 15). Once `yearly_counts.csv` is completed from the CNKI export, re-run `scripts/figures.py` to regenerate the figure from **exact** values and re-compute the trend regression with `scripts/descriptives.py`.
- **Reported trend.** The manuscript reports a linear slope of **0.983** and **R² = 0.444** (manuscript Sections 2.5 / 3.1). These should be re-verified against the completed `yearly_counts.csv`.

---

## Reproduction

```bash
# 1. descriptive statistics (verifies the aggregated table; annual trend if yearly_counts.csv exists)
python scripts/descriptives.py

# 2. regenerate the figures into ./figures
python scripts/figures.py
```

No external data download is required to reproduce the aggregated tables and Figures 2–3. Figure 1 requires the completed `data/yearly_counts.csv`.

---

## Software

| Component | Version |
|-----------|---------|
| Python    | 3.13.x  |
| matplotlib| ≥ 3.8   |
| python-docx (manuscript build only) | ≥ 1.1 |

Chinese glyphs rely on a system CJK font (Microsoft YaHei / SimHei on Windows).

---

## Citation & license

See `CITATION.cff`. Author: **Yongxin Yang**, The Second Affiliated Hospital of Fujian University of Traditional Chinese Medicine, Fuzhou, Fujian 350003, China (ORCID [0009-0004-9698-6552](https://orcid.org/0009-0004-9698-6552)).

Released under the **MIT License** (see `LICENSE`).
