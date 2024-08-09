import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data from the CSV file
data = pd.read_csv('D:\\Python\\Pandas\\cars_2010_2020.csv')

# Print the unique list of car companies available in the dataset
companies = data['Company'].unique()
print(f"Available car companies in the dataset:\n{companies}\n")

# Prompt the user to input the name of the company they want to analyze
company_name = input('Enter the name of the company you want to see the total details for: ').strip()

def company_model_details(company_name):
    """
    Display the detailed sales information for all models of a specific company.
    Also, visualize the total sales for each model using matplotlib.
    
    Parameters:
    company_name (str): The name of the company to analyze.
    """

    # Filter the dataset to only include rows for the selected company
    company_data = data[data['Company'] == company_name]
    
    # Extract the unique car models offered by the company
    models = company_data['Model'].unique()
    
    # Count the total number of distinct models offered by the company
    total_models = len(models)
    
    print(f'\n{company_name} has offered a total of {total_models} models between 2010 and 2020.\n')
    
    print('The models offered are:')
    # Display each model in a separate line for clarity
    for model in models: 
        print(f'- {model}')
    
    print(f'\nSales analysis for each model of {company_name}:\n')
    
    # Prepare data for visualization
    model_names = []
    total_sales = []
    
    # Define an inner function to display sales details for each model
    def model_detail(model):
        # Filter data for the specific model
        detail = company_data[company_data['Model'] == model]
        
        # Get the unique fuel types for the model
        fuel_types = detail['Fuel Type'].unique()
        
        # Calculate the total sales price for the model
        total_price = detail['Price (USD)'].sum()
        
        # Store the model name and total sales for plotting
        model_names.append(model)
        total_sales.append(total_price)
        
        # Display sales information by fuel type
        for engine in fuel_types:
            # Filter data for the specific engine type and sum the sales
            engine_total_price = detail[detail['Fuel Type'] == engine]['Price (USD)'].sum()
            print(f'{model} model with {engine} engine sold for a total worth of ${engine_total_price:.2f}')
        
        # Display the total sales of the model across all engine types
        print(f'Total sales for {model} model: ${total_price:.2f}\n')
    
    # Iterate over each model and display its sales details
    for model in models:
        model_detail(model)
    
    # Plotting the total sales for each model
    plt.figure(figsize=(10, 6))
    plt.barh(model_names, total_sales, color='skyblue')
    plt.xlabel('Total Sales (USD)')
    plt.ylabel('Car Model')
    plt.title(f'Total Sales by Model for {company_name}')
    plt.grid(True)
    plt.show()

def company_detail(company_name): 
    """
    Display the total sales information for the entire company.
    
    Parameters:
    company_name (str): The name of the company to analyze.
    """
    
    # Filter the dataset for the selected company
    detail = data[data['Company'] == company_name]
    
    # Calculate the total sales for the company
    total_sale = detail['Price (USD)'].sum()
    
    print(f'\nHence, the total sales done by {company_name} is ${total_sale:.2f}')

# Display total sales for the selected company
company_detail(company_name)

# Display detailed sales information for each model of the selected company
company_model_details(company_name)
