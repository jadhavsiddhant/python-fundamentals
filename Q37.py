# Write a program that generates all prime numbers in a given range [start,
# end].
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if (num % i) == 0:
                break
        else:
            print(num)