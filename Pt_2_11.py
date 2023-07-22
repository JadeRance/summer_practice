print("Введите диапазон чисел для нахождения их суммы: ")
a = int(input())
b = int(input())
i = a
sum = 0
while i <= b:
    sum += i
    i += 1
print("Сумма чисел от", a, "до", b, "равна", sum)
