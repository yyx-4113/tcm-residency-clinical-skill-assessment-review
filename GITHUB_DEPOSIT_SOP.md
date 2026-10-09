# GITHUB 数据仓库操作手册（SOP）

> 项目：中医住培临床技能考核研究现状与思考（107 篇文献内容分析）
> 仓库：`https://github.com/yyx-4113/tcm-residency-clinical-skill-assessment-review`

## 一、仓库用途
存放本稿件的**语料库编码数据、分析脚本与元数据**，用于支撑稿件的"数据可用性声明"。
数据可用性声明一律写**实名仓库 URL**，严禁 "available on request" 式措辞。

## 二、当前内容状态
| 文件 | 状态 | 说明 |
|------|------|------|
| `data/coding_aggregates.csv` | ✅ 完整 | 稿件中报告的全部汇总编码结果（可直接与正文表格核对） |
| `data/bibliography_template.csv` | ⚠️ 待补全 | 已含稿件引用的 36 篇核心文献，其余 71 篇需作者从 CNKI 导出补全 |
| `data/yearly_counts_template.csv` | ⚠️ 待补全 | 2014—2025 逐年发文量，需作者从 CNKI 导出填写 |
| `scripts/*.py` | ✅ 完整 | 描述性统计 + 图 1–3 复现脚本 |

## 三、作者待办（投稿前）
1. 登录 CNKI，按稿件 2.1 检索式（检索日期 2025-06-10）导出全部 **107 篇**题录（含题名、作者、年份、关键词、单位）。
2. 将 107 行补入 `data/bibliography_template.csv`，并逐篇填写四维编码列。
3. 将逐年发文量填入 `data/yearly_counts_template.csv`。
4. 本地运行 `python scripts/descriptives.py` 与 `python scripts/figures.py` 复算，核对与稿件数字一致。
5. 打 tag 并 release，把版本号（如 `v1.0.0`）与 `MANIFEST.txt` 校验和写回稿件"数据可用性声明"。

## 四、版本与发布
```bash
git add -A
git commit -m "data: complete 107-row bibliography + yearly counts"
git tag v1.0.0
git push origin main --tags
```
推送 tag 后，GitHub Actions 会自动生成 release 并附带 `MANIFEST.txt` 与图件。

## 五、合规检查
- [ ] 无患者隐私 / 无未授权数据（本研究为公开文献二次分析）
- [ ] 作者头衔仅"杨永新"，**不带 MD / PhD**
- [ ] 单位统一为"福建中医药大学附属第二人民医院"
- [ ] 数据可用性声明中的 URL、版本 tag、MANIFEST 三者一致
