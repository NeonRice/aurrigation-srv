import json
import jsonschema


# Load the JSON schema from file
def validate(data, schema_path):
    with open(schema_path, 'r') as f:
        schema = json.load(f)
    try:
        jsonschema.validate(data, schema)
        return True
    except jsonschema.exceptions.ValidationError as e:
        print("Validation failed:", e.message)
        return False


def get_properties(schema_path):
    with open(schema_path, "r") as file:
        schema = json.load(file)

    return schema["properties"]
