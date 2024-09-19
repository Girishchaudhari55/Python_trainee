class Patient:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"

class PatientManagementSystem:
    def __init__(self):
        self.patients = []

    def add_patient(self, id, name):
        new_patient = Patient(id, name)
        self.patients.append(new_patient)
        print(f"Patient added: {new_patient}")

    def remove_patient(self, id):
        for patient in self.patients:
            if patient.id == id:
                self.patients.remove(patient)
                print(f"Patient removed: {patient}")
                return
        print("Patient not found!")

    def display_patients(self):
        if not self.patients:
            print("No patients to display.")
        for patient in self.patients:
            print(patient)

def menu():
    print("\nPatient Management System")
    print("1. Add Patient")
    print("2. Remove Patient")
    print("3. Display Patients")
    print("4. Exit")

def driver_program():
    system = PatientManagementSystem()
    
    while True:
        menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            id = input("Enter patient ID: ")
            name = input("Enter patient name: ")
            system.add_patient(id, name)
        elif choice == '2':
            id = input("Enter patient ID to remove: ")
            system.remove_patient(id)
        elif choice == '3':
            system.display_patients()
        elif choice == '4':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    driver_program()