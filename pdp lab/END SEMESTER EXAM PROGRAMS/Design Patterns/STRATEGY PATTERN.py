from abc import ABC, abstractmethod

# Strategy interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Concrete Strategies
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying ${amount} using credit card.")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying ${amount} using PayPal.")

class BankTransferPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying ${amount} via bank transfer.")

# Context
class ShoppingCart:
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def checkout(self, total_amount):
        self.payment_strategy.pay(total_amount)

# Example Usage
credit_card_payment = CreditCardPayment()
paypal_payment = PayPalPayment()
bank_transfer_payment = BankTransferPayment()

# Using different payment strategies
cart1 = ShoppingCart(payment_strategy=credit_card_payment)
cart1.checkout(total_amount=100)

cart2 = ShoppingCart(payment_strategy=paypal_payment)
cart2.checkout(total_amount=50)

cart3 = ShoppingCart(payment_strategy=bank_transfer_payment)
cart3.checkout(total_amount=200)
