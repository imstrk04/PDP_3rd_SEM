from abc import ABC, abstractmethod

# State interface
class AdmissionState(ABC):
    @abstractmethod
    def process_admission(self, context):
        pass

# Concrete States

class RegistrationState(AdmissionState):
    def process_admission(self, context):
        print(f"{context.student_name} has registered for college admission.")
        context.state = ApplicationSubmissionState()

class ApplicationSubmissionState(AdmissionState):
    def process_admission(self, context):
        print(f"{context.student_name} has submitted the online application.")
        context.state = InterviewState()

class InterviewState(AdmissionState):
    def process_admission(self, context):
        print(f"{context.student_name} has appeared for the interview.")
        context.state = FeePaymentState()

class FeePaymentState(AdmissionState):
    def process_admission(self, context):
        print(f"{context.student_name} has paid the admission fees.")
        context.state = None  # Admission process completed

# Context
class CollegeAdmission:
    def __init__(self, student_name):
        self.student_name = student_name
        self.state = RegistrationState()

    def process_admission(self):
        self.state.process_admission(self) #here self is the collegeadmission class itself 

# Example Usage
student_admission = CollegeAdmission("John Doe")

# Execute the admission process steps
student_admission.process_admission()
student_admission.process_admission()
#student_admission.process_admission()
#student_admission.process_admission()
