import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

print("S.KAVIYA - 24BAD059")
df = pd.read_csv("C:\\Users\\Kaviya\\Desktop\\Machine_learning_lab\\Housing.csv")

print("COLUMNS:\n", df.columns)
print("\nHEAD:\n", df.head())
print("\nINFO:")
df.info()
print("\nDESCRIBE:\n", df.describe())

missing = df.isnull().sum()
print("\nMissing Values per Column:\n", missing[missing > 0])

numerical_features = ["area", "bedrooms", "bathrooms", "stories"]

for feature in numerical_features:
    plt.figure()
    plt.scatter(df[feature], df["price"])
    plt.title(f"Price vs {feature}")
    plt.xlabel(feature.capitalize())
    plt.ylabel("Price")
    plt.show()

corr = df.select_dtypes(include=np.number).corr()

plt.figure()
plt.imshow(corr)
plt.colorbar()
plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.title("Correlation Heatmap of Numerical Features")
plt.show()

print("\nKey Insights:")
print("- Area shows a strong positive correlation with house price.")
print("- Bathrooms and bedrooms moderately influence price.")
print("- Missing values can bias predictions and should be handled before modeling.")
print("- Strong correlations help identify important features for regression models.")