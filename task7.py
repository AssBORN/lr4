from datetime import datetime

def log_function_call(func):
    def wrapper(*args):
        print(f"[{datetime.now()}] Вызов функции: {func.__name__}")
        print(f"    Аргументы: args={args}")
        result = func(*args)
        print(f"    Результат: {result}")
        print(f"[{datetime.now()}] Завершение функции: {func.__name__}")
        return result
    return wrapper

@log_function_call
def add_numbers(a, b):
    return a + b

add_numbers(5, 3)
