import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    try:
        with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open(json_file_path, mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        print(f" Successfully converted '{csv_file_path}' to '{json_file_path}'")

    except FileNotFoundError:
        print(f" Error: File '{csv_file_path}' not found.")
    except Exception as e:
        print(f" An error occurred: {e}")

if __name__ == "__main__":
    csv_file = input("Enter the path to your CSV file: ")  # e.g., data.csv
    json_file = input("Enter the desired JSON output path: ")  # e.g., output.json
    csv_to_json(csv_file, json_file)
