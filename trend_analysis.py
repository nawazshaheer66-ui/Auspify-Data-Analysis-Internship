import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load cleaned dataset
df = pd.read_csv('cleaned_netflix_dataset.csv')

# Step 2: Organize content by release year (focusing on 2000–2021)
yearly_type = df[df['release_year'] >= 2000].groupby(['release_year', 'type']).size().unstack(fill_value=0)

print("--- Yearly Releases Summary (2015–2021) ---")
print(yearly_type.tail(7))

# Step 3: Create line plot for trend analysis
plt.figure(figsize=(12, 6))
sns.set_theme(style="whitegrid")

plt.plot(yearly_type.index, yearly_type['Movie'], marker='o', color='#E50914', linewidth=2.5, label='Movies')
plt.plot(yearly_type.index, yearly_type['TV Show'], marker='s', color='#221F1F', linewidth=2.5, label='TV Shows')

plt.title('Netflix Content Production Trend by Release Year (2000–2021)', fontsize=14, fontweight='bold')
plt.xlabel('Release Year', fontsize=12)
plt.ylabel('Number of Releases', fontsize=12)
plt.legend(title='Content Type', fontsize=11)
plt.xticks(range(2000, 2022, 2))

# Step 4: Save trend visualization
plt.tight_layout()
plt.savefig('yearly_trend_analysis.png', dpi=300)
print("\nVisualization saved as 'yearly_trend_analysis.png'")