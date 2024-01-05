from abc import ABC, abstractmethod

# Define the states
class OrderState(ABC):
    @abstractmethod
    def process_order(self):
        pass

class SelectItemsState(OrderState):
    def process_order(self):
        print("Selecting items")

class CheckCartState(OrderState):
    def process_order(self):
        print("Checking the cart")

class ConfirmAddressState(OrderState):
    def process_order(self):
        print("Confirming the address")

class SelectPaymentState(OrderState):
    def process_order(self):
        print("Selecting mode of payment")

class PaymentProcessState(OrderState):
    def process_order(self):
        print("Processing payment")

class PlaceOrderState(OrderState):
    def process_order(self):
        print("Placing the order")

# Context class that uses the state
class OrderContext:
    def __init__(self):
        self.order_state = None

    def set_order_state(self, state):
        self.order_state = state

    def process_order(self):
        if self.order_state:
            self.order_state.process_order()
        else:
            print("Invalid order state")

# Example Usage
order_context = OrderContext()

# Customer goes through the order process step by step
order_context.set_order_state(SelectItemsState())
order_context.process_order()

order_context.set_order_state(CheckCartState())
order_context.process_order()

order_context.set_order_state(ConfirmAddressState())
order_context.process_order()

order_context.set_order_state(SelectPaymentState())
order_context.process_order()

order_context.set_order_state(PaymentProcessState())
order_context.process_order()

order_context.set_order_state(PlaceOrderState())
order_context.process_order()
