# Write a recursive function power(base, exp) that computes base^exp.
def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)