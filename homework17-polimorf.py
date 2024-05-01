# Task 1
class Animal:
    def talk(self):
        pass

class Dog(Animal):
    def talk(self):
        return "woof woof"

class Cat(Animal):
    def talk(self):
        return "meow"

def perform_talk(animal_instance):
    if isinstance(animal_instance, Animal):
        return animal_instance.talk()
    else:
        raise ValueError("Input must be an instance of Animal class or its subclass")


# Testing
dog = Dog()
cat = Cat()

print(perform_talk(dog))  # Output: "woof woof"
print(perform_talk(cat))  # Output: "meow"
# Task2
class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return f"Author(name='{self.name}', country='{self.country}', birthday='{self.birthday}')"

    def __str__(self):
        return f"Author: {self.name}, Country: {self.country}, Birthday: {self.birthday}"


class Book:
    total_books = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        author.books.append(self)
        Book.total_books += 1

    def __repr__(self):
        return f"Book(name='{self.name}', year={self.year}, author={self.author})"

    def __str__(self):
        return f"Book: {self.name}, Year: {self.year}, Author: {self.author.name}"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def new_book(self, name, year, author):
        book = Book(name, year, author)
        self.books.append(book)
        return book

    def group_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year):
        return [book for book in self.books if book.year == year]

    def __repr__(self):
        return f"Library(name='{self.name}', books={self.books})"

    def __str__(self):
        return f"Library: {self.name}, Number of books: {len(self.books)}"


# Testing
if __name__ == "__main__":
    author1 = Author("John Doe", "USA", "1980-01-01")
    author2 = Author("Jane Smith", "UK", "1975-05-05")

    library = Library("My Library")

    book1 = library.new_book("Book1", 2000, author1)
    book2 = library.new_book("Book2", 2010, author1)
    book3 = library.new_book("Book3", 2005, author2)

    print(book1)
    print(book2)
    print(book3)

    print(library.group_by_author(author1))
    print(library.group_by_year(2005))

    print(Book.total_books)  # Output: 3
# task3
class Fraction:
    def __init__(self, numerator, denominator=1):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        self.value = numerator / denominator

    def __repr__(self):
        return f"Fraction({self.value})"

    def __add__(self, other):
        return Fraction(self.value + other.value)

    def __sub__(self, other):
        return Fraction(self.value - other.value)

    def __mul__(self, other):
        return Fraction(self.value * other.value)

    def __truediv__(self, other):
        if other.value == 0:
            raise ValueError("Division by zero")
        return Fraction(self.value / other.value)

# Testing
x = Fraction(1, 2)
y = Fraction(1, 4)

print(x + y)  # Output: Fraction(0.75)