# Task 1
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

    @check_full
    def put(self, element):
        """Put an element into the sequence."""
        self._storage.append(element)

    @check_empty
    def get(self):
        """Get an element from the sequence."""
        return self._storage.pop(0)

    def is_full(self):
        """Check if the sequence is full."""
        return len(self._storage) == self._capacity

    def is_empty(self):
        """Check if the sequence is empty."""
        return not bool(self._storage)

class Stack(BaseSequence):
    """A Last-In-First-Out (LIFO) data structure."""
    @check_empty
    def pop(self):
        """Remove and return the last element."""
        return self._storage.pop()

    @check_empty
    def peek(self):
        """Return the last element without removing it."""
        return self._storage[-1]

class Queue(BaseSequence):
    """A First-In-First-Out (FIFO) data structure."""
    @check_empty
    def get_beginning(self):
        """Remove and return the first element."""
        return self._storage.pop(0)

class Dequeue(Queue, Stack):
    """A sequence that allows insertion and removal from both ends."""
    @check_full
    def put_beginning(self, element):
        """Insert an element at the beginning of the dequeue."""
        self._storage.insert(0, element)
        import pytest
        def test_empty_stack_pop():
            stack = Stack([])
            with pytest.raises(ValueError, match="Storage is empty."):
                stack.pop()

        def test_full_stack_put():
            stack = Stack([1, 2, 3], capacity=3)
            with pytest.raises(ValueError, match="Storage is full."):
                stack.put(4)

        def test_empty_queue_get_beginning():
            queue = Queue([])
            with pytest.raises(ValueError, match="Storage is empty."):
                queue.get_beginning()

        def test_full_queue_put():
            queue = Queue([1, 2, 3], capacity=3)
            with pytest.raises(ValueError, match="Storage is full."):
                queue.put(4)

        def test_empty_dequeue_put_beginning():
            dequeue = Dequeue([], capacity=0)
            with pytest.raises(ValueError, match="Storage is full."):
                dequeue.put_beginning(1)

        def test_full_dequeue_put_beginning():
            dequeue = Dequeue([1, 2, 3, 4, 5], capacity=5)
            with pytest.raises(ValueError, match="Storage is full."):
                dequeue.put_beginning(6)

        def test_dequeue_operations():
            dequeue = Dequeue([1, 2, 3], capacity=5)
            dequeue.put_beginning(0)
            assert dequeue.get_beginning() == 0
            dequeue.put(4)
            assert dequeue.pop() == 4
def is_balanced(sequence):
    stack = []
    bracket_pairs = {')': '(', '}': '{', ']': '['}

    for char in sequence:
        if char in bracket_pairs.values():  # check if it's an opening bracket
            stack.append(char)
        elif char in bracket_pairs:  # check if it's a closing bracket
            if not stack or stack[-1] != bracket_pairs[char]:
                return False
            stack.pop()

    return len(stack) == 0

# Test the function using assertions
def test_is_balanced():
    test_cases = [
        ("()", True),      # balanced
        ("())", False),    # not balanced
        (")(", False),     # not balanced
        ("([])", True),    # balanced
        ("([{}])", True),  # balanced
        ("([{]})", False), # not balanced
        ("[(){}[]]()", True),  # balanced
    ]

    for sequence, expected in test_cases:
        assert is_balanced(sequence) == expected, f"Failed for sequence: {sequence}"

    print("All test cases passed successfully.")

# Run the tests
test_is_balanced()



