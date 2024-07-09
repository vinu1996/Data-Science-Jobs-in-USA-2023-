import pandas as pd
import numpy as np
import os


# data cleaning

df=pd.read_csv('salary_data_cleaned.csv')
df.describe()
df.head()
df.info
df.replace(['NaN', 'N/A', 'NA', 'n/a', 'n.a.', 'N#A', 'n#a', '?'], 'other', inplace=True)
df.isna().sum()
df.shape

df.duplicated()
duplicated=df[df.duplicated()]
print(duplicated)
df[df.duplicated()==1]
df=df.drop_duplicates()
df.shape
df.info()
# Unique values for categorical features
print(df.select_dtypes(include=['object']).nunique())
df.Location.value_counts()
df['Location']=df['Location'].str.split(pat=',').str[0]
df.Sector.value_counts()
df.tail(10)
df.info()

numerical_vars = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
categorical_vars = df.select_dtypes(include=['object']).columns.tolist()                           
print('Numerical variables:', numerical_vars)
print('Categorical variables:', categorical_vars)

categorical_count = df.select_dtypes(include='object').shape[1]
numerical_count = df.select_dtypes(exclude='object').shape[1]
print(categorical_count)
print(numerical_count)

missing_values = df.isnull().sum()

fill_values = {}
for col in df.columns:
    if df[col].dtype == 'object':
        fill_values[col] = df[col].mode()[0]
    else:
        fill_values[col] = df[col].mean()

df.max_salary= df.max_salary*1000
df.min_salary= df.min_salary*1000
df.avg_salary= df.avg_salary*1000
df.head(10)
df['max_salary']


df.to_excel('jobs_final.xlsx', sheet_name='Data')