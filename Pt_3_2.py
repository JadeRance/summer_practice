import math
from functools import reduce

def find_quantity(n):
    x = [0, 1]
    while (x[-1] <= n):
        x.append(x[-1]+x[-2])
    return len(x)-1

print("Введите число, до которого будут искаться числа Фибоначчи: ")
n = int(input())
fibonacci = lambda n: reduce(lambda x, n: x + [x[-1] + x[-2]], range(find_quantity(n) - 2), [0, 1])
print(*fibonacci(n), sep=', ')