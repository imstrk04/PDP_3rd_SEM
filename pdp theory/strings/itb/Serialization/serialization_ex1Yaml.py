#Need to install pyyaml 

import yaml

with open('patient.yml','r') as f:
    file_1=yaml.safe_load(f)

print(type(file_1))
print(file_1)

print(file_1['patient_details']['phone'])
    
with open('student.yml','r') as f:
    files=yaml.safe_load_all(f)

    for each_file in files:
        print(each_file)
