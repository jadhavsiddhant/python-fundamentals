# Write a Python function that takes a string and returns its length without using the built-in len() function.

def stringlength(string):
    count = 0
    for i in string:
        count += 1
    return count

inputstring = input("Enter a string: ")
x = stringlength(inputstring)
print("The length of the string is:", x)
