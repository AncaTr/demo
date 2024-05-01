import string
ASCII_MAPPING = {}
INDEX = 0
for letter in string.ascii_letters + "0123456789 ,.!?()[]":
    ASCII_MAPPING[letter] = INDEX
    INDEX += 1
def hash_function(key: str, size=100):
    """Take a key as an input and calculate an integer output
    Output should be between 0 and size
    """
    key = str(key)
    hash_value = 0
    for letter in key:
        hash_value += ASCII_MAPPING[letter]
    hash_value = hash_value % size
    return hash_value
class Dictionary:
    def __init__(self):
        self._capacity = 10
        self._size = 0
        self._storage = []
        self._resize_and_rehash()

    def _resize_and_rehash(self):
        old_storage = self._storage.copy()
        self._capacity *= 2
        self._storage = []
        for _ in range(self._capacity):
            self._storage.append([])

        for cell in old_storage:
            for key, value in cell:
                self.put(key, value)

    def get(self, search_key):
        index = hash_function(search_key, size=self._capacity)
        for key, value in self._storage[index]:
            if search_key == key:
                return value
        raise KeyError(search_key)

    def put(self, key, value):
        self._size += 1
        if self._size == self._capacity:
            self._resize_and_rehash()
        index = hash_function(key, size=self._capacity)
        self._storage[index].append((key, value))

    def keys(self):
        all_keys = []
        for cell in self._storage:
            for key, _ in cell:
                all_keys.append(key)
        return all_keys

    def values(self):
        all_values = []
        for cell in self._storage:
            for _, value in cell:
                all_values.append(value)
        return all_values

    def items(self):
        all_items = []
        for cell in self._storage:
            all_items.extend(cell)
        return all_items

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __str__(self):
        return str(self.items())


demo_dict = Dictionary()
demo_dict["1"] = 1
print(demo_dict["1"])
demo_dict["2"] = 2
demo_dict[(1, 2, 3)] = (1, 2, 3)
print(demo_dict.keys())
print(demo_dict.values())
print(demo_dict.items())
print(demo_dict)