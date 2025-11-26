def fibonacci(stop):
    a, b = 0, 1
    while (stop-1)>=0:
        yield a
        a, b = b, a + b
        stop = stop - 1

for num in fibonacci(10):
    print(num)