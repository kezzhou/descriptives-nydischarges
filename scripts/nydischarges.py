#### Imports ####

import pandas as pd
import researchpy as rp
import tableone as t1
from tableone import TableOne, load_dataset

#### Dataset Pruning ####

## for the sake of code efficiency, we'll clean and cut down the dataset a little before performing analysis

df = pd.read_csv('data/Hospital_Inpatient_Discharges__SPARCS_De-Identified___2016.csv')

newdf = df.drop(['Facility Id', 'Length of Stay'], axis=1)

newdf = df.drop(df.loc[339:].index, inplace=True)

newdf = df.dropna(axis=0) ## this will drop rows with nan values

newdf.shape

newdf.to_csv('data/new_SPARCS.csv')



#### Building a table with TableOne ####

my_data = pd.read_csv('data/new_SPARCS.csv')

df = my_data.copy()

df.dtypes

df.columns

df.head(5)

df_columns = ['Age', 'HR', 'Group', 'sBP', 'Smoke']

df_categories = ['Smoke', 'Group']

df_groupby = ['Smoke']

# df2['Vocation'].value_counts()

df2_table1 = TableOne(df2, columns=df2_columns, 
    categorical=df2_categories, groupby=df2_groupby, pval=False)

print(df2_table1.tabulate(tablefmt = "fancy_grid"))

df2_table1.to_csv('descriptive/example1/data/test2.csv')


#### Data Analysis with ResearchPy ####

df = pd.read_csv('data/Hospital_Inpatient_Discharges__SPARCS_De-Identified___2016.csv')

rp.codebook(df)

df.columns

rp.summary_cont(df[['Total Charges', 'Total Costs']])

rp.summary_cat(df[[]])