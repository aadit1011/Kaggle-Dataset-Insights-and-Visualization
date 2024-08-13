import matplotlib.pyplot as plt 
import pandas as pd 

# Load the dataset from a CSV file
# This dataset contains information about car sales from 2010 to 2020, including the car company and the price in USD.
data = pd.read_csv('D:\\Python\\Pandas\\cars_2010_2020.csv')


# Extract a list of unique car companies from the 'Company' column in the dataset.
# This list will be used to categorize the data by each car company.
cars = data['Company'].unique()

# Initialize an empty list to store the total sales for each car company.
total_sales = []

# Loop through each car company and calculate the total sales for the period 2010-2020.
# For each company, filter the data to include only rows corresponding to that company, 
# then sum the 'Price (USD)' values to get the total sales for that company.
for car in cars: 
    company_data = data[data['Company'] == car]  # Filter the dataset to include only the current company
    total_price = company_data['Price (USD)'].sum()  # Calculate the total sales for the current company
    total_sales.append(total_price)  # Add the total sales to the 'total_sales' list

# Define a list of colors to use for the bars in the bar chart.
# The list is repeated to ensure there are enough colors for all companies, 
# even if the number of companies exceeds the number of colors in the list.
colors = ['r', 'b', 'g', 'y'] * (len(cars) // 4 + 1)  # Repeat colors if needed

# Create a bar chart to visualize the total sales for each car company between 2010-2020.
plt.figure(figsize=(10, 6))  # Set the size of the figure to ensure the chart is easy to read
plt.bar(cars, total_sales, color=colors[:len(cars)])  # Create the bar chart with appropriate colors
plt.xlabel('Car Company', fontsize=12)  # Label the x-axis as 'Car Company'
plt.ylabel('Total Sales (USD)', fontsize=12)  # Label the y-axis as 'Total Sales (USD)'
plt.title('Total Sales Between 2010-2020', fontsize=16)  # Set the title of the chart
plt.xticks(rotation=90)  # Rotate the x-axis labels by 90 degrees to make them easier to read
plt.tight_layout()  # Adjust the layout to ensure everything fits within the figure
plt.show()  # Display the bar chart

# Extract a list of unique years from the 'Year' column in the dataset.
# This list will be used to generate separate charts for each year.
years = data['Year'].unique()

# Loop through each year to create a bar chart showing the sales data for all companies in that specific year.
for year in years: 
    yearly_data = data[data['Year'] == year]  # Filter the dataset to include only data for the current year
    price = []  # Initialize an empty list to store the sales data for the current year
    
    # Loop through each car company and calculate the total sales for that company in the current year.
    # For each company, filter the data to include only rows corresponding to that company and year,
    # then sum the 'Price (USD)' values to get the total sales for that company in that year.
    for car in cars: 
        company_year_data = yearly_data[yearly_data['Company'] == car]  # Filter data for the current company and year
        total = company_year_data['Price (USD)'].sum()  # Calculate the total sales for the current company and year
        price.append(total)  # Add the total sales to the 'price' list
    
    # Create a bar chart to visualize the sales data for the current year.
    plt.figure(figsize=(10, 6))  # Set the size of the figure for readability
    plt.bar(cars, price, color=colors[:len(cars)])  # Create the bar chart with appropriate colors
    plt.xlabel('Car Company', fontsize=12)  # Label the x-axis as 'Car Company'
    plt.ylabel('Total Sales (USD)', fontsize=12)  # Label the y-axis as 'Total Sales (USD)'
    plt.title(f'Total Sales in Year {year}', fontsize=16)  # Set the title to indicate the specific year
    plt.xticks(rotation=90)  # Rotate the x-axis labels by 90 degrees for readability
    plt.tight_layout()  # Adjust the layout to fit everything within the figure
    plt.show()  # Display the bar chart for the current year
