print("Введите число: ")
value = input()
numbers = list(map(int, value))
fwd_number = numbers.index(max(numbers))+1
back_number = len(numbers) - numbers.index(max(numbers))
print("Индекс самой большой цифры с начала: ", fwd_number, '\n', "Индекс самой большой цифры с конца: ", back_number, sep='')