'''Design a simple notification system for a messaging application using a
combination of design patterns. Implement the State pattern to manage the d
ifferent states of a message (e.g., draft, sent, delivered). Use the Strategy
pattern to define various sending strategies, such as normal message sending
and urgent message sending. Apply the Singleton pattern to ensure a single
instance of the messaging system. Utilize the Iterator pattern to iterate
through the messages in a message list. Additionally, implement the
Observer pattern to notify users when their messages are delivered.
Finally, use the Decorator pattern to add additional features to a
message, such as encryption.
Provide a client code demonstrating the usage of the system with
comments explaining each part of the design. Import the necessary
modules and include meaningful comments in your implementation.'''
from itertools import cycle
import time

# StateInterface
class MessageState:
    def process_state(self):
        pass

class DraftState(MessageState):
    def process_state(self):
        return 'Draft'

class SentState(MessageState):
    def process_state(self):
        return 'Sent'

class DeliveredState(MessageState):
    def process_state(self):
        return 'Delivered'


# Strategy interface
class MessageStrategy:
    def send_message(self, message):
        pass

class NormalStrategy(MessageStrategy):
    def send_message(self, message):
        print(f'Sending normal message: {message}')

class UrgentStrategy(MessageStrategy):
    def send_message(self, message):
        print(f'Sending message urgently: {message}')

# Observer Interface
class Observer:
    def update(self):
        pass

# Singleton pattern to ensure a single instance of the messaging system
class Messagingsystem:

    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Messagingsystem, cls).__new__(cls)
            cls._instance.observers = []
            cls._instance.sending_strategy = NormalStrategy()
            cls._instance.state = DraftState()  # Initialize with DraftState
            cls._instance.messages = []
        return cls._instance

    def set_state(self, state):
        self.state = state

    def set_strategy(self, sending_strategy):
        self.sending_strategy = sending_strategy

    def add_observer(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def remove_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update()

    def send_message(self, message):
        print(f'Current message State: {self.state.process_state()}')
        self.sending_strategy.send_message(message)
        self.set_state(SentState()) 
        print(f'Current message State: {self.state.process_state()}')
        self.notify_observers()


# Concrete class observer
class MessageObserver(Observer):

    def update(self):
        print('Delivery notification: Message delivered')

# Iterator pattern to iterate over message list
class MessageIterator:

    def __init__(self, messages):
        self.messages = messages
        self.index = 0

    def __iter__(self):  # for iterator to work properly give this
        return self

    def __next__(self):
        if self.index < len(self.messages):
            current_message = self.messages[self.index]
            self.index += 1
            return current_message
        else:
            raise StopIteration

# Decorator interface
class MessageDecorator:
    def decorate(self):
        pass

# Concrete decorator
class EncryptedMessage(MessageDecorator):
    def decorate(self, message):
        print(f'{message} Encrypted')

# DRIVER CODE
MessagingSystem = Messagingsystem()  # Corrected class name

observer1 = MessageObserver()
MessagingSystem.add_observer(observer1)

print('sending normal message')
MessagingSystem.send_message('Hi how are you')

# setting the strategy to urgent and sending the message
urgent_strategy = UrgentStrategy()
MessagingSystem.set_strategy(urgent_strategy)
print('sending urgent message')
MessagingSystem.send_message('hello im in a hurry')


#decorator pattern
encrypted_message_decorator = EncryptedMessage()
encrypted_message_decorator.decorate("Confidential information")

#iterator pattern
messages = ["Message 1", "Message 2", "Message 3"]
message_iterator = MessageIterator(messages)
    
print("\nIterating through Messages:")
for message in cycle(message_iterator):
    print(message)
    time.sleep(1)

