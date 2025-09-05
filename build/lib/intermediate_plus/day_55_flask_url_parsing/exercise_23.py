def logging_decorator(function):
    def wrapper(*args):
        result = function(*args)
        print(f"You called {function.__name__}{args}\nIt returned: {result}")
        return result
    return wrapper

@logging_decorator
def a_function(*args):
    return sum(args)


a_function(1, 2, 3)
a_function(4, 5, 6)