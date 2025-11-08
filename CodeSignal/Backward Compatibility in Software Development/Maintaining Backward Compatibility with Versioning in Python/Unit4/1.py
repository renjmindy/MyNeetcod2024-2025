class CreditCardPayment:
    def process_payment(self, amount):
        print(f"Processing {amount} payment through credit card.")

class PayPalPayment:
    def process_payment(self, amount):
        print(f"Processing {amount} payment through PayPal.")

# TODO: Implement the CryptoPayment class
class CryptoPayment:
    def process_payment(self, amount):
        print(f"Processing {amount} payment through cryptocurrency.")
    
# TODO: Implement the StripePayment class
class StripePayment:
    def process_payment(self, amount):
        print(f"Processing {amount} payment through Stripe.")

class PaymentFacade:
    # TODO: Implement PaymentFacade class that supports the method `process_payment(method, amount)
    # where `method` is the payment method ("credit_card", "paypal", "crypto", or "stripe")
    # If another payment is provided, print "Invalid payment method."
    # If the `amount` is greater than `10000`, the payment should be declined and print "Transaction limit exceeded."
    # as this is a too big amount
    def __init__(self):
        self.creditcard = CreditCardPayment()
        self.paypal = PayPalPayment()
        self.crypto = CryptoPayment()
        self.stripe = StripePayment()
        
    def process_payment(self, method, amount):
        #pass
        if method == 'credit_card':
            if amount <= 10000: self.creditcard.process_payment(amount)
            else: print("Transaction limit exceeded.")
        elif method == "paypal":
            if amount <= 10000: self.paypal.process_payment(amount)
            else: print("Transaction limit exceeded.")
        elif method == "crypto":
            if amount <= 10000: self.crypto.process_payment(amount)
            else: print("Transaction limit exceeded.")
        elif method == "stripe":
            if amount <= 10000: self.stripe.process_payment(amount)
            else: print("Transaction limit exceeded.")
        else:
            print("Invalid payment method.")
