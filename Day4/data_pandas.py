from itertools import count
from xml import dom
import pandas as pd

data = pd.read_csv(
    "C:\kani\Data_Incubator\Day4\Value_of_Energy_Cost_Savings_Program_Savings_for_Businesses_-_FY2020.csv")
print(data.head())
companies = data["Company Name"]
print(companies.head())
count_job = data[data["Borough"] == "Queens"]
print("number of jobs created in queens: ", count_job["Job created"].count())
# print(data["company email"])
email = data["company email"]
domain = email.str.split("@").str[1]
print(domain)
unique_domain = set(domain)
print("Number of unique email domains:", len(unique_domain))

data['NTA_mod'] = data['NTA'].str.split('-')
df = data.explode('NTA_mod').reset_index(drop=True)

df_NTA_grp = df.groupby(['NTA_mod'])
# df_NTA_grp_size = df_NTA_grp.size().reset_index(name='counts')
# NTA_ge_5 = df_NTA_grp_size[df_NTA_grp['counts'] >= 5]
df_ge_5 = df_NTA_grp.filter(lambda x: len(x) >= 5)

df_ge_5.groupby('NTA_mod').agg({
    'Total Savings': 'mean',
    'Job created': 'sum',
})
# Or, renaming columns with named aggregation
aggn = {
    'Average Total Savings': ('Total Savings', 'mean'),
    'Total Jobs Created': ('Job created', 'sum'),
}
df_ge_5.groupby('NTA_mod').agg(**aggn)

print("\nAverage total savings and total jobs crerateed for NTA with at least 5 listed business\n")
print(df_ge_5)

groupby_csv = df_ge_5.to_csv("NTA.csv")
