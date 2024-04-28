# Task 1
class Person:
    def __init__(self,first_name,last_name,age,high,gender,eyes,hair_color):
        self.first_name = first_name
        self.last_name= last_name
        self.age= age
        self.high= high
        self.gender= gender
        self.eyes= eyes
        self.hair_color=hair_color
class Student:
        def __init__(self,class_number):
            self.class_number=class_number
class Teacher:
    def __init__(self,salary,subject):
        self.salary= salary
        self.subject= subject
person=Person("John","Doe",18,1.85,"male","brown","black")
student=Student(10)
teacher=Teacher(5000 ,"English")
print(person.first_name, person.last_name, person.age, person.high,person.gender,person.eyes,person.hair_color)
print(student.class_number)
print(teacher.salary,teacher.subject)
# Task 2

class Mathematician:
    def square_nums(self, nums):
        squares = []
        for num in nums:
            squares.append(num*num)
        return squares

    def remove_positives(self, nums):
        negatives = []
        for num in nums:
            if num < 0:
                negatives.append(num)
        return negatives

    def filter_leaps(self, years):
        leap_years = []
        for year in years:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                leap_years.append(year)
        return leap_years

m = Mathematician()
print("Square numbers:", m.square_nums([7, 11, 5, 4]))
print("Negative numbers:", m.remove_positives([26, -11, -8, 13, -90]))
print("Leap years:", m.filter_leaps([2001, 1884, 1995, 2003, 2020]))
assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
print("All assertions passed successfully.")


class Product:
    pass


class Product:
    def __init__(self,type,name,price):
        self.type = type
        self.name = name
        self.price = price
    product= Product()
class Productore:
    def __add__(self,product,amount):
        self.product = product
        self.amount = amount
class Product:
    def __init__(self, product_type, name, price):
        self.type = product_type
        self.name = name
        self.price = price
class ProductStore:
    def __init__(self):
        self.products = {}
        self.income = 0

    def add(self, product, amount):
        if not isinstance(product, Product):
            raise ValueError("Invalid product")
        if amount <= 0:
            raise ValueError("Amount must be greater than zero")
        price_with_premium = product.price * 1.3

        if product.name in self.products:
            self.products[product.name]['amount'] += amount
        else:
            self.products[product.name] = {'type': product.type, 'price': price_with_premium, 'amount': amount}

    def set_discount(self, identifier, percent, identifier_type='name'):
        if identifier_type == 'name':
            for product_name, product_info in self.products.items():
                if product_name == identifier:
                    product_info['price'] *= (1 - percent / 100)
        elif identifier_type == 'type':
            for product_name, product_info in self.products.items():
                if product_info['type'] == identifier:
                    product_info['price'] *= (1 - percent / 100)
        else:
            raise ValueError("Invalid identifier type")

    def sell_product(self, product_name, amount):
        if product_name not in self.products:
            raise ValueError("Product not found")
        if amount <= 0:
            raise ValueError("Amount must be greater than zero")
        if self.products[product_name]['amount'] < amount:
            raise ValueError("Insufficient stock")

        self.products[product_name]['amount'] -= amount
        self.income += self.products[product_name]['price'] * amount

    def get_income(self):
        return self.income

    def get_all_products(self):
        return self.products

    def get_product_info(self, product_name):
        if product_name not in self.products:
            raise ValueError("Product not found")
        return product_name, self.products[product_name]['amount']

# Testing
p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)
s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
s.sell_product('Ramen', 10)

assert s.get_product_info('Ramen') == ('Ramen', 290)
class CustomException(Exception):
    def __init__(self, message):
        super().__init__(message)
        with open('logs.txt', 'a') as log_file:
            log_file.write(message + '\n')


class Product:
    def __init__(self, product_type, name, price):
        self.type = product_type
        self.name = name
        self.price = price


class ProductStore:
    def __init__(self):
        self.products = {}
        self.income = 0

    def add(self, product, amount):
        if not isinstance(product, Product):
            raise CustomException("Invalid product")
        if amount <= 0:
            raise CustomException("Amount must be greater than zero")
        price_with_premium = product.price * 1.3

        if product.name in self.products:
            self.products[product.name]['amount'] += amount
        else:
            self.products[product.name] = {'type': product.type, 'price': price_with_premium, 'amount': amount}

    def set_discount(self, identifier, percent, identifier_type='name'):
        if identifier_type == 'name':
            for product_name, product_info in self.products.items():
                if product_name == identifier:
                    product_info['price'] *= (1 - percent / 100)
        elif identifier_type == 'type':
            for product_name, product_info in self.products.items():
                if product_info['type'] == identifier:
                    product_info['price'] *= (1 - percent / 100)
        else:
            raise CustomException("Invalid identifier type")

    def sell_product(self, product_name, amount):
        if product_name not in self.products:
            raise CustomException("Product not found")
        if amount <= 0:
            raise CustomException("Amount must be greater than zero")
        if self.products[product_name]['amount'] < amount:
            raise CustomException("Insufficient stock")

        self.products[product_name]['amount'] -= amount
        self.income += self.products[product_name]['price'] * amount

    def get_income(self):
        return self.income

    def get_all_products(self):
        return self.products

    def get_product_info(self, product_name):
        if product_name not in self.products:
            raise CustomException("Product not found")
        return product_name, self.products[product_name]['amount']


# Testing
p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)
s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
s.sell_product('Ramen', 10)

assert s.get_product_info('Ramen') == ('Ramen', 290)
# Testing
p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)
s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
s.sell_product('Ramen', 10)

result = s.get_product_info('Ramen')
print("Product info after selling Ramen:", result)
assert result == ('Ramen', 290)