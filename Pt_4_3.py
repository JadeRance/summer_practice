import math
low = int(input())
high = int(input())
simple_numbers = []
for i in range(low, high + 1):
    divider_count = 0
    for j in range(1, math.floor(math.sqrt(i)) + 1):
        if i % j == 0:
            divider_count += 1
    if divider_count == 1:
        simple_numbers.append(i)
print(simple_numbers)