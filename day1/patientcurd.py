class Patient:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f'[id={self.id}, name={self.name}]'

    def __repr__(self):
        return self.__str__()

# Global list of patients
patients = []

def patient_add(id, name):
    """Add a new patient to the list."""
    global patients
    patient = Patient(id, name)
    patients.append(patient)
    print(f'Patient added: {patient}')

def patient_remove(id):
    """Remove a patient from the list by ID."""
    global patients
    patient_to_remove = None

    # Find the patient by ID
    for patient in patients:
        if patient.id == id:
            patient_to_remove = patient
            break

    if patient_to_remove:
        print(f'Patient to be removed: {patient_to_remove}')
        if input('Are you sure you want to delete this patient (yes/no)? ').lower() == 'yes':
            patients.remove(patient_to_remove)
            print('Patient deleted successfully')
        else:
            print('Deletion cancelled')
    else:
        print(f'No patient found with ID {id}')

def patient_display():
    """Display all patients in the list."""
    global patients
    if not patients:
        print('No patients to display.')
    else:
        for patient in patients:
            print(patient)

def patient_update(id, new_name):
    """Update the name of a patient identified by ID."""
    global patients
    for patient in patients:
        if patient.id == id:
            print(f'Patient before update: {patient}')
            patient.name = new_name
            print(f'Patient updated: {patient}')
            return
    print(f'No patient found with ID {id}')

def menu():
    """Display menu and handle user choices."""
    try:
        choice = int(input('''1. Add patient
2. Delete patient by ID
3. Display all patients
4. Update patient name
7. End
Your choice: '''))
    except ValueError:
        print('Invalid input. Please enter a number.')
        return None

    if choice == 1:
        try:
            id = int(input('Enter patient ID: '))
            name = input('Enter patient name: ')
            patient_add(id, name)
        except ValueError:
            print('Invalid ID. Please enter a numeric value.')
    elif choice == 2:
        try:
            id = int(input('Enter patient ID to delete: '))
            patient_remove(id)
        except ValueError:
            print('Invalid ID. Please enter a numeric value.')
    elif choice == 3:
        patient_display()
    elif choice == 4:
        try:
            id = int(input('Enter patient ID to update: '))
            new_name = input('Enter new patient name: ')
            patient_update(id, new_name)
        except ValueError:
            print('Invalid ID. Please enter a numeric value.')
    elif choice == 7:
        return 7
    else:
        print('Invalid choice. Please try again.')
    return choice

def menus():
    """Continuously display the menu until the user decides to end."""
    choice = menu()
    while choice != 7:
        choice = menu()
    print('Thank you for using the app')

# Driver program
if __name__ == "__main__":
    menus()
