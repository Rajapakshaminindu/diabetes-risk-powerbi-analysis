// Power Query M Script: Diabetes Risk Data Pipeline
// Description: Automated data ingestion, missing value imputation, type casting, and WHO BMI categorization

let
    // 1. Load Primary Dataset
    Source = Csv.Document(File.Contents("data/diabetes_risk.csv"), [Delimiter=",", Columns=12, Encoding=65001, QuoteStyle=QuoteStyle.None]),
    
    // 2. Promote First Row as Column Headers
    #"Promoted Headers" = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),

    // 3. Set Explicit Data Types
    #"Changed Types" = Table.TransformColumnTypes(#"Promoted Headers",{
        {"patient_id", Int64.Type},
        {"age", Int64.Type},
        {"gender", type text},
        {"city", type text},
        {"bmi", type number},
        {"family_history_diabetes", type text},
        {"physical_activity_level", type text},
        {"diet_type", type text},
        {"smoking_status", type text},
        {"alcohol_consumption", type text},
        {"diabetes_risk", type text}
    }),

    // 4. Impute Missing/Blank Values in Categorical Fields
    #"Replaced Missing Smoking" = Table.ReplaceValue(#"Changed Types", "", "Unknown", Replacer.ReplaceText, {"smoking_status"}),
    #"Replaced Null Smoking" = Table.ReplaceValue(#"Replaced Missing Smoking", null, "Unknown", Replacer.ReplaceValue, {"smoking_status"}),
    #"Replaced Missing Alcohol" = Table.ReplaceValue(#"Replaced Null Smoking", "", "Unknown", Replacer.ReplaceText, {"alcohol_consumption"}),
    #"Replaced Null Alcohol" = Table.ReplaceValue(#"Replaced Missing Alcohol", null, "Unknown", Replacer.ReplaceValue, {"alcohol_consumption"}),

    // 5. Add Custom Conditional Column: WHO BMI Category
    #"Added BMI Category" = Table.AddColumn(#"Replaced Null Alcohol", "bmi_category", each 
        if [bmi] <= 18.5 then "Underweight"
        else if [bmi] <= 24.9 then "Normal"
        else if [bmi] <= 29.9 then "Overweight"
        else "Obese", 
        type text
    )
in
    #"Added BMI Category"
