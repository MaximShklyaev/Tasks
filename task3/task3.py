import sys
import json

def load_json(file_path):
    with open(file_path) as file:
            json_data = json.load(file)
            return json_data

def values_to_dict(values):
    values_dict = {}
    for obj in values.get("values"):
        if obj.get("id"):
            values_dict[obj.get("id")] = obj.get('value')
    return values_dict

def values_to_tests(tests_data, values_dict):
    for obj in tests_data:
        if obj.get("id") and obj.get("id") in values_dict:
            obj["value"] = values_dict[obj.get("id")]
        if obj.get("values"):
            values_to_tests(obj.get("values"), values_dict)

def dump_json(json_data, file_path):
    with open(file_path, "w") as file:
            json.dump(json_data, file)

values_path = sys.argv[1]
tests_path = sys.argv[2]
report_path = sys.argv[3]
values_data = load_json(values_path)
tests_data = load_json(tests_path)
values_dict = values_to_dict(values_data)
values_to_tests(tests_data.get("tests"), values_dict)
dump_json(tests_data, report_path)
