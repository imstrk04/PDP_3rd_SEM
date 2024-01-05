from UniversityManagementSystem.university_management_system import UniversityManagementSystem

def main():
    u = UniversityManagementSystem()
    u.add()
    print()

    check1 = input("Do you want to store the datas(y/n)? ")
    if check1.lower() == 'y':
        u.serialisation()
    elif check1.lower() == 'n':
        print()
    check2 = input("Do you want to see your details(y/n)? ")
    if check2 == 'y':
        u.deserialisation()
    elif check2 == 'n':
        print()
    u.search_by_name()
    print("THANK YOU FOR USING UNIVERSITY MANAGEMENT SYSTEM")

main()