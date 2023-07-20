number = int(input())
numbers = (sorted(list(map(int, str(number))), reverse=True))
print(int("".join(map(str, numbers))))