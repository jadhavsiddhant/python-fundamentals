# Write a program that prompts the user for a line of text and writes that line
# to a file.
filename = "output.txt"
line_of_text = input("Please enter a line of text: ")

with open(filename, "w") as file:
    file.write(line_of_text)

print(f"The line has been written to {filename}")