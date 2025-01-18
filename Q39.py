# Print a diamond-shaped pattern of stars with a width given by the user
# (e.g., for 5).

n = int(input("Enter the width of the diamond (odd number): "))

for i in range(n//2 + 1):
    print(" " * (n//2 - i) + "*" * (2*i + 1))

for i in range(n//2 - 1, -1, -1):
    print(" " * (n//2 - i) + "*" * (2*i + 1))