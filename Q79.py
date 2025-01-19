# Write a Python program to copy the contents of one file to another.
# Prompt the user for the source and destination file paths
source_path = input("Enter the path of the source file: ")
destination_path = input("Enter the path of the destination file: ")

# Open the source file in read mode
source_file = open(source_path, 'r')
# Read the contents of the source file
contents = source_file.read()
# Close the source file
source_file.close()

# Open the destination file in write mode
destination_file = open(destination_path, 'w')
# Write the contents to the destination file
destination_file.write(contents)
# Close the destination file
destination_file.close()