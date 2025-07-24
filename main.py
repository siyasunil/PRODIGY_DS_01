import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv", skiprows=4)

top10_2020 = df[['Country Name', '2020']].dropna()
top10_2020 = top10_2020.sort_values(by='2020', ascending=False).head(10)

plt.figure(figsize=(12, 6))
plt.bar(top10_2020['Country Name'], top10_2020['2020'], color='steelblue')
plt.title('Top 10 Countries/Regions by Population in 2020')
plt.xlabel('Country')
plt.ylabel('Population')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()