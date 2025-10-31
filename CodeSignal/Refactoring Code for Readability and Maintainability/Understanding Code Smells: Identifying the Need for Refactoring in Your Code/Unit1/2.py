#def calculate_total_bill(product_quantities, product_prices):
    # Start with a total bill amount of 0
#    total_bill = 0
    # Loop through each product in product_quantities dictionary
#    for product in product_quantities:
        # For each product, find the quantity
#        quantity = product_quantities[product]
        # Find the unit price of the product from product_prices dictionary
#        unit_price = product_prices.get(product, 0)
        # Calculate the total price for the product
#        total_price = quantity * unit_price
        # Add the total price of the current product to the total bill
#        total_bill += total_price
    # Return the final total bill
#    return total_bill

def calculate_total_bill(quantities, prices):
    
    plist = zip(quantities.values(), prices.values())
    
    return sum([p[0] * p[1] for p in plist])

# Product quantities and prices
quantities = {'apple': 2, 'banana': 5, 'cherry': 15}
prices = {'apple': 0.50, 'banana': 0.30, 'cherry': 0.20}

ans = calculate_total_bill(quantities, prices)

# Compute the total bill for the products
#total_bill = calculate_total_bill(quantities, prices)

print(f"Total Bill: ${ans:.2f}")

#def calculate_total_bill(product_quantities, product_prices):
    # Start with a total bill amount of 0
#    total_bill = 0
    # Loop through each product in product_quantities dictionary
#    for product in product_quantities:
        # For each product, find the quantity
#        quantity = product_quantities[product]
        # Find the unit price of the product from product_prices dictionary
#        unit_price = product_prices.get(product, 0)
        # Calculate the total price for the product
#        total_price = quantity * unit_price
        # Add the total price of the current product to the total bill
#        total_bill += total_price
    # Return the final total bill
#    return total_bill

#def calculate_total_bill(quantities, prices):
    
#    plist = zip(quantities.values(), prices.values())
    
#    return sum([p[0] * p[1] for p in plist])

def cal_prices(quantity, price):
    return quantity * price
    
def tot_prices(quantities, prices):
    
    comp = zip(quantities.values(), prices.values())
    
    return sum([cal_prices(z[0], z[1]) for z in comp])

# Product quantities and prices
quantities = {'apple': 2, 'banana': 5, 'cherry': 15}
prices = {'apple': 0.50, 'banana': 0.30, 'cherry': 0.20}

#ans = calculate_total_bill(quantities, prices)

# Compute the total bill for the products
#total_bill = calculate_total_bill(quantities, prices)

print(f"Total Bill: ${tot_prices(quantities, prices):.2f}")
