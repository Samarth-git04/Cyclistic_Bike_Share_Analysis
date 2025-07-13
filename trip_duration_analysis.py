import pandas as pd 
import os 
import matplotlib.pyplot as plt 
import seaborn as sns

# Setting seaborn style
sns.set_style("whitegrid")

file_path = os.path.join(os.getcwd(), r'Data', 'trip_duration.csv')

df = pd.read_csv(file_path)

# Convert trip_duration column to timedeltas
df['trip_duration'] = pd.to_timedelta(df['trip_duration'])

# Convert duration to minutes
df['duration_minutes'] = df['trip_duration'].dt.total_seconds() / 60

# Separate data by member_casual type
member_df = df[df['member_casual'] == 'member']
casual_df = df[df['member_casual'] == 'casual']

mean_duration_casual = casual_df['duration_minutes'].mean()
mean_duration_member = member_df['duration_minutes'].mean()

print(f"Mean trip duration for Casual users: {mean_duration_casual:.2f} minutes")
print(f"Mean trip duration for Annual Members: {mean_duration_member:.2f} minutes")

plt.figure(figsize=(12, 6))
plt.hist(member_df['duration_minutes'], bins=50, density=True, color='blue', histtype='step', linewidth=2, label='Annual Members')
plt.hist(casual_df['duration_minutes'], bins=50, density=True, color='red', histtype='step', linewidth=2, label='Casual')
plt.xlim(0, 200)
plt.title('Trip Duration Histogram by Member Type', fontsize=16, fontweight='bold')
plt.xlabel('Trip Duration (minutes)', fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(frameon=True, fontsize=12)
plt.tight_layout()
plt.show()