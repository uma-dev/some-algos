m = 8
fib = [-1] * m


def dp_fib(n):
    if n == 0 or n == 1:
        fib[n] = n
        return fib[n]
    if fib[n] != -1:
        return fib[n]
    fib[n] = dp_fib(n - 1) + dp_fib(n - 2)
    return fib[n]


def db_fib_less_space(n):
    a = 0
    b = 1
    sum = 0

    for i in range(2, n + 1):
        sum = a + b
        a = b
        b = sum
    return n if n == 0 or n == 1 else sum


# Pruebas
for i in range(m):
    print(dp_fib(i), " ", db_fib_less_space(i))
