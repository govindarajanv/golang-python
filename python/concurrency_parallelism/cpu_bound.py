import time
import concurrent.futures
import multiprocessing

# single thread, single process
def cpu_bound(number):
    return sum(i * i for i in range(number))


def find_sums_sync(numbers):
    for number in numbers:
        cpu_bound(number)

def find_sums_mt(numbers):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(cpu_bound, numbers)

def find_sums_mp(numbers):
    with multiprocessing.Pool() as pool:
        pool.map(cpu_bound, numbers)

def calculate(func,numbers):
    start_time = time.time()
    func(numbers)
    duration = time.time() - start_time
    print(f"{func.__name__} took {duration} seconds")    

if __name__ == "__main__":
    numbers = [5000000 + x for x in range(30)]
    
    # synchronous version
    calculate(find_sums_sync,numbers)

    # multi-threading version
    calculate(find_sums_mt,numbers)

    # multi-processing version
    calculate(find_sums_mp,numbers)