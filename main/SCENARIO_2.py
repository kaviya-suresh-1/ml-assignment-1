
import matplotlib
matplotlib.use("TkAgg")

import pandas as pd
import matplotlib.pyplot as plt
print("S.KAVIYA - 24BAD059")


df = pd.read_csv(
    r"C:\Users\Kaviya\Desktop\Machine_learning_lab\diabetes.csv"
)



print("HEAD:\n", df.head())
print("\nINFO:")
df.info()
print("\nDESCRIBE:\n", df.describe())


print("\nMissing Values:\n", df.isnull().sum())
print("\nZero Values (treated as missing):\n")
print((df == 0).sum())


plt.figure()
plt.hist(df["Glucose"], bins=20)
plt.title("Glucose Level Distribution")
plt.xlabel("Glucose")
plt.ylabel("Frequency")
plt.show()


plt.figure()
plt.hist(df["Age"], bins=20)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()


plt.figure()
plt.boxplot(df["Glucose"])
plt.title("Boxplot of Glucose Levels")
plt.ylabel("Glucose")
plt.show()


plt.figure()
plt.boxplot(df["Age"])
plt.title("Boxplot of Age")
plt.ylabel("Age")
plt.show()


print("\nObservations:")
print("- Zero values in Glucose, BloodPressure, SkinThickness, Insulin, and BMI indicate missing data.")
print("- Glucose shows wide spread and outliers, linked to diabetes risk.")
print("- Age distribution is right-skewed, with more patients in younger age groups.")