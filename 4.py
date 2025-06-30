def gen_fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in gen_fib(6):
    print(num)