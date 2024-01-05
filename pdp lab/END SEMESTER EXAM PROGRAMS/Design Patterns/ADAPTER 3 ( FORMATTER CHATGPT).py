# Target
class newformatter:
    def __init__(self):
        pass

    def start_formatting(self):
        pass

    def end_formatting(self):
        pass

# Adaptee
class oldformatter:
    def __init__(self, text):
        self.text = text

    def format_text(self, text):
        print(f'formatted text: <i>{self.text}</i>')

# Formatter Adapter
class formatteradapter(newformatter):
    def __init__(self, text):
        super().__init__()
        self.old_formatter = oldformatter(text)

    def start_formatting(self):
        self.old_formatter.format_text(f'<i>{self.old_formatter.text}')

    def end_formatting(self):
        print('</i>')

# Example of how to use the adapter
old_formatter = oldformatter('This is the text to format')
adapter = formatteradapter(old_formatter.text)  # Pass the text to the adapter
adapter.start_formatting()
adapter.end_formatting()
