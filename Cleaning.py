import pandas as pd 
from sklearn.impute import SimpleImputer
import numpy as np

df = pd.read_excel("E:\\DEPI\\FinalProject\\final_resultt.xlsx")

print(df.info())
print("Number of NUlls before Cleaning: ")
print(df.isnull().sum())     

imputer = SimpleImputer(strategy='mean')
df.loc[:, df.select_dtypes(include=np.number).columns] = imputer.fit_transform(df.select_dtypes(include=np.number))
cat_imputer = SimpleImputer(strategy='most_frequent')
df.loc[:, df.select_dtypes(exclude=np.number).columns] = cat_imputer.fit_transform(df.select_dtypes(exclude=np.number))
print("Number of NUlls after Cleaning: ")
print(df.isna().sum())


print("Number of Duplicates before cleaning is: ", end= "")    
print(df.duplicated().sum())
df.drop_duplicates(inplace= True)  

print("Number of Duplicates after cleaning is: ", end= "" )    
print(df.duplicated().sum())

  
df.to_excel("E:\\DEPI\\FinalProject\\hypertensionClean.xlsx", index=False)



