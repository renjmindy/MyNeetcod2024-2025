class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item_v1(self, item_name, quantity):
        for _ in range(quantity):
            self.items.append({'name': item_name})
        print(f"{quantity} items of {item_name} added. No price or discount applied.")
    
    # TODO: Implement the add_item_v2 method, which also handles price and optional discount_code
    def add_item_v2(self, item_name, quantity, price, discount_code=None):
        for _ in range(quantity):
            self.items.append({'name': item_name, 'price': price})
        if discount_code != None:
            print(f"Item added with price: {price * quantity * 0.9} with discount: {discount_code}.")
        else:
            print(f"Item added with price: {price * quantity} without discount: {discount_code}.")
    
    def add_item(self, version, item_name, quantity, price=None, discount_code=None):
        # TODO: This method needs to be updated to call add_item_v2 for version 2
        if len(self.items) >= 500:
            print("Cart is full, cannot add more items.")
        elif version == 2:
            self.add_item_v2(item_name, quantity, price, discount_code)
        elif version == 1:
            self.add_item_v1(item_name, quantity)
        else:
            print("Invalid operation.")
