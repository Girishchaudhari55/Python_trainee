import json

patients = [
    {'id': 101, 'name': 'Mahesh'},
    {'id': 102, 'name': 'Rahul'}  
]


patient_str = json.dumps(patients)

print(patients, patient_str)
with open('patient_data.json', 'w') as patient_db:  
    patient_db.write(patient_str) 
patients_list = json.loads(patient_str)  
print(patients_list, type(patients_list))
