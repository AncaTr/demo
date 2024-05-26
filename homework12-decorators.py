# Task 1
# For example:
#  "add called with 4, 5"
def logger(func):
    pass
@logger
def add(x, y):
    return x + y
@logger
def square_all(*args):
    return [arg ** 2 for arg in args]
def produs(funct):
    pass
@produs
def pro(a,b):
    a=3
    b=6
    return a*b
@produs
def pro(*args):
    return(arg ** 2 for arg in args)
def logger(func):
    def wrapper(rez=None, *args, **kwargs):
        print(f"Function '{func.__name__}' called with arguments: {args}, {kwargs},result: {rez}")
        return func(*args, **kwargs)
    return wrapper
@logger
def example_function(x, y):
    rez=x*y
    return rez
# example_function(6,10)
def logger(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' called with arguments: {args}, {kwargs}, result: {result}")
        return result
    return wrapper
@logger
def example_function(x, y):
    rez = x * y
    return rez
example_function(6, 10)
def stop_words(words):
    def decorator(func):
        def wrapper(name):
            result = func(name)
            for word in words:
                result = result.replace(word, '*')
            return result
        return wrapper
    return decorator

@stop_words(['pepsi', 'BMW'])
def create_slogan(name):
    return f"{name} drinks pepsi in his brand new BMW!"
assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
create_slogan("")
# task 2
def stop_words(words):
    def decorator(func):
        def wrapper(name):
            result = func(name)
            for word in words:
                result = result.replace(word, '*')
            return result
        return wrapper
    return decorator

@stop_words(['pepsi', 'BMW'])
def create_slogan(name):
    return f"{name} drinks pepsi in his brand new BMW!"

result = create_slogan("Steve")
print(result)
# TASK3
def stop_words(words):
    def decorator(func):
        def wrapper(name):
            result = func(name)
            for word in words:
                result = result.replace(word, '*')
            return result
        return wrapper
    return decorator

def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrapper(name):
            if type(name) != type_:
                return False
            if len(name) > max_length:
                return False
            for substring in contains:
                if substring not in name:
                    return False
            return func(name)
        return wrapper
    return decorator

@arg_rules(type_=str, max_length=15, contains=['05', '@'])
@stop_words(['pepsi', 'BMW'])
def create_slogan(name):
    return f"{name} drinks pepsi in his brand new BMW!"
result = create_slogan("Steve")
print(result)
def logger(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' called with arguments: {args}, {kwargs}, result: {result}")
        return result
    return wrapper
def logger(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' called with arguments: {args}, {kwargs}, result: {result}")
        return result
    return wrapper

@logger
def example_function(x, y):
    rez = x * y
    return rez

result = example_function(6, 10)
print("Result:", result)