from functools import reduce

def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    def add_next_number(fib_sequence, _):
        next_number = fib_sequence[-1] + fib_sequence[-2]
        return fib_sequence + [next_number]
    return reduce(add_next_number, range(n - 2), [0, 1])

result = fibonacci(10)
print(result)