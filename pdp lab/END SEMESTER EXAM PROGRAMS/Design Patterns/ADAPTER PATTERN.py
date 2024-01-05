#Adapter pattern
'''creates an interface between 2 incompatible classes'''

#example 1 (printer adapter)

#target interface
class printer:
    def print_document(self):
        pass


#adapter
class LegacyPrinterAdapter:
    def __init__(self,legacy_printer):
        self.legacy_printer=legacy_printer

    def print_document(self):
        self.legacy_printer.print_content()


#adaptee 
class LegacyPrinter:
    def __init__(self,content):
        self.content=content

    def print_content(self):
        print(f'legacy printer : {self.content}')


legacy_printer=LegacyPrinter('hello legacy world')
adapter=LegacyPrinterAdapter(legacy_printer)
adapter.print_document()