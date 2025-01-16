# Write a program that counts the number of vowels in a string.
count = 0
string = input("Enter any string")
vowel = 'aeiouAEIOU'
for i in string:
    if i in vowel:
        count +=1

print("there are",count,"vowels in the string")