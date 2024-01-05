#YAML to JSON

import yaml
import json

with open('patient.yml', 'r') as file:
    yml_file = yaml.safe_load(file) #reads from unreliable and untrusted sources

with open('patient_new.json', 'w') as json_file:
    json.dump(yml_file, json_file,indent=2)
    
with open('patient_new.json', 'r') as json_file:
    patient_json=json.load(json_file)

print(patient_json)
