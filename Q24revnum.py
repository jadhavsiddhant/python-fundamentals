# Write a Python program to reverse a number
num = 123
rev = 0

while num > 0:
    dig = num % 10
    rev = rev * 10 + dig
    num = num // 10

print(rev)

