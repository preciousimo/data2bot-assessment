import unittest
import json

from main import *


class TestSchemaExtractor(unittest.TestCase):
    def test_schema_extraction(self):
        # Read the expected output JSON file
        with open('./schema/expected_output.json', 'r') as f:
            expected_output = json.load(f)

        # Extract the schema from the input JSON file
        extract_schema('./data/input.json', './schema/output.json')

        # Read the actual output JSON file
        with open('./schema/output.json', 'r') as f:
            actual_output = json.load(f)

        # Assert that the extracted schema matches the expected output
        self.assertDictEqual(actual_output, expected_output)
        
    def test_different_schemas(self):
        # Read the input JSON file with a different schema
        with open('./data/input_different_schema.json', 'r') as f:
            input_data = json.load(f)

        # Extract the schema from the input JSON file
        extract_schema('./data/input_different_schema.json', './schema/output.json')

        # Read the actual output JSON file
        with open('./schema/output.json', 'r') as f:
            actual_output = json.load(f)

        # Assert that the extracted schema does not match the expected output
        self.assertNotEqual(actual_output, expected_output)