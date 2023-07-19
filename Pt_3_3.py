value = int(input())
check = lambda value: "Число чётное" if value % 2 == 0 else "Число нечётное"
print(check(value))