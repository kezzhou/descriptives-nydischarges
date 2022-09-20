#### Imports ####

import pandas as pd

import researchpy as rp

import tableone as t1
from tableone import TableOne, load_dataset

import matplotlib.pyplot as plt

import numpy as np

import pandas.plotting as pdp

#### Dataset Pruning ####

## for the sake of code efficiency, we'll clean and cut down the dataset a little before performing analysis

df = pd.read_csv('data/Hospital_Inpatient_Discharges__SPARCS_De-Identified___2016.csv')

newdf = df.drop(df.loc[339:].index, inplace=True) ## drops rows beyond row 339. all rows retain their original row number

newdf = df.dropna(axis=0) ## this will drop rows with nan values

newdf.shape

newdf.dtypes

newdf.to_csv('data/new_SPARCS.csv') ## setting the new csv into stone



#### Building a table with TableOne ####

my_data = pd.read_csv('data/new_SPARCS.csv') 

df = my_data.copy()

df.dtypes

df.columns

df.head(5)

df_columns = ['Length of Stay', 'Gender', 'Ethnicity']

df_categories = ['Gender', 'Ethnicity']

df_groupby = ['Emergency Department Indicator']

df_table1 = TableOne(df, columns=df_columns, 
    categorical=df_categories, groupby=df_groupby, pval=False)

print(df_table1.tabulate(tablefmt = "fancy_grid"))

df_table1.to_csv('data/tableone.csv')




#### Data Analysis with ResearchPy ####

df = pd.read_csv('data/new_SPARCS.csv')

rp.codebook(df) ## works very well with categorical data

df.columns

df.dtypes

rp.summary_cont(df[['Length of Stay', 'Birth Weight']])

rp.summary_cat(df[['Health Service Area', 'Hospital County', 'Emergency Department Indicator', 'Abortion Edit Indicator', 'Payment Typology 1', 'Payment Typology 2', 'Payment Typology 3', 'APR Medical Surgical Description', 'APR Risk of Mortality', 'APR Severity of Illness Description', 'APR Severity of Illness Code', 'APR MDC Description', 'APR MDC Code', 'APR DRG Description', 'APR DRG Code', 'CCS Procedure Description']])

df.describe() ## to get a sweeping descriptive stat summary we can use .describe()
## however, not all of these are relevant. even though Operating Certificate Number is int type, it makes no sense to compare them like this


## let's say we want to look at the average Length of Stay by an individual's Gender

groupby_gender = df.groupby('Gender')
for gender, value in groupby_gender['Length of Stay']:
    print(
        gender, np.log(value.mean())
        )

## the average stay for Females is 1.2 days and the average stay for Males is 1.4 days

#### Visualization ####

## let's sprinkle in some visualization for the nurses

## we can start with a pie chart on Gender

df['Gender'].value_counts()

x, y = 182, 118

fig, ax = plt.subplots()

ax.pie((x, y), labels=('F', 'M'), autopct='%1.1f%%')

plt.show()

## now let's do a bar chart for Age Group

df['Age Group'].value_counts()

x = ['0 to 17', '18 to 29', '30 to 49', '50 to 69', '70 or Older']

h = [58, 50, 38, 64, 90]

plt.barh(x, h)

plt.xlabel('Age Group')

plt.ylabel('Patient Count')

plt.title('Patient Count by Age Group')

plt.show()


## Scatter matrices 

pdp.scatter_matrix(
    df[['Length of Stay', 'Birth Weight']] ## unfortunately the dataset leaves much to be desired for by way of numerical data