"""
Diabetes Risk Dataset Validation & EDA Script
---------------------------------------------
Performs data integrity verification, WHO BMI classification checking,
and key demographic & clinical summary metrics generation.
"""

import csv
import json
from pathlib import Path
from collections import Counter

DATA_PATH = Path(__file__).parent.parent / "data" / "diabetes_risk.csv"
SUMMARY_OUTPUT_PATH = Path(__file__).parent.parent / "docs" / "data_summary.json"


def categorize_bmi(bmi: float) -> str:
    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 24.9:
        return "Normal"
    elif bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"


def run_validation():
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Dataset not found at {DATA_PATH}")

    records = []
    with open(DATA_PATH, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append(row)

    total_records = len(records)
    print("==================================================")
    print(" Diabetes Risk Dataset Audit & Summary")
    print("==================================================")
    print(f"Total Patient Records: {total_records}")

    # Metrics calculation
    total_age = 0.0
    total_bmi = 0.0
    bmi_categories = Counter()
    risk_distribution = Counter()
    activity_risk = Counter()
    activity_totals = Counter()
    missing_counts = Counter()

    for r in records:
        # Check missing values
        for k, v in r.items():
            if v is None or v.strip() == "":
                missing_counts[k] += 1

        age = float(r["age"])
        bmi = float(r["bmi"])
        total_age += age
        total_bmi += bmi

        calculated_cat = categorize_bmi(bmi)
        bmi_categories[calculated_cat] += 1

        risk = r["diabetes_risk"]
        risk_distribution[risk] += 1

        act = r["physical_activity_level"]
        activity_totals[act] += 1
        if risk == "High":
            activity_risk[act] += 1

    avg_age = round(total_age / total_records, 2)
    avg_bmi = round(total_bmi / total_records, 2)

    print(f"Average Age: {avg_age} years")
    print(f"Average BMI: {avg_bmi} kg/m^2")

    print("\n--- WHO BMI Category Breakdown ---")
    for cat, count in bmi_categories.most_common():
        pct = round((count / total_records) * 100, 2)
        print(f" - {cat}: {count} ({pct}%)")

    print("\n--- Diabetes Risk Distribution ---")
    for risk, count in risk_distribution.most_common():
        pct = round((count / total_records) * 100, 2)
        print(f" - {risk} Risk: {count} ({pct}%)")

    print("\n--- Physical Activity vs High Risk Rate ---")
    activity_rates = {}
    for act, total in activity_totals.items():
        high_cnt = activity_risk[act]
        rate = round((high_cnt / total) * 100, 2)
        activity_rates[act] = {"total_patients": total, "high_risk_count": high_cnt, "high_risk_rate_pct": rate}
        print(f" - {act}: {high_cnt}/{total} High Risk ({rate}%)")

    sedentary_rate = activity_rates.get("Sedentary", {}).get("high_risk_rate_pct", 0)
    active_rate = activity_rates.get("Active", {}).get("high_risk_rate_pct", 0)
    protective_factor = round(sedentary_rate / active_rate, 2) if active_rate > 0 else 0
    print(f"\nProtective Factor (Sedentary vs Active Risk): {protective_factor}x higher risk in Sedentary group")

    # Export JSON Summary
    summary_data = {
        "total_records": total_records,
        "average_age": avg_age,
        "average_bmi": avg_bmi,
        "bmi_categories": dict(bmi_categories),
        "risk_distribution": dict(risk_distribution),
        "activity_analysis": activity_rates,
        "protective_factor_ratio": protective_factor,
        "missing_fields": dict(missing_counts)
    }

    SUMMARY_OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(SUMMARY_OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(summary_data, f, indent=2)

    print(f"\nSummary exported to {SUMMARY_OUTPUT_PATH}")
    print("==================================================")


if __name__ == "__main__":
    run_validation()
