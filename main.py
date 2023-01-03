import json

# Read the input JSON file
with open('./data/input.json', 'r') as f:
  data = json.load(f)

# Get the message attribute from the input data
message = data['message']

# Create an empty schema object
schema = {}

# Iterate through the attributes in the message
for attr, value in message.items():
  # Set the data type for the attribute based on its value
  if isinstance(value, str):
    data_type = 'string'
  elif isinstance(value, int):
    data_type = 'integer'
  elif isinstance(value, list):
    # Check if the list contains strings or objects
    if all(isinstance(item, str) for item in value):
      data_type = 'enum'
    else:
      data_type = 'array'
  else:
    data_type = 'object'
  
  # Add the attribute to the schema object with the data type and required flag
  schema[attr] = {
    'type': data_type,
    'required': False,
    'tag': '',
    'description': ''
  }

# Dump the schema object to a JSON file
with open('./schema/output.json', 'w') as f:
  json.dump(schema, f)
