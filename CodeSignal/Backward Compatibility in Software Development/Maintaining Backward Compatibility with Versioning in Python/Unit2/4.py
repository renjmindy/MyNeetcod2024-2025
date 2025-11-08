class ReportGenerator:
    def __init__(self):
        # Initialize with a dictionary of months, each containing an empty list for transactions
        self.transactions = {
            'January': [],
            'February': [],
            'March': [],
            'April': [],
            'May': [],
            'June': [],
            'July': [],
            'August': [],
            'September': [],
            'October': [],
            'November': [],
            'December': [],
        }
        self.months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # TODO: add an optional parameter `include_comparative_analysis`, and adjust the logic based on that
    def generate_monthly_report(self, month, include_comparative_analysis=False):
        current_month_data = self.summarize_transactions(month)
        if include_comparative_analysis:
            pre = self.months.index(month) - 1
            return f"Financial Report for {month}:\nTotal Transactions: {current_month_data}\nComparative Analysis against {self.months[pre]}:\nVariation: {self.summarize_transactions(month) - self.summarize_transactions(self.months[pre])}\n"
        else:    
            return f"Financial Report for {month}:\nTotal Transactions: {current_month_data}\n"

    def summarize_transactions(self, month):
        # Assuming each transaction is a float, returning the sum of all transactions for simplicity
        if len(self.transactions[month]) < 500:
            return sum(self.transactions[month])

    # Placeholder method to allow adding transactions for testing
    def add_transaction(self, month, amount):
        # Assuming validation of month and amount is handled elsewhere
        if len(self.transactions[month]) < 500:
            self.transactions[month].append(amount)
