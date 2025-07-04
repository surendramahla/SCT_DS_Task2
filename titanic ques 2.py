import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ===================== Load and Prepare Population Dataset =====================

# Load the dataset (skip metadata rows)
df = pd.read_csv(
    r"C:\Users\Asus\Downloads\API_SP.POP.TOTL_DS2_en_csv_v2_38144\API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv",
    skiprows=4
)

# Convert 2022 population column to numeric
df['2022'] = pd.to_numeric(df['2022'], errors='coerce')

# Drop rows with missing population data
df = df.dropna(subset=['2022'])

# ===================== 1. Histogram: Population Distribution =====================

plt.figure(figsize=(10, 6))
sns.histplot(df['2022'], bins=30, kde=True, color='skyblue')
plt.title("Population Distribution Across Countries (2022)")
plt.xlabel("Population")
plt.ylabel("Number of Countries")
plt.xscale('log')  # Use log scale for wide range of population
plt.tight_layout()
plt.show()

# ===================== 2. Bar Chart: Top 10 Most Populous Countries =====================

top10 = df[['Country Name', '2022']].sort_values(by='2022', ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(
    data=top10,
    y='Country Name',
    x='2022',
    hue='Country Name',
    palette='viridis',
    legend=False
)
plt.title("Top 10 Most Populous Countries (2022)")
plt.xlabel("Population")
plt.ylabel("Country")
plt.tight_layout()
plt.show()

# ===================== 3. Bar Chart: Age Distribution  =====================

# Sample age group data
age_groups = ['0–20', '21–40', '41–60', '61–80', '81+']
counts = [512, 680, 430, 210, 60]

plt.figure(figsize=(9, 5))
bars = plt.bar(age_groups, counts, color='mediumseagreen', edgecolor='black')

# Add value labels on top of each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 10, yval, ha='center', va='bottom')

plt.xlabel('Age Groups')
plt.ylabel('Number of People')
plt.title('Age Distribution')
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.show()
