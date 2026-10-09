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
│   ├── bibliography_template.csv# 36 core references; full 107-row bibliography pending CNKI export
│   └── yearly_counts.csv        # EXACT per-year counts 2014–2025 (recovered, regression-verified)
├── scripts/
│   ├── descriptives.py          # descriptive statistics + annual trend regression
│   └── figures.py               # regenerates Figures 1–3 (incl. trend line + regression annotation)
└── figures/                     # the three manuscript figures (PNG, 300 dpi)
```

---

## Data provenance and **important caveats**

- **Source.** All 107 articles were retrieved from the **CNKI journal database** (search date **2025-06-10**), publication window **2014-01-01 – 2025-12-31**, using the Boolean search string documented in the manuscript (Section 2.1).
- **What is exact here.** `data/coding_aggregates.csv` reproduces **verbatim** the counts/percentages reported in the manuscript (research theme; assessment format; teaching method; evaluation tool; TCM-specific and emergency-skill flags; year-segment totals). `data/yearly_counts.csv` now contains the **exact per-year counts (2014–2025)**, recovered from the original embedded figure of the manuscript and verified to reproduce the reported trend regression (**slope = 0.983, R² = 0.444, total = 107**). Re-running `scripts/descriptives.py` and `scripts/figures.py` regenerates Figure 1 and the regression from these exact values — the deposited figures and the published manuscript are therefore reproducible from first principles.
- **What the author must still complete.** The full **107-row** bibliographic table (title / author / year / source / codes) is **not yet** included. The author must export it from CNKI (search date 2025-06-10) and append the rows to `data/bibliography_template.csv`. Until that is done, the manuscript's data-availability statement (§2.6, "107-article bibliography and coding table deposited") is **only partially satisfied** by this package: the deposited materials are the aggregated coding results, the exact yearly counts, the analysis scripts, the three figures, and this README/MANIFEST. The author should either complete the 107-row table before submission or tighten §2.6 to describe only what is actually deposited.
- **Continuous-release workflow.** The optional GitHub Actions workflow (`.github/workflows/release.yml`) is **not bundled** in this release because the repository was created with a token lacking the `workflow` scope. The workflow file is supplied separately by the author; once added with a token that has `workflow` scope, pushing a `v*` tag will auto-generate MANIFEST.txt and a release containing the figures.

---

## Reproduction

```bash
# 1. descriptive statistics (verifies the aggregated table; annual trend if yearly_counts.csv exists)
python scripts/descriptives.py

# 2. regenerate the figures into ./figures
python scripts/figures.py
```

No external data download is required: all aggregated tables and Figures 1–3 reproduce directly from the deposited data files.

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
