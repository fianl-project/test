import pandas as pd

# before cleaning overview
df = pd.read_excel("E:\\DEPI\\FinalProject\\Messy\\HyperTensionUNclean.xlsx")

print(df.head(5)) 

# -----------------------------------------------------------------
# remove extra spaces 
print("BEFORE removing spaces:")
print(df.select_dtypes(include='object').head(5))

df_obj = df.select_dtypes(include='object').columns
for col in df_obj:
    df[col] = df[col].astype(str).str.strip()

print("\nAFTER removing spaces:")
print(df[df_obj].head(5))

# ==============================================================

# fix typos in categorical
print("BEFORE fixing typos:")
print(df[['Has_Hypertension','Gender','Smoking_Status']].head(10))

replace_map = {
    "Has_Hypertension": {
        "Yess":"Yes", "yes":"Yes","YES":"Yes",
        "no":"No","NO":"No","N o":"No",
    },
    "Gender": {
        "male":"Male","Male ":"Male","M ale":"Male",
        "female":"Female","Fem ale":"Female"
    },
    "Smoking_Status": {
        "sm0ker":"Smoker","smoker":"Smoker","Smokerr":"Smoker",
        "non smoker":"Non-Smoker","NonSmokerr":"Non-Smoker"
    }
}

for col, mapping in replace_map.items():
    df[col] = df[col].replace(mapping)

print("\nAFTER fixing typos:")
print(df[['Has_Hypertension','Gender','Smoking_Status']].head(10))

# ================================================================

# fix numeric columns 
print("BEFORE fixing numeric types:")
print(df.dtypes) 

num_cols = ['Age','Salt_Intake','Stress_Score','Sleep_Duration','BMI','Caffeine_Intake']

for col in num_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')  

df['Age'] = df['Age'].astype('Int64')


print("\nAFTER fixing numeric types:")
print(df.dtypes) 

# ===========================================================

# handling missing values 
print("Missing values BEFORE:")
print(df.isna().sum())

for col in df.columns:
    if df[col].dtype in ['float64','int64']:
        df[col] = df[col].fillna(df[col].median())
    else:
        df[col] = df[col].fillna(df[col].mode()[0])

print("\nMissing values AFTER:")
print(df.isna().sum())

# ============================================================

#removing duplicates 

print("Shape BEFORE removing duplicates:", df.shape)

df = df.drop_duplicates()

print("Shape AFTER removing duplicates:", df.shape)

# ============================================================

# after cleaning overview
print("\nFINAL CLEAN DATA SAMPLE:")
print(df.head(10))

df.to_excel("E:\\DEPI\\FinalProject\Messy\\hypertension_cleaned.xlsx", index=False) 