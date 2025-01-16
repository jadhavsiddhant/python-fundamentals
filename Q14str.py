# Write a function that takes a string s and an integer n, and returns the string repeated n 

def repeat_string(s, n):
    result = ""
    for _ in range(n):
        result += s
    return result

print(repeat_string("hello", 3))  
