# 📐 Power BI DAX Measures Documentation

This document provides the Data Analysis Expressions (DAX) used to calculate core clinical indicators, patient volumes, and risk ratios in the **Diabetes Risk & Patient Health Analytics Dashboard**.

---

## 📊 Core Aggregation & Demographic Measures

### 1. Total Patients
Calculates the distinct count of patient records in the dataset.
```dax
Total Patients = 
COUNTROWS('diabetes_risk')
```

### 2. Average Age
Computes the mean age across the selected patient population.
```dax
Average Age = 
AVERAGE('diabetes_risk'[age])
```

### 3. Average BMI
Calculates the average Body Mass Index ($kg/m^2$).
```dax
Average BMI = 
AVERAGE('diabetes_risk'[bmi])
```

---

## 🎯 Risk Classification & Prevalence Measures

### 4. High Risk Patient Count
Counts patients categorized as having High Diabetes Risk.
```dax
High Risk Patient Count = 
CALCULATE(
    COUNTROWS('diabetes_risk'),
    'diabetes_risk'[diabetes_risk] = "High"
)
```

### 5. High Risk Rate (%)
Determines the percentage of the current selection classified as High Risk.
```dax
High Risk Rate % = 
DIVIDE(
    [High Risk Patient Count],
    [Total Patients],
    0
)
```

### 6. Low Risk Patient Count
```dax
Low Risk Patient Count = 
CALCULATE(
    COUNTROWS('diabetes_risk'),
    'diabetes_risk'[diabetes_risk] = "Low"
)
```

### 7. Medium Risk Patient Count
```dax
Medium Risk Patient Count = 
CALCULATE(
    COUNTROWS('diabetes_risk'),
    'diabetes_risk'[diabetes_risk] = "Medium"
)
```

---

## 🏃 Lifestyle & Activity Analytical Ratios

### 8. Sedentary Cohort High Risk Rate
Calculates the High-Risk percentage specifically for sedentary patients.
```dax
Sedentary High Risk Rate % = 
CALCULATE(
    [High Risk Rate %],
    'diabetes_risk'[physical_activity_level] = "Sedentary"
)
```

### 9. Active Cohort High Risk Rate
Calculates the High-Risk percentage specifically for active patients.
```dax
Active High Risk Rate % = 
CALCULATE(
    [High Risk Rate %],
    'diabetes_risk'[physical_activity_level] = "Active"
)
```

### 10. Physical Activity Protective Factor
Measures the relative risk reduction of active vs. sedentary lifestyle.
```dax
Activity Protective Factor = 
DIVIDE(
    [Sedentary High Risk Rate %],
    [Active High Risk Rate %],
    0
)
```

---

## ⚖️ BMI Category Distribution Measures

### 11. BMI Category Share (%)
Calculates proportional patient share per WHO BMI category regardless of visual breakdown filters.
```dax
BMI Category Share % = 
DIVIDE(
    COUNTROWS('diabetes_risk'),
    CALCULATE(
        COUNTROWS('diabetes_risk'),
        ALL('diabetes_risk'[bmi_category])
    ),
    0
)
```

---

## 📌 Usage Instructions
1. Open **Power BI Desktop**.
2. Go to the **Modeling** tab and click **New Measure**.
3. Copy and paste any DAX measure above into the formula bar.
4. Format percentage measures as `Percentage (%)` with 2 decimal places.
