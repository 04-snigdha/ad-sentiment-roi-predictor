import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/facebook_ads.csv")

# Remove rows with 0 impressions to avoid divide-by-zero
df = df[df['impressions'] > 0]

# Add CTR column
df['CTR'] = df['clicks'] / df['impressions']

# Basic info
print("🔍 Dataset shape:", df.shape)
print("\n📊 Columns:", df.columns.tolist())
print("\n📈 CTR summary:")
print(df['CTR'].describe())

# CTR distribution plot
plt.figure(figsize=(8, 5))
sns.histplot(df['CTR'], bins=30, kde=True)
plt.title("Click-Through Rate (CTR) Distribution")
plt.xlabel("CTR (clicks/impressions)")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("data/ctr_distribution.png")
plt.show()

# Save cleaned dataset
df.to_csv("data/facebook_ads_cleaned.csv", index=False)
print("✅ Cleaned dataset saved to data/facebook_ads_cleaned.csv")