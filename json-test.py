import json
import os
from pprint import pprint

# Get the absolute path for the directory where this file is located "here"
here = os.path.abspath(os.path.dirname("example.json"))

# Read in the JSON text
with open(os.path.join(here, "example.json")) as file:
    json_text = file.read()

# Display the type of the json_text variable
print("json_text is a", type(json_text))

# Display the contents of the json_text variable
print(json_text)