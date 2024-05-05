#TASK1
from functools import wraps
def check_full(method):
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        if self.is_full():
            raise ValueError("Storage is full.")
        return method(self, *args, **kwargs)
    return wrapper

def check_empty(method):
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        if self.is_empty():
            raise ValueError("Storage is empty.")
        return method(self, *args, **kwargs)
    return wrapper

class BaseSequence:
    """A base sequence class."""
    def __init__(self, initial_items: list, capacity=10):
        self._storage = initial_items
        self._capacity = capacity

    @check_empty
    def put(self, element):
        """Put an element into the sequence."""
        if self.is_full():
            raise ValueError("Storage is full.")
        self._storage.append(element)

    def is_empty(self):
        """Check if the sequence is empty."""
        return not bool(self._storage)

    def is_full(self):
        """Check if the sequence is full."""
        return len(self._storage) == self._capacity


class Stack(BaseSequence):
    """A Last-In-First-Out (LIFO) data structure."""
    @check_empty
    def pop(self):
        """Remove and return the last element."""
        if self.is_empty():
            raise ValueError("Storage is empty.")
        return self._storage.pop()

    def peek(self):
        """Return the last element without removing it."""
        if self.is_empty():
            raise ValueError("Storage is empty.")
        return self._storage[-1]

class Queue(BaseSequence):
    """A First-In-First-Out (FIFO) data structure."""
    def get_beginning(self):
        """Remove and return the first element."""
        if self.is_empty():
            raise ValueError("Storage is empty.")
        return self._storage.pop(0)


class Dequeue(Queue, Stack):
    """A sequence that allows insertion and removal from both ends."""
    @check_full
    def put_beginning(self, element):
        """Insert an element at the beginning of the dequeue."""
        if len(self._storage) >= self._capacity:
            raise ValueError("Storage is full.")
        self._storage.insert(0, element)

def test_sequence_operations():
    """Test various operations on the sequences."""
    # Test an empty stack
    stack = Stack([])
    try:
        stack.pop()  # Should raise ValueError
    except ValueError as e:
        assert str(e) == "Storage is empty."

    # Test a full stack
    stack = Stack([1, 2, 3], capacity=3)
    try:
        stack.put(4)  # Should raise ValueError
    except ValueError as e:
        assert str(e) == "Storage is full."

    # Test an empty queue
    queue = Queue([])
    try:
        queue.get_beginning()  # Should raise ValueError
    except ValueError as e:
        assert str(e) == "Storage is empty."

    # Test a full queue
    queue = Queue([1, 2, 3], capacity=3)
    try:
        queue.put(4)  # Should raise ValueError
    except ValueError as e:
        assert str(e) == "Storage is full."

    # Test an empty dequeue
    dequeue = Dequeue([])
    try:
        dequeue.put_beginning(1)  # Should raise ValueError
    except ValueError as e:
        assert str(e) == "Storage is full."

    # Test a full dequeue
    dequeue = Dequeue([1, 2, 3, 4, 5], capacity=5)
    try:
        dequeue.put_beginning(6)  # Should raise ValueError
    except ValueError as e:
        assert str(e) == "Storage is full."

    # Test putting and getting from dequeue
    dequeue = Dequeue([1, 2, 3], capacity=5)
    dequeue.put_beginning(0)
    assert dequeue.get_beginning() == 0
    dequeue.put(4)
    assert dequeue.pop() == 4

    print("All test cases passed successfully.")

# Run the test cases
test_sequence_operations()
#TASK2
def is_balanced(sequence):
    stack = []
    opening_brackets = "({["
    closing_brackets = ")}]"
    bracket_pairs = {')': '(', '}': '{', ']': '['}

    for char in sequence:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or stack[-1] != bracket_pairs[char]:
                return False
            stack.pop()

    return len(stack) == 0

# Test the function
test_cases = [
    "()",      # balanced
    "())",     # not balanced
    ")( ",     # not balanced
    "([])",    # balanced
    "([{}])",  # balanced
    "([{]})",  # not balanced
    "[(){}[]]()",  # balanced
]

for test_case in test_cases:
    result = is_balanced(test_case)
    print(f"Sequence: '{test_case}' => Balanced: {result}")

