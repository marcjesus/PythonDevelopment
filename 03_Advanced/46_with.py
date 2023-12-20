# Using 'with' statement to open and read a file
file_path = "example.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except PermissionError:
    print(f"You don't have permission to read '{file_path}'.")
except Exception as e:
    print(f"An error occurred: {e}")
