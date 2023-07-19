import math
n = int(input())
simple = []
for i in range(2, n+1):
    count = 0
    for j in range(2, i+1):
        if i % j == 0:
            count += 1
    if count == 1:
        simple.append(i)
print(*simple, sep=', ')