# HOMEWORK RECURSION
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
