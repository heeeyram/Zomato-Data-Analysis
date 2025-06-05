import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Load Data
df = pd.read_csv("zomato.csv")  # Ensure this file is in the same folder
print("Initial Data:\n", df.head())

# Step 2: Data Cleaning
df.dropna(how="any", inplace=True)
df.drop_duplicates(inplace=True)

# Clean 'rate' column
df['rate'] = df['rate'].astype(str).apply(lambda x: x.split('/')[0])
df['rate'] = df['rate'].replace('NEW', np.nan).replace('-', np.nan).astype(float)

# Clean 'cost_for_two' column
df['approx_cost(for two people)'] = df['approx_cost(for two people)'].astype(str).str.replace(',', '')
df['approx_cost(for two people)'] = pd.to_numeric(df['approx_cost(for two people)'], errors='coerce')

# Rename columns
df.rename(columns={
    'approx_cost(for two people)': 'cost_for_two',
    'listed_in(type)': 'type',
    'listed_in(city)': 'city'
}, inplace=True)

# Step 3: Basic Info
print("\nCleaned Data Info:")
print(df.info())
print("\nNull Values:\n", df.isnull().sum())

# Step 4: Visualizations

# Online Order Count
plt.figure(figsize=(6,4))
sns.countplot(x='online_order', data=df)
plt.title('Online Order Availability')
plt.savefig("online_order.png")
plt.show()

# Book Table Count
plt.figure(figsize=(6,4))
sns.countplot(x='book_table', data=df)
plt.title('Table Booking Availability')
plt.savefig("book_table.png")
plt.show()

# Restaurant Type vs Average Rating
plt.figure(figsize=(10,6))
sns.barplot(x='type', y='rate', data=df, ci=None)
plt.xticks(rotation=45)
plt.title('Average Rating by Restaurant Type')
plt.savefig("type_vs_rating.png")
plt.show()

# Votes Distribution
plt.figure(figsize=(8,5))
sns.histplot(df['votes'], bins=30, kde=True)
plt.title('Votes Distribution')
plt.savefig("votes_distribution.png")
plt.show()

# Cost for Two Distribution
plt.figure(figsize=(8,5))
sns.histplot(df['cost_for_two'], bins=30, kde=True)
plt.title('Cost for Two Distribution')
plt.savefig("cost_distribution.png")
plt.show()

# Correlation Heatmap
plt.figure(figsize=(8,6))
sns.heatmap(df[['rate', 'votes', 'cost_for_two']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.savefig("correlation_heatmap.png")
plt.show()

# Step 5: Top Rated Restaurants
top_rated = df.sort_values(by='rate', ascending=False).head(10)
print("\nTop 10 Rated Restaurants:\n", top_rated[['name', 'rate', 'votes', 'cost_for_two']])

