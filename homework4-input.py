# Task 1
import random
generator=random.randint(1,10)
print(generator)
guest=int(input("guess a number from 1 to 10="))
if generator==guest:
    print("Congratulations! You guessed the correct number:", generator)
else:
    print("Sorry, the correct number was:", generator)
# Task 2
name=input("enter your name:")
age=int(input("enter your age="))
print(f"Hello {name},on your next birthday you’ll be {age+1} years")
Task 3
import random
input_string = input("Enter a word: ")
characters = list(input_string)
b=len(input_string)
for _ in range(b):
    random.shuffle(characters)
    print(''.join(characters))
#Task 4
answer=int(input("give a solution to 6 la puterea 3="))
if answer==6*6*6:
 print("right")
else:
   print("wrong")
