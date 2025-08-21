import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris_bunch = load_iris()
iris = pd.DataFrame(iris_bunch.data,columns = iris_bunch.feature_names)
iris['species'] = iris_bunch.target
iris['species'] = iris['species'].map(dict(enumerate(iris_bunch.target_names)))

print("shape of dataset:",iris.shape)
print("\n First 5 rows:")
print(iris.head())

print("\n Data types and Non-Nulls:")
print(iris.info())

print("\n summary statistics:")
print(iris.describe())

print("\n class missing values:")
print(iris.isnull().sum())

print("\n class distributioon:")
print(iris['species'].value_counts())

sns.pairplot(iris,hue='species',diag_kind='kde')
plt.suptitle("pairplot of iris features",y=1.02)
plt.show()

plt.figure(figsize=(8,6))
sns.heatmap(iris.drop('species',axis=1).corr(),annot=True,cmap='coolwarm')
plt.title("features correlation matrix")
plt.show()

plt.figure(figsize=(10,6))
sns.boxplot(data=iris.drop('species',axis=1))
plt.title("boxplot for each feature")
plt.show()
