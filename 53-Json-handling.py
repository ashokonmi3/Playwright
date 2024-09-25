import datetime
import inspect

# json.dump(): Write Python objects into a JSON file.
# json.dumps(): Convert Python objects into a JSON-formatted string.
# json.load(): Read JSON data from a file and convert it into Python objects.
# json.loads(): Convert a JSON-formatted string into Python objects.

import json

# Python dictionary to write into a JSON file
# data = {
#     "name": "John Doe",
#     "age": 30,
#     "city": "New York",
#     "skills": ["Python", "Machine Learning", "Automation"]
# }

# # Writing to a JSON file
# with open('data.json', 'w') as json_file:
#     json.dump(data, json_file, indent=4)

# print("Data written to file successfully.")
# =======================
# import json

# # Reading from a JSON file
# with open('data.json', 'r') as json_file:
#     data = json.load(json_file)

# # Display the data
# print("Data read from file:")
# print(data)
# print(type(data))
# =====================
#  Converting Python Object to JSON String(json.dumps)

# import json

# # Python dictionary
# data = {
#     "name": "Jane Smith",
#     "age": 25,
#     "hobbies": ["Reading", "Gaming", "Cycling"]
# }

# # Convert Python dictionary to JSON string
# json_string = json.dumps(data, indent=4)

# # Output the JSON string
# print("JSON formatted string:")
# print(json_string)
# =================
# Parsing JSON String into Python Object(json.loads)
# import json

# # JSON string
# json_string = '''
# {
#     "name": "Alice",
#     "age": 22,
#     "active": true,
#     "courses": ["Math", "Physics"]
# }
# '''

# # Convert JSON string to Python dictionary
# data = json.loads(json_string)

# # Display the data
# print("Data parsed from JSON string:")
# print(data)
# print(type(data))

# =========================
# import json

# # Nested Python dictionary
# data = {
#     "employee": {
#         "name": "Tom",
#         "age": 35,
#         "address": {
#             "street": "123 Main St",
#             "city": "Los Angeles",
#             "state": "CA"
#         }
#     },
#     "salary": 60000,
#     "status": True
# }

# # # Writing the nested dictionary to a JSON file
# with open('nested_data.json', 'w') as file:
#     json.dump(data, file, indent=4)

# # # Reading the nested JSON file
# with open('nested_data.json', 'r') as file:
#     read_data = json.load(file)

# print("Nested data read from file:")
# print(read_data)
# =============
# Error Handling in JSON

# Invalid JSON(keys must be in quotes)
# invalid_json_string = "{name: John, age: 30}"

# try:
#     data = json.loads(invalid_json_string)
# except json.JSONDecodeError as e:
#     print(f"Error decoding JSON: {e}")
# =====================
# Modifying JSON Data
# import json

# # Load existing JSON data
# with open('data.json', 'r') as json_file:
#     data = json.load(json_file)

# # Modify the data
# data["age"] = 35
# data["skills"].append("Cloud Computing")
# print(data)
# # Write the updated data back to the file
# with open('data.json', 'w') as json_file:
#     json.dump(data, json_file, indent=4)

# print("Data updated successfully.")
# =======================

# import requests
# import json

# # URL of a sample REST API that returns JSON data
# url = "https://jsonplaceholder.typicode.com/users"

# # Send a GET request to the API
# response = requests.get(url)

# # Check if the request was successful
# if response.status_code == 200:# 2** 4** 5**
#     # Parse the JSON content
#     users = response.json()

#     # Display all user data
#     print("User Data from API:")
#     print(json.dumps(users, indent=4))  # Pretty-print JSON data

#     # Access specific fields from the JSON data
#     for user in users:
#         print(f"Name: {user['name']}")
#         print(f"Email: {user['email']}")
#         print(f"City: {user['address']['city']}")
#         print("-" * 20)
# else:
#     print(f"Failed to retrieve data. Status code: {response.status_code}")

# ============================
# Error Handling in REST API Responses
import requests
import json

url = "https://jsonplaceholder.typicode.com/user"

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)

    # Parse JSON content if request is successful
    users = response.json()

    # Pretty print the JSON data
    print(json.dumps(users, indent=4))

    # Access specific data
    for user in users:
        print(f"Name: {user['name']}")
        print(f"Email: {user['email']}")
        print(f"City: {user['address']['city']}")
        print("-" * 20)

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except Exception as err:
    print(f"Other error occurred: {err}")


# Assignment
# Exercise 1: Write a Python dictionary to a JSON file
# Create a Python dictionary that contains student information(name, age, subjects) and write it to a JSON file.
# Exercise 2: Read and print a nested JSON structure
# Create a JSON file that represents an employee's information, including nested data for address and skills. Read and display the contents of the file.
# Exercise 3: Convert a list of Python dictionaries to a JSON file
# Write a list of dictionaries representing different students to a JSON file and read it back.
# Exercise 4: Handle JSONDecodeError
# Write a script that takes a JSON string as input and handles any errors that may occur if the JSON is improperly formatted.
