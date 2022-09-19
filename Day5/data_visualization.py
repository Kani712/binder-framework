from bdb import effective
import matplotlib.pyplot as plt

# fig, ax = plt.subplots()
# ax.plot([1, 2, 3, 4, 5], [1, 3, 5, 2, 4])
# plt.show()

from itertools import count
from xml import dom
import pandas as pd
import matplotlib.dates as mdates

data = pd.read_csv(
    "C:\kani\Data_Incubator\Day4\Value_of_Energy_Cost_Savings_Program_Savings_for_Businesses_-_FY2020.csv")
# print(data.head())
# print(data.columns)
# data["Job created"] = data['Job created']
# data['Total Savings'] = data['Total Savings']

plt.scatter('Job created', 'Total Savings', data=data)
plt.xlabel("Job created")
plt.ylabel("Total Savings")
plt.show()


date = data['Effective Date']
value = data['Job created']

fig, ax = plt.subplots(figsize=(8, 6))

half_year_locator = mdates.MonthLocator(interval=6)
year_month_formatter = mdates.DateFormatter(
    "%Y-%m")  # four digits for year, two for month

ax.xaxis.set_major_locator(half_year_locator)
# formatter for major axis only
ax.xaxis.set_major_formatter(year_month_formatter)

ax.plot(date, value)

plt.show()
