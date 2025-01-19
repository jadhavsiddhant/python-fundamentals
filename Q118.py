import multiprocessing

# Use the multiprocessing module to run a function in parallel processes and
# aggregate the results.
def worker(num):
    return num * num

if __name__ == "__main__":
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(worker, range(10))
    print(results)