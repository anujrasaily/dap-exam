import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load data
df = pd.read_csv("fitness_data.csv", parse_dates=["Date"])

# Ensure output directory exists
os.makedirs("outputs", exist_ok=True)

# Line Plot: Steps and Sleep
plt.figure(figsize=(10, 5))
sns.lineplot(x="Date", y="Steps", data=df, label="Steps")
sns.lineplot(x="Date", y="SleepHours", data=df, label="Sleep Hours")
plt.title("Daily Steps and Sleep Hours")
plt.xlabel("Date")
plt.ylabel("Count")
plt.legend()
plt.tight_layout()
plt.savefig("outputs/steps_sleep.png")

# Correlation Heatmap
plt.figure(figsize=(8, 6))
corr = df.drop(columns=["Date"]).corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Between Fitness Metrics")
plt.tight_layout()
plt.savefig("outputs/correlation_heatmap.png")

# Line Plot: Resting Heart Rate
plt.figure(figsize=(10, 5))
sns.lineplot(x="Date", y="RestingHeartRate", data=df, marker="o")
plt.title("Resting Heart Rate Over Time")
plt.xlabel("Date")
plt.ylabel("BPM")
plt.tight_layout()
plt.savefig("outputs/heart_rate.png")

# Bar Chart: Average Active Minutes per Week
df['Week'] = df['Date'].dt.isocalendar().week
weekly_avg = df.groupby('Week')['ActiveMinutes'].mean().reset_index()
plt.figure(figsize=(8, 5))
sns.barplot(x='Week', y='ActiveMinutes', data=weekly_avg)
plt.title("Average Active Minutes per Week")
plt.xlabel("Week Number")
plt.ylabel("Average Active Minutes")
plt.tight_layout()
plt.savefig("outputs/bar_active_minutes_weekly.png")

# Pie Chart: Proportion of Calories Burned per Week
weekly_cal = df.groupby('Week')['CaloriesBurned'].sum()
plt.figure(figsize=(6, 6))
weekly_cal.plot.pie(autopct='%1.1f%%')
plt.title("Weekly Calories Burned Distribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig("outputs/pie_calories_burned.png")

# Scatter Plot: Sleep vs Resting Heart Rate
plt.figure(figsize=(8, 5))
sns.scatterplot(x="SleepHours", y="RestingHeartRate", data=df)
plt.title("Sleep Hours vs. Resting Heart Rate")
plt.xlabel("Sleep Hours")
plt.ylabel("Resting Heart Rate")
plt.tight_layout()
plt.savefig("outputs/scatter_sleep_heart_rate.png")

print("All visualizations generated successfully.")