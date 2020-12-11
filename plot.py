import matplotlib.dates as md
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Setting seaborn as default style even if use only matplotlib
sns.set()

# Read csv file and treat month and year as one, and hour separately
csvfile = './sim_time_resTol_1e-4_TSMP.csv'
TSMP_sim_times = pd.read_csv(csvfile, infer_datetime_format=True, parse_dates=[[0, 1], 2])

# Chooses only a subset of the data, because it would jump from 1965 to 1999
data_year = TSMP_sim_times[
    (TSMP_sim_times['year_month'] > '1999-01-01') & (TSMP_sim_times['year_month'] < '2000-01-01')]

# 2 rows of plots, 1 column, 14 per 8 inches
fig, ax = plt.subplots(figsize=(14, 8))
# plt.tight_layout()

# Removes date from y axis
ax.yaxis.set_major_formatter(md.DateFormatter('%H:%M:%S'))

# Set number of ticks on the plot according to the data
ax.xaxis.set_major_locator(plt.MaxNLocator(len(data_year) + 1))

# Rotates the labels and aligns to the right
ax.set_xticks(TSMP_sim_times["year_month"])
ax.set_xticklabels(TSMP_sim_times["year_month"], rotation=30, ha='right')

# Format X as December 1965 for example.
ax.xaxis.set_major_formatter(md.DateFormatter('%B %Y'))


# Plot
plot = sns.lineplot(ax=ax, data=data_year, x="year_month", y="sim_time", legend="full")
plot.set(xlabel='Date\n ← Older  Newer  →', ylabel='Execution time')

plt.show()
