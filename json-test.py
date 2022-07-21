import json

# Read the json file and output
with open('example.json', 'r') as fcc_file:
    fcc_data = json.load(fcc_file)
    print(json.dumps(fcc_data, indent=4))
