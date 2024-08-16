# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
df = pd.read_csv('zomato_sales.csv')

# Clean and Preprocess Data
# Handle missing values
df.fillna(method='ffill', inplace=True)

# Remove duplicate entries
df.drop_duplicates(inplace=True)

# Convert data types
df['date'] = pd.to_datetime(df['date'])

# Extract useful information
df['month'] = df['date'].dt.month
df['city'] = df['address'].apply(lambda x: x.split(',')[-2])

# Exploratory Data Analysis (EDA)
# Descriptive statistics
print(df.describe())

# Distribution of restaurants across countries
plt.figure(figsize=(10, 6))
sns.countplot(y='country', data=df, order=df['country'].value_counts().index)
plt.title('Distribution of Restaurants Across Countries')
plt.xlabel('Number of Restaurants')
plt.ylabel('Country')
plt.show()

# Top cuisines by votes in India
top_cuisines = df[df['country'] == 'India']['cuisine'].value_counts().head(10)
plt.figure(figsize=(10, 6))
top_cuisines.plot(kind='bar', color='orange')
plt.title('Top 10 Cuisines by Votes in India')
plt.xlabel('Cuisine')
plt.ylabel('Number of Votes')
plt.show()

# Correlation heatmap
plt.figure(figsize=(10, 8))
correlation = df.corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# Answer Key Business Questions
# Total restaurants and total cuisines all over the world
total_restaurants = df['restaurant_id'].nunique()
total_cuisines = df['cuisine'].nunique()
print(f'Total Restaurants: {total_restaurants}')
print(f'Total Cuisines: {total_cuisines}')

# Which countries have the greatest number of restaurants enrolled in Zomato?
top_countries = df['country'].value_counts().head()
print('Top Countries by Number of Restaurants:')
print(top_countries)

# Which cities in India have the greatest number of "value for money" restaurants?
value_for_money_cities = df[(df['country'] == 'India') & (df['price_range'] == 1)]['city'].value_counts().head()
print('Top Cities in India with "Value for Money" Restaurants:')
print(value_for_money_cities)

# What are the top 10 cuisines that have the highest number of votes in India?
top_cuisines_india = df[df['country'] == 'India'].groupby('cuisine')['votes'].sum().sort_values(ascending=False).head(10)
print('Top 10 Cuisines by Number of Votes in India:')
print(top_cuisines_india)

# Which countries have restaurants that deliver online?
online_delivery_countries = df[df['online_delivery'] == 'Yes']['country'].unique()
print('Countries with Restaurants that Deliver Online:')
print(online_delivery_countries)

# In terms of the number of restaurants, which locality has the most?
top_locality = df['locality'].value_counts().head(1)
print(f'Locality with the Most Restaurants: {top_locality.index[0]} ({top_locality.values[0]} restaurants)')

# Which Restaurants have Good Cuisine and an average rating?
good_cuisine_restaurants = df[(df['rating'] >= 4) & (df['votes'] > 1000) & (df['price_range'] == 2)]
print('Restaurants with Good Cuisine and an Average Rating:')
print(good_cuisine_restaurants[['restaurant_name', 'cuisine', 'rating', 'votes']])

# Recommendations (Sample Output)
print("\nRecommendations:")
print("1. Focus on expanding in countries with high demand for online delivery.")
print("2. Promote the top cuisines in regions where they are underrepresented.")
print("3. Invest in cities with a high concentration of 'value for money' restaurants to attract budget-conscious customers.")
