# Begin with a single messy function doing everything
def process_orders(object, quantities, prices):
    discount_rate = 0.05 
    if quantities > 100:
        discount = (prices * quantities) * discount_rate
    else:
        discount = 0

    price_final = (prices * quantities) - discount
    print(f"The final price for {object}: ${price_final:.2f}")

#def process_orders():
    # Discount rate for all items
#    discount_rate = 0.05  # 5% discount, applicable if more than 100 items are ordered

    # Prices for notebook and pen
#    price_notebook, price_pen = 1.99, 0.99

    # Quantities for notebook and pen
#    q_notebook, q_pen = 150, 75
    
    # Total price calculation for a notebook with an in-line discount
    # Check if the discount is applicable
#    if q_notebook > 100:
        # Apply discount if the condition is met
#        discount_notebook = (price_notebook * q_notebook) * discount_rate
#    else:
        # No discount if the condition is not met
#        discount_notebook = 0
#    price_final_notebook = (price_notebook * q_notebook) - discount_notebook
#    print(f"The final price for notebook: ${price_final_notebook:.2f}")

    # Repeat calculations for pen with in-line discount application
#    if q_pen > 100:
#        discount_pen = (price_pen * q_pen) * discount_rate
#    else:
#        discount_pen = 0
#    price_final_pen = (price_pen * q_pen) - discount_pen
#    print(f"The final price for pen: ${price_final_pen:.2f}")

# Call the messy function to process orders
price_notebook, price_pen = 1.99, 0.99
q_notebook, q_pen = 150, 75
process_orders("notebook", q_notebook, price_notebook)
process_orders("pen", q_pen, price_pen)
