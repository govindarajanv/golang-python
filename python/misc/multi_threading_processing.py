import threading
import random
from functools import reduce
import multiprocessing
import time


def func(number):
    random_list = random.sample(range(1000000), number)
    return reduce(lambda x, y: x*y, random_list)

def multi_threading(number):

    start = time.time()
    thread1 = threading.Thread(target=func, args=(number,))
    thread2 = threading.Thread(target=func, args=(number,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    end = time.time()
    print ("Multithreading took",end-start)


def multi_processing(number):
    start = time.time()
    process1 = multiprocessing.Process(target=func, args=(number,))
    process2 = multiprocessing.Process(target=func, args=(number,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()
    end = time.time()
    print ("Multiprocessing took",end-start)

if __name__ == "__main__":
    number = 50000
    multi_threading(number)
    multi_processing(number)