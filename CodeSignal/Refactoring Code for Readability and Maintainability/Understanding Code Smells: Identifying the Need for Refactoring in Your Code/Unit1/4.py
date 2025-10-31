# Begin with generic non-descriptive function and variable names
def total_cost(quantities, prices):
    return quantities * prices

def display_cost(n, cost):
    print(f"The total cost for item is: ${cost:.2f}")

# Variables for pencil unit prices
price_product1 = 0.25
price_product2 = 0.50

# Variables for pencil quantities
quantity_product1 = 100
quantity_product2 = 200

# Calculating and printing total costs
cost_product1 = total_cost(quantity_product1, price_product1)
cost_product2 = total_cost(quantity_product2, price_product2)

display_cost("item", cost_product1)
display_cost("item", cost_product2)
