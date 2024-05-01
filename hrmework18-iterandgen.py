# task 1
def with_index(iterable, start=0):
    index = start
    for item in iterable:
        yield index, item
        index += 1

# Example usage:
my_list = ['a', 'b', 'c', 'd']
for i, value in with_index(my_list):
    print(i, value)
# Task 2
def in_range(start, end, step=1):
    if step == 0:
        raise ValueError("step cannot be zero")
    elif step < 0:
        while start > end:
            yield start
            start += step
    else:
        while start < end:
            yield start
            start += step

if __name__ == "__main__":
    for i in in_range(1, 10, 3):
        print(i)
# task 3
class MyIterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return iter(self.data)

    def __getitem__(self, index):
        return self.data[index]


# Example usage:
my_iterable = MyIterable([1, 2, 3, 4, 5])

print("Iterating using for-in loop:")
for item in my_iterable:
    print(item)

# Accessing elements using square brackets syntax
print("\nAccessing elements using square brackets:")
print("Element at index 0:", my_iterable[0])
print("Element at index 2:", my_iterable[2])
print("Element at index 4:", my_iterable[4])
