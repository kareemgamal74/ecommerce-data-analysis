import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv(r"C:\Users\AdminOS\Desktop\python\amazon data\amazon.csv")
pd.set_option("display.max_columns",None)
pd.set_option("display.max_rows",None)
pd.set_option("display.max_colwidth", None)

df = df.dropna(subset=["rating_count"])
# print(df.isnull().sum())
print(df.duplicated().sum())
print(df.dtypes)
df["discounted_price"] =df["discounted_price"].str.replace("₹","",regex=False)
df["discounted_price"] =df["discounted_price"].str.replace(",","",regex=False)
df["discounted_price"] = pd.to_numeric(df["discounted_price"],errors="coerce")

df['actual_price'] = df['actual_price'].str.replace('₹', '', regex=False)
df['actual_price'] = df['actual_price'].str.replace(',', '', regex=False)
df['actual_price'] = pd.to_numeric(df['actual_price'], errors='coerce')

df['discount_percentage'] = df['discount_percentage'].str.replace('%', '', regex=False)
df['discount_percentage'] = pd.to_numeric(df['discount_percentage'], errors='coerce')


df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
df['rating_count'] = df['rating_count'].str.replace(',', '', regex=False)
df["rating_count"] = pd.to_numeric(df["rating_count"],errors = "coerce")


# df['rating_count'] = pd.to_numeric(df['rating_count'], errors='coerce')
# print("number oc rows:", df.shape[0])
# print("number of cloumns :", df.shape[1])
# print("number of Categories:", df['category'].nunique())
# print("number of uniqe item :", df['product_id'].nunique())
# print("max disscount : ", df['discount_percentage'].max(), "%")
# print("max rate :", df['rating'].max())

top_products = df.groupby("product_name")["rating_count"].sum().sort_values(ascending=False).head(10)
top_categories = df.groupby('category')['rating_count'].sum().sort_values(ascending=False).head(10)
print(top_products)
print(top_categories)
print("avvarage actual price : ", df['actual_price'].mean())
print(" avvarage discounted price: ", df['discounted_price'].mean())
plt.figure(figsize=(12,6))
sns.barplot(y=top_products.index, x=top_products.values,palette='crest')
plt.title('Top 10 Products by Total Rating Count')
plt.xlabel('Total Rating Count')
plt.ylabel('Product Name')
plt.tight_layout()
plt.show()

plt.figure(figsize=(12,6))
sns.barplot(x=top_categories.values, y=top_categories.index, palette='magma')
plt.title('Top 10 Categories by Total Rating Count')
plt.xlabel('Total Rating Count')
plt.ylabel('Category')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,5))
sns.histplot(df['discount_percentage'], bins=30, kde=True, color='skyblue')
plt.title('Distribution of Discount Percentage')
plt.xlabel('Discount Percentage')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

prices = pd.DataFrame({
    'Price Type': ['Actual Price', 'Discounted Price'],
    'Average Price': [df['actual_price'].mean(), df['discounted_price'].mean()]
})

plt.figure(figsize=(8,5))
sns.barplot(x='Price Type', y='Average Price', data=prices, palette='Set2')
plt.title('Average Actual Price vs Discounted Price')
plt.ylabel('Average Price')
plt.tight_layout()
plt.show()





# print(df.info())
# print(df.describe())
# print(df.head(5))