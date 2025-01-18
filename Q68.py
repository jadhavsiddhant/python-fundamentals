# Implement a function fib(n) to return the nth Fibonacci number using
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
