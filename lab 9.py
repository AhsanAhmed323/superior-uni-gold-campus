import pandas as pd
import numpy as np

data = pd.read_csv('titanic.csv') 

print("### Dataset Overview ###")
print(data.head())  

print("\n### Dataset Information ###")
data.info() 

print("\n### Statistical Summary ###")
print(data.describe())  

print("\n### Null Values ###")
print(data.isnull().sum())  

print("\n### Dataset Shape ###")
print(f"Rows: {data.shape[0]}, Columns: {data.shape[1]}")  

print("\n### Unique Values in Each Column ###")
for col in data.columns:
    print(f"{col}: {data[col].nunique()} unique values")

print("\n### Checking for Duplicates ###")
duplicates = data.duplicated().sum()
print(f"Number of duplicate rows: {duplicates}")

if 'Survived' in data.columns:
    print("\n### Survival Count ###")
    print(data['Survived'].value_counts())

if 'Age' in data.columns:
    median_age = data['Age'].median()
    data['Age'].fillna(median_age, inplace=True)
    print("\nMissing Age values filled with median.")

print("\n### Dataset After Preprocessing ###")
print(data.info())