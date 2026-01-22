import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("marketing_campaign.csv", sep="\t")

print(df.head())
df.info()
print(df.describe())
print(df.isnull().sum())

df["Age"] = 2025 - df["Year_Birth"]

spend_cols = [
    "MntWines", "MntFruits", "MntMeatProducts",
    "MntFishProducts", "MntSweetProducts", "MntGoldProds"
]
df["Total_Spending"] = df[spend_cols].sum(axis=1)

plt.figure()
df["Age"].value_counts().sort_index().head(15).plot(kind="bar")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

plt.figure()
plt.boxplot(df["Income"].dropna())
plt.ylabel("Income")
plt.show()

plt.figure()
plt.boxplot(df["Total_Spending"])
plt.ylabel("Total Spending")
plt.show()

print("Income contains missing values.")
print("Most customers are middle-aged.")
print("Spending shows high variability with outliers.")
print("Income and spending help in customer segmentation.")