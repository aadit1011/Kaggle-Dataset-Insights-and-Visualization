import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

# Load customer data from CSV
data = pd.read_csv('customers.csv')

# Extract unique country names
countries = data['Country'].unique()

# Initialize lists to hold population (number of customers) and corresponding country names
population = []
country = []

# Count the number of customers per country
for country_name in countries:
    # Filter the data for the current country
    count_per_country = data[data['Country'] == country_name]
    # Append the number of customers for this country
    population.append(len(count_per_country))
    # Append the country name to the list
    country.append(country_name)

# Create a list to 'explode' the slice with the maximum population for emphasis
# Explode the slice with the maximum population
explode = [0.1 if pop == max(population) else 0 for pop in population]

# Set up the pie chart for customer distribution by country
plt.figure(figsize=(8, 6), dpi=200)  # Set figure size (width x height) in inches and resolution (DPI)
plt.title('Customer Distribution According to the Country', fontsize=12, fontweight='bold', loc='center', pad=50)  # Add a title with specified font size and weight
plt.pie(population, labels=country, textprops={'fontsize': 10, 'fontweight': '300'}, autopct='%0.2f%%', radius=2.5, explode=explode)  # Create pie chart with labels, percentage display, and explode effect
plt.show()  # Display the pie chart

# Process subscription data
year = data['Subscription Date']

# Create a DataFrame for 'Subscription Date' and convert it to datetime format
df = pd.DataFrame(year)
df['Subscription Date'] = pd.to_datetime(df['Subscription Date'])

# Define month names for labeling purposes (index 0 is empty for alignment)
months = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# Extract year and month from 'Subscription Date' and add them as new columns
df['year'] = df['Subscription Date'].dt.year
df['month'] = df['Subscription Date'].dt.month

# Count subscriptions per year
subscription_counts_year = df['year'].value_counts().sort_index()  # Count occurrences of each year and sort by year

# Create a list to 'explode' the slice with the maximum subscription count for emphasis
# Explode the slice with the maximum subscription count
explode = [0.01 if subs == max(subscription_counts_year) else 0 for subs in subscription_counts_year]

# Set up the pie chart for subscription distribution by year
plt.figure(figsize=(8, 6), dpi=100)  # Set figure size and resolution
plt.title('Subscription Trend Per Year', fontsize=12, fontweight='bold', loc='center', pad=50)  # Add a title with specified font size and weight
plt.pie(subscription_counts_year, labels=subscription_counts_year.index, autopct='%0.2f%%', explode=explode, labeldistance=0.8)  # Create pie chart with labels, percentage display, and explode effect
plt.show()  # Display the pie chart

# Count subscriptions per month across all years
subscription_counts_month = df['month'].value_counts().sort_index()  # Count occurrences of each month and sort by month

# Create a list to 'explode' the slice with the maximum subscription count for emphasis
# Explode the slice with the maximum subscription count
explode = [0.1 if subs == max(subscription_counts_month) else 0 for subs in subscription_counts_month]

# Set up the pie chart for subscription distribution by month
plt.figure(figsize=(8, 6), dpi=100)  # Set figure size and resolution
plt.title('Subscription Trend Per Month', fontsize=12, fontweight='bold', loc='center', pad=50)  # Add a title with specified font size and weight
plt.pie(subscription_counts_month, labels=[months[i] for i in subscription_counts_month.index], autopct='%0.2f%%', explode=explode, labeldistance=0.85, radius=1)  # Create pie chart with labels (converted month indices to names), percentage display, and explode effect
plt.show()  # Display the pie chart
