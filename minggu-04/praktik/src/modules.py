
    >>> def fib(n):
    ...     a, b = 0, 1
    ...     while a < n:
    ...             print(a, end=' ')
    ...             a, b = b, a+b
    ...     print()
    ...
    >>> def fib2(n):
    ...     result = []
    ...     a, b = 0, 1
    ...     while a < n:
    ...             result.append(a)
    ...             a, b = b, a+b
    ...     return result
    ...
    >>> import sys
    >>> sys.path.append(r'D:\python')
    >>> import fibo
    >>> fibo.fib(1000)
    0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
