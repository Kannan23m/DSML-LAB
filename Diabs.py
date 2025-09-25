import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes

# Load data
diabetes = load_diabetes()
df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
df['target'] = diabetes.target

# Basic info
print("Shape:", df.shape)
print(df.head())
print(df.info())
print(df.describe())
print("Nulls:\n", df.isnull().sum())

# Heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(df.corr(), annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# Distribution of target
sns.histplot(df['target'], bins=30, kde=True, color='skyblue')
plt.title("Target Value Distribution (Diabetes Progression)")
plt.show()

# Pairplot for top 4 correlated features
top_corr = df.corr()['target'].abs().sort_values(ascending=False)[1:5].index
sns.pairplot(df[top_corr.to_list() + ['target']])
plt.suptitle("Top Correlated Features with Target", y=1.02)
plt.show()

# Boxplot
plt.figure(figsize=(12, 6))
sns.boxplot(data=df[top_corr])
plt.title("Boxplot of Top Correlated Features")
plt.show()
