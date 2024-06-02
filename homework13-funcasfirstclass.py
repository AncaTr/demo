# Task 1
class FunctionAnalyzer:
    @staticmethod
    def count_local_variables(func):
        code = func.__code__
        num_locals = code.co_argcount + code.co_nlocals
        return num_locals
# Task 2
    @staticmethod
    def sum_local_variables(func):
        def wrapper(*args, **kwargs):
            a = 1
            b = 2
            c = 3
            d = 4
            e = 5
            return func(*args, **kwargs) + a + b + c + d + e
        return wrapper

# Task 3
    @staticmethod
    def choose_func(nums: list, func1, func2):
        if all(num > 0 for num in nums):
            return func1(nums)
        else:
            return func2(nums)

def square_nums(nums):
    return [num ** 2 for num in nums]

def remove_negatives(nums):
    return [num for num in nums if num > 0]

if __name__ == "__main__":
    analyzer = FunctionAnalyzer()

    nums1 = [1, 2, 3, 4, 5]
    nums2 = [1, -2, 3, -4, 5]
    result1 = analyzer.choose_func(nums1, square_nums, remove_negatives)
    result2 = analyzer.choose_func(nums2, square_nums, remove_negatives)

    print("Result for nums1:", result1)
    print("Result for nums2:", result2)


