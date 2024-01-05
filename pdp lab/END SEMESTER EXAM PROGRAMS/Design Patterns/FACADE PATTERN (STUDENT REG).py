# Subsystem components

class PersonalDetails:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


class HobbyDetails:
    def __init__(self, hobbies):
        self.hobbies = hobbies


class FileStorage:
    def save_to_file(self, filename, data):
        with open(filename, 'w') as file:
            file.write(data)


# Facade
class StudentRegistrationFacade:
    def __init__(self, personal_details, hobby_details, file_storage):
        self.personal_details = personal_details
        self.hobby_details = hobby_details
        self.file_storage = file_storage

    def register_student(self):
        # Get personal details
        name = input("Enter name: ")
        age = input("Enter age: ")
        address = input("Enter address: ")
        personal_details = PersonalDetails(name, age, address)

        # Get hobby details
        hobbies = input("Enter hobbies (comma-separated): ").split(',')
        hobby_details = HobbyDetails(hobbies)

        # Save details to a file
        registration_data = f"Name: {name}\nAge: {age}\nAddress: {address}\nHobbies: {', '.join(hobbies)}"
        self.file_storage.save_to_file("student_details.txt", registration_data)

        print("Student registration successful.")

    def display_details(self):
        with open("student_details.txt", 'r') as file:
            details = file.read()
            print("Student Details:\n", details)


# Client code
personal_details = PersonalDetails("", "", "")
hobby_details = HobbyDetails([])
file_storage = FileStorage()

registration_facade = StudentRegistrationFacade(personal_details, hobby_details, file_storage)

# Register a student
registration_facade.register_student()

# Display student details
registration_facade.display_details()
