# Write a Python script that reads a text file and prints its contents.
file_path = 'sample.txt'

with open(file_path, 'w') as file:
    file.write("This is a sample text.")

with open(file_path, 'r') as file:
    contents = file.read()
    print(contents)