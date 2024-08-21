import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

# Part 1: Sum of Popular Cities Population by Country (2023-2024)

# Read the CSV file containing city population data
data = pd.read_csv('World Largest Cities by Population 2024.csv')

# Initialize empty lists to store countries and their total populations
country = []
pop2023 = []
pop2024 = []

# Get a list of unique countries from the data
countries = data['Country'].unique()

# Loop through each country to calculate the sum of populations for 2023 and 2024
for c in countries:
    country.append(c)  # Append the country name to the list
    
    # Calculate the total population for 2023 for the country
    total_pop2023 = data[data['Country'] == c]['Population (2023)'].sum()
    pop2023.append(total_pop2023)  # Append the total population for 2023
    
    # Calculate the total population for 2024 for the country
    total_pop2024 = data[data['Country'] == c]['Population (2024)'].sum()
    pop2024.append(total_pop2024)  # Append the total population for 2024

# Define the width of the bars and the position of the bars on the x-axis
width = 0.6
position = np.arange(len(country)) * 2  # Adjust position to increase space between bars

# Create the bar plot
plt.figure(figsize=(20, 10))
plt.bar(position - width/2, pop2023, width=width, color='red', label='Population-2023')
plt.bar(position + width/2, pop2024, width=width, color='blue', label='Population-2024')

# Add a legend, title, and labels to the plot
plt.legend(loc='upper right', fontsize=20)
plt.title('Sum of Popular Cities Population by Country (2023-2024)', fontsize=30)
plt.xlabel('Country', fontsize=14)
plt.ylabel('Total Population', fontsize=14)

# Adjust layout for better readability
plt.tight_layout() 
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.3)

# Add gridlines and set the x-ticks to display the country names with rotation
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.xticks(ticks=position, labels=country, rotation=90, fontsize=10)

# Display the plot
plt.show()

# Part 2: Population Comparison for a Specific Country's Cities (2023-2024)

# Prompt the user to input a country's name
name = input('Enter the name of the country: ')

# Filter the dataset for the selected country
country_data = data[data['Country'] == name]

# Initialize empty lists to store city names and their populations for 2023 and 2024
city = []
p2023 = []
p2024 = []

# Get a list of unique cities within the selected country
cities = country_data['City'].unique()

# Loop through each city to get its population data for 2023 and 2024
for c in cities:
    city.append(c)  # Append the city name to the list
    
    # Extract the population for 2023 and 2024
    pop2023 = country_data[country_data['City'] == c]['Population (2023)'].values[0]
    pop2024 = country_data[country_data['City'] == c]['Population (2024)'].values[0]
    
    # Append the populations to their respective lists
    p2023.append(pop2023)
    p2024.append(pop2024)

# Define the width of the bars and the position of the bars on the x-axis
width = 0.6
position = np.arange(len(city)) * 1.5  # Adjust position to increase space between bars

# Create the bar plot
plt.figure(figsize=(30, 15))
plt.bar(position - width/2, p2023, color='red', label='Population 2023', width=width)
plt.bar(position + width/2, p2024, color='blue', label='Population 2024', width=width)

# Add a legend, title, and labels to the plot
plt.legend(loc='upper right', fontsize=30)
plt.xlabel('City', fontsize=20)
plt.ylabel('Population', fontsize=20)

# Adjust layout for better readability
plt.tight_layout()

# Customize the y-axis and x-axis for readability
plt.yticks(fontsize=20)
plt.xticks(ticks=position, labels=city, rotation=90, fontsize=20)

# Add gridlines to the plot
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Print a summary message
print(f'The total data of {len(city)} cities are displayed.')

# Display the plot
plt.show()
