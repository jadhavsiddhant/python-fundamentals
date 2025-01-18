# Write a function that inverts a dictionary (keys become values, values
# become keys).
def invert_dict(d):
    return {v: k for k, v in d.items()}