# Task 1

import random
numbers = [random.randint(1, 1000) for _ in range(10)]
largest = max(numbers)
print("List of random numbers:", numbers)
print("The largest number is:", largest)
# MY EXAMPLE
import random
numbers=[random.randint(1,10000) for _ in range (20)]
minimal=min(numbers)
print("the list of random numbers is:",numbers)
print("the minimal number is: ",minimal)
# Task 2

import random
list1=[random.randint(1,10) for _ in range(10)]
list2=[random.randint(1,10) for _ in range(10)]
list3 = list(set(list1) & set(list2))
print("the numbers in list 1 are:",list1)
print("the numbers in list 2 are:",list2)
print("the numbers in list 3 are:",list3)
# Task 3

my_list = [x for x in range(1, 101) if x % 7 == 0 and x % 5 != 0]
print(my_list)
my_list = []
number = 1
while number <= 100:
    if number % 7 == 0 and number % 5 != 0:
        my_list.append(number)
    number += 1
print(my_list)
list = []
a = 1
while a<=100:
    if a % 7 == 0 & a % 5 != 0:
        list.append(a)
        a += 1
print(list)