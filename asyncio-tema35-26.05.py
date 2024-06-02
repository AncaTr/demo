import asyncio
import multiprocessing
import time


# Asynchronous implementations of Fibonacci, factorial, squares, and cubes
async def async_fibonacci(n):
    if n <= 1:
        return n
    else:
        return await async_fibonacci(n - 1) + await async_fibonacci(n - 2)


async def async_factorial(n):
    if n == 0:
        return 1
    else:
        return n * await async_factorial(n - 1)


async def async_squares(n):
    return [i ** 2 for i in range(1, n + 1)]


async def async_cubes(n):
    return [i ** 3 for i in range(1, n + 1)]


# Asynchronous main function to calculate Fibonacci, factorial, squares, and cubes for a list of numbers
async def async_main(numbers):
    fibonacci_results = await asyncio.gather(*(async_fibonacci(num) for num in numbers))
    factorial_results = await asyncio.gather(*(async_factorial(num) for num in numbers))
    squares_results = await asyncio.gather(*(async_squares(num) for num in numbers))
    cubes_results = await asyncio.gather(*(async_cubes(num) for num in numbers))
    return fibonacci_results, factorial_results, squares_results, cubes_results


# Multiprocessing implementations of Fibonacci, factorial, squares, and cubes
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def squares(n):
    return [i ** 2 for i in range(1, n + 1)]


def cubes(n):
    return [i ** 3 for i in range(1, n + 1)]


# Main function to calculate Fibonacci, factorial, squares, and cubes for a list of numbers using multiprocessing
def multiprocessing_main(numbers):
    with multiprocessing.Pool() as pool:
        fibonacci_results = pool.map(fibonacci, numbers)
        factorial_results = pool.map(factorial, numbers)
        squares_results = pool.map(squares, numbers)
        cubes_results = pool.map(cubes, numbers)
    return fibonacci_results, factorial_results, squares_results, cubes_results


if __name__ == '__main__':
    numbers = list(range(1, 11))

    # Asynchronous implementation using asyncio
    start_time = time.time()
    asyncio_results = asyncio.run(async_main(numbers))
    asyncio_duration = time.time() - start_time

    print("Asyncio Results:")
    print("Fibonacci:", asyncio_results[0])
    print("Factorial:", asyncio_results[1])
    print("Squares:", asyncio_results[2])
    print("Cubes:", asyncio_results[3])
    print("Asyncio Duration:", asyncio_duration)

    # Multiprocessing implementation
    start_time = time.time()
    multiprocessing_results = multiprocessing_main(numbers)
    multiprocessing_duration = time.time() - start_time

    print("\nMultiprocessing Results:")
    print("Fibonacci:", multiprocessing_results[0])
    print("Factorial:", multiprocessing_results[1])
    print("Squares:", multiprocessing_results[2])
    print("Cubes:", multiprocessing_results[3])
    print("Multiprocessing Duration:", multiprocessing_duration)




