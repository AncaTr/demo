import concurrent.futures
import time

NUMBERS = [
   2,  # prime
   1099726899285419,
   1570341764013157,  # prime
   1637027521802551,  # prime
   1880450821379411,  # prime
   1893530391196711,  # prime
   2447109360961063,  # prime
   3,  # prime
   2772290760589219,  # prime
   3033700317376073,  # prime
   4350190374376723,
   4350190491008389,  # prime
   4350190491008390,
   4350222956688319,
   2447120421950803,
   5,  # prime
]

def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def filter_primes_threadpool(numbers):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(is_prime, numbers))
    return [num for num, prime in zip(numbers, results) if prime]

def filter_primes_processpool(numbers):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = list(executor.map(is_prime, numbers))
    return [num for num, prime in zip(numbers, results) if prime]

def main():
#     Using ThreadPoolExecutor
    start_time = time.time()
    primes_threadpool = filter_primes_threadpool(NUMBERS)
    end_time = time.time()
    threadpool_duration = end_time - start_time
    print(f"ThreadPoolExecutor Primes: {primes_threadpool}")
    print(f"ThreadPoolExecutor Time: {threadpool_duration:.4f} seconds")

#      Using ProcessPoolExecutor
    start_time = time.time()
    primes_processpool = filter_primes_processpool(NUMBERS)
    end_time = time.time()
    processpool_duration = end_time - start_time
    print(f"ProcessPoolExecutor Primes: {primes_processpool}")
    print(f"ProcessPoolExecutor Time: {processpool_duration:.4f} seconds")
#      Comparing results
    assert primes_threadpool == primes_processpool, "The results are not the same!"
    print("Both methods give the same result.")

if __name__ == "__main__":
    main()
