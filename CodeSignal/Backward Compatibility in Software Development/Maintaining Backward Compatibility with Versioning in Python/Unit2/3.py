class BeverageCreator:
    def __init__(self):
        self.orders = []

    def create_order(self, beverage_name, special_instructions=None, snack=None):
        # TODO: Enhance this method to optionally include special_instructions (a string for any special instructions) 
        # and a snack (a string representing the name of a complimentary snack), keeping backward compatibility
        # The method should return a dictionary detailing the order, including the beverage, special_instructions (if any), 
        # and snack (if any).
        if special_instructions and snack:
            order = {"beverage": beverage_name, "special_instructions": special_instructions, "snack": snack}
        elif special_instructions:
            order = {"beverage": beverage_name, "special_instructions": special_instructions}
        elif snack:
            order = {"beverage": beverage_name, "snack": snack}
        else:
            order = {"beverage": beverage_name}
        self.orders.append(order)
        return order
