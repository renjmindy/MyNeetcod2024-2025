def calculate(quantity, price):
    return quantity * price

# Beverage quantities and prices
tea_quantity, tea_price = 50, 1.5
coffee_quantity, coffee_price = 80, 2

# Calculate total costs directly
#total_tea_cost = tea_quantity * tea_price
#total_coffee_cost = coffee_quantity * coffee_price

print(f"Total Tea Cost: ${calculate(tea_quantity, tea_price)}")
print(f"Total Coffee Cost: ${calculate(coffee_quantity, coffee_price)}")
