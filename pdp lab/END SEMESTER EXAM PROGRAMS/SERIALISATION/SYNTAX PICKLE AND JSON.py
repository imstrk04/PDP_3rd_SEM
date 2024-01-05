data = {'name': 'John', 'age': 30, 'city': 'New York'}

#PICKLE SYNTAX 
import pickle 
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

#JSON SYNTAX STRING
import json
# Serialize the object to a JSON-formatted string
json_string = json.dumps(data)
loaded_data = json.loads(json_string)

#ALTERNATIVE METHOD
with open('data.json', 'w') as file:
    json.dump(data, file)
    
with open('data.json', 'r') as file:
    loaded_data = json.load(file)
