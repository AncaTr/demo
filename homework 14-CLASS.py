# Task 1
def cont(a, b, c, d,e,f,g):
    count = 1
    while count > 1:  # This loop will never execute as count starts at 0
        count ++ 1  # Fixing the syntax error, use += instead of ++
    return count
def count_local_variables(func):
    code = func.__code__
    num_locals = len(code.co_varnames)
    return num_locals

# Test the function
# print("Number of local variables in 'cont' function:", count_local_variables(cont))
def cont(a, b):
    count = 1
    while count > 1:  # This loop will never execute as count starts at 0
        count += 1  # Fixing the syntax error, use += instead of ++
    return count

def count_local_variables(func):
    code = func.__code__
    # Exclude function arguments from the count
    num_locals = len(code.co_varnames) - code.co_argcount
    return num_locals
print("Number of local variables in 'cont' function:", count_local_variables(cont))

def cont(a, b, c, e, d):
    count =0
    while count > 0:  # This loop will never execute as count starts at 0
        count += 1  # Fixing the syntax error, use += instead of ++
    return count

def count_local_variables(func):
    code = func.__code__
    num_locals = len(code.co_varnames)
    return num_locals
def cont(a, b, c, e, d):
    count =0
    while count > 0:  # This loop will never execute as count starts at 0
        count += 1  # Fixing the syntax error, use += instead of ++
    return count

# Test the function
print("Number of local variables in 'cont' function:", count_local_variables(cont))


def count_local_variables(func):
    # Get the local symbol table of the function
    local_symbols = func.__code__.co_varnames
    # Exclude function arguments and built-in names
    local_vars = [var for var in local_symbols if var != 'func' and var != '__builtins__']
    return len(local_vars)

# Test the function
def test_function(a, b, c,d,e,f):
  return a + b + c
print("Number of local variables in 'test_function':", count_local_variables(test_function))
# Task 2
def sum_local_variables(func):
    def wrapper(a, b, c, d, e):
        a=1
        b=2
        c=3
        d=4
        e=5
        return a + b + c+ d +e;

    returned_function = sum_local_variables(func)
  # Now you can call the inner function
    returned_function()
    print(returned_function)
def sum_local_variables(func):
    def wrapper(a, b, c, d, e):
        a = 1
        b = 2
        c = 3
        d = 4
        e = 5
        return a + b + c + d + e

    # Now you can call the inner function
    return wrapper(func)

# Define a function to pass to sum_local_variables
def example_function(a, b, c, d, e):
    return a * b * c * d * e

# Call sum_local_variables with example_function
returned_function = sum_local_variables(example_function)

# Now you can call the returned_function
print("Result of the returned function:", returned_function)
def sum_local_variables(func):
    def wrapper(*args, **kwargs):
        a = 1
        b = 2
        c = 3
        d = 4
        e = 5
        # Call the original function 'func' with the same arguments
        return func(*args, **kwargs) + a + b + c + d + e

    # Return the modified function
    return wrapper

# Define a function to pass to sum_local_variables
def example_function(a, b, c, d, e):
    return a * b * c * d * e

# Call sum_local_variables with example_function
returned_function = sum_local_variables(example_function)

# Now you can call the returned_function
result = returned_function(1, 2, 3, 4, 5)
print("Result of the returned function:", result)
# Task 3
def choose_func(nums: list, func1, func2):
    pass
# Assertions
nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]
def square_nums(nums):
    return [num ** 2 for num in nums]
def remove_negatives(nums):
    return [num for num in nums if num > 0]
assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]
def choose_func(nums: list, func1, func2):
    # Check if all numbers in nums are positive
    if all(num > 0 for num in nums):
        return func1(nums)  # Execute func1 on nums
    else:
        return func2(nums)  # Execute func2 on nums

# Assertions
nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]

def square_nums(nums):
    return [num ** 2 for num in nums]

def remove_negatives(nums):
    return [num for num in nums if num > 0]
result1= choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
result2= choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]
print("Result for nums1:", result1)
print("Result for nums2:", result2)