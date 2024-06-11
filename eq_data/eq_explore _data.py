from pathlib import Path 
import json

# Define the file paths using raw strings to avoid issues with backslashes
input_path = Path(r"eq_data\eq_data_1_day_m1.geojson")
output_path = Path(r"eq_data\readable_eq_data.geojson")

# Read the file content with the correct encoding
try:
    contents = input_path.read_text(encoding='utf-8')
except UnicodeDecodeError as e:
    print(f"Error reading file: {e}")
    contents = None

if contents:
    all_eq_data = json.loads(contents)

    # Create a more readable version of the data file.
    readable_contents = json.dumps(all_eq_data, indent=4)

    # Write the processed contents to the output file
    try:
        output_path.write_text(readable_contents, encoding='utf-8')
        print(f"File written successfully to {output_path}")
    except OSError as e:
        print(f"Error writing file: {e}")
else:
    print("No content to write due to earlier error.")
