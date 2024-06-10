import json

# Open and load the JSON file using a context manager
with open('json_file.json', 'r', encoding='utf-8') as file_obj:
    try:
        movie = json.load(file_obj)
        print(movie['web-app']['servlet']['init-param'])
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")