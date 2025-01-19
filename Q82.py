# Modify the file-reading program to handle exceptions (e.g., file not found)
# gracefully.
try:
    with open('/Users/siddhantsmac/Desktop/120 Questions/Q82.py', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The file was not found.")
except Exception as e:
    print(f"An error occurred: {e}")