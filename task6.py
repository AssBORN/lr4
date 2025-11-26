
def repeat(times=1):
    def decorator(func):
        def wrapper(*args):
            for i in range(times):
                print(f"Круг {i+1}/{times}")
                result = func(*args)
        return wrapper
    return decorator

@repeat(times=4)
def say_hello(name):
    print(f"Привет, {name}!")

say_hello("Олег")