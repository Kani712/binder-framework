# Day 4

from datetime import datetime
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = data = pd.read_csv(
    "C:\kani\Data_Incubator\Day4\Value_of_Energy_Cost_Savings_Program_Savings_for_Businesses_-_FY2020.csv")
print("Data shape:", data.shape)

print("columns: ", data.columns)

# Problem 1
# Unique companies represented in the dataset
print("Number of unique companies represented: ",
      len(data['Company Name'].unique()))

# Problem 2
# Number of jobs created for business in Queens

data_queens = data.query('Borough == "Queens"')
print(data_queens.head())
print("\nNumber of jobs created in Queens: ",
      int(data_queens['Job created'].sum()))

# Probelm 3
# Umique email domains in data set


company_email = data.dropna(subset=['company email'])
domains = company_email['company email'].str.split('@')
domains_list = set(domains.str[1].values)
print(f"Number of unique emails: {len(domains_list)}")

# Probelm 4
# Considering only NTAs with at least 5 listed business, total average savings and total job created for each NTA
data_nta = data.groupby('NTA').agg({'Company Name': ['count'],
                                    'Total Savings': ['mean'],
                                    'Job created': ['sum']})
data_nta.columns = ['company_count', 'average_savings', 'jobs_created']
data_nta = data_nta[data_nta['company_count'] >= 5]
print(data_nta, '\n')

# saving it in csv file
data_nta.to_csv('dat_4_nta_results.csv')

# Plotting the graph
sns.scatterplot(data=data_nta, x='average_savings', y='jobs_created')
plt.show()
sns.histplot(data=data_nta, x='average_savings', log_scale=True)
plt.show()

# Problem 5
# line plot for total jobs created for each month


def get_month(date_str):
    return datetime.strptime(date_str, "%m/%d/%Y").strftime("%b")


def get_date(date_str):
    return datetime.strptime(date_str, "%m/%d/%Y").strftime("%Y %m")


data["Month"] = data['Effective Date'].apply(get_month)
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
data['Month'] = pd.Categorical(data['Month'], categories=months, ordered=True)
jobs_per_month = data.groupby(['Month']).sum()

fig, ax = plt.subplots()
plt.xticks(rotation=45)
plt.plot(jobs_per_month.index, jobs_per_month['Job created'])
ax.set_xlabel('Months')
ax.set_ylabel('Jobs_Created')
ax.set_title("Jobs_Created_Month")
plt.show()
