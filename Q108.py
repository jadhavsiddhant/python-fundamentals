import json

# Write a script that reads a JSON file, modifies a value, and writes the
# updated data back to the file.
# Path to the JSON file
file_path = '/Users/siddhantsmac/Desktop/120 Questions/data.json'

# Read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)

# Modify a value in the JSON data
data['key_to_modify'] = 'new_value'

# Write the updated data back to the JSON file
with open(file_path, 'w') as file:
    json.dump(data, file, indent=4)

print("JSON file has been updated.")