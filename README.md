# 🍽️ Zomato Data Analysis Project

This project performs an in-depth exploratory data analysis (EDA) on a Zomato restaurant dataset using Python and its powerful libraries like Pandas, NumPy, Matplotlib, and Seaborn. The goal is to derive meaningful insights into restaurant trends such as online ordering, table booking, restaurant type, cost analysis, and rating distribution.

---

## 📂 Dataset Overview

The dataset contains information about restaurants listed on Zomato, including:

- `name`: Name of the restaurant
- `online_order`: Whether online ordering is available
- `book_table`: Whether table booking is available
- `rate`: Overall rating given by users
- `votes`: Number of votes received
- `approx_cost(for two people)`: Estimated cost for two people
- `listed_in(type)`: Type of service (e.g., Buffet, Cafes, Dining, etc.)

---

## 📊 Objectives

- Clean the dataset and handle missing or inconsistent data
- Visualize key trends in customer preferences
- Understand how online ordering, table booking, and cost impact ratings
- Identify the most popular types of restaurants and services

---

## 🛠️ Tools Used

- **Python**: Programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical operations
- **Matplotlib**: Plotting and visualization
- **Seaborn**: Advanced data visualization

---

## 🧹 Data Cleaning

The following steps were taken to clean the dataset:

- Removed rows with missing values using `dropna()`
- Removed duplicate records using `drop_duplicates()`
- Transformed the `rate` column by splitting values like `4.1/5` to just `4.1`
- Replaced invalid rating values such as `'NEW'` and `'-'` with `NaN`
- Converted cost and rate columns to numerical types for analysis

---

## 📈 Data Analysis & Visualizations

Key analysis performed includes:

- **Online Order vs Rating**  
  Checked whether restaurants with online ordering have better ratings.

- **Table Booking vs Rating**  
  Explored if restaurants that allow table bookings perform better in ratings.

- **Restaurant Type Distribution**  
  Counted different service types like Buffet, Cafes, Dining, etc.

- **Votes vs Rating Scatterplot**  
  Checked if more votes lead to better ratings.

- **Cost vs Rating Analysis**  
  Analyzed how price affects customer ratings.

- **Top Rated Restaurants**  
  Identified best-rated restaurants based on average ratings and vote count.

- **Heatmap of Correlations**  
  Plotted correlation between numerical fields like rating, cost, and votes.

---

## 📌 Insights & Conclusions

- Restaurants offering **online ordering** generally received **higher ratings**.
- **Buffet and Cafe** type restaurants were most frequent and best-rated.
- **Higher number of votes** often correlated with **higher ratings**, but not always.
- There is no strong linear correlation between **cost and rating**, implying affordability doesn't guarantee satisfaction.

---

## 🧾 How to Run This Project

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/zomato-analysis.git
   cd zomato-analysis
