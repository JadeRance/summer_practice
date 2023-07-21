from itertools import chain, combinations

def powerset(numbers, s):
    return chain.from_iterable(combinations(numbers, s) for s in range(len(numbers)+1))

def cut_numbers(numbers):
    for i in range(len(numbers)):
        if numbers[i] > summation:
            del numbers[i:]
            break

def find_s(numbers):
    total = 0
    for i in range(len(numbers)):
        if total + numbers[i] < summation:
            total += 1
    return total

numbers = sorted([1, 2, 2, 4, 5, 7])
summation = int(input())
candidates = []
cut_numbers(numbers)
s = find_s(numbers)
for x in powerset(numbers, s):
    if sum(x) == summation and x not in candidates:
        candidates.append(x)
print(candidates)