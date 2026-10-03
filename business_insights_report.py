import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load cleaned dataset
df = pd.read_csv('cleaned_netflix_dataset.csv')

# Step 2: Configure layout style
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
palette_red = ['#E50914', '#221F1F']

# Panel 1: Content Type Proportions
type_counts = df['type'].value_counts()
axes[0, 0].pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', startangle=140, 
               colors=palette_red, explode=(0.05, 0), textprops={'fontsize': 11, 'fontweight': 'bold'})
axes[0, 0].set_title('1. Content Type Split (Movies vs TV Shows)', fontsize=13, fontweight='bold')

# Panel 2: Top 5 Global Content Hubs
top_countries = df[df['country'] != 'Not Given']['country'].value_counts().head(5)
sns.barplot(x=top_countries.values, y=top_countries.index, ax=axes[0, 1], palette="Reds_r")
axes[0, 1].set_title('2. Top 5 Global Content Hubs', fontsize=13, fontweight='bold')
axes[0, 1].set_xlabel('Number of Titles', fontsize=10)
for p in axes[0, 1].patches:
    width = p.get_width()
    axes[0, 1].annotate(f'{int(width):,}', (width, p.get_y() + p.get_height() / 2.),
                        ha='left', va='center', xytext=(5, 0), textcoords='offset points', fontweight='bold')

# Panel 3: Content Release Trend (2010-2021)
yearly_type = df[df['release_year'] >= 2010].groupby(['release_year', 'type']).size().unstack(fill_value=0)
axes[1, 0].plot(yearly_type.index, yearly_type['Movie'], marker='o', color='#E50914', linewidth=2, label='Movies')
axes[1, 0].plot(yearly_type.index, yearly_type['TV Show'], marker='s', color='#221F1F', linewidth=2, label='TV Shows')
axes[1, 0].set_title('3. Content Release Trend (2010–2021)', fontsize=13, fontweight='bold')
axes[1, 0].set_xlabel('Release Year', fontsize=10)
axes[1, 0].set_ylabel('Releases', fontsize=10)
axes[1, 0].legend(title='Type')

# Panel 4: Primary Audience Rating Categories
top_ratings = df['rating'].value_counts().head(6)
sns.barplot(x=top_ratings.index, y=top_ratings.values, ax=axes[1, 1], palette="Dark2")
axes[1, 1].set_title('4. Primary Audience Rating Categories', fontsize=13, fontweight='bold')
axes[1, 1].set_ylabel('Number of Titles', fontsize=10)
for p in axes[1, 1].patches:
    height = p.get_height()
    axes[1, 1].annotate(f'{int(height):,}', (p.get_x() + p.get_width() / 2., height),
                        ha='center', va='center', xytext=(0, 6), textcoords='offset points', fontweight='bold')

# Step 3: Save Executive Dashboard
plt.suptitle('Netflix Executive Business Intelligence Dashboard', fontsize=16, fontweight='bold', y=0.98)
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig('executive_business_dashboard.png', dpi=300)
print("Executive dashboard successfully generated and saved as 'executive_business_dashboard.png'")