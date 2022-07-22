import xmltodict
import os

# Get the absolute path for the directory where this file is located "here"
here = os.path.abspath(os.path.dirname("test.xml"))

# Read in the XML text
with open(os.path.join(here, "test.xml")) as file:
    xml_text = file.read()

# Convert the XML to a dict
d = xmltodict.parse(xml_text)
print(d)

# Display the type of d
print("d is a", type(d))

# Display the organisation from the xml file
print(d["root"]["organization"])

# Loop through switches and print hostname, model, and ip address
for switch in d["root"]["switches"]:
 print(switch["hostname"] + "\t\t-\t\t" + switch["model"] + "\t\t-\t\t" + switch["ipaddress"])