import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load cleaned dataset
df = pd.read_csv('cleaned_netflix_dataset.csv')

# Step 2: Extract content count by country (excluding 'Not Given')
country_counts = df[df['country'] != 'Not Given']['country'].value_counts()
top_10_countries = country_counts.head(10)

print("--- Top 10 Content-Producing Countries ---")
print(top_10_countries)

# Step 3: Create visualization
plt.figure(figsize=(12, 6))
sns.set_theme(style="whitegrid")
palette = sns.color_palette("Reds_r", 10)

ax = sns.barplot(x=top_10_countries.values, y=top_10_countries.index, palette=palette)
plt.title('Top 10 Content-Producing Countries on Netflix', fontsize=14, fontweight='bold')
plt.xlabel('Number of Titles', fontsize=12)
plt.ylabel('Country', fontsize=12)

# Annotate bar totals
for p in ax.patches:
    width = p.get_width()
    ax.annotate(f'{int(width):,}', 
                (width, p.get_y() + p.get_height() / 2.),
                ha='left', va='center', xytext=(5, 0), 
                textcoords='offset points', fontweight='bold')

# Step 4: Save plot image
plt.tight_layout()
plt.savefig('country_content_analysis.png', dpi=300)
print("\nVisualization saved as 'country_content_analysis.png'")