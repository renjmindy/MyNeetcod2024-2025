# Calculate final price in a single function without using calculate_discount
def calculate_final_price(original_price, discount_percentage):
    #discount = original_price * (discount_percentage / 100)  # Inline discount calculation
    return original_price - calculate_discount(original_price, discount_percentage)
    
def calculate_discount(original_price, discount_percentage):
    return original_price * (discount_percentage / 100)

# Example usage
original_price = 50.00
discount_percentage = 20
final_price = calculate_final_price(original_price, discount_percentage)
print(f"The final price after a {discount_percentage}% discount is ${final_price:.2f}")
