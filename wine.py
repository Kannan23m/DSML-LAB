import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine

# Load the wine dataset
wine_bunch = load_wine()
wine_df = pd.DataFrame(wine_bunch.data, columns=wine_bunch.feature_names)

# Add target and class labels
wine_df['target'] = wine_bunch.target
wine_df['class'] = wine_df['target'].map(dict(enumerate(wine_bunch.target_names)))

# Basic info
print("Wine Dataset Shape:", wine_df.shape)
print("\nFirst 5 Rows:")
print(wine_df.head())

print("\nData Types and Nulls:")
print(wine_df.info())

print("\nSummary Statistics:")
print(wine_df.describe())

print("\nMissing Values:")
print(wine_df.isnull().sum())

print("\nClass Distribution:")
print(wine_df['class'].value_counts())

# Countplot of wine classes
sns.countplot(x='class', data=wine_df, palette='pastel')
plt.title("Wine Class Distribution")
plt.show()

# Pairplot
sns.pairplot(wine_df, hue='class', corner=True)
plt.suptitle("Pairplot of Wine Dataset", y=1.02)
plt.show()

# Correlation heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(wine_df.drop(['target', 'class'], axis=1).corr(), annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Correlation Matrix of Wine Features")
plt.tight_layout()
plt.show()

# Boxplot for all features
plt.figure(figsize=(15, 10))
wine_df.drop(['target', 'class'], axis=1).plot(
    kind='box', subplots=True, layout=(4, 4), figsize=(15, 10), sharex=False, 
    patch_artist=True, boxprops=dict(facecolor='lightblue', color='blue'))
plt.suptitle("Boxplots of Wine Features", fontsize=16)
plt.tight_layout()
plt.show()

# Violin plots for selected features
selected_features = wine_df.columns[:6]  # First 6 features
plt.figure(figsize=(12, 10))
for i, col in enumerate(selected_features):
    plt.subplot(2, 3, i + 1)
    sns.violinplot(x='class', y=col, data=wine_df, palette='Set2')
    plt.title(f'{col} by Class')
plt.tight_layout()
plt.show()

# Histograms of all features
wine_df.drop(['target', 'class'], axis=1).hist(figsize=(15, 12), bins=20, edgecolor='black', color='skyblue')
plt.suptitle("Feature Distributions in Wine Dataset", fontsize=16)
plt.tight_layout()
plt.show()
