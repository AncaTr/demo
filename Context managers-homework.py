# HOMEWORK context managers
# TASK 1
from typing import Optional, Union
def to_power(x: Union[int, float], exp: int) -> Optional[Union[int, float]]:
    if exp < 0:
        raise ValueError("This function works only with exp > 0.")
    elif exp == 0:
        return 1
    elif exp == 1:
        return x
    else:
        return x * to_power(x, exp - 1)
# Test cases
print(to_power(2, 3))  # Output: 8
print(to_power(3.5, 2))  # Output: 12.25
print(to_power(2, -1))
# Task 2
import unittest
import os

# Import the CustomFileManager class from Task 1
from custom_file_manager import CustomFileManager

class TestCustomFileManager(unittest.TestCase):
    def setUp(self):
        self.file_manager = CustomFileManager()

    def tearDown(self):
        pass

    def test_file_open_read(self):
        with self.file_manager.open_file("test_file.txt", "r") as file:
            content = file.read()
            self.assertEqual(content, "This is a test file.")

    def test_file_open_write(self):
        with self.file_manager.open_file("test_write.txt", "w") as file:
            file.write("Testing write operation.")

        with open("test_write.txt", "r") as file:
            content = file.read()
            self.assertEqual(content, "Testing write operation.")

    def test_file_open_nonexistent(self):
        with self.assertRaises(FileNotFoundError):
            with self.file_manager.open_file("nonexistent_file.txt", "r"):
                pass

if __name__ == "__main__":
    unittest.main()
    print("Test")
    print("Done")
    # task 3
    import pytest
    from custom_file_manager import CustomFileManager


    # Function to perform some logic with text data obtained from a file object
    def process_data(file_obj):
        return file_obj.read().upper()


    # Test case for the process_data function using pytest
    def test_process_data(custom_file):
        with custom_file.open("test.txt", "r") as file:
            data = process_data(file)
            assert data == 'THIS IS A TEST FILE.'


    # Pytest fixture using our custom file manager context manager
    @pytest.fixture
    def custom_file():
        with CustomFileManager() as file_manager:
            yield file_manager
