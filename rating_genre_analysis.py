import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load cleaned dataset
df = pd.read_csv('cleaned_netflix_dataset.csv')

# Step 2: Analyze rating categories
top_ratings = df['rating'].value_counts().head(8)

# Step 3: Explode comma-separated genres in 'listed_in'
genres_series = df['listed_in'].str.split(', ').explode()
top_genres = genres_series.value_counts().head(10)

print("--- Top 8 Ratings ---")
print(top_ratings)
print("\n--- Top 10 Genres ---")
print(top_genres)

# Step 4: Create visualizations
fig, axes = plt.subplots(1, 2, figsize=(16, 6))
sns.set_theme(style="whitegrid")

# Ratings Plot
sns.barplot(x=top_ratings.values, y=top_ratings.index, ax=axes[0], palette="Reds_r")
axes[0].set_title('Top 8 Netflix Content Ratings', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Count', fontsize=12)

for p in axes[0].patches:
    width = p.get_width()
    axes[0].annotate(f'{int(width):,}', (width, p.get_y() + p.get_height() / 2.),
                     ha='left', va='center', xytext=(5, 0), textcoords='offset points', fontweight='bold')

# Genres Plot
sns.barplot(x=top_genres.values, y=top_genres.index, ax=axes[1], palette="Dark2")
axes[1].set_title('Top 10 Netflix Genres', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Count', fontsize=12)

for p in axes[1].patches:
    width = p.get_width()
    axes[1].annotate(f'{int(width):,}', (width, p.get_y() + p.get_height() / 2.),
                     ha='left', va='center', xytext=(5, 0), textcoords='offset points', fontweight='bold')

# Save Dashboard
plt.tight_layout()
plt.savefig('rating_genre_dashboard.png', dpi=300)
print("\nDashboard saved as 'rating_genre_dashboard.png'")