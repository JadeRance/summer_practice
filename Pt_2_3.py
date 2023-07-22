print("Введите число для проверки на чиcло Армстронга: ")
enter_value = input()
value_numbers = list(map(int, enter_value))
check_value = 0
power = 1
while (check_value < int(enter_value)):
    check_value = 0
    for i in range(len(value_numbers)):
        check_value += value_numbers[i] ** power
    power += 1
if check_value == int(enter_value):
    print("Число", enter_value, "- число Армстронга")
else:
    print("Число", enter_value, "не является числом Армстронга")
