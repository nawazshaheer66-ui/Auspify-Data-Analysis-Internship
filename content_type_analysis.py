import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the cleaned dataset
df = pd.read_csv('cleaned_netflix_dataset.csv')

# Step 2: Calculate total counts and percentages
type_counts = df['type'].value_counts()
type_percentages = df['type'].value_counts(normalize=True) * 100

print("--- Content Type Analysis Summary ---")
print(f"Total Movies: {type_counts['Movie']} ({type_percentages['Movie']:.1f}%)")
print(f"Total TV Shows: {type_counts['TV Show']} ({type_percentages['TV Show']:.1f}%)")

# Step 3: Create visualizations
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Bar Chart
palette = ['#E50914', '#221F1F']
sns.barplot(x=type_counts.index, y=type_counts.values, ax=axes[0], palette=palette)
axes[0].set_title('Netflix Content Count by Type', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Content Type', fontsize=12)
axes[0].set_ylabel('Total Count', fontsize=12)

# Annotate bar totals
for p in axes[0].patches:
    axes[0].annotate(f'{int(p.get_height()):,}', 
                    (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', xytext=(0, 8), 
                    textcoords='offset points', fontweight='bold')

# Pie Chart
axes[1].pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', 
            startangle=140, colors=palette, explode=(0.05, 0), 
            textprops={'fontsize': 12, 'fontweight': 'bold'})
axes[1].set_title('Proportion of Content Types', fontsize=14, fontweight='bold')

# Step 4 & 5: Save figure
plt.tight_layout()
plt.savefig('content_type_dashboard.png', dpi=300)
print("\nVisualization dashboard saved as 'content_type_dashboard.png'")