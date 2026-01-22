print("KAVIYA- 24BAD059")
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(
    "C:/Users/Kaviya/Desktop/Machine_learning_lab/lab 1.csv",
    encoding="ISO-8859-1"
)


print("HEAD:\n", df.head())
print("\nTAIL:\n", df.tail())
print("\nINFO:")
df.info()
print("\nDESCRIBE:\n", df.describe(include="all"))

print("\nMissing Values:\n", df.isnull().sum())

sales_per_product = df.groupby("Description")["Quantity"].sum().head(10)


plt.figure()
sales_per_product.plot(kind="bar")
plt.title("Top 10 Products by Sales Quantity")
plt.xlabel("Product")
plt.ylabel("Total Quantity Sold")
plt.show()


plt.figure()
sales_per_product.plot(kind="line", marker="o")
plt.title("Sales Trend of Top 10 Products")
plt.xlabel("Product")
plt.ylabel("Total Quantity Sold")
plt.show()