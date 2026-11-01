# Budget vs. Actual Variance Analysis

> **Key finding:** Total spend looks fine at +0.7% over budget, but 5 lines run more than 10% over — Contract Labor alone is +$1,650 (+20.6%).

A budget variance report: for each spending category, how far actual
spending landed from budget in dollars and percent, with the lines that
need attention flagged instead of buried in a table.

All data is sample/practice data created for portfolio purposes. No real
company financial data is used anywhere in this project.

## The questions it answers

1. Which categories are over budget, and by how much ($ and %)?
2. Which over-runs are big enough to act on — here, any line more than
   10% over budget gets flagged.
3. What is the overall position once over- and under-spends are netted?

## What was done

- Loaded `budget_vs_actual.csv` (12 categories) with pandas.
- Computed `variance = actual − budget` and `variance_pct = variance ÷
  budget` for every line — positive means over budget.
- Flagged every line with variance_pct above +10% and sorted the report
  so the worst percentage over-runs appear first.
- Totaled budget and actual, and wrote an "attention first" list of the
  flagged lines ranked by dollars over.

## Results (from running `variance_report.py` on the sample data)

- Overall: $92,380 actual vs. $91,750 budget — only **$630 over (+0.7%)**
  in total, which hides what is happening line by line.
- **5 lines are more than 10% over budget:** Contract Labor (+$1,650,
  +20.6%), Cloud & Hosting (+$715, +22.3%), Travel (+$410, +13.7%),
  Miscellaneous (+$335, +33.5%), Utilities (+$170, +17.9%).
- The biggest under-spend, Marketing at $1,270 under (−16.9%), is what
  keeps the total looking calm — exactly why variance is reviewed per
  line and not just in total.

## Recommendations / What I would do next

- **Start with Contract Labor.** At +$1,650 (+20.6%) it is the largest
  dollar over-run: review what the extra hours bought, who approved
  them, and whether the work should be insourced, re-scoped, or
  explicitly re-budgeted instead of drifting.
- **Audit Cloud & Hosting usage.** +$715 (+22.3%) on a usage-priced line
  usually means idle resources or an unplanned environment. A usage
  review and commitment-based pricing check are the standard first
  moves before accepting the higher run-rate.
- **Interrogate Miscellaneous.** The highest percentage over-run in the
  report (+33.5%) is the category with the least definition. Tighten
  what is allowed to land in Miscellaneous — a growing "misc" line is
  usually a categorization problem hiding real spending.
- **Don't let underspend silently fund overspend.** Marketing being
  $1,270 under is the only reason the total is +0.7%. If that money is
  to cover the Contract Labor over-run, make it an explicit reallocation
  decision at the next reforecast, not an accident of netting.
- **Keep the 10% flag as a monthly habit.** The flagged list (5 lines
  this period) is short enough to review line by line every month —
  which is the point of the threshold.

## The same analysis in Excel

From a three-column extract (Category, Budget, Actual):

- Variance $: `=C2-B2`
- Variance %: `=IF(B2=0,"",C2/B2-1)` formatted as a percentage
- Flag: `=IF(AND(B2>0, C2/B2-1>0.1), "OVER BUDGET", "")`
- Totals: `=SUM(B2:B13)` and `=SUM(C2:C13)`, with the same variance
  formulas applied to the totals row
- Conditional formatting on the variance % column (red fill above +10%)
  gives the same "attention first" view as the script

## Skills shown

- pandas calculated columns, threshold flags, and sorted reporting
- Variance analysis done the way it's reviewed in practice: per line,
  in both dollars and percent, with totals reconciled
- Explaining why a near-zero total variance can still contain real
  problems

## Run it

```bash
pip install pandas
python variance_report.py
```

## Files

- `README.md` — this file
- `variance_report.py` — the variance report script
- `budget_vs_actual.csv` — sample budget and actual figures by category
