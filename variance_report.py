"""Budget vs actual variance report.

Computes variance in dollars and percent for each budget line, flags any
line more than 10% OVER budget, totals everything, and prints the lines
that need attention first. Sample data for portfolio use.
"""
import pandas as pd

FILE = "budget_vs_actual.csv"
OVER_PCT = 10.0  # flag threshold: percent over budget


def main() -> None:
    df = pd.read_csv(FILE)
    df["variance"] = df["actual"] - df["budget"]
    df["variance_pct"] = 100.0 * df["variance"] / df["budget"]
    df["flag"] = df["variance_pct"].apply(
        lambda p: "OVER BUDGET" if p > OVER_PCT else "")

    total_budget = df["budget"].sum()
    total_actual = df["actual"].sum()
    total_var = total_actual - total_budget

    print("=" * 68)
    print("BUDGET VS ACTUAL — VARIANCE REPORT")
    print("=" * 68)
    print(f"{'Category':<18}{'Budget':>10}{'Actual':>10}"
          f"{'Variance':>10}{'Var %':>8}  Flag")
    for _, r in df.sort_values("variance_pct", ascending=False).iterrows():
        print(f"{r['category']:<18}{r['budget']:>10,.0f}{r['actual']:>10,.0f}"
              f"{r['variance']:>+10,.0f}{r['variance_pct']:>+7.1f}%  {r['flag']}")
    print("-" * 68)
    print(f"{'TOTAL':<18}{total_budget:>10,.0f}{total_actual:>10,.0f}"
          f"{total_var:>+10,.0f}{100.0 * total_var / total_budget:>+7.1f}%")

    flagged = df[df["flag"] == "OVER BUDGET"].sort_values(
        "variance", ascending=False)
    print(f"\nLines more than {OVER_PCT:.0f}% over budget: {len(flagged)}")
    for _, r in flagged.iterrows():
        print(f"  {r['category']}: ${r['variance']:,.0f} over "
              f"({r['variance_pct']:+.1f}%)")

    under = df.loc[df["variance"].idxmin()]
    print(f"\nLargest under-spend: {under['category']} at "
          f"${-under['variance']:,.0f} under budget ({under['variance_pct']:+.1f}%).")
    print(f"Overall position: ${abs(total_var):,.0f} "
          f"{'over' if total_var > 0 else 'under'} budget "
          f"({100.0 * total_var / total_budget:+.1f}%).")


if __name__ == "__main__":
    main()
