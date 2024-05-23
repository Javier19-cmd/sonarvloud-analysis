import os
import subprocess

def read_file(file_path):
    # Validate file_path to prevent path traversal attacks
    if '..' in file_path or file_path.startswith('/'):
        print("Invalid file path")
        return None
    try:
        with open(file_path, 'r') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        print(f"The file at {file_path} does not exist.")
        return None

def write_file(file_path, data):
    # Validate file_path to prevent path traversal attacks
    if '..' in file_path or file_path.startswith('/'):
        print("Invalid file path")
        return
    try:
        with open(file_path, 'w') as file:
            file.write(data)
    except IOError as e:
        print(f"Error writing to file: {e}")

def get_user_input():
    user_input = input("Enter some text: ")
    if len(user_input) > 1000:  # Example limit
        print("Input is too long")
        return ""
    return user_input

def process_data(data):
    # Ensure sensitive data is not logged or improperly handled
    processed_data = data.lower()  # Example process, might need more secure handling
    return processed_data

def main():
    file_path = "example.txt"
    # Reading from a file
    data = read_file(file_path)
    if data is None:
        return

    # Processing data
    processed_data = process_data(data)
    print(f"Processed Data: {processed_data}")

    # Getting user input and writing to a file
    user_input = get_user_input()
    write_file(file_path, user_input)

if __name__ == "__main__":
    main()
