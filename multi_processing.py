import math, time, multiprocessing
from unicodedata import name

def fun(numbers):
    c = []
    for i in numbers:
        c.append(math.sqrt(i ** 5))

if __name__ == '__main__':
    num_list = list(range(1_500_000))
    p1 = multiprocessing.Process(target=fun, args=(num_list,))
    p2 = multiprocessing.Process(target=fun, args=(num_list,))
    p3 = multiprocessing.Process(target=fun, args=(num_list,))
    start = time.time()
    p1.start()
    p2.start()
    p3.start()
    end = time.time()
    print("With Multiprocessing: ¬ ", round(end - start, 2), "seconds")
    fun(num_list)
    fun(num_list)
    fun(num_list)
    end = time.time()
    print("Without Multiprocessing: ¬ ", round(end - start, 2), "seconds")