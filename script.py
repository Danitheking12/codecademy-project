import codecademylib3  # Codecademy’s helper library (needed for running on their platform)
import pandas as pd     # Import pandas for data analysis

# Read the inventory dataset into a pandas DataFrame
inventory = pd.read_csv('inventory.csv')

# Select the first 10 rows (products) for Staten Island store
staten_island = inventory.head(10)

# Get only the product descriptions from the Staten Island store
product_request = staten_island.product_description

# Create a new column 'in_stock' that is True if quantity > 0, otherwise False
inventory['in_stock'] = inventory.quantity.apply(lambda x: True if x > 0 else False)

# Filter inventory: only rows where location is 'Brooklyn' and product_type is 'seeds'
seed_request = inventory[(inventory.location == 'Brooklyn') & (inventory.product_type == 'seeds')]

# Create a new column 'total_value' = price × quantity (total worth of that item in stock)
inventory['total_value'] = inventory.price * inventory.quantity

# Define a function that combines product_type and product_description into one string
combine_lambda = lambda row: '{} - {}'.format(row.product_type,
                                              row.product_description)

# Apply the combine_lambda function row by row → create 'full_description' column
inventory['full_description'] = inventory.apply(combine_lambda, axis=1)

# Print the final inventory DataFrame with all new columns
print(inventory)
