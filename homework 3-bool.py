
#Task 1
a = input("give text:")
b = len(a)
if (b >= 2):
    print(a[0] + a[1]+a[b-2]+a[b-1])
elif(b<2):
    print("empty string")
# Task 2
phone_number = input("Give phone number: ")
if phone_number.isdigit() and len(phone_number) == 10:
    print(phone_number, "has correct format")
else:
    print(phone_number, "does not have correct format")
# Task 3
stored_name ="anca"
user_name = input("Enter your name: ")
if user_name.lower() == stored_name:
       print("true")
else:
       print("false")