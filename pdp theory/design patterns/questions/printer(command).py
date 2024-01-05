from abc import ABC, abstractmethod
from queue import Queue

#receiver

class Printer:

    def __init__(self):
        self.printer_queue = Queue()
    
    def enqueue_printJob(self, job):
        self.printer_queue.put(job)
    
    def dequeue_printJob(self):
        if not self.printer_queue.empty():
            self.printer_queue.get()
        else:
            print("Printer Empty")
    
#Icommand Interface
class ICommand(ABC):

    @abstractmethod
    def execute(self):
        pass

class PrintJobCommand(ICommand):

    def __init__(self,printer, category, job_id):
        self.printer = printer
        self.category = category
        self.job_id = job_id
    
    def execute(self):
        print(f"PrintJob({self.category}, {self.job_id})")
        self.printer.enqueue_printJob((self.category, self.job_id))
    
class DeleteJobCommand(ICommand):

    def __init__(self, printer, category, job_id):
        self.printer = printer
        self.category = category
        self.job_id = job_id
    
    def execute(self):
        print(f"DeleteJob({self.category}, {self.job_id})")

class ApplicationInvoker:

    def __init__(self):
        self.command = None
    
    def setCommand(self, command):
        self.command = command
    
    def press_button(self):
        if self.command:
            self.command.execute()
        else:
            print("No command set.")
    
if __name__ == '__main__':
    printer = Printer()
    invoker = ApplicationInvoker()

    #Client 1
    print_job1 = PrintJobCommand(printer, "EmployeeX", 123)
    invoker.setCommand(print_job1)
    invoker.press_button()

    #client 2
    print_job2 = PrintJobCommand(printer,"SystemA", 456)
    invoker.setCommand(print_job2)
    invoker.press_button()

    #delete
    delete_print_command = DeleteJobCommand(printer, "EmployeeX", 123)
    invoker.setCommand(delete_print_command)
    invoker.press_button()

    print("Printer Queue:", printer.printer_queue.queue)