def f(n):
    if n == 0:
        return 1
    else:
        return n*f(n-1)

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(50))