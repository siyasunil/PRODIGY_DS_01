import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv", skiprows=4)


# Select a subset of countries (example: top 10 by 2024 population)
df = df[['Country Name', '1960', '2024']].dropna()
df['1960'] = df['1960'].astype(float)
df['2024'] = df['2024'].astype(float)

# Calculate Growth Rate (%) and Growth Factor
df['Growth Rate (%)'] = ((df['2024'] - df['1960']) / df['1960']) * 100
df['Growth Factor'] = (df['2024'] / df['1960'])

# Sort by growth rate (top 10)
df_sorted = df.sort_values('Growth Rate (%)', ascending=False).head(10)

# Plot
plt.figure(figsize=(12, 6))
bars = plt.bar(df_sorted['Country Name'], df_sorted['Growth Rate (%)'], color='red')

# Add annotations (Percentage + Growth Factor)
for bar, rate, factor in zip(bars, df_sorted['Growth Rate (%)'], df_sorted['Growth Factor']):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 10,
             f"{rate:.1f}%\n({factor:.1f}x)",
             ha='center', fontsize=10, color='black')

plt.title("Top 10 Countries by Population Growth (1960-2024)", fontsize=14)
plt.ylabel("Growth Rate (%)")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
