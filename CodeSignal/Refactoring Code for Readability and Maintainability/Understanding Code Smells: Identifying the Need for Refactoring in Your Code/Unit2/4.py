def print_summary(item, sp, q, tr, dr):
    print(f"Purchasing {q} of '{item}'")
    print(f"Original bulk price: ${bulk_price(sp, q):.2f}")
    print(f"Price after discount: ${discount(sp, q, dr):.2f}")
    print(f"Total price with tax: ${tax(sp, q, dr, tr):.2f}")
    
def bulk_price(sp, q): return sp * q
def discount(sp, q, dr): return (sp * q) - (sp * q * dr / 100)
def tax(sp, q, dr, tr): return ((sp * q) - (sp * q * dr / 100)) + (((sp * q) - (sp * q * dr / 100)) * tr / 100)

ITEM_NAME = "Premium Coffee Maker"
SINGLE_ITEM_PRICE = 99.99
QUANTITY = 5
TAX_RATE = 7  # Tax rate in percent
DISCOUNT_RATE = 10  # Discount rate in percent

print_summary(ITEM_NAME, SINGLE_ITEM_PRICE, QUANTITY, TAX_RATE, DISCOUNT_RATE)
