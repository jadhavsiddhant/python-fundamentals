import time

start_time = time.time()
list_comp = [x * 2 for x in range(1000000)]
end_time = time.time()
print(f"List comprehension took {end_time - start_time} seconds")

start_time = time.time()
gen_exp = (x * 2 for x in range(1000000))
end_time = time.time()
print(f"Generator expression took {end_time - start_time} seconds")

start_time = time.time()
list_sum = sum(list_comp)
end_time = time.time()
print(f"Summing list comprehension took {end_time - start_time} seconds")

start_time = time.time()
gen_sum = sum(gen_exp)
end_time = time.time()
print(f"Summing generator expression took {end_time - start_time} seconds")
