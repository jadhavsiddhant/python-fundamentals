import os

# Write a program that lists all files and directories in the current directory
# using os.listdir().
def list_files_and_directories():
    current_directory = os.getcwd()
    items = os.listdir(current_directory)
    for item in items:
        print(item)

list_files_and_directories()