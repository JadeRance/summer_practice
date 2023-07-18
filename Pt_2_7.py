sum = 0
print("Введите отрицательное число:")
value = int(input())
while (value < 0):
    sum += value
    print("Введите отрицательное число:")
    value = int(input())
print("Сумма отрицательных чисел:", sum)