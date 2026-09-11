# 🏥 Diabetes Risk & Patient Health Analytics Dashboard

An end-to-end Healthcare Business Intelligence and Data Analytics project built using **Microsoft Power BI** and **Power Query**. This interactive dashboard investigates how patient lifestyle habits, physical activity levels, and clinical metrics correlate with diabetes risk across major urban populations.

---

## 📊 Interactive Dashboard Overview

![Diabetes Risk Analytics Dashboard](images/dashboard_preview.png)

---

## 💡 Key Analytical Findings & Clinical Insights

From the dashboard visualizations and multi-attribute slicing of **1,535 patient records**:

1. **Sedentary Lifestyle Directly Elevates Diabetes Risk**:
   - **Sedentary Cohort**: High-risk prevalence reaches nearly **100 patients** (~18.5% high-risk rate within the group).
   - **Active Cohort**: Exhibits the lowest high-risk cases (**~40 patients**, <8% high-risk rate), with over **350 patients** safely categorized as Low Risk.
   - **Takeaway**: Regular physical activity demonstrates a **>2x protective factor** against high diabetes risk compared to a sedentary routine.

2. **BMI Category Breakdown**:
   - **Normal Weight**: **57.85%** (888 patients)
   - **Overweight**: **23.45%** (360 patients)
   - **Underweight**: **13.22%** (203 patients)
   - **Obese**: **5.47%** (84 patients)
   - **Takeaway**: Nearly **29% of the total cohort** is classified as Overweight or Obese, highlighting a critical population segment for preventive dietary and lifestyle intervention programs.

3. **Demographic & Clinical Baseline**:
   - **Total Patient Population**: 1,535 patients
   - **Average Age**: 44.48 years
   - **Average BMI**: 22.97 $kg/m^2$

---

## 🛠️ Data Pipeline & Transformation (Power Query)

- **Missing Data Handling**: Replaced blank and null values in `smoking_status` and `alcohol_consumption` with `"Unknown"` to maintain data integrity across slicers.
- **Clinical Categorization (`bmi_category`)**: Implemented standard World Health Organization (WHO) BMI classifications using Power Query M:
  ```powerquery
  if [bmi] <= 18.5 then "Underweight"
  else if [bmi] <= 24.9 then "Normal"
  else if [bmi] <= 29.9 then "Overweight"
  else "Obese"
  ```
- **Aggregation Correction**: Transformed visual field aggregations from raw sums to distinct counts (`COUNT(patient_id)`), ensuring accurate population metrics across all charts.

---

## 🎛️ Dashboard Features & Visual Architecture

| Component | Visual Type | Analytical Purpose |
| :--- | :--- | :--- |
| **Executive KPIs** | Single-value Cards | Instant visibility into Total Patients (1,535), Average Age (44.48), and Average BMI (22.97) |
| **Activity vs. Risk** | Clustered Column Chart | Cross-analyzes `physical_activity_level` (Sedentary, Moderate, Active) against `diabetes_risk` (Low, Medium, High) |
| **Weight Distribution**| Donut Chart | Shows proportional breakdown of patient health across WHO BMI categories |
| **Geographic Analysis**| Clustered Bar Chart | Tracks patient volume and health trends across cities |
| **Interactive Slicers**| Slicer Panels | Dynamic filtering across `city` (Bengaluru, Mumbai, Delhi, etc.) and `gender` (Female, Male, Other) |

---

## 📁 Repository Structure

```text
├── data/
│   └── diabetes_risk.csv            <-- Primary dataset (1,535 patient records)
├── images/
│   └── dashboard_preview.png        <-- High-resolution dashboard screenshot
└── README.md                        <-- Comprehensive project documentation & findings
```

---

## 📋 Data Dictionary

| Field Name | Data Type | Description |
| :--- | :--- | :--- |
| `patient_id` | Integer | Unique identifier for each patient |
| `age` | Integer | Patient age (in years) |
| `gender` | Text | Male, Female, Other |
| `city` | Text | Patient residential city |
| `bmi` | Decimal | Body Mass Index ($kg/m^2$) |
| `bmi_category` | Text | Custom calculated WHO category |
| `family_history_diabetes` | Text | Genetic risk indicator (Yes / No) |
| `physical_activity_level` | Text | Sedentary, Moderate, Active |
| `diet_type` | Text | Vegetarian, Non-Vegetarian |
| `smoking_status` | Text | Never, Current, Former, Unknown |
| `alcohol_consumption` | Text | Never, Occasional, Regular, Unknown |
| `diabetes_risk` | Text | Target risk outcome (Low, Moderate, High) |

---

## 🚀 How to Open / Recreate the Project

1. Clone this repository:
   ```bash
   git clone https://github.com/Rajapakshaminindu/diabetes-risk-powerbi-analysis.git
   ```
2. Open **Power BI Desktop** or **Power BI Service** ([app.powerbi.com](https://app.powerbi.com)).
3. Import `data/diabetes_risk.csv` and apply the Power Query steps documented above.
4. Interact with the slicers to explore demographic and lifestyle patterns!

---

## 👤 Author
- **GitHub**: [@Rajapakshaminindu](https://github.com/Rajapakshaminindu)
