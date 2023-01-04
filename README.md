# data2bot-assessment
 
## Objective
This is a genertic program that:
- Reads a JSON file similar to what's present in this location (./data/)
- Sniffs the schema of the JSON file 
- Dumps the output in (./schema/)

## Informations for test cases
- Padding: All attributes in the JSON schema is padded with "tag" and "description" keys
- The schema output captures ONLY the attributes within the "message" key of the input JSON source data. All attributes withn the key "attributes" is excluded
- The JSON schema properties is set at "required": false
- For data types of the JSON schema:
STRING: program identifies what is a string and map accordingly in JSON schema output
INTEGER: program identifies what is an integer and map accordingly in JSON schema output
ENUM: When the value in an array is a string, the program maps the data type as an ENUM 
ARRAY: When the value in an array is another JSON object, the program maps the data type as an ARRAY 

# Example of expected output
./schema/expected_output.json

NB: Program can be run from test.py as it goes through the unit test, but it can still be seamlessly executed at main.py without test.
